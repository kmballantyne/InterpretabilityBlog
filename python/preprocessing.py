#%% [markdown]
# # Preprocessing

#%%
# pip install pandas
# pip install numpy

import pandas as pd
import numpy as np

#%% [markdown]
# Here I imported necessary libraries for preprocessing. I will use pandas for data manipulation and numpy for mathematical operations.

#%%
class Text_Preprocessor:
    def __init__(self, data):
        self.data = data
        