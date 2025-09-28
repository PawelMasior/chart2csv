# %reset -f
import os
import base64
import base64
import json
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image
from dotenv import load_dotenv
import openai
from pydantic import BaseModel, Field
from typing import List, Dict, Optional

load_dotenv()
client_openai = openai.OpenAI(api_key=os.getenv('openai_key2'))

# =============================================================================
# images
# =============================================================================
figures = [
    #'figure_1.png',
    #'figure_10.png',
    'figure_11.png',
    'figure_2.png',
    'figure_6.png',
    'figure_7.png',
    'figure_online_travel_booking.png',
    ]

for fig in figures:
    name = fig.split('.')[0]

    image_path = os.path.join("..", "input", "charts", fig)
    image = Image.open(image_path).convert("RGB")
    #with open(image_path, "rb") as f: image_b64 = base64.b64encode(f.read()).decode()

    buffer = BytesIO()
    image.save(buffer, format="PNG")   # you can choose "JPEG", "PNG", etc.
    image_bytes = buffer.getvalue()
    image_b64 = base64.b64encode(image_bytes).decode("utf-8")

    # =============================================================================
    # deplot
    # =============================================================================
    from transformers import Pix2StructProcessor, Pix2StructForConditionalGeneration
    import requests
    processor = Pix2StructProcessor.from_pretrained('google/deplot')
    model = Pix2StructForConditionalGeneration.from_pretrained('google/deplot')
    
    inputs = processor(images=image, text="Generate underlying data table of the figure below:", return_tensors="pt")
    predictions = model.generate(**inputs, max_new_tokens=512)
    out_deplot = processor.decode(predictions[0], skip_special_tokens=True)
    # print(processor.decode(predictions[0], skip_special_tokens=True))
    with open(os.path.join("..", "out", f"{name}_deplot.txt"), "w", encoding="utf-8") as f:
        f.write(out_deplot)
    with open(os.path.join("..", "out", f"{name}_deplot.txt"), "r", encoding="utf-8") as f:
        out_deplot = f.read()
    
    # =============================================================================
    # openai
    # =============================================================================
    class LegendItem(BaseModel):
        label: str = Field(..., description="Legend label")
        color: str = Field(..., description="Legend color in hex or name")
    
    class FormatAtr(BaseModel):
        title: str = Field(..., description="Chart title")
        chart_type: str = Field(..., description="Chart type")
        x_name: str = Field(..., description="X-axis name")
        x_type: str = Field(..., description="X-axis type (e.g., categorical, numeric, datetime)")
        y_name: str = Field(..., description="Y-axis name")
        y_type: str = Field(..., description="Y-axis type (e.g., categorical, numeric, percentage)")
        x_min: Optional[float] = Field(None, description="Minimum value on X-axis (if numeric)")
        x_max: Optional[float] = Field(None, description="Maximum value on X-axis (if numeric)")
        y_min: Optional[float] = Field(None, description="Minimum value on Y-axis (if numeric)")
        y_max: Optional[float] = Field(None, description="Maximum value on Y-axis (if numeric)")
        legend: List[LegendItem] = Field(
            ..., description="List of legend items with their colors"
        )
        
    def _openai_chart_atr(image_b64: str, out_deplot: str) -> dict:
        syst_msg = "You are an assistant that extracts structured chart attributes from plots."
        user_msg = f"""
        Extract these attributes:
        - title
        - x-axis name and type
        - y-axis name and type
        - min and max values for both axes (if numeric)
        - legend items with their colors
    
        Here is a DePlot extraction for reference:
        {out_deplot}
        """
    
        response = client_openai.chat.completions.parse(
            model="gpt-4o-mini",   # or "gpt-4o" for more accuracy
            messages=[
                {"role": "system", "content": syst_msg},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": user_msg},
                        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_b64}"}}
                    ],
                },
            ],
            temperature=0.0,
            max_tokens=1500,
            response_format=FormatAtr,
        )
        return response.choices[0].message.parsed.dict()
    
    def _openai_chart_data(image_b64: str, out_deplot: str, chart_atr: dict) -> str:
        syst_msg = """
        You are converting charts to original data.
        Respond with *only* a CSV string (no explanations, no markdown).
        """
    
        user_msg = f"""
        Prepare CSV for the underlying chart data.
        Columns should match what is visible in the chart.
        
        Chart attributes (for guidance):
        {json.dumps(chart_atr, indent=2)}
    
        Here is a DePlot extraction for reference:
        {out_deplot}
        """
    
        response = client_openai.chat.completions.create(
            model="gpt-4o-mini",   # or "gpt-4o" for more accuracy
            messages=[
                {"role": "system", "content": syst_msg},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": user_msg},
                        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_b64}"}}
                    ]
                }
            ],
            temperature=0.0,
            max_tokens=2000   # safer for longer CSVs
        )
        return response.choices[0].message.content.strip()
    
    chart_atr = _openai_chart_atr(image_b64, out_deplot)
    chart_csv = _openai_chart_data(image_b64, out_deplot, chart_atr)
    with open(os.path.join("..", "out", f"{name}_deplot_openai.txt"), "w", encoding="utf-8") as f:
        f.write(chart_csv)
    print(f"{name} CSV Output:\n", chart_csv)

    # to do: replot!

# =============================================================================
# # =============================================================================
# # other - to speed up pytorch
# # =============================================================================
# from transformers import BitsAndBytesConfig
# quantization_config = BitsAndBytesConfig(load_in_8bit=True)
# model = Pix2StructForConditionalGeneration.from_pretrained(
#     "google/deplot",
#     quantization_config=quantization_config,
#     device_map="auto"
# )
# =============================================================================
# =============================================================================
# # =============================================================================
# # other - login huggingface
# # =============================================================================
# from dotenv import load_dotenv
# load_dotenv()
# huggingface_key = os.getenv('huggingface')
# from huggingface_hub import login
# login(f"{huggingface_key}")
# =============================================================================
