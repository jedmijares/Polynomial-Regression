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

def regression(data, order):
    theta = [1.0] * order
    alpha = (1.0 * 10**-5)
    for i in range(1000):
        for j, value in enumerate(theta):
            value = value - (alpha * loss(data, theta, j))
    return theta

def plot(theta, x = np.linspace(-3,3), color = '-r'):
    y = generateLine(theta, x)
    plt.plot(x, y, color) # , label='order' + order + 'approximation')

for fileName in [r'data/synthetic-1.csv', r'data/synthetic-2.csv', r'data/synthetic-3.csv']:
    data = np.genfromtxt(fileName, delimiter=',')

    plt.scatter(data[:,0], data[:,1])
    plt.ylim(min(data[:,1])-0.5, max(data[:,1])+0.5)

    for order in [2]: #, 3, 5, 8]:
        theta = regression(data, order)
        # theta = [1.0] * order
        # alpha = (1.0 * 10**-5)
        # for i in range(1000):
        #     for j in range(len(theta)):
        #         theta[j] = theta[j] - (alpha * loss(data, theta, j))

        # x = np.linspace(-3,3)
        x = np.linspace(min(data[:,0]-0.5), max(data[:,0])+0.5)
        plot(theta, x)
        # y = generateLine(theta, x)
        # plt.plot(x, y, '-r') # , label='order' + order + 'approximation')
        print(meanSquaredError(theta, data))
    plt.show()