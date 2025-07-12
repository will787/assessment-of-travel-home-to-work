# %% 
import sys
import pandas as pd
import numpy as np

# %% 
sys.path.append('../query')
from extract_data_cloud import database


# %% 

def percent_better_than_median_or_whorse(value, database):
    """
    (menor é melhor) - calcula seu tempo comparado ao da base.
    coloca o percentual de pessoas que tem tempo melhor ou pior que o seu.
    Se o tempo for maior que a mediana, calcula o percentual de pessoas com tempo melhor
    Se o tempo for menor que a mediana, calcula o percentual de pessoas com tempo pior
    """
    median = database.median()

    data_array = np.array(database)

    if value > median:
      pct = (data_array > value).sum() / len(data_array) * 100
      return f"{value} é um tempo melhor que {pct:.2f}% da base"
    else:
      pct = (data_array < value).sum() / len(data_array) * 100
      return f"{value} é um tempo pior que {pct:.2f}% da base."        

print(percent_better_than_median_or_whorse(36, database['tempo_medio_deslocamento']))
# %%
