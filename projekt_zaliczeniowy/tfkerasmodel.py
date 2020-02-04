#Korzystam z wcześniej wytrenowanego zbioru do wieku i plci
# git clone https://github.com/dzkb/age-gender-estimation

# Musimy również pobrać sam zapisany model, czyli liczby(wagi) opisujące połączenia pomiędzy kolejnymi neuronami w głębokiej sieci neuronowej.
# wget https://github.com/yu4u/age-gender-estimation/releases/download/v0.5/weights.29-3.76_utk.hdf5

# potrzebne, by zaimportować pobrane repozytorium
import sys
sys.path.append("./age-gender-estimation")
from PIL import Image
import numpy as np
from wide_resnet import WideResNet

#Budujemy model: tworzymy obiekt klasy WideResNet
deep_model = WideResNet(image_size=64)
deep_model = deep_model()
deep_model.load_weights("weights.29-3.76_utk.hdf5")
# deep_model.summary()

# Powyższa lista opisuje architekturę sieci neuronowej - istotne są dwie rzeczy:
# input layer  - `input_4 (InputLayer)`
# output layer - `pred_gender` i `pred_age`

# Wczytanie i przygotowanie obrazu
adam = Image.open("resources/adam.jpg")
adam = adam.resize((64, 64))

# Aby możliwe było przekazanie obrazu do konwolucyjnej sieci neuronowej, wymagane jest 
# przekształcenie go do postaci tablicy NumPy
np_adam = np.array(adam)
np_adam.shape
array_adam = np_adam.reshape((1, 64, 64, 3))


prediction = deep_model.predict(array_adam)
gender = np.argmax(prediction[0])
age = np.argmax(prediction[1])
print(f" Age: {age}")
print(f"Gender: {gender}")





