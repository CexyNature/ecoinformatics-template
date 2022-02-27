#!/usr/bin/env python3

"""Utility module for {{ cookiecutter.project_name }}.

Consider populating the sections below so you can documentate well your project

This module contains ...


Example
-------
You can get access to functions in this module by importing the whole module
or specific functions within the module

    $ import utils

    $ from utils import dummy_function


Notes
-----
    Remember to document your Modules, Classes and Functions as you develop.

Attributes
----------
seed : int
    This variable is a random seed intended for reproducibility.
"""

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = "{{ cookiecutter.email }}"
__version__ = "{{ cookiecutter.version }}"


import os
import numpy as np
import matplotlib.pyplot as plt


seed = 10


def dummy_function(sample_size, random_seed=seed):
    """This dummy function plots the relationship between two random variables x and y,
    which are randomly sample from two normal distributions. The function returns a
    matplotlib figure together with variables x and y.

    This dummy function uses as random seed a module level variable, but it can be overwrite
    by the user when calling the function.


    Args:
        sample_size (int): number of points to plot
        random_seed (int): random seed for reproducibility

    Returns:
        matplotlib.figure.Figure: Matplolib scatter figure
        x: random variable x
        y: random variable y
    """

    np.random.seed(random_seed)
    x = np.random.normal(loc=10.0, scale=3.4, size=sample_size)
    y = np.random.normal(loc=36.0, scale=1.3, size=sample_size)

    fig, ax = plt.subplots(figsize=(8, 8), facecolor="white")
    ax.scatter(x, y, c="#0091ad", s=12)

    return fig, x, y
