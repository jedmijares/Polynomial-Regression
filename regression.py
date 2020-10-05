# Gerard (Jed) Mijares
# Polynomial Regression
# Machine Learning Fall 2020

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

def regression(theta, data, lambdaValue = 0):
    alpha = (1.0 * 10**-5)
    for j in range(len(theta)):
        theta[j] = theta[j] - (alpha * stochasticLoss(data, theta, j)) - alpha * lambdaValue * theta[j]
    return theta

def addSubplot(theta, label, x = np.linspace(-3,3), color = '-r'):
    y = generateLine(theta, x)
    plt.plot(x, y, color, label = label)

class Polynomial:
    def __init__(self, order, color):
        self.thetaCount = order + 1
        self.plotColor = color

plt.figure(figsize=(17,12))
plt.suptitle("Plots")
for index, fileName in enumerate([r'data/synthetic-1.csv', r'data/synthetic-2.csv', r'data/synthetic-3.csv']):
# for index, fileName in enumerate([r'data/synthetic-3.csv']):
    subplot = plt.subplot(2, 2, index + 1)
    subplot.set_title(fileName)
    data = np.genfromtxt(fileName, delimiter=',')

    plt.scatter(data[:,0], data[:,1])
    plt.ylim(min(data[:,1])-0.5, max(data[:,1])+0.5)

    for polynomial in [Polynomial(1, '-r'), Polynomial(2, '-b'), Polynomial(4, '-y'), Polynomial(7, '-g')]:
        theta = [0] * polynomial.thetaCount
        for _ in range(20000):
        # while(meanSquaredError(theta, data) > 15):
            theta = regression(theta, data)

        # x = np.linspace(-3,3)
        x = np.linspace(min(data[:,0]-0.5), max(data[:,0])+0.5)
        roundedMSE = "{:.2f}".format(meanSquaredError(theta, data))
        label='order ' + str(len(theta) - 1) + ' approximation (MSE: ' + roundedMSE + ')'
        addSubplot(theta, label, x, polynomial.plotColor)
        # print(theta)
        # print("MSE for order", polynomial.thetaCount - 1, ":", meanSquaredError(theta, data))
    plt.legend()
# plt.show()
plt.savefig(r'media/plots.png', bbox_inches='tight')
plt.close()

plt.figure(figsize=(17,12))
plt.suptitle("Regularized Plots")
for index, fileName in enumerate([r'data/synthetic-1.csv', r'data/synthetic-2.csv', r'data/synthetic-3.csv']):
# for index, fileName in enumerate([r'data/synthetic-3.csv']):
    subplot = plt.subplot(2, 2, index + 1)
    subplot.set_title(fileName)
    data = np.genfromtxt(fileName, delimiter=',')

    plt.scatter(data[:,0], data[:,1])
    plt.ylim(min(data[:,1])-0.5, max(data[:,1])+0.5)

    for polynomial in [Polynomial(1, '-r'), Polynomial(2, '-b'), Polynomial(4, '-y'), Polynomial(7, '-g')]:
        theta = [0] * polynomial.thetaCount
        for _ in range(20000):
        # while(meanSquaredError(theta, data) > 15):
            theta = regression(theta, data, 25)

        # x = np.linspace(-3,3)
        x = np.linspace(min(data[:,0]-0.5), max(data[:,0])+0.5)
        roundedMSE = "{:.2f}".format(meanSquaredError(theta, data))
        label='order ' + str(len(theta) - 1) + ' approximation (MSE: ' + roundedMSE + ')'
        addSubplot(theta, label, x, polynomial.plotColor)
        # print(theta)
        # print("MSE for order", polynomial.thetaCount - 1, ":", meanSquaredError(theta, data))
    plt.legend()
# plt.show()
plt.savefig(r'media/regularizedPlots.png', bbox_inches='tight')
plt.close()