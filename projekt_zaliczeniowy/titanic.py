import numpy as np
import pandas as pd

# Preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Drzewa decyzyjne
from sklearn.tree import DecisionTreeClassifier

# Miary jakości
from sklearn.metrics import precision_score

# Wizualizacja drzew decyzyjnych
from sklearn.externals.six import StringIO  
from IPython.display import Image  
from sklearn.tree import export_graphviz
import pydotplus
# Przechowywanie modeli
import pickle

# Wczytanie danych
titanic = pd.read_csv("dataset/titanic.csv") 
print(titanic.head(n=5))


# Usun niepotrzebne kolumny
X = titanic.drop(columns=["PassengerId", "Name", "Ticket", 
                          "Cabin", "Survived", "Embarked"])

y = titanic.loc[:, "Survived"]
                        
# transformacja cechy plci na binarna
encoder = LabelEncoder()
sex_category = titanic.loc[:, "Sex"]
encoder.fit(sex_category)
binary_cat = encoder.transform(sex_category)

X["Sex"] = binary_cat
# 0 female
# 1 male

print(X.head(n=5))

# Znalezienie brakujących wartości w kolumnie age. Uzupełniam srednia wieku.
X.info()
mean_age = X["Age"].mean() 
X["Age"] = X["Age"].fillna(mean_age) 
X.info()


# Podział zbioru na treningowy(80%) i testowy(20%) 
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2)

print("Zbiór treningowy:", train_X.shape, train_y.shape)
print("Zbiór testowy:", test_X.shape, test_y.shape)

# uczenie modelu drzewa decyzyjnego
tree = DecisionTreeClassifier()
tree.fit(train_X, train_y)

# predykcja na zbiorze testowym
predicted_y = tree.predict(test_X)

precision = precision_score(test_y, predicted_y, average="micro")
print("Precyzja: {:.2f}".format(precision))


titanic_feature_names = X.columns
#  nazwy przwidywanych klas
titanic_class_names = y.unique()

# Wizualizacja drzewa decyzyjnego

# dot_data = StringIO()
# export_graphviz(tree, out_file=dot_data,  
#                 filled=True, rounded=True,
#                 special_characters=True)
# graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
# Image(graph.create_png())

#Zapisanie modelu
model = (encoder, tree)

with open("titanic.pkl", "wb") as model_file:
  pickle.dump(model, model_file)