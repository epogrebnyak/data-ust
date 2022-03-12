import os
import pandas as pd
from ust import save_xml, read_rates, available_years

# save UST yield rates to local folder for selected years
for year in available_years():
    save_xml(year, folder="./xml")

# run later - force update last year (overwrites existing file)
save_xml(2022, folder="./xml", overwrite=True)

# read UST yield rates as pandas dataframe
df = read_rates(start_year=2020, end_year=2022, folder="./xml")
print(df)

# save as single CSV file
df.to_csv("rates.csv")

# read back later
df = pd.read_csv("rates.csv", parse_dates=["date"]).set_index("date")
