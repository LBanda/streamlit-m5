from tensorflow import keras
from tensorflow.keras import layers

#Crear red neuronal de una capa 
model = keras.Sequential([
    layers.Dense(units=1, input_shape=[10])
])

print(model.summary())

w, b = model.weights
print(w)
print(b)
