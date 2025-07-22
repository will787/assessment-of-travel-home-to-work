# %% 
import sys
import pandas as pd
import numpy as np

# %% 
sys.path.append('../query')
from extract_data_cloud import database


# %% 

def percent_better_than_median_or_whorse(value, database, uf):
    """
    (lower is better) - calculates your time compared to the baseline.
    Enter the percentage of people who have better or worse time than you.
    If the time is greater than the median, calculate the percentage of people with better time.
    If the time is less than the median, calculate the percentage of people with worse time.
    """
    median = database.median()

    data_array = np.array(database)

    if value > median:
      pct = (data_array > value).sum() / len(data_array) * 100
      return f"{value} é um tempo melhor que {pct:.2f}% da base"
    else:
      pct = (data_array < value).sum() / len(data_array) * 100
      return f"{value} é um tempo pior que {pct:.2f}% da base."        

# %%
#print(percent_better_than_median_or_whorse(36, database['tempo_medio_deslocamento']))
