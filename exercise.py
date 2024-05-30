import numpy as np
import pandas as pd

# Logic


def check_uniqueness(lst):
    """
    Check if a list contains only unique values.
    Returns True only if all values in the list are unique, False otherwise
    """
    pass


def smallest_difference(array):
    """
    Code a function that takes an array and returns the smallest
    absolute difference between two elements of this array
    Please note that the array can be large and that the more
    computationally efficient the better
    """
    pass


# Finance and DataFrame manipulation


def macd(prices, window_short=12, window_long=26):
    """
    Code a function that takes a DataFrame named prices and
    returns it's MACD (Moving Average Convergence Difference) as
    a DataFrame with same shape
    Assume simple moving average rather than exponential moving average
    The expected output is in the output.csv file
    """
    pass


def sortino_ratio(prices):
    """
    Code a function that takes a DataFrame named prices and
    returns the Sortino ratio for each column
    Assume risk-free rate = 0
    On the given test set, it should yield 0.321853
    """
    pass


def expected_shortfall(prices, level=0.95):
    """
    Code a function that takes a DataFrame named prices and
    returns the expected shortfall at a given level
    On the given test set, it should yield -0.024844
    """
    pass


# Plot


def visualize(prices, path):
    """
    Code a function that takes a DataFrame named prices and
    saves the plot to the given path
    """
    pass
