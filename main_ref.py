import numpy as np
import matplotlib.pyplot as plt


def load_data(filename):
    return np.loadtxt(filename)


# some random comment









def plot_data(data, output_file="plot_v1.png"):
    plt.plot( np.arange(20),
        np.poly1d(np.polyfit(data[:, 0], data[:, 1], 1))(np.arange(20)),
        color="r",)
    plt.scatter(data[:, 0], data[:, 1])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.savefig(output_file)


def main():
    data = load_data("data.csv")
    plot_data(data)
    assert False  # Some intentional failure for testing
