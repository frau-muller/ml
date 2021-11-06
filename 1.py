import numpy as np
weight = 0.1

def neural_network(input, weight):
    prediction = input * weight
    return prediction

number_of_toes = [8.5, 9.5, 10, 9]
input = number_of_toes[1]
pred = neural_network(input, weight)
print(pred)


weights = np.array([0.1, 0.2, 0])

def neural_network(input, weights):
    pred = input.dot(weights)
    return pred
toes = np.array([8.5, 9.5,9.9, 9.0])
wlrec = np.array([0.65,0.8,0.8,0.9])
nfans = np.array([1.2, 1.3, 0.5, 1.0])

input = np.array([toes[0], wlrec[0],nfans[0]])
pred = neural_network(input,weights)
print(pred)

a = np.array([0,1,2,3])
b = np.array([4,5,6,7])
c = np.random.rand(2,5)

print(a)
print(b)
print(c)

print(a*0.1)