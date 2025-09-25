# %reset -f
import os
import base64
from PIL import Image

# =============================================================================
# image
# =============================================================================
image_path = os.path.join("..", "input", "charts", "figure_10.png")
image = Image.open(image_path).convert("RGB")
with open(image_path, "rb") as f: 
    image_b64 = base64.b64encode(f.read()).decode()

# =============================================================================
# deplot
# =============================================================================
# =============================================================================
# from transformers import Pix2StructProcessor, Pix2StructForConditionalGeneration
# import requests
# processor = Pix2StructProcessor.from_pretrained('google/deplot')
# model = Pix2StructForConditionalGeneration.from_pretrained('google/deplot')
# 
# inputs = processor(images=image, text="Generate underlying data table of the figure below:", return_tensors="pt")
# predictions = model.generate(**inputs, max_new_tokens=512)
# print(processor.decode(predictions[0], skip_special_tokens=True))
# # =============================================================================
# # TITLE |  <0x0A> Midpoint Yield | Super Prime | Prime | Secondary <0x0A> Jun-15 | 7.5 | 7.1 | 10.2 <0x0A> Dec-18 | 7.1 | 7. | 8.9 <0x0A> Jun-16 | 7.6 | 7. | 10.0 <0x0A> Dec-17 | 6.5 | 7. | 8.8 <0x0A> Jun-18 | 6.4 | 7. | 8.0 <0x0A> Dec-18 | 6.5 | 7. | 8.5 <0x0A> Jun-19 | 6.2 | 7. | 8.6 <0x0A> Dec-19 | 6.1 | 7. | 8.3 <0x0A> Jun-20 | 6.0 | 6.6 | 7.8 <0x0A> Dec-20 | 5.4 | 6.2 | 7.3 <0x0A> Jun-21 | 4.4 | 5.2 | 5.8 <0x0A> Dec-21 | 4.2 | 5.2 | 5.8 <0x0A> Dec-22 | 4.7 | 5.2 | 6.5 <0x0A> Dec-23 | 5.6 | 6.1 | 6.8 <0x0A> Jun-23 | 6.0 | 6.4 | 6.5 <0x0A> Dec-24 | 6.2 | 6.2 | 6.8 <0x0A> Jun-25 | 6.2 | 6.2 | 6.8
# # =============================================================================
# =============================================================================
out_deplot = "TITLE |  <0x0A> Midpoint Yield | Super Prime | Prime | Secondary <0x0A> Jun-15 | 7.5 | 7.1 | 10.2 <0x0A> Dec-18 | 7.1 | 7. | 8.9 <0x0A> Jun-16 | 7.6 | 7. | 10.0 <0x0A> Dec-17 | 6.5 | 7. | 8.8 <0x0A> Jun-18 | 6.4 | 7. | 8.0 <0x0A> Dec-18 | 6.5 | 7. | 8.5 <0x0A> Jun-19 | 6.2 | 7. | 8.6 <0x0A> Dec-19 | 6.1 | 7. | 8.3 <0x0A> Jun-20 | 6.0 | 6.6 | 7.8 <0x0A> Dec-20 | 5.4 | 6.2 | 7.3 <0x0A> Jun-21 | 4.4 | 5.2 | 5.8 <0x0A> Dec-21 | 4.2 | 5.2 | 5.8 <0x0A> Dec-22 | 4.7 | 5.2 | 6.5 <0x0A> Dec-23 | 5.6 | 6.1 | 6.8 <0x0A> Jun-23 | 6.0 | 6.4 | 6.5 <0x0A> Dec-24 | 6.2 | 6.2 | 6.8 <0x0A> Jun-25 | 6.2 | 6.2 | 6.8"


# =============================================================================
# openai
# =============================================================================
from dotenv import load_dotenv
import openai
load_dotenv()
client_openai = openai.OpenAI(api_key=os.getenv('openai_key2'))

# better to recognize firs variables, axis values etc.

syst_msg = """
You are converting charts to original data.
Respond with *only* a CSV string (no explanations, no markdown).
Columns: Date, Super Prime, Prime, Secondary.
"""

user_msg = f"""
Prepare CSV for the underlying data.
Also, here is a DePlot extraction for reference:
{out_deplot}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",   # or "gpt-4o" for more accuracy
    messages=[
        {"role": "system", "content": syst_msg},
        {
            "role": "user",
            "content": [
                {"type": "text", "text": user_msg},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/png;base64,{image_b64}"}
                }
            ]
        }
    ],
    temperature=0.0,   # works with GPT-4 family
    max_tokens=1500    # CSV won’t be cut off
)

csv_output = response.choices[0].message.content
print("CSV Output:\n", csv_output)

# =============================================================================
# CSV Output:
#  Here is the CSV format for the underlying data:
# 
# ```csv
# Date,Super Prime,Prime,Secondary
# Jun-15,7.5,7.1,10.2
# Jun-16,7.6,7.0,10.0
# Dec-16,7.1,7.0,8.9
# Dec-17,6.5,7.0,8.8
# Jun-18,6.4,7.0,8.0
# Dec-18,6.5,7.0,8.5
# Jun-19,6.2,7.0,8.6
# Dec-19,6.1,7.0,8.3
# Jun-20,6.0,6.6,7.8
# Dec-20,5.4,6.2,7.3
# Jun-21,4.4,5.2,5.8
# Dec-21,4.2,5.2,5.8
# Dec-22,4.7,5.2,6.5
# Dec-23,5.6,6.1,6.8
# Jun-23,6.0,6.4,6.5
# Dec-24,6.2,6.2,6.8
# Jun-25,6.2,6.2,6.8
# ```
# =============================================================================


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
# # login
# # =============================================================================
# from dotenv import load_dotenv
# load_dotenv()
# huggingface_key = os.getenv('huggingface')
# from huggingface_hub import login
# login(f"{huggingface_key}")
# =============================================================================
