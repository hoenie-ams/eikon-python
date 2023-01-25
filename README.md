# Eikon with Python

### Overview:

The Refinitiv Eikon API provides simple access to users who require programmatic access to
Refinitiv data on the desktop. Check out the
[Official API Documentation](https://developers.refinitiv.com/en/api-catalog/eikon/eikon-data-api) for more information.

### Steps:

##### 1) Download the Eikon package for Python with pip*:

```shell
pip install eikon
```

*If you cannot use pip, you can install the package with wheel (https://pypi.python.org/pypi/eikon)

##### 2) Get your AppID" from the "Application ID Generator" in Eikon (you can find it through the search bar)

##### 3) Import the Eikon Python and set your AppID (while the Eikon is running):

```python
import eikon

eikon.set_app_key('xxxxxxxxxxxxxxxxxxxxxxx')
```

##### 4) Now you can use the following commands:

```python
eikon.get_symbology()
eikon.get_news_headlines()
eikon.get_news_story()
eikon.get_timeseries()
eikon.get_data()
```

##### 5) *EXAMPLE*: Retrieve data for an index and its constituents with `index_plus_constituents_time_series.py`

### Licence:

The Refinitiv (formerly Thomson Reuters) Eikon end user license agreement prohibits any type of data redistribution. If
you require redistribution of data, then you should consider one of the Thomson Reuters Enterprise products. Application
developers using Eikon APIs do not need to worry about data entitlements as these are enforced by Eikon and shared with
the APIs.

### Requirements:

- Python 2.7+ or 3.4+
- Eikon Scripting Proxy
- EikonID

### Release Notes:

- 2023-01-25: updated code example with type hints and f-strings
- 2017-05-16: Initial publication
