import numpy as np
import matplotlib.pyplot as plt

def averageRawError(data, theta, power = 0):
    error = 0.0
    for point in data:
        error += theta[0] + theta[1]*point[0] + theta[2] * point[0] ** 2 - point[1]
    return error/len(data)

def error2(data, theta):
    error = 0.0
    for point in data:
        error += ((theta[0] + theta[1]*point[0] - point[1]) * point[0])
    return error/len(data)

def error3(data, theta):
    error = 0.0
    for point in data:
        error += ((theta[0] + theta[1]*point[0] - point[1]) * point[0] ** 2)
    return error/len(data)

data = np.genfromtxt(r'data\synthetic-2.csv', delimiter=',')

# print(data[:,0])
plt.scatter(data[:,0], data[:,1])

theta = [10.0, 10.0, 10.0]
alpha = 10.0 ** -4
# print(averageRawError(data,theta))
for i in range(10000):
    error = averageRawError(data,theta)
    theta[0] = theta[0] - alpha * error
    theta[1] = theta[1] - alpha * error2(data,theta)
    theta[2] = theta[1] - alpha * error3(data,theta)

print(theta)
print(averageRawError(data,theta))
x = np.linspace(-3,3)
# y = theta[0] + theta[1] * x
second = theta[0] + theta[1] * x + theta[2] * x ** 2
# plt.plot(x, y, '-r', label='first order approximation')
plt.plot(x, second, '-r', label='second order approximation')
plt.show()