# Current Weather PWS

Using Python(language), Flask (framework) and Jinja2 (template) to get and display current weather conditions from [WUnderground API](https://www.wunderground.com/weather/api/). From one station in WU's 250,000+ [Personal Weather Station Network](https://www.wunderground.com/weatherstation/overview.asp)

![current]

## Imports

```py
from flask import Flask, flash, redirect, render_template, request
from urllib3 import PoolManager
import json
```

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

[current]: current-weather-pws.png "get current weather conditions"
