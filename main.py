import streamlit as st
from PIL import Image
from tensorflow.keras.models import load_model
from keras_contrib.layers.normalization.instancenormalization import InstanceNormalization
import numpy as np
from numpy import vstack


from bg import set_background

set_background('./bground/caballo-zebra.jpg')

cust = {'InstanceNormalization':InstanceNormalization}
model_horse_to_zebra = load_model('./g_model_Atob_023740.h5',cust)
model_zebra_to_horse = load_model('./g_model_BtoA_023740.h5',cust)

def load_image(image):
    image = np.array(image)
    image = image[np.newaxis, ...]
    return(image)


def generate_image(model,image):
    generated_image = model.predict(image)
    images = vstack(generated_image)
    images = (images+1)/2.0

    return(images)




st.title(" GAN web App: Horse to Zebra and viceversa")
st.image(Image.open('./1.png'))

pick = st.selectbox("Please, select a GAN model to use: ", ["Horse to Zebra GAN","Zebra to Horse GAN"])

if pick == "Horse to Zebra GAN":
    st.write("This is a GAN model for generating Zebra images from Horses")
    st.write("Try out the GAN model with a default image of a horse or simply upload an imgae")
    
    
    if st.button("Try with default image"):
        image = load_image(Image.open('./horse.jpg'))
        st.subheader("Horse image")
        st.image(image)

        st.subheader("Generated Zebra image")
        st.image(generate_image(model_horse_to_zebra,image))


    st.subheader("Upload an image file of a horse to convert it to a Zebra: ")
    uploaded_file = st.file_uploader("Upload JPG image file of a horse only",type=["jpg","jpeg","png"])

    if uploaded_file:
        image = load_image(Image.open(uploaded_file))
        st.image(generate_image(model_horse_to_zebra,image))
else:
    st.write("This is a GAN model for generating Horse images from Zebras")
    st.write("Try out the GAN model with a default image of a horse or simply upload an imgae")
    
    
    if st.button("Try with default image"):
        image = load_image(Image.open('./zebra.jpg'))
        st.subheader("Zebra image")
        st.image(image)

        st.subheader("Generated Horse image")
        st.image(generate_image(model_zebra_to_horse,image))


    st.subheader("Upload an image file of a zebra to convert it to a Horse: ")
    uploaded_file = st.file_uploader("Upload JPG image file of a horse only",type=["jpg","jpeg","png"])

    if uploaded_file:
        image = load_image(Image.open(uploaded_file))
        st.image(generate_image(model_zebra_to_horse,image))

        


