# Current Weather PWS

Using Python(language), Flask (framework) and Jinja2 (template) to get and display current weather conditions from [WUnderground API](https://www.wunderground.com/weather/api/). From one station in WU's 250,000+ [Personal Weather Station Network](https://www.wunderground.com/weatherstation/overview.asp)

![current]

## Imports

```py
from flask import Flask, flash, redirect, render_template, request
from urllib3 import PoolManager
import json
```

## Dependencies

The [Anaconda Python distribution](https://anaconda.org/) was used to develop this app, so related dependencies have been linked below:

 * [python 3.6.4](https://repo.continuum.io/pkgs/main/linux-64/python-3.6.4-hc3d631a_1.tar.bz2)
 * [flask 0.12.2](https://conda.anaconda.org/conda-forge/linux-64/flask-0.12.2-py36_0.tar.bz2)
   - [click 6.7](https://conda.anaconda.org/conda-forge/noarch/click-6.7-py_1.tar.bz2)
   - [itsdangerous 0.24](https://conda.anaconda.org/conda-forge/noarch/itsdangerous-0.24-py_2.tar.bz2)
   - [jinja2 2.10](https://conda.anaconda.org/conda-forge/linux-64/jinja2-2.10-py36_0.tar.bz2)
   - [werkzeug 0.14.1](https://conda.anaconda.org/conda-forge/noarch/werkzeug-0.14.1-py_0.tar.bz2)
 * [urllib3 1.22](https://conda.anaconda.org/conda-forge/linux-64/urllib3-1.22-py36_0.tar.bz2)
 * [simplejson 3.13.2](https://pypi.python.org/pypi/simplejson/3.13.2) (PyPI)

Sudden changes may not reflect the list above, since additional required modules may be overlooked.

**NOTE**: **virtual environments** should act jointly with development environments, since operating systems use a subset of Python. Added modules may modify important dependencies which potentially corrupt the system. 

## Jinja2

_Jinja2_ is inclusive, just as templates live in a specific directory, e.g. `/templates`. Since templates specify HTML document structure. Notice the _handlebar_ structure insertion below, e.g. `{{ co['weather'] }}`.

```html
<table>
    <tr>
      <td><span class="blue">Weather condition</span></td>
      <td>{{ co['weather'] }}</td>
    </tr>
...
```

## current_cond()

The `current_cond()` method assigns a dictionary variable for insertion of URL parts.

```py
@app.route("/current/")
def current_cond():
    d = {'api_key': '51857b97d97c71a0',
         'state_code': 'IL',
         'personal_weather_station': 'pws:KILMORRI2'}
    pm = PoolManager()
```

Values from that dictionary are spliced into the URL to `GET` raw weather data from the API.

```py
    r = pm.request('GET', 'http://api.wunderground.com/api/' +
                   d['api_key'] + '/conditions/q/' + d['state_code'] +
                   '/' + d['personal_weather_station'] + '.json')
```

[current]: current-weather-pws.png "get current weather conditions"
