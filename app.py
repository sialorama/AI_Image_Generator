# Import modules
from openai import OpenAI
from PIL import Image
import streamlit as st
from apikey import apikey
from streamlit_carousel import carousel

# Initialize your image generation client
client=OpenAI(api_key=apikey)

single_img=dict(
            title="",
            text="",
            interval=None,
            img="",

        )

def generate_images(image_description, number_of_images):
    image_galery = []
    for i in range (number_of_images):
        img_response = client.images.generate(
                        model = "dall-e-3",
                        prompt = image_description,
                        n = 1,
                        size = "1024x1024"
                        )
        image_url = img_response.data[0].url
        new_image=single_img.copy()
        new_image["title"]=f"Image(i+1)"
        new_image["texte"]=image_description
        new_image["img"]=image_url
        image_galery.append(new_image)

    return image_galery

st.set_page_config(page_title="Générateur d'images Dalle", page_icon=":camera:", layout="wide")

# Create title
st.title("Générateur d'images avec Dall-E-3")

# Create a subheader
st.subheader("Réalisé avec le puissant model de génération d'images API-Dall-E")
image_description = st.text_input("Entrer une description de l'image que vous souhaitez générer",  "Brest by night")
number_of_images = st.number_input("Séléctionnez le nombre d'images que vous vouez générer", min_value=1, max_value=10, value=1)

# Create a submit button
if st.button("Générer"):
    generate_images = generate_images(image_description, number_of_images)

    carousel(items=generate_images, width=1)