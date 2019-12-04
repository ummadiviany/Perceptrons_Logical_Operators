import numpy as np

def cross_entropy(Y, P):
    Y = np.float_(Y)
    P = np.float_(P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))

Y=[1,0,1,1]
P=[0.4,0.6,0.1,0.5]

print("The correct answer is  4.8283137373")
print("And your code returned  %.10f" %cross_entropy(Y,P))


print("Correct!!")
