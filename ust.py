import requests
import os
import bs4
from datetime import datetime
import pandas as pd

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


def get_url(year: int) -> str:
    return (
        "https://www.treasury.gov/resource-center/"
        + "data-chart-center/interest-rates/pages/"
        + "XmlView.aspx?data=yieldyear&year={}".format(year)
    )


def get_web_xml(year: int) -> str:
    """Returns XML content as string"""
    url = get_url(year)
    r = requests.get(url)
    return r.text


def get_xml_content_from_web(year: int) -> str:
    """Safely return XML content as string"""
    content = get_web_xml(year)
    if "Error" in content:
        # when calling API too often an error emerges. Should not be a problem with local files.
        raise ValueError("Cannot read {} from web. Try again later.".format(year))
    else:
        return content


def filepath(year: int):
    dirname = "xml"
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    fn = "{}.xml".format(year)
    return os.path.join(dirname, fn)


def exists(year):
    return os.path.exists(filepath(year))


def read_local_xml(year):
    path = filepath(year)
    with open(path, "r") as f:
        return f.read()


def save_local_xml(year: int, content: str):
    path = filepath(year)
    with open(path, "w") as f:
        f.write(content)


def save_year(year):
    content = get_xml_content_from_web(year)
    save_local_xml(year, content)


def get_date(string):
    dt = datetime.strptime(string, "%Y-%m-%dT%H:%M:%S")
    return dt.strftime("%Y-%m-%d")


def as_float(s: str):
    # Needed to work around omissions in 30yr data starting year 2002
    try:
        return float(s)
    except:
        # FIXME: some stable NA, accepted by pandas, is better.
        return 0


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


def get_df(year):
    gen = get_datapoints(year)
    df = pd.DataFrame(gen)[DF_COLUMNS]
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)
    return df


def get_dfs(year_start, year_end):
    years = range(year_start, year_end + 1)
    dfs = [get_df(year) for year in years]
    df = pd.concat(dfs).sort_index()
    return df[(df.sum(axis=1) != 0)]

def today():
    from datetime import datetime
    return datetime.today().year


def update():
    save_year(year=today())  
    df = get_dfs(1990, 2021)
    df.to_csv("ust.csv")  
    

if __name__ == "__main__":
    if not os.path.exists("ust.csv"):
        update()

    df = pd.read_csv("ust.csv", parse_dates=["date"]).set_index("date")
    ax = df[["BC_3MONTH", "BC_10YEAR"]].plot()

    # refine plot
    import matplotlib.dates as dates
    import matplotlib.pyplot as plt

    ax.xaxis.set_major_locator(dates.YearLocator(5))
    ax.xaxis.set_major_formatter(dates.DateFormatter("%Y"))
    plt.tight_layout()
    
    plt.savefig("ust.png")