import requests
import os
import bs4
from datetime import datetime
import pandas as pd
from dataclasses import dataclass

BC_KEYS = [
    "BC_1MONTH",
    "BC_3MONTH",
    "BC_6MONTH",
    "BC_1YEAR",
    "BC_2YEAR",
    "BC_3YEAR",
    "BC_5YEAR",
    "BC_7YEAR",
    "BC_10YEAR",
    "BC_20YEAR",
    "BC_30YEAR",
    "BC_30YEARDISPLAY",
]
DF_COLUMNS = ["date"] + BC_KEYS
BASE_URL = (
    "https://home.treasury.gov/resource-center/"
    "data-chart-center/interest-rates/pages/xml?"
    "data=daily_treasury_yield_curve&field_tdr_date_value={}"
)


def get_url_all():
    """Return URL for XML file that holds all data from 1990 to present.
    Currently not used, reserved for furture use.
    """
    return BASE_URL.format("all")


def get_url(year: int) -> str:
    return BASE_URL.format(year)


def fetch(url: str):
    return requests.get(url).text


def raise_if_empty(content: str) -> str:
    if "Error" in content:
        # when calling API too often an error emerges.
        raise ValueError("Cannot read {} from web. Try again later.".format(url))
    else:
        return content


def get_xml_content_from_web(year: int) -> str:
    """Safely return XML content as string"""
    url = get_url(year)
    return raise_if_empty(fetch(url))


def default_folder():
    dirname = "xml"
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    return dirname


def filepath(year: int, folder=None):
    if not folder:
        folder = default_folder()
    filename = "{}.xml".format(year)
    return os.path.join(folder, filename)


def read_local_xml(year):
    return read(path=filepath(year))


def read(path):
    with open(path, "r") as f:
        return f.read()


def save_local_xml(year: int, content: str):
    path = filepath(year)
    save(path, content)


def save(path: str, content: str):
    with open(path, "w") as f:
        f.write(content)


def save_year(year: int):
    content = get_xml_content_from_web(year)
    save_local_xml(year, content)


def rates(year):
    """Return Rates(year) for default location."""
    return Rates(year, default_folder())


@dataclass
class Rates:
    year: int
    folder: str

    @property
    def path(self):
        return os.path.join(self.folder, f"{self.year}.xml")

    def fetch_xml(self):
        return get_xml_content_from_web(self.year)

    def save_local(self):
        content = self.fetch_xml()
        save(self.path, content)
        return self

    def yield_datapoints(self):
        xml_content = read(self.path)
        return yield_datapoints_from_string(xml_content)

    def dataframe(self):
        return to_dataframe(self.yield_datapoints())


def get_date(string):
    dt = datetime.strptime(string, "%Y-%m-%dT%H:%M:%S")
    return dt.strftime("%Y-%m-%d")


def as_float(s: str):
    # Needed to work around omissions in 30yr data starting year 2002
    try:
        return float(s)
    except:
        # FIXME: some stable NA, accepted by pandas, is better.
        return pd.NA


def yield_datapoints_from_string(xml_content: str) -> iter:
    """Parse XML string and yield one dictionary per date."""
    soup = bs4.BeautifulSoup(xml_content, "xml")
    data = soup.find_all("content")
    for datum in data:
        cur_dict = dict((key, as_float(datum.find(key).text)) for key in BC_KEYS)
        cur_dict["date"] = get_date(datum.find("NEW_DATE").text)
        yield cur_dict


def save_datapoints_from_web(year):
    xml_content = get_xml_content_from_web(year)
    save_local_xml(year, xml_content)


def get_datapoints(year: int):
    if not os.path.exists(filepath(year)):
        save_year(year)
        print("Read {} data from web and saved to local xml file.".format(year))
    xml_content = read_local_xml(year)
    print("Read {} data from local xml file.".format(year))
    return yield_datapoints_from_string(xml_content)


def to_dataframe(gen):
    df = pd.DataFrame(gen)[DF_COLUMNS]
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)
    return df


def get_df(year):
    gen = get_datapoints(year)
    df = pd.DataFrame(gen)[DF_COLUMNS]
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)
    return df


def get_dataframes(year_start, year_end):
    years = range(year_start, year_end + 1)
    dfs = [get_df(year) for year in years]
    df = pd.concat(dfs).sort_index()
    return df[(df.sum(axis=1) != 0)]


def year_now():
    from datetime import datetime

    return datetime.today().year


def update():
    current_year = year_now()
    save_year(year=current_year)
    df = get_dataframes(1990, current_year)
    df.to_csv("ust.csv")
    make_chart(df)


def make_chart(df, output_file="ust.png"):
    import matplotlib.dates as dates
    import matplotlib.pyplot as plt

    ax = df[["BC_3MONTH", "BC_10YEAR"]].plot()
    ax.xaxis.set_major_locator(dates.YearLocator(5))
    ax.xaxis.set_major_formatter(dates.DateFormatter("%Y"))
    plt.tight_layout()

    plt.savefig(output_file)
