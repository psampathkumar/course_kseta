import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data.csv")
plt.plot(
    np.arange(20),
    np.poly1d(np.polyfit(data[:, 0], data[:, 1], 1))(np.arange(20)),
    color="r",
)
plt.scatter(data[:, 0], data[:, 1])
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("plot.png")


assert False
