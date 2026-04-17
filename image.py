import streamlit as st

from google import genai
from dotenv import load_dotenv
import os

from PIL import Image

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key = api_key)

img = st.file_uploader(
        "upload the photos of your note",
        type = ['jpg','jpeg','png'],
        accept_multiple_files=True
    )



if img:
    PIL_img = []

    for i in img:
        pil_image = Image.open(i)   # single image
        PIL_img.append(pil_image) 

    prompt = """summarize the picture in note format at mx 100 word, 
    make sure to add necessary markdown to differentiate different section"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[PIL_img,prompt],
    )

    st.markdown(response.text)