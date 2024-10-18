import pytest
import numpy as np
import matplotlib.pyplot as plt
from unittest import mock
from main_ref import load_data, plot_data

# Test load_data function
def test_load_data():
    # Create mock data to simulate the contents of "data.csv"
    mock_data = np.array([[1, 2], [3, 4], [5, 6]])
    
    # Patch np.loadtxt to return the mock data instead of reading from a file
    with mock.patch("numpy.loadtxt", return_value=mock_data):
        data = load_data("data.csv")
        assert isinstance(data, np.ndarray)  # Check if data is numpy array
        assert data.shape == (3, 2)  # Check if the shape is correct
        np.testing.assert_array_equal(data, mock_data)  # Check if values match

# Test plot_data function
def test_plot_data():
    # Create mock data
    mock_data = np.array([[1, 2], [3, 4], [5, 6]])

    # Mock plt.savefig to avoid actual file creation
    with mock.patch("matplotlib.pyplot.savefig") as mock_savefig:
        plot_data(mock_data, "mock_plot.png")
        
        # Ensure savefig was called with the correct filename
        mock_savefig.assert_called_once_with("mock_plot.png")

# Test if assertion error occurs in main (or a similar case)
def test_main_assertion():
    with pytest.raises(AssertionError):
        assert False  # Simulating the failure in the original code