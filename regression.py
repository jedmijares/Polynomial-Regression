import numpy as np
import matplotlib.pyplot as plt

def averageRawError(data, theta, power, otherPower):
    error = 0.0
    for point in data:
        # error += theta[0] + theta[1]*point[0] + theta[2] * point[0] ** 2 - point[1]
        sum = 0.0
        for i in range(power):
            sum += theta[i] * (point[0] ** i)
        error += (sum - point[1]) * (point[0] ** otherPower)
    return error/len(data)

# def error2(data, theta):
#     error = 0.0
#     for point in data:
#         error += ((theta[0] + theta[1]*point[0] - point[1]) * point[0])
#     return error/len(data)

# def error3(data, theta):
#     error = 0.0
#     for point in data:
#         error += ((theta[0] + theta[1]*point[0] - point[1]) * point[0] ** 2)
#     return error/len(data)

data = np.genfromtxt(r'data\synthetic-1.csv', delimiter=',')

# print(data[:,0])
plt.scatter(data[:,0], data[:,1])

theta = [10.0, 10.0, 0.0]
alpha = 1.0 ** -4
# print(averageRawError(data,theta))
for i in range(10000):
    # error = averageRawError(data,theta)
    # theta[0] = theta[0] - alpha * error
    # theta[1] = theta[1] - alpha * error2(data,theta)
    # theta[2] = theta[1] - alpha * error3(data,theta)
    for j in range(len(theta)):
        theta[j] = theta[j] - alpha * averageRawError(data, theta, len(theta), j)

print(theta)
print(averageRawError(data,theta, 2, 0))
x = np.linspace(-3,3)
# y = theta[0] + theta[1] * x
second = theta[0] + theta[1] * x + theta[2] * x ** 2
# plt.plot(x, y, '-r', label='first order approximation')
plt.plot(x, second, '-r', label='second order approximation')
plt.show()