import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt("data.csv")
# Fit a linear regression line to the data
m, b = np.polyfit(data[:,0], data[:,1], 1)
# Generate x values for plotting the line
x_plot = np.linspace(data[:,0].min(), data[:,0].max(), 100)
# Calculate y values for plotting the line
y_plot = m*x_plot + b

# Plotting the data points
plt.scatter(data[:,0], data[:,1], label='Data Points')
# Plotting the linear regression line
plt.plot(x_plot, y_plot, color='r', label='Linear Regression Line')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig("plot.png")

# Simple test for the code
#assert len(data) > 0, "No data loaded"
assert False