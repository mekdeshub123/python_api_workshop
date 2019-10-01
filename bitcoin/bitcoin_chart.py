from datetime import date 

from bokeh.plotting import figure, output_file, show 
from bokeh.palettes import Spectral6
from bokeh.transform import linear_cmap 

import requests 

coinbase_url = 'https://api.coindesk.com/v1/bpi/historical/close.json'

response = requests.get(coinbase_url).json()
bpi = response['bpi']

dates = []
prices = []

for d, price in bpi.items():
    dates.append(date.fromisoformat(d))
    prices.append(price)

output_file('bitcoin.html')

mapper = linear_cmap(field_name='y', palette=Spectral6, low=min(prices), high=max(prices))

plot = figure(title='Bitcoin Price, from Coindesk.com', x_axis_label='Date', y_axis_label='Price, US Dollars', x_axis_type="datetime")

plot.line(dates, prices, line_width=1, color='gray', line_alpha=0.5)
plot.circle(dates, prices, legend='Bitcoin Price', line_width=7, color=mapper)

show(plot)