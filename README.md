# Current Weather PWS

Using Python(language), Flask (framework) and Jinja2 (template) to get and display current weather conditions from [WUnderground API](https://www.wunderground.com/weather/api/). From one station in WU's 250,000+ [Personal Weather Station Network](https://www.wunderground.com/weatherstation/overview.asp)

![current]

## Imports

```py
from flask import Flask, flash, redirect, render_template, request
from urllib3 import PoolManager
import json
```

[current]: current-weather-pws.png "get current weather conditions"
