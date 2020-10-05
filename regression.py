import numpy as np
import matplotlib.pyplot as plt
import random

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

def plot(theta, x = np.linspace(-3,3), color = '-r'):
    y = generateLine(theta, x)
    label='order ' + str(len(theta)) + ' approximation'
    plt.plot(x, y, color, label = label) # , label='order' + order + 'approximation')

# # https://stackoverflow.com/a/45395003
# def sample_floats(low, high, k=1):
#     """ Return a k-length list of unique random floats
#         in the range of low <= x <= high
#     """
#     result = []
#     seen = set()
#     for i in range(k):
#         x = random.uniform(low, high)
#         while x in seen:
#             x = random.uniform(low, high)
#         seen.add(x)
#         result.append(x)
#     return result

# for fileName in [r'data/synthetic-1.csv', r'data/synthetic-2.csv', r'data/synthetic-3.csv']:
for fileName in [r'data/synthetic-2.csv']:
    data = np.genfromtxt(fileName, delimiter=',')

    plt.scatter(data[:,0], data[:,1])
    plt.ylim(min(data[:,1])-0.5, max(data[:,1])+0.5)

    for orderColor in [(2, '-r'), (3, '-b'), (5, '-y'), (8, '-g')]:
    # for orderColor in [(5, '-r')]:
        theta = [0] * orderColor[0]
        # theta = sample_floats(-2, 2, k = orderColor[0])
        theta = regression(theta, data)
        # i = 0
        for _ in range(20000):
        # while(meanSquaredError(theta, data) > 15):
            theta = regression(theta, data)
            # i += 1
            # print(i)
        # theta = [1.0] * order
        # alpha = (1.0 * 10**-5)
        # for i in range(1000):
        #     for j in range(len(theta)):
        #         theta[j] = theta[j] - (alpha * loss(data, theta, j))

        # x = np.linspace(-3,3)
        x = np.linspace(min(data[:,0]-0.5), max(data[:,0])+0.5)
        plot(theta, x, orderColor[1])
        # y = generateLine(theta, x)
        # plt.plot(x, y, '-r') # , label='order' + order + 'approximation')
        print(theta)
        # print(meanSquaredError(theta, data))
    plt.legend()#(loc='upper left')
    plt.show()