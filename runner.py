import os

import pandas as pd

from ust import force_save, read_rates, save

# save UST yield rates to local folder for selected years
for year in [2020, 2021, 2022]:
    save(year, folder="./xml")

# force update last year (overwrites existing file)
force_save(2022, folder="./xml")

# read UST yield rates as pandas dataframe
df = read_rates(start_year=2021, end_year=2022, folder="./xml")

# save as single CSV file
df.to_csv("rates.csv")

# read back later
df = pd.read_csv("rates.csv", parse_dates=["date"]).set_index("date")


"""
            BC_1MONTH  BC_3MONTH  BC_6MONTH  ...  BC_20YEAR  BC_30YEAR  BC_30YEARDISPLAY
date                                         ...                                        
2021-01-04       0.09       0.09       0.09  ...       1.46       1.66              1.66
2021-01-05       0.08       0.09       0.09  ...       1.49       1.70              1.70
2021-01-06       0.09       0.09       0.09  ...       1.60       1.81              1.81
2021-01-07       0.09       0.09       0.09  ...       1.64       1.85              1.85
2021-01-08       0.08       0.08       0.09  ...       1.67       1.87              1.87
...               ...        ...        ...  ...        ...        ...               ...
2022-03-02       0.13       0.34       0.68  ...       2.32       2.24              2.24
2022-03-03       0.19       0.38       0.69  ...       2.32       2.24              2.24
2022-03-04       0.15       0.34       0.69  ...       2.23       2.16              2.16
2022-03-07       0.17       0.38       0.75  ...       2.29       2.19              2.19
2022-03-08       0.16       0.36       0.72  ...       2.34       2.24              2.24
"""
