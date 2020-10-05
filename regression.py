import numpy as np
import matplotlib.pyplot as plt
import random

random.seed(12) # for repeatability

def loss(data, theta, power):
    error = 0.0
    for point in data:
        sum = 0.0
        for i in range(len(theta)):
            sum += theta[i] * (point[0] ** i)
        error += (sum - point[1]) * (point[0] ** power)
    return error/len(data)

def stochasticLoss(data, theta, power):
    point = random.choice(data)
    sum = 0.0
    for i in range(len(theta)):
        sum += theta[i] * (point[0] ** i)
    error = (sum - point[1]) * (point[0] ** power)
    return error

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

def regression(theta, data):
    alpha = (1.0 * 10**-5)
    # for _ in range(1000):
    for j in range(len(theta)):
        theta[j] = theta[j] - (alpha * stochasticLoss(data, theta, j))
    return theta

def addSubplot(theta, x = np.linspace(-3,3), color = '-r'):
    y = generateLine(theta, x)
    label='order ' + str(len(theta)) + ' approximation'
    plt.plot(x, y, color, label = label) # , label='order' + order + 'approximation')

plt.figure(figsize=(17,12))
for index, fileName in enumerate([r'data/synthetic-1.csv', r'data/synthetic-2.csv', r'data/synthetic-3.csv']):
# for index, fileName in enumerate([r'data/synthetic-3.csv']):
    print(fileName)
    subplot = plt.subplot(2, 2, index + 1)
    subplot.set_title(fileName)
    data = np.genfromtxt(fileName, delimiter=',')

    plt.scatter(data[:,0], data[:,1])
    plt.ylim(min(data[:,1])-0.5, max(data[:,1])+0.5)

    class Polynomial:
        def __init__(self, order, color):
            self.thetaCount = order
            self.plotColor = color

    for polynomial in [Polynomial(2, '-r'), Polynomial(3, '-b'), Polynomial(5, '-y'), Polynomial(8, '-g')]:
        theta = [0] * polynomial.thetaCount
        theta = regression(theta, data)
        for _ in range(20000):
        # while(meanSquaredError(theta, data) > 15):
            theta = regression(theta, data)

        # x = np.linspace(-3,3)
        x = np.linspace(min(data[:,0]-0.5), max(data[:,0])+0.5)
        addSubplot(theta, x, polynomial.plotColor)
        # print(theta)
        print("MSE for order", polynomial.thetaCount - 1, ":", meanSquaredError(theta, data))
    plt.legend()#(loc='upper left')
# plt.show()
plt.savefig(r'media/plots.png', bbox_inches='tight')