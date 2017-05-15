# Eikon_Python
## Python: Thomson Reuters Eikon API


### Overview:
The Thomson Reuters Eikon API provides simple access to users who require programmatic access to Thomson Reuters data on the desktop.   Check out https://developers.thomsonreuters.com/ for more information.

### Steps:

First, download, install and run the Eikon Scripting Proxy from the [developers portal](https://developers.thomsonreuters.com/) and request an AppID.

Download the Eikon package for Python with pip*:
```
pip install eikon
```
*If you cannot use pip, you can install the package with wheel (https://pypi.python.org/pypi/eikon)

Start and set your AppID (while the Eikon Scripting Proxy is running):
```
import eikon
eikon.set_app_id('xxxx')
```

Now you can use the following commands:
```
eikon.get_symbology()
eikon.get_news_headlines()
eikon.get_news_story()
eikon.get_timeseries()
eikon.get_data()
```

### Licence:
The Thomson Reuters Eikon end user license agreement prohibits any type of data redistribution. If you require redistribution of data, then you should consider one of the Thomson Reuters Enterprise products. Application developers using Eikon APIs do not need to worry about data entitlements as these are enforced by Eikon and shared with the APIs. 


### Requirements:
- Python 2.7+ or 3.4+
- Eikon Scripting Proxy
- EikonID



### Release Notes:
-update-
