import os
import pandas as pd
import ust

# Download xml files
# current_year = ust.today().year
# ust.save_year(current_year)


if not os.path.exists("ust.csv"):
    update()


df = pd.read_csv("ust.csv", parse_dates=["date"]).set_index("date")
ust.make_chart(df)
