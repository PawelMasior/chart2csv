# chart2csv

**chart2csv** is a research playground for converting chart images into reliable, structured data. This repository explores and compares different tools, models, and approaches for extracting data from visual charts.

## Project Goals

- Develop a robust pipeline to extract data from chart images (e.g., bar, pie, line charts)
- Evaluate and compare existing chart digitization tools and AI models
- Identify best practices and common pitfalls in chart-to-data extraction
- Experiment with combining multiple models and cross-validation for improved accuracy

## Related Services & Tools

Below is a list of chart digitization services and tools identified so far:

- [deplot (Hugging Face)](https://huggingface.co/spaces/nielsr/deplot) – Transformer-based model for chart-to-table conversion; works well for simple bar/line charts, but may struggle with complex layouts.

### Unchecked tools that may work
- [ChartOCR](https://github.com/zmykevin/ChartOCR) – Open-source deep learning approach for extracting data from chart images; promising for automation, but may require setup and tuning.
- [Pix2Struct](https://huggingface.co/docs/transformers/en/model_doc/pix2struct) – Vision-language model for structured data extraction from images; experimental, best for prototyping and research.
- [Chart2Data (Microsoft Store)](https://apps.microsoft.com/detail/9wzdncrdrx6f?hl=pl-PL&gl=PL) – Windows app for chart digitization; easy to use, but limited to desktop and closed-source.
- [Mindee](https://www.mindee.com) – Commercial API for document and data extraction; chart support is limited, but useful for broader document workflows.
- [Extracta.ai](https://extracta.ai/) – Online service for extracting data from images and documents; chart support is basic, but can be integrated into pipelines.
- [Trullion](https://trullion.com/products/data-extract/) – Enterprise solution focused on financial documents; chart extraction is a feature, but platform is not open for general use.
- [SciSpace](https://scispace.com/extract-data) – AI-powered tool for extracting data from scientific PDFs, including charts; best for academic/research use cases.
- [ProductHubX - Chart2Data](https://producthubx.com/product/chart2data/143843) – Marketplace product for chart digitization; details and performance may vary.
- [Docupipe.ai](https://www.docupipe.ai/) – AI platform for document automation; chart extraction is one of many features, more suited for business workflows.

### Checked tools that didnt work

Here are some additional tools, that i didnt find user friendly, no demo or bad performance
- [PlotDigitizer](https://plotdigitizer.com/) – User-friendly web app for manual and semi-automatic chart digitization; good for quick, small-scale tasks.
- [WebPlotDigitizer](https://automeris.io/) ([YouTube Demo](https://www.youtube.com/watch?v=-U15YSho61Y)) – Versatile, widely used tool supporting many chart types; offers both manual and automated extraction, suitable for research and batch processing. It is an app - not API service. Looks like most usecases came from academia.

## Usage Example

This repository includes a sample script [`src/deplot.py`](src/deplot.py) that demonstrates how to use the DePlot model to extract structured data from a chart image. The script loads an example chart (`charts/figure_10.png`), runs it through the DePlot model, and prints the extracted table or CSV data. You can adapt this script for your own chart images or integrate it into your data extraction pipeline.


## Approach & Key Considerations

- **Focus on charts directly:** Work with chart images, not full PDF pages. (Requires chart cropping/extraction step.)
- **Avoid per-chart prompting:** Using a unique prompt for each chart is inefficient and slows iteration. Prefer generic, reusable approaches.
- **LLM limitations:** Raw chart images fed to LLMs can result in hallucinated or incorrect numbers. Preprocessing and structured extraction are preferred.
- **Stepwise extraction:** Break down the process—first extract easy metadata (chart type, axis ranges, number of variables/colors, legend info, etc.), then extract data points.
- **Cross-validation:** Where possible, compare outputs from multiple models/tools to improve reliability.
- **Contextual information:** Use surrounding text (e.g., captions, labels) as additional context when available.

---

_This repository is a work in progress. Contributions, suggestions, and tool recommendations are welcome!_
