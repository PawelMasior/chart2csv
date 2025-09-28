# chart2csv

**Tags:** Visual Question Answering, Transformers, PyTorch, pix2struct, image-to-text  
**Languages:** Python, Shell, Markdown, Jupyter Notebook, YAML  
**arXiv:** [2210.03347](https://arxiv.org/abs/2210.03347)  
**License:** apache-2.0

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
