# EDA chapter

This is the chapter's working folder in Git. Keep its student notebook, solution, Pingo questions and dataset source together. Other chapters can follow the same pattern under SCA_2026.

| File | Purpose |
|---|---|
| EDA_Student.ipynb | Student exercises |
| EDA_Student_Solutions.ipynb | Answers and explanations |
| EDA_Pingo.xml | Eight questions for import |
| EDA_Pingo_Answer_Key.md | Instructor answer key |
| data/EDA_shipments.csv | Raw illustrative dataset snapshot |
| chapter.json | Slide paths, export exclusions, links and publication status |
| export_student_pdf.py | Generate the student PDF from the complete class deck |

## Slides

Maintain one editable deck: `EDA_Class.pptx` in the matching EDA folder under Slides/Class Sessions 2026. Its full path is recorded in chapter.json.

The student deliverable is `EDA_Student.pdf`, generated from that deck. Exclude slides whose title contains “Significance of Tasks” or “Wrap Up - Pingo”. There is no separate student PPTX to maintain. The exported PDF has no speaker notes. Inspect any new answer slides and add their titles to the exclusion rules before export.

To regenerate the PDF, ask Codex to export this chapter's student slides, or run `python export_student_pdf.py` from this folder. Automatic export requires LibreOffice and pypdf (listed in requirements-export.txt). You can also select the recorded slide ranges when exporting manually in PowerPoint. Slide numbers change when you edit the deck; the automatic exporter matches the exclusion text each time.

## Publishing

Review the contents of this chapter folder, then add/commit/push this folder once. That publishes the notebooks, data snapshot and Pingo files together. It does not publish the slide folder, create a Gist or configure TinyURL.

chapter.json includes the new chapter-based Colab destinations, explicitly labelled “after push”. The existing student Colab path is also recorded. Old repository paths have been preserved so existing links continue to target their existing files. Treat this chapter folder as the working source going forward; old paths do not automatically receive future edits.

The student TinyURL is copied from the class deck; its destination has not been checked. The solution TinyURL and Gist fields are blank rather than invented. Record both short links and full destinations when configured. The notebooks currently generate their illustrative data internally. The CSV is an exact snapshot, not an active external dependency. Moving to a Gist must update and test both notebooks together.

## Routine

1. Update the class deck and this chapter's notebooks/Pingo/data as needed.
2. Check that tasks, outputs, solutions and Pingo answers agree.
3. Generate and inspect the student PDF, excluding answers and Pingo.
4. Push the chapter folder and verify published Colab/data links.
5. Upload the student PDF before class; share solutions afterwards when appropriate.
