import ust
import os

# Download xml files
# current_year = ust.today().year
# ust.save_year(current_year)


if not os.path.exists("ust.csv"):
    update()
    df = pd.read_csv("ust.csv", parse_dates=["date"]).set_index("date")
    make_chart(df)


df = pd.read_csv("ust.csv", parse_dates=["date"]).set_index("date")
make_chart()
