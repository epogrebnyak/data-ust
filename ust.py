# -*- coding: utf-8 -*-

import os
from datetime import datetime

import requests
import bs4
import pandas as pd

BC_KEYS = ['BC_1MONTH',
           'BC_3MONTH', 'BC_6MONTH', 'BC_1YEAR', 'BC_2YEAR', 'BC_3YEAR',
           'BC_5YEAR', 'BC_7YEAR', 'BC_10YEAR', 'BC_20YEAR', 'BC_30YEAR',
           'BC_30YEARDISPLAY']
DF_COLUMNS = ['date'] + BC_KEYS

CSV_PATH = 'ust.csv'

# -----------------------------------------------------------------------------
#
# Parsing XML string to dict
#
# -----------------------------------------------------------------------------

def get_date(string):
    dt = datetime.strptime(string, '%Y-%m-%dT%H:%M:%S')
    return dt.strftime('%Y-%m-%d')


def as_float(s: str):
    # Needed to work around omissions in 30yr data starting year 2002
    try:
        x = float(s)
        return x
    except:
        # NOFIX: some stable NA, accepted by pandas, is better.
        return 0


def yield_datapoints_from_string(xml_content: str) -> iter:
    """Parse XML string and yield one dictionary per date."""
    soup = bs4.BeautifulSoup(xml_content, 'xml')
    # maybe data = soup.find_all('content',type="application/xml")       
    data = soup.find_all('content')
    for datum in data:
        cur_dict = dict((key, as_float(datum.find(key).text)) for key in BC_KEYS)
        cur_dict['date'] = get_date(datum.find('NEW_DATE').text)
        yield (cur_dict)


def yield_datapoints_from_string_2(xml_content: str) -> iter:
    """Alternative syntax to parse XML string and yield one dictionary per date."""
    soup = bs4.BeautifulSoup(xml_content, 'xml')
    properties = soup.find_all('properties')
    for prop in properties:
        children = prop.findChildren()
        # FIXME: this should use field name 'NEW_DATE', not absolute referencing
        #        probably .find('NEW_DATE') is better
        point = dict(date=get_date(children[1].text))
        # ----
        for child in children:
            if child.name.startswith('BC_'):
                point[child.name] = float(child.text)
        yield point


# -----------------------------------------------------------------------------
#
# Local XML file cache
#
# -----------------------------------------------------------------------------

def filepath(year: int):
    dirname = 'xml'
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    fn = "{}.xml".format(year)
    return os.path.join(dirname, fn)


def read_local_xml(year):
    path = filepath(year)
    with open(path, 'r') as f:
        return f.read()


def save_local_xml(year: int, content: str):
    path = filepath(year)
    with open(path, "w") as f:
        f.write(content)


# -----------------------------------------------------------------------------
#
# Web request
#
# -----------------------------------------------------------------------------

def get_url(year: int) -> str:
    return "https://www.treasury.gov/resource-center/data-chart-center/interest-rates/pages/XmlView.aspx?data=yieldyear&year={}".format(
        year)


def get_web_xml(year: int) -> str:
    """Returns XML content as string"""
    url = get_url(year)
    r = requests.get(url)
    return r.text


def get_xml_content_from_web(year: int) -> str:
    """Safely returns XML content as string"""
    content = get_web_xml(year)
    if "Error" in content:
        # when calling API too error emerges. Should not be a problem with local files. 
        raise ValueError("Cannot read {} from web. Try again later.".format(year))
    else:
        return content


# -----------------------------------------------------------------------------
#
# End-use functions
#
# -----------------------------------------------------------------------------

def get_datapoints(year: int, from_web=False):
    if from_web or year == datetime.today().year \
            or not os.path.exists(filepath(year)):
        xml_content = get_xml_content_from_web(year)
        save_local_xml(year, xml_content)
        print("Read {} data from web and saved to local file.".format(year))
    else:
        xml_content = read_local_xml(year)
        print("Read {} data from local file.".format(year))
    return yield_datapoints_from_string(xml_content)


def get_df(year):
    gen = get_datapoints(year)
    df = pd.DataFrame(gen)[DF_COLUMNS]
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    return df


def get_dfs(years: list):
    dfs = [get_df(year) for year in years]
    return pd.concat(dfs)


def to_monthly_average(df: pd.DataFrame):
    if pd.__version__ >= "0.19.2":
        # on earlier versions expression below does averaging on wrong axis
        # mean(axis=1) does not help
        mf = df.resample("M").mean().round(2)
    else:
        mf = df.resample("M", how='mean').round(2)
    mf.insert(0, "month", mf.index.month)
    mf.insert(0, "year", mf.index.year)
    return mf


def update_dfs():
    #  - when updating read csv in pandas and detect last year
    #  - read from last year in csv to pandas, overwriting local files
    #  - concat and replace with existing data in df
    df0 = pd.read_csv(CSV_PATH, index_col=0, converters={0: pd.to_datetime})
    years = range(max(df0.index).year, datetime.today().year + 1)
    df1 = get_dfs(years)
    # -----------------
    # TODO: merge df0 and df1, replacing old values in df0 with new values 
    #       from df1    
    # df = <merge result>
    # -----------------
    df.to_csv(CSV_PATH)
    return df


if __name__ == "__main__":
    cur_year = datetime.today().year
    YEARS = [x for x in range(1990, cur_year + 1)]
    # YEARS = [2017]
    # daily data
    dfs = [get_df(year) for year in YEARS]
    df = pd.concat(dfs)
    df.to_excel("ust_daily.xlsx")
    # monthly averages
    mf = to_monthly_average(df)
    mf.to_excel("ust_month_average.xlsx")




# ------------------------------------------------------- Developement notes:

# NOT TODO 1: docopt interface '''python ust.py 2017'''

# NOT TODO 2: read all-time xml
#             https://www.treasury.gov/resource-center/data-chart-center/interest-rates/pages/XmlView.aspx?data=yieldall

# NOT TODO 3: check for excel file permission error at start of script

# NOT TODO  : bokeh visualisation

# NOT TODO  : latest values in readme.md, possibly using mako

# ----------------------------------------------------------------------------
