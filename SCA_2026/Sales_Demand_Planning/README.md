# Sales & Demand Planning

The working source is one class PowerPoint in the chapter slides folder; the student PDF is exported from it. There is no separate student PowerPoint.

Run Sales_Demand_Planning_Student.ipynb in Jupyter or upload it to Colab. No external download or upload of the dataset is necessary: the raw snapshot is embedded and supplied in data/. The solution notebook uses the same case/functions/tasks with the prescribed settings and explanations.

Five tasks: verify the history; compare promotion weeks; change forecast window3→6; reset to SKU_A/window3/factor1 and change inventory position180→90; reset position180 and change buffer factor1→1.65. Earlier task settings do not contaminate later stock scenarios.

Use the class deck for teaching. Its significance table and Pingo QR remain in the master; they are excluded from the student PDF. Import Sales_Demand_Planning_Pingo.xml into the intended Pingo session; its five questions match these five runs. Live import/session access has not been tested.

Export again with `python export_student_pdf.py`. The exporter reads chapter.json and excludes slides by title text, checking the required exclusions. It writes a page-selection receipt beside the PDF. Rendering requires LibreOffice; PDF processing requires pypdf.

chapter.json records actual file locations, dataset lineage, evaluation conditions and publication status. Notebook links in the class deck are local files. Colab repository links and TinyURLs are pending publication; this task does not claim a Git push, Gist or short-link update.


Visual update: the class deck contains 26 slides. Four theory tables/text explanations are replaced by plots or a stock-gap diagram. Two instructor-only `Solutions:` plot slides follow the significance table. The student PDF still has 22 pages; the exporter excludes significance, solution plots and Pingo. The same five exercises now display corresponding notebook plots. Analytical rules and results are unchanged.
