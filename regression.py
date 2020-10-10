# Gerard (Jed) Mijares
# Polynomial Regression
# Machine Learning Fall 2020

import numpy as np
import matplotlib.pyplot as plt

def regression(theta, data, lambdaValue = 0):
    alpha = 0.00001
    for power in range(len(theta)):
        # update theta once for each point (stochastic)
        for point in data:
            hypothesis = 0.0
            # calculate hypothesis
            for index, value in enumerate(theta):
                hypothesis += value * (point[0] ** index)
            error = ((hypothesis - point[1]) * (point[0] ** power))
            theta[power] = theta[power] - (alpha * error) - alpha * lambdaValue * theta[power]
    return theta

def meanSquaredError(thetas, data):
    error = 0.0
    for point in data:
        hypothesis = 0.0
        for i in range(len(thetas)):
            hypothesis += thetas[i] * (point[0] ** i)
        error += ((hypothesis - point[1]) ** 2)
    return error/len(data)

def addSubplot(thetas, label, x = np.linspace(-3,3), color = '-r'):
    y = 0
    for power in range(len(thetas)):
        y += thetas[power] * x ** power
    plt.plot(x, y, color, label = label)

class Polynomial:
    def __init__(self, order, color):
        self.thetaCount = order + 1
        self.plotColor = color

plt.figure(figsize=(17,12))
for index, fileName in enumerate([r'data/synthetic-1.csv', r'data/synthetic-2.csv', r'data/synthetic-3.csv']):
    print(fileName)
    subplot = plt.subplot(2, 2, index + 1)
    subplot.set_title(fileName)
    data = np.genfromtxt(fileName, delimiter=',')

    # plot given points
    plt.scatter(data[:,0], data[:,1])
    plt.ylim(min(data[:,1])-0.5, max(data[:,1])+0.5)

    for polynomial in [Polynomial(1, '-r'), Polynomial(2, '-b'), Polynomial(4, '-y'), Polynomial(7, '-g')]:
        theta = [0] * polynomial.thetaCount
        for _ in range(400):
            theta = regression(theta, data)
        x = np.linspace(min(data[:,0]-0.5), max(data[:,0])+0.5)
        roundedMSE = "{:.2f}".format(meanSquaredError(theta, data))
        label='order ' + str(len(theta) - 1) + ' approximation (MSE: ' + roundedMSE + ')'
        addSubplot(theta, label, x, polynomial.plotColor)
        roundedTheta = []
        for value in theta:
            roundedTheta.append(round(value, 3))
        print(roundedTheta)
    plt.legend()
plt.savefig(r'media/plots.png', bbox_inches='tight')
plt.close()

# repeat for regularized plots
plt.figure(figsize=(17,12))
for index, fileName in enumerate([r'data/synthetic-1.csv', r'data/synthetic-2.csv', r'data/synthetic-3.csv']):
    print(fileName)
    subplot = plt.subplot(2, 2, index + 1)
    subplot.set_title(fileName)
    data = np.genfromtxt(fileName, delimiter=',')

    plt.scatter(data[:,0], data[:,1])
    plt.ylim(min(data[:,1])-0.5, max(data[:,1])+0.5)

    for polynomial in [Polynomial(7, '-g')]:
        theta = [0] * polynomial.thetaCount
        for _ in range(400):
            theta = regression(theta, data, 10)

        x = np.linspace(min(data[:,0]-0.5), max(data[:,0])+0.5)
        roundedMSE = "{:.2f}".format(meanSquaredError(theta, data))
        label='order ' + str(len(theta) - 1) + ' approximation (MSE: ' + roundedMSE + ')'
        addSubplot(theta, label, x, polynomial.plotColor)
        roundedTheta = []
        for value in theta:
            roundedTheta.append(round(value, 3))
        print(roundedTheta)
    plt.legend()
plt.savefig(r'media/regularizedPlots.png', bbox_inches='tight')
plt.close()