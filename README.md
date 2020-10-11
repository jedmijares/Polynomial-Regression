# Polynomial Regression

This script uses gradient descent to perform polynomial regression on 2D datasets. My method uses stochastic gradient descent to reduce the required runtime for the script. I used an alpha value of 0.00001 and updated theta 400 times for each point in each dataset, as this gave me good enough accuracy for the required runtime.

For the three given datasets, the script fits a polynomial of order 1, 2, 4, and 7 to its points. It plots both the original points as well as each polynomial. Additionally, the mean squared error of each approximation is listed:

![Plots](/media/plots.png)

The rounded theta values (in increasing index order) are listed below:
```
data/synthetic-1.csv
[1.355, 0.094]
[0.856, 0.085, 1.57]
[0.563, -0.029, 0.479, 0.069, 0.526]
[0.609, -0.081, 0.54, 0.007, 0.578, 0.278, -0.036, -0.075]
data/synthetic-2.csv
[-1.181, 0.817]
[-1.01, 0.835, -0.582]
[-0.981, 0.902, -0.441, -0.17, 0.007]
[-0.995, 1.072, -0.558, 0.881, -0.414, 0.753, 0.189, -0.369]
data/synthetic-3.csv
[0.066, -0.002]
[0.048, -0.004, 0.058]
[0.03, -0.001, -0.013, -0.007, 0.037]
[0.034, -0.001, -0.032, 0.006, -0.083, 0.033, 0.039, -0.011]
```
## Bonus

As bonus, I implemented L2 norm regularization to my regression implemetation. I did this by simply adding an optional lambda parameter to my regression algorithm, defaulting to 0 in the case that regression is not used. For this example, I passed it a value of 10.

The regularized lines of fit for the 7th order polynomials look as follows:

![Regularized Plots](/media/regularizedPlots.png)

These plots are similar, though it can be seen that the plots are slightly "damped" towards the x-axis. This makes sense, since the initial line of fit is always a line through the x-axis.

The rounded theta values are:
```
data/synthetic-1.csv
[0.18, -0.016, 0.174, 0.015, 0.215, 0.102, 0.115, -0.027]
data/synthetic-2.csv
[-0.279, 0.31, -0.167, 0.283, -0.138, 0.279, 0.036, -0.152]
data/synthetic-3.csv
[0.008, 0.0, -0.009, 0.002, -0.02, 0.009, 0.019, -0.004]
```