import numpy as np

# Creación de un conjunto de datos para entrenamiento
trX = np.linspace( -2, 2, 10)
trY = 5 * trX + 10.0
def gradient_func(W, x, b):
    return W*x + b
# Definición de los ajustes y parámetros iniciales
num_steps = 100
learningRate =  0.10
criteria = 1e-8
b = 1
W = 1

# Proceso iterativo
for step in range(0, num_steps):
    b_gradient = 0
    W_gradient = 0
    N = float(len(trX))
    for i in range(0, len(trX)):
        b_gradient -= (2/N) * (trY[i] - gradient_func(W, trX[i], b))
        W_gradient -= (2/N) * (trY[i] - gradient_func(W, trX[i], b)) * trX[i]
        print(W_gradient)
    print('=============================')   
    b = b - (learningRate * b_gradient)
    W = W - (learningRate * W_gradient)
    print(W_gradient, b_gradient)
    print(W, b)
    print('----')
    if max(abs(learningRate * b_gradient), abs(learningRate * W_gradient)) < criteria:
        break
  
# Impresión de los resultados
print("Los valores que se obtienen son:", W, b, "en pasos", step)