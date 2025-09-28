## 📚 Literature Review

### 📝 Key Papers

- [AskChart: Universal Chart Understanding through Textual Enhancement](https://arxiv.org/abs/2412.19146)  
  *Proposes a universal approach for chart understanding using textual enhancement.*

- [VProChart: Answering Chart Question through Visual Perception Alignment Agent and Programmatic Solution Reasoning](https://arxiv.org/abs/2409.01667)  
  *Introduces a visual perception alignment agent for chart question answering.*

- [OneChart: Purify the Chart Structural Extraction via One Auxiliary Token](https://arxiv.org/abs/2404.09987)  
  *Presents a method for improving chart structure extraction using an auxiliary token.*

- [ChartCoder: Advancing Multimodal Large Language Model for Chart-to-Code Generation](https://arxiv.org/abs/2501.06598)  
  *Focuses on generating code from charts using multimodal LLMs.*

- [deplot (arXiv:2210.03347)](https://arxiv.org/abs/2210.03347)  
  *Transformer-based model for chart-to-table conversion.*

- [Model card for Pix2Struct - Finetuned on ChartQA](https://huggingface.co/google/pix2struct-chartqa-base)  
  *Pix2Struct model adapted for chart question answering.*

- [DiagramAgent/Diagram_to_Code_Agent](https://huggingface.co/DiagramAgent/Diagram_to_Code_Agent)  
  *Agent for converting diagrams to code.*

- [MiniCPM: Unveiling the Potential of Small Language Models with Scalable Training Strategies](https://arxiv.org/abs/2404.06395)  
  *Discusses scalable training strategies for small language models.*

 - [Enhancing Chart-to-Text Conversion](https://cs231n.stanford.edu/2024/papers/enhancing-chart-to-text-conversion.pdf) 
  *Explores techniques to enhance the chart-to-text conversion capabilities of the Matcha framework, which employs
a Vision Transformer (ViT) encoder and a transformer decoder*

#### 🌟 Other Notable Works

- [AskChart (GitHub)](https://github.com/Sootung/AskChart)
  *Discusses advancement of multimodal large language models (MLLMs).*

---

### 📊 Datasets

- [niups/DeepRuleDataset](https://huggingface.co/datasets/niups/DeepRuleDataset/tree/main)  
  *A dataset for deep rule-based chart understanding.*

---

## 🛠️ Related Services & Tools

Below is a list of chart digitization services and tools identified so far, with brief notes on applicability and usefulness:

- [deplot (Hugging Face)](https://huggingface.co/spaces/nielsr/deplot)  
  *Transformer-based model for chart-to-table conversion; works well for simple bar/line charts, but may struggle with complex layouts.*

### 🧪 Unchecked Tools That May Work

- [ChartOCR](https://github.com/zmykevin/ChartOCR)  
  *Open-source deep learning approach for extracting data from chart images; promising for automation, but may require setup and tuning.*

- [Pix2Struct](https://huggingface.co/docs/transformers/en/model_doc/pix2struct)  
  *Vision-language model for structured data extraction from images; experimental, best for prototyping and research.*

### ⚠️ Checked Tools That Didn't Work or Had Issues

Here are some additional tools that I found not user-friendly, lacking a demo, or with poor performance:

- [PlotDigitizer](https://plotdigitizer.com/)  
  *User-friendly web app for manual and semi-automatic chart digitization; good for quick, small-scale tasks.*

- [WebPlotDigitizer](https://automeris.io/) ([YouTube Demo](https://www.youtube.com/watch?v=-U15YSho61Y))  
  *Versatile, widely used tool supporting many chart types; offers both manual and automated extraction, suitable for research and batch processing. It is an app, not an API service. Most use cases seem to come from academia.*

- [Docupipe.ai](https://www.docupipe.ai/)  
  *AI platform for document automation; chart extraction is one of many features, more suited for business workflows. Chart data extraction was inaccurate in my tests.*

- [ProductHubX - Chart2Data](https://producthubx.com/product/chart2data/143843)  
  *Marketplace product for chart digitization; details and performance may vary. Did not work in my tests.*

- [SciSpace](https://scispace.com/extract-data)  
  *AI-powered tool for extracting data from scientific PDFs, including charts; best for academic/research use cases. Uploading files can be slow or unreliable.*

- [Trullion](https://trullion.com/products/data-extract/)  
  *Enterprise solution focused on financial documents; chart extraction is a feature, but the platform is not open for general use. Requires booking a demo; unclear if chart extraction works as advertised.*

- [Extracta.ai](https://extracta.ai/)  
  *Online service for extracting data from images and documents; chart support is basic, but can be integrated into pipelines. Manual field setting required; output was sometimes invalid.*

- [Mindee](https://www.mindee.com)  
  *Commercial API for document and data extraction; chart support is limited, but useful for broader document workflows. Requires creating a custom model for charts, which did not work as expected.*

- [Chart2Data (Microsoft Store)](https://apps.microsoft.com/detail/9wzdncrdrx6f?hl=pl-PL&gl=PL)  
  *Windows app for chart digitization; easy to use, but limited to desktop and closed-source. GUI app with a poor interface.*