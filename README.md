# Eikon_Python
## Python: Thomson Reuters Eikon API


### Overview:
Thomson Reuters Eikon (licenced) provides access to real-time market data, news, fundamental and reference data, research and analytics etc. Most of the data available from Eikon can be retrieved programmatically using APIs. These APIs are designed for ease of use and for rapid application development. The APIs could also be utilized in a variety of development environments including Microsoft Visual Studio, Matlab, R, Microsoft Office VBA. Check out https://developers.thomsonreuters.com/ for more information.

### Steps:

First, download, install and run the Eikon Scripting Proxy from the [developers portal](https://developers.thomsonreuters.com/) and request an AppID.

Install Eikon Python API:
```
pip install eikon
```

Start and set your AppID (while the Eikon Scripting Proxy is running):
```
import eikon
eikon.set_app_id('xxxx')
```

Commands:
```
eikon.get_symbology()
eikon.get_news_headlines()
eikon.get_news_story()
eikon.get_timeseries()
eikon.get_data()
eikon.MarketPriceStream()
```

### Licence:
The Thomson Reuters Eikon end user license agreement prohibits any type of data redistribution. If you require redistribution of data, then you should consider one of the Thomson Reuters Enterprise products. Application developers using Eikon APIs do not need to worry about data entitlements as these are enforced by Eikon and shared with the APIs. 


### Requirements:
- Python 2.7+ or 3.4+
- Eikon Scripting Proxy
- EikonID



### Release Notes:
-update-
