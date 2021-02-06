import tensorflow as tf
import keras
import streamlit as st
import numpy as np
from PIL import Image
from skimage.transform import resize
from tensorflow.keras.applications.imagenet_utils import preprocess_input

tf.function(experimental_relax_shapes=False)

st.title('Clasificador de Imágenes')
image_size = 64
def main():
    model = ''
    if model=='':
        model = tf.keras.models.load_model('cnn_3.h5')
    pred_label = ''
    img_file_buffer = st.file_uploader('Cargar una imagen')
    if img_file_buffer is not None:
        image = np.array(Image.open(img_file_buffer))  
        st.image(image, caption='Image', use_column_width=False)

    if st.button('Predicción'):
        image_resize = resize(image, (image_size, image_size))
        x = preprocess_input(image_resize*255)
        x = np.expand_dims(x, axis=0)
        pred_prob = model.predict(x)
        st.success(f'Es el número: {np.argmax(pred_prob)}')

if __name__=='__main__':
    main()
