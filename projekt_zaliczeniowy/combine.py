import numpy as np
import pandas as pd

from flask import Flask, request

import pickle
from PIL import Image

import tensorflow as tf

# właściwa część aplikacji
app = Flask(__name__)

with open("model.pkl", "rb") as f:
  labelEncoder, treeModel = pickle.load(f)

import sys
sys.path.append("/age_gender_estimation")


from age_gender_estimation.wide_resnet import WideResNet
deep_model = WideResNet(image_size=64)
deep_model = deep_model()
deep_model.load_weights("weights.29-3.76_utk.hdf5")
deep_model._make_predict_function()

# miejsce na definicję endpointu
@app.route("/estimate", methods=["POST"])
def index():
  image_file = request.files["image"]
  n_children = request.form["children"]
  n_siblings = request.form["siblings"]
  p_class = request.form["class"]
  
  
  img = Image.open(image_file)
  img = img.resize((64, 64))
  
  np_img = np.array(img)
  np_img = np_img.reshape((1, 64, 64, 3))
  
  sex, age = deep_model.predict(np_img)
  
  features = [p_class, np.argmax(sex), np.argmax(age), n_siblings, n_children]
  np_features = np.array(features).reshape((1, -1))
  survival_prediction = treeModel.predict(np_features)
  
  # 2. przyjęcie danych z obiektu request
  #     - zdjęcie z request.files
  #     - pozostałe pola z request.form
  # 3. przygotowanie obrazu do przetworzenia
  # 4. przetworzenie obrazu i pozyskanie wartości wieku i płci
  # 5. przygotowanie wektora wejściowego dla drzewa decyzyjnego (m. in. preprocessing)
  # 6. przekazanie wektora do drzewa decyzyjnego
  # 7. zwrócenie wyniku
  
  return str(survival_prediction)

app.run()