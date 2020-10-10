# Polynomial Regression

This script uses gradient descent to perform polynomial regression on 2D datasets.

For the three given datasets, the script fits a polynomial of order 1, 2, 4, and 7 to its points. It plots both the original points as well as each polynomial. Additionally, the mean squared error of each approximation is listed:

![Plots](/media/plots.png)

## Bonus

As bonus, I implemented L2 norm regularization to my regression implemetation. I did this by simply adding an optional lambda parameter to my regression algorithm, defaulting to 0 in the case that regression is not used.

The regularized lines of fit look as follows:

![Regularized Plots](/media/regularizedPlots.png)

These plots are similar, though it can be seen that the plots are slightly "damped" towards the x-axis. This makes sense, since the initial line of fit is always a line through the x-axis.