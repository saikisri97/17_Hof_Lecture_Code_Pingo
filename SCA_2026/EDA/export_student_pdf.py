"""Export a student PDF from the class deck; never edit the class PPTX."""
import argparse
import json
import posixpath
import shutil
import subprocess
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import ZipFile


def slide_titles(pptx):
    ns = {"p": "http://schemas.openxmlformats.org/presentationml/2006/main",
          "a": "http://schemas.openxmlformats.org/drawingml/2006/main"}
    rid = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"
    with ZipFile(pptx) as archive:
        rels = {r.get("Id"): r.get("Target") for r in ET.fromstring(
            archive.read("ppt/_rels/presentation.xml.rels"))}
        presentation = ET.fromstring(archive.read("ppt/presentation.xml"))
        titles = []
        for slide in presentation.findall("p:sldIdLst/p:sldId", ns):
            target = rels[slide.get(rid)]
            part = target.lstrip("/") if target.startswith("/") else posixpath.normpath("ppt/" + target)
            root = ET.fromstring(archive.read(part))
            titles.append(" | ".join(t.text or "" for t in root.findall(".//a:t", ns)))
    return titles


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--class-pptx", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    config = json.loads(Path(__file__).with_name("chapter.json").read_text())
    source = args.class_pptx or Path(config["slides"]["class_pptx"])
    output = args.output or Path(config["slides"]["student_pdf"])
    if not source.is_file():
        raise SystemExit(f"Class deck not found: {source}")
    office = shutil.which("soffice") or shutil.which("libreoffice")
    if not office:
        raise SystemExit("LibreOffice is required for automatic export. Alternatively export selected slides in PowerPoint.")
    from pypdf import PdfReader, PdfWriter
    titles = slide_titles(source)
    rules = config["slides"]["exclude_title_contains"]
    excluded = [i for i, title in enumerate(titles) if any(
        rule.casefold() in title.casefold() for rule in rules)]
    for required in config["slides"]["required_exclusions"]:
        if not any(required.casefold() in titles[i].casefold() for i in excluded):
            raise SystemExit(f"Expected exclusion not found: {required}. Check the deck before exporting.")
    with tempfile.TemporaryDirectory(prefix="eda_student_export_") as temp:
        temp = Path(temp)
        command = [office, f"-env:UserInstallation={temp.joinpath('office_profile').as_uri()}",
                   "--headless", "--convert-to", "pdf", "--outdir", str(temp), str(source.resolve())]
        result = subprocess.run(command, capture_output=True, text=True, timeout=180)
        rendered = temp / (source.stem + ".pdf")
        if result.returncode or not rendered.is_file():
            raise SystemExit("PDF conversion failed: " + result.stdout + result.stderr)
        reader = PdfReader(rendered)
        if len(reader.pages) != len(titles):
            raise SystemExit("Rendered page count differs from slide count; check hidden slides/export settings.")
        writer = PdfWriter()
        for i, page in enumerate(reader.pages):
            if i not in excluded:
                writer.add_page(page)
        writer.add_metadata({"/Title": "EDA — Student slides"})
        output.parent.mkdir(parents=True, exist_ok=True)
        writer.write(output)
    record = {"class_slides": len(titles), "student_pages": len(titles) - len(excluded),
              "excluded_slides": [{"number": i + 1, "text": titles[i]} for i in excluded],
              "source": str(source.resolve()), "output": str(output.resolve())}
    output.with_suffix(".export.json").write_text(json.dumps(record, indent=2, ensure_ascii=False))
    print(f"Created {output}: {record['student_pages']} pages. Excluded: {[i+1 for i in excluded]}")


if __name__ == "__main__":
    main()
