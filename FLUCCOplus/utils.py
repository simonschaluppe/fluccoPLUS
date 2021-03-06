

# imports shared throughout the project
import sys
import importlib

import datetime as dt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from pathlib import Path


# CONSTANTS

PJ_TO_GWH = 277.7778 # [GWh / PJ]
GWH_TO_PJ = 1/PJ_TO_GWH #[PJ/GWH]


# HELPER

def log(f):
    def wrapper(*args, **kwargs):
        tic = dt.datetime.now()
        result = f(*args, **kwargs)
        toc = dt.datetime.now()
        print(f"{f.__name__} took {toc-tic}")
        return result
    return wrapper


def logg(f):
    def wrapper(dataframe, *args, **kwargs):
        tic = dt.datetime.now()
        result = f(dataframe, *args, **kwargs)
        toc = dt.datetime.now()
        ro, co = result.shape
        print(f"{f.__name__} took {toc-tic} for {ro} rows, {co} columns in df")
        # print(result.info())
        return result
    return wrapper


