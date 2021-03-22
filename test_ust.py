# -*- coding: utf-8 -*-
"""Pytest test cases for ust.py"""

XML_CONTENT_2017 = """
<pre>
<title xmlns="http://www.w3.org/2005/Atom" type="text">DailyTreasuryYieldCurveRateData</title>
<id xmlns="http://www.w3.org/2005/Atom">
http://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData
</id>
<updated xmlns="http://www.w3.org/2005/Atom">2017-04-17T20:02:19Z</updated>
<link xmlns="http://www.w3.org/2005/Atom" rel="self" title="DailyTreasuryYieldCurveRateData" href="DailyTreasuryYieldCurveRateData"/>
<entry xmlns="http://www.w3.org/2005/Atom">
<id>
http://data.treasury.gov/Feed.svc/DailyTreasuryYieldCurveRateData(6820)
</id>
<title type="text"/>
<updated>2017-04-17T20:02:19Z</updated>
<author>
<name/>
</author>
<link rel="edit" title="DailyTreasuryYieldCurveRateDatum" href="DailyTreasuryYieldCurveRateData(6820)"/>
<category term="TreasuryDataWarehouseModel.DailyTreasuryYieldCurveRateDatum" scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme"/>
<content type="application/xml">
<m:properties xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata">
<d:Id xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Int32">6820</d:Id>
<d:NEW_DATE xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.DateTime">2017-04-03T00:00:00</d:NEW_DATE>
<d:BC_1MONTH xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">0.73</d:BC_1MONTH>
<d:BC_3MONTH xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">0.79</d:BC_3MONTH>
<d:BC_6MONTH xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">0.92</d:BC_6MONTH>
<d:BC_1YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.02</d:BC_1YEAR>
<d:BC_2YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.24</d:BC_2YEAR>
<d:BC_3YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.47</d:BC_3YEAR>
<d:BC_5YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.88</d:BC_5YEAR>
<d:BC_7YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.16</d:BC_7YEAR>
<d:BC_10YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.35</d:BC_10YEAR>
<d:BC_20YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.71</d:BC_20YEAR>
<d:BC_30YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.98</d:BC_30YEAR>
<d:BC_30YEARDISPLAY xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.98</d:BC_30YEARDISPLAY>
</m:properties>
</content>
</entry>
<entry xmlns="http://www.w3.org/2005/Atom">
<id>
http://data.treasury.gov/Feed.svc/DailyTreasuryYieldCurveRateData(6821)
</id>
<title type="text"/>
<updated>2017-04-17T20:02:19Z</updated>
<author>
<name/>
</author>
<link rel="edit" title="DailyTreasuryYieldCurveRateDatum" href="DailyTreasuryYieldCurveRateData(6821)"/>
<category term="TreasuryDataWarehouseModel.DailyTreasuryYieldCurveRateDatum" scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme"/>
<content type="application/xml">
<m:properties xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata">
<d:Id xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Int32">6821</d:Id>
<d:NEW_DATE xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.DateTime">2017-04-04T00:00:00</d:NEW_DATE>
<d:BC_1MONTH xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">0.77</d:BC_1MONTH>
<d:BC_3MONTH xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">0.79</d:BC_3MONTH>
<d:BC_6MONTH xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">0.92</d:BC_6MONTH>
<d:BC_1YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.03</d:BC_1YEAR>
<d:BC_2YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.25</d:BC_2YEAR>
<d:BC_3YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.47</d:BC_3YEAR>
<d:BC_5YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.88</d:BC_5YEAR>
<d:BC_7YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.16</d:BC_7YEAR>
<d:BC_10YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.36</d:BC_10YEAR>
<d:BC_20YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.72</d:BC_20YEAR>
<d:BC_30YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.99</d:BC_30YEAR>
<d:BC_30YEARDISPLAY xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.99</d:BC_30YEARDISPLAY>
</m:properties>
</content>
</entry>
<entry xmlns="http://www.w3.org/2005/Atom">
<id>
http://data.treasury.gov/Feed.svc/DailyTreasuryYieldCurveRateData(6822)
</id>
<title type="text"/>
<updated>2017-04-17T20:02:19Z</updated>
<author>
<name/>
</author>
<link rel="edit" title="DailyTreasuryYieldCurveRateDatum" href="DailyTreasuryYieldCurveRateData(6822)"/>
<category term="TreasuryDataWarehouseModel.DailyTreasuryYieldCurveRateDatum" scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme"/>
<content type="application/xml">
<m:properties xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata">
<d:Id xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Int32">6822</d:Id>
<d:NEW_DATE xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.DateTime">2017-04-05T00:00:00</d:NEW_DATE>
<d:BC_1MONTH xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">0.77</d:BC_1MONTH>
<d:BC_3MONTH xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">0.8</d:BC_3MONTH>
<d:BC_6MONTH xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">0.93</d:BC_6MONTH>
<d:BC_1YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.03</d:BC_1YEAR>
<d:BC_2YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.24</d:BC_2YEAR>
<d:BC_3YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.44</d:BC_3YEAR>
<d:BC_5YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.85</d:BC_5YEAR>
<d:BC_7YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.14</d:BC_7YEAR>
<d:BC_10YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.34</d:BC_10YEAR>
<d:BC_20YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.71</d:BC_20YEAR>
<d:BC_30YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.98</d:BC_30YEAR>
<d:BC_30YEARDISPLAY xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.98</d:BC_30YEARDISPLAY>
</m:properties>
</content>
</entry>
<entry xmlns="http://www.w3.org/2005/Atom">
<id>
http://data.treasury.gov/Feed.svc/DailyTreasuryYieldCurveRateData(6823)
</id>
<title type="text"/>
<updated>2017-04-17T20:02:19Z</updated>
<author>
<name/>
</author>
<link rel="edit" title="DailyTreasuryYieldCurveRateDatum" href="DailyTreasuryYieldCurveRateData(6823)"/>
<category term="TreasuryDataWarehouseModel.DailyTreasuryYieldCurveRateDatum" scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme"/>
<content type="application/xml">
<m:properties xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata">
<d:Id xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Int32">6823</d:Id>
<d:NEW_DATE xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.DateTime">2017-04-06T00:00:00</d:NEW_DATE>
<d:BC_1MONTH xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">0.78</d:BC_1MONTH>
<d:BC_3MONTH xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">0.79</d:BC_3MONTH>
<d:BC_6MONTH xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">0.94</d:BC_6MONTH>
<d:BC_1YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.05</d:BC_1YEAR>
<d:BC_2YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.24</d:BC_2YEAR>
<d:BC_3YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.45</d:BC_3YEAR>
<d:BC_5YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.87</d:BC_5YEAR>
<d:BC_7YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.15</d:BC_7YEAR>
<d:BC_10YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.34</d:BC_10YEAR>
<d:BC_20YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.72</d:BC_20YEAR>
<d:BC_30YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.99</d:BC_30YEAR>
<d:BC_30YEARDISPLAY xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.99</d:BC_30YEARDISPLAY>
</m:properties>
</content>
</entry>
<entry xmlns="http://www.w3.org/2005/Atom">
<id>
http://data.treasury.gov/Feed.svc/DailyTreasuryYieldCurveRateData(6824)
</id>
<title type="text"/>
<updated>2017-04-17T20:02:19Z</updated>
<author>
<name/>
</author>
<link rel="edit" title="DailyTreasuryYieldCurveRateDatum" href="DailyTreasuryYieldCurveRateData(6824)"/>
<category term="TreasuryDataWarehouseModel.DailyTreasuryYieldCurveRateDatum" scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme"/>
<content type="application/xml">
<m:properties xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata">
<d:Id xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Int32">6824</d:Id>
<d:NEW_DATE xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.DateTime">2017-04-07T00:00:00</d:NEW_DATE>
<d:BC_1MONTH xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">0.77</d:BC_1MONTH>
<d:BC_3MONTH xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">0.82</d:BC_3MONTH>
<d:BC_6MONTH xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">0.95</d:BC_6MONTH>
<d:BC_1YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.08</d:BC_1YEAR>
<d:BC_2YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.29</d:BC_2YEAR>
<d:BC_3YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.52</d:BC_3YEAR>
<d:BC_5YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.92</d:BC_5YEAR>
<d:BC_7YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.2</d:BC_7YEAR>
<d:BC_10YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.38</d:BC_10YEAR>
<d:BC_20YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.74</d:BC_20YEAR>
<d:BC_30YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">3</d:BC_30YEAR>
<d:BC_30YEARDISPLAY xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">3</d:BC_30YEARDISPLAY>
</m:properties>
</content>
</entry>
<entry xmlns="http://www.w3.org/2005/Atom">
<id>
http://data.treasury.gov/Feed.svc/DailyTreasuryYieldCurveRateData(6825)
</id>
<title type="text"/>
<updated>2017-04-17T20:02:19Z</updated>
<author>
<name/>
</author>
<link rel="edit" title="DailyTreasuryYieldCurveRateDatum" href="DailyTreasuryYieldCurveRateData(6825)"/>
<category term="TreasuryDataWarehouseModel.DailyTreasuryYieldCurveRateDatum" scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme"/>
<content type="application/xml">
<m:properties xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata">
<d:Id xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Int32">6825</d:Id>
<d:NEW_DATE xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.DateTime">2017-04-10T00:00:00</d:NEW_DATE>
<d:BC_1MONTH xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">0.77</d:BC_1MONTH>
<d:BC_3MONTH xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">0.82</d:BC_3MONTH>
<d:BC_6MONTH xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">0.97</d:BC_6MONTH>
<d:BC_1YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.07</d:BC_1YEAR>
<d:BC_2YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.29</d:BC_2YEAR>
<d:BC_3YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.52</d:BC_3YEAR>
<d:BC_5YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.91</d:BC_5YEAR>
<d:BC_7YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.18</d:BC_7YEAR>
<d:BC_10YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.37</d:BC_10YEAR>
<d:BC_20YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.72</d:BC_20YEAR>
<d:BC_30YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.99</d:BC_30YEAR>
<d:BC_30YEARDISPLAY xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.99</d:BC_30YEARDISPLAY>
</m:properties>
</content>
</entry>
<entry xmlns="http://www.w3.org/2005/Atom">
<id>
http://data.treasury.gov/Feed.svc/DailyTreasuryYieldCurveRateData(6826)
</id>
<title type="text"/>
<updated>2017-04-17T20:02:19Z</updated>
<author>
<name/>
</author>
<link rel="edit" title="DailyTreasuryYieldCurveRateDatum" href="DailyTreasuryYieldCurveRateData(6826)"/>
<category term="TreasuryDataWarehouseModel.DailyTreasuryYieldCurveRateDatum" scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme"/>
<content type="application/xml">
<m:properties xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata">
<d:Id xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Int32">6826</d:Id>
<d:NEW_DATE xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.DateTime">2017-04-11T00:00:00</d:NEW_DATE>
<d:BC_1MONTH xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">0.74</d:BC_1MONTH>
<d:BC_3MONTH xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">0.82</d:BC_3MONTH>
<d:BC_6MONTH xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">0.94</d:BC_6MONTH>
<d:BC_1YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.05</d:BC_1YEAR>
<d:BC_2YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.24</d:BC_2YEAR>
<d:BC_3YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.45</d:BC_3YEAR>
<d:BC_5YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.84</d:BC_5YEAR>
<d:BC_7YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.11</d:BC_7YEAR>
<d:BC_10YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.32</d:BC_10YEAR>
<d:BC_20YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.67</d:BC_20YEAR>
<d:BC_30YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.93</d:BC_30YEAR>
<d:BC_30YEARDISPLAY xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.93</d:BC_30YEARDISPLAY>
</m:properties>
</content>
</entry>
<entry xmlns="http://www.w3.org/2005/Atom">
<id>
http://data.treasury.gov/Feed.svc/DailyTreasuryYieldCurveRateData(6827)
</id>
<title type="text"/>
<updated>2017-04-17T20:02:19Z</updated>
<author>
<name/>
</author>
<link rel="edit" title="DailyTreasuryYieldCurveRateDatum" href="DailyTreasuryYieldCurveRateData(6827)"/>
<category term="TreasuryDataWarehouseModel.DailyTreasuryYieldCurveRateDatum" scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme"/>
<content type="application/xml">
<m:properties xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata">
<d:Id xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Int32">6827</d:Id>
<d:NEW_DATE xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.DateTime">2017-04-12T00:00:00</d:NEW_DATE>
<d:BC_1MONTH xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">0.77</d:BC_1MONTH>
<d:BC_3MONTH xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">0.81</d:BC_3MONTH>
<d:BC_6MONTH xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">0.95</d:BC_6MONTH>
<d:BC_1YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.04</d:BC_1YEAR>
<d:BC_2YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.24</d:BC_2YEAR>
<d:BC_3YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.44</d:BC_3YEAR>
<d:BC_5YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.81</d:BC_5YEAR>
<d:BC_7YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.09</d:BC_7YEAR>
<d:BC_10YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.28</d:BC_10YEAR>
<d:BC_20YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.65</d:BC_20YEAR>
<d:BC_30YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.92</d:BC_30YEAR>
<d:BC_30YEARDISPLAY xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.92</d:BC_30YEARDISPLAY>
</m:properties>
</content>
</entry>
<entry xmlns="http://www.w3.org/2005/Atom">
<id>
http://data.treasury.gov/Feed.svc/DailyTreasuryYieldCurveRateData(6828)
</id>
<title type="text"/>
<updated>2017-04-17T20:02:19Z</updated>
<author>
<name/>
</author>
<link rel="edit" title="DailyTreasuryYieldCurveRateDatum" href="DailyTreasuryYieldCurveRateData(6828)"/>
<category term="TreasuryDataWarehouseModel.DailyTreasuryYieldCurveRateDatum" scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme"/>
<content type="application/xml">
<m:properties xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata">
<d:Id xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Int32">6828</d:Id>
<d:NEW_DATE xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.DateTime">2017-04-13T00:00:00</d:NEW_DATE>
<d:BC_1MONTH xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">0.76</d:BC_1MONTH>
<d:BC_3MONTH xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">0.81</d:BC_3MONTH>
<d:BC_6MONTH xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">0.94</d:BC_6MONTH>
<d:BC_1YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.03</d:BC_1YEAR>
<d:BC_2YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.21</d:BC_2YEAR>
<d:BC_3YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.4</d:BC_3YEAR>
<d:BC_5YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.77</d:BC_5YEAR>
<d:BC_7YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.05</d:BC_7YEAR>
<d:BC_10YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.24</d:BC_10YEAR>
<d:BC_20YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.62</d:BC_20YEAR>
<d:BC_30YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.89</d:BC_30YEAR>
<d:BC_30YEARDISPLAY xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.89</d:BC_30YEARDISPLAY>
</m:properties>
</content>
</entry>
<entry xmlns="http://www.w3.org/2005/Atom">
<id>
http://data.treasury.gov/Feed.svc/DailyTreasuryYieldCurveRateData(6829)
</id>
<title type="text"/>
<updated>2017-04-17T20:02:19Z</updated>
<author>
<name/>
</author>
<link rel="edit" title="DailyTreasuryYieldCurveRateDatum" href="DailyTreasuryYieldCurveRateData(6829)"/>
<category term="TreasuryDataWarehouseModel.DailyTreasuryYieldCurveRateDatum" scheme="http://schemas.microsoft.com/ado/2007/08/dataservices/scheme"/>
<content type="application/xml">
<m:properties xmlns:m="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata">
<d:Id xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Int32">6829</d:Id>
<d:NEW_DATE xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.DateTime">2017-04-17T00:00:00</d:NEW_DATE>
<d:BC_1MONTH xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">0.76</d:BC_1MONTH>
<d:BC_3MONTH xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">0.83</d:BC_3MONTH>
<d:BC_6MONTH xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">0.94</d:BC_6MONTH>
<d:BC_1YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.04</d:BC_1YEAR>
<d:BC_2YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.21</d:BC_2YEAR>
<d:BC_3YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.42</d:BC_3YEAR>
<d:BC_5YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">1.79</d:BC_5YEAR>
<d:BC_7YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.07</d:BC_7YEAR>
<d:BC_10YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.26</d:BC_10YEAR>
<d:BC_20YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.65</d:BC_20YEAR>
<d:BC_30YEAR xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.92</d:BC_30YEAR>
<d:BC_30YEARDISPLAY xmlns:d="http://schemas.microsoft.com/ado/2007/08/dataservices" m:type="Edm.Double">2.92</d:BC_30YEARDISPLAY>
</m:properties>
</content>
</entry>
</pre>"""

CHECK_POINTS = {
    2017: dict(
        date="2017-04-03",
        BC_1MONTH=0.73,
        BC_3MONTH=0.79,
        BC_6MONTH=0.92,
        BC_1YEAR=1.02,
        BC_2YEAR=1.24,
        BC_3YEAR=1.47,
        BC_5YEAR=1.88,
        BC_7YEAR=2.16,
        BC_10YEAR=2.35,
        BC_20YEAR=2.71,
        BC_30YEAR=2.98,
        BC_30YEARDISPLAY=2.98,
    )
}

# NOT TODO: extend CHECK_POINTS for each year in 1990:2016.
#          (may use actual parsing data for 1990:2016)

# NOT TODO: check data in pandas DataFrame

import ust


def test_sample_string():
    pts = list(ust.yield_datapoints_from_string(xml_content=XML_CONTENT_2017))
    assert CHECK_POINTS[2017] in pts
    assert pts[0] == CHECK_POINTS[2017]
    assert len(pts) == 10
    assert len(pts[0]) == 13


def test_2017_web_call():
    content = ust.get_xml_content_from_web(2017)
    pts = list(ust.yield_datapoints_from_string(content))
    assert CHECK_POINTS[2017] in pts


def test_url():
    assert (
        ust.get_url(2017)
        == "https://www.treasury.gov/resource-center/data-chart-center/interest-rates/pages/XmlView.aspx?data=yieldyear&year=2017"
    )


def replicate_no_data_error():
    """Causes server overload and getting html file instead of xml.
    WARNING: error may not replicate, seems to depend on your IP address."""
    for i in range(10):
        content = ust.get_web_xml(2002)
        print(content[:100])
        if not content.startswith("<?xml"):
            ust.save_local_xml("error", content)


if __name__ == "__main__":
    test_sample_string()
    test_url()
    # test_2017_web_call()
    # replicate_no_data_error()
