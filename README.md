# ClasificadorDeImagenes
Código de ejemplo para clasificación de imágenes usando Streamlit
# 1. Crear y preparar el entorno virtual
- conda create -n C2 anaconda python 
- conda activate C2
- conda install ipykernel
- python -m ipykernel install --user --name C2 --display-name "C2"
- conda install tensorflow-gpu cudatoolkit
- pip install tensorflow
- pip install jupyter
- pip install keras
- pip install numpy scipy Pillow cython matplotlib scikit-image opencv-python h5py imgaug IPython[all] streamlit

# 2. Crear el código de la aplicación-CNN_for_signs.py

# 3. Ejecutar el código: 
streamlit run CNN_for_signs.py

