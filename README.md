# chart2csv

<h2 align="center">Chart2CSV: Chart to Data</h2>

<p align="center">
    <img alt="hf_space" src="https://img.shields.io/badge/🤗-Placeholder%20In%20HF-blue.svg">
    <img alt="hf_space" src="https://img.shields.io/badge/🤗-Placeholder%20In%20HF-red.svg">
    <img alt="arXiv" src="https://img.shields.io/badge/Arxiv-2401.15947-b31b1b.svg?logo=arXiv">
    <img alt="youtube" src="https://img.shields.io/badge/-YouTube-000000?logo=youtube&amp;logoColor=FF0000">
    <img alt="GitHub issues" src="https://img.shields.io/github.com/PawelMasior/chart2csv?color=critical&amp;label=Issues">
    <img alt="tags" src="https://img.shields.io/badge/Tags-Visual%20QA%2C%20Transformers%2C%20PyTorch%2C%20pix2struct%2C%20image--to--text-blueviolet">
    <img alt="languages" src="https://img.shields.io/badge/Languages-Python%2C%20Shell%2C%20Markdown%2C%20Jupyter%20Notebook%2C%20YAML-brightgreen">
    <a href="https://github.com/PawelMasior/chart2csv/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0-yellow" alt="License"></a>
</p>

**chart2csv** is a research playground for converting chart images into reliable, structured data. This repository explores and compares different tools, models, and approaches for extracting data from visual charts.

## Project Goals

- Develop a robust pipeline to extract data from chart images (e.g., bar, pie, line charts)
- Evaluate and compare existing chart digitization tools and AI models
- Identify best practices and common pitfalls in chart-to-data extraction
- Experiment with combining multiple models and cross-validation for improved accuracy

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