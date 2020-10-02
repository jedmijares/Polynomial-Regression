import numpy as np
import matplotlib.pyplot as plt

def loss(data, theta, power):
    error = 0.0
    for point in data:
        sum = 0.0
        for i in range(len(theta)):
            sum += theta[i] * (point[0] ** i)
        error += (sum - point[1]) * (point[0] ** power)
    return error/len(data)

def generateLine(thetas, xVals):
    yVals = 0
    for i in range(len(thetas)):
        yVals += thetas[i] * xVals ** i
    return yVals

def meanSquaredError(thetas, data):
    error = 0.0
    for point in data:
        sum = 0.0
        for i in range(len(theta)):
            sum += theta[i] * (point[0] ** i)
        error += ((sum - point[1]) ** 2)
    return error/len(data)

data = np.genfromtxt(r'data\synthetic-1.csv', delimiter=',')

plt.scatter(data[:,0], data[:,1])

theta = [1.0] * 3
alpha = (1.0 * 10**-5)
for i in range(1000):
    for j in range(len(theta)):
        theta[j] = theta[j] - (alpha * loss(data, theta, j))

x = np.linspace(-3,3)
y = theta[0] + theta[1] * x
second = generateLine(theta, x)
plt.plot(x, second, '-r', label='second order approximation')
print(meanSquaredError(theta, data))
plt.show()