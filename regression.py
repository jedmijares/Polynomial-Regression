import numpy as np
import matplotlib.pyplot as plt

def averageRawError(data, theta, power):
    error = 0.0
    for point in data:
        # error += theta[0] + theta[1]*point[0] + theta[2] * point[0] ** 2 - point[1]
        sum = 0.0
        for i in range(len(theta)):
            sum += theta[i] * (point[0] ** i)
            # print("-"*i, sum)
        error += (sum - point[1]) * (point[0] ** power)
    # print(error/len(data))
    return error/len(data)

data = np.genfromtxt(r'data\synthetic-1.csv', delimiter=',')

# print(data[:,0])
plt.scatter(data[:,0], data[:,1])

theta = [1.0] * 4
alpha = (1.0 * 10**-5)
for i in range(1000):
    for j in range(len(theta)):
        # print(averageRawError(data, theta, j))
        # print(alpha * averageRawError(data, theta, j))
        theta[j] = theta[j] - (alpha * averageRawError(data, theta, j))

print(theta)
# print(averageRawError(data,theta, 2, 0))
x = np.linspace(-3,3)
y = theta[0] + theta[1] * x
second = theta[0] + theta[1] * x + theta[2] * x ** 2 + theta[3] * x ** 3
# plt.plot(x, y, '-r', label='first order approximation')
plt.plot(x, second, '-r', label='second order approximation')
plt.show()