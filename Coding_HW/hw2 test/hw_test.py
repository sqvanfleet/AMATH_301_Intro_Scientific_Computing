#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 13:12:05 2024

@author: samvanfleet

"""

import numpy as np

import subprocess
import sys
from contextlib import contextmanager
from pathlib import Path

def generate_requirements(path, output_path):
    """
    Generates a requirements.txt file using pipreqs package.

    WARNING: pipreqs executes and scans ALL files in the `path` directory, related to the solution or not.
    It's because it treats the `path` directory as a Python project's root and all .py files inside it,
    including the ones in subdirectories, as the project's code. In past it led to many confusing situations
    when pipreqs was failing to produce the file because the instructor had other python files in the same directory,
    and those failed to execute.
    Putting the solution file into a temporary folder is also not a solution because then we won't be able
    to accommodate solutions with multiple files: how would you decide what is relevant and what is not?
    The best advice to manage failures of this function is start with checking
    whether there are irrelevant Python files in the directory.
    Another solution would be to list all the packages explicitly in
    "requirements" variable, in which case this function won't be called.

    :param path: Path to the directory which contains the solution file.
    :param output_path: Path where to save the requirements file
    :return:
    """
    process = subprocess.Popen(["pipreqs", "--no-pin", "--savepath", f"{output_path}", f"{path}"], stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
    return process.communicate()


x = 15
y = -2
z = np.pi

A1 = x + y - z
A2 = x ** 3

A3 = np.array([[1,2,3],[3,4,6]])







test_suite = [
    {
        "test_name": "Addition",
        "variable_name": "A1",
        "description": "Evaluating x + y - z",
        "score": 1
    },
    {
        "test_name": "Power",
        "variable_name": "A2",
        "description": "Evaluating x^3",
        "hint_tolerance": "Check power.",
        "score": 1
    },
    {
        "test_name": "Matrix",
        "variable_name": "A3",
        "hint_wrong_size": "Check transposition",
        "rtol": 1e-5,
        "atol": 1e-2,
        "score": 3
    }
]


