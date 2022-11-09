#Распознавание букв
import numpy as np 

w0 = np.zeros((40))
w1 = np.zeros((40))
w2 = np.zeros((40))

D = np.array([
   [1,1,1,1,1,1,1,1,
    0,0,0,1,1,0,0,1,
    1,1,1,1,1,0,0,1,
    1,0,0,0,1,0,0,1,
    1,1,1,1,1,1,1,1,],
   [0,1,1,1,0,1,1,0,
    0,0,0,1,1,0,0,1,
    0,1,1,1,1,0,0,1,
    0,1,0,0,1,0,0,1,
    0,1,1,1,0,1,1,0,],
   [1,1,1,1,1,1,1,1,
    0,0,0,1,1,0,0,1,
    1,1,1,1,1,0,0,1,
    0,0,0,1,1,0,0,1,
    1,1,1,1,1,1,1,1,],
   [0,1,1,1,0,1,1,0,
    0,0,0,1,1,0,0,1,
    0,1,1,1,1,0,0,1,
    0,0,0,1,1,0,0,1,
    0,1,1,1,0,1,1,0,],
   [1,1,1,1,1,1,1,1,
    1,0,0,0,1,0,0,1,
    1,1,1,1,1,0,0,1,
    1,0,0,1,1,0,0,1,
    1,1,1,1,1,1,1,1,],
   [1,1,1,0,0,1,1,0,
    1,0,0,0,1,0,0,1,
    1,1,1,0,1,0,0,1,
    1,0,1,0,1,0,0,1,
    1,1,1,0,0,1,1,0,],
])

Y0 = np.array([1,1,0,0,0,0])
Y1 = np.array([0,0,1,1,0,0])
Y2 = np.array([0,0,0,0,1,1])

α =  0.2 
β = -0.4 
σ = lambda x: 1 if x > 0 else 0

def f(x, _w):
    s = β + np.sum(x @ _w)
    return σ(s)

def train(w, D, Y):
    _w = w.copy()
    for x, y in zip(D, Y):
        w += α * (y - f(x, w)) * x
    return (w != _w).any()

while train(w0, D, Y0) and train(w1, D, Y1) and train(w2, D, Y2):
    print(w0, w1, w2)

D = np.array([
   [1,1,1,1,1,1,1,1,
    0,0,0,1,1,0,0,1,
    1,1,1,1,1,0,0,1,
    1,0,0,0,1,0,0,1,
    1,1,1,1,1,1,1,1,], 
   [1,1,1,1,1,1,1,1,
    0,0,0,1,1,0,0,1,
    1,1,1,1,1,0,0,1,
    0,0,0,1,1,0,0,1,
    1,1,1,1,1,1,1,1,],
   [1,1,1,0,0,1,1,0,
    1,0,0,0,1,0,0,1,
    1,1,1,0,1,0,0,1,
    1,0,1,0,1,0,0,1,
    1,1,1,0,0,1,1,0,],
])

for x in D:
    print(x, f(x, w0), f(x,w1), f(x, w2))

