from bs4 import BeautifulSoup, SoupStrainer #HTML parsing
import numpy as np
import matplotlib.pyplot as plt
import requests
import os
import pandas as pd
plt.rcParams.update({'text.usetex': True, 'mathtext.fontset': 'stix'}) #['dejavuserif', 'cm', 'custom', 'stix', 'stixsans', 'dejavusans']

# ======================================================= 
# Search parameters
# ======================================================= 
country   = 'D'
max_page  = 20 # The autoscout24 website does not show more than 20 pages (and ~20 cars per page, so search is complete only if filters result in about 400 cars)
min_year  = '2016'
body_type = 'kombi'

# Audi
#brand = 'audi'
#model = 'a4'

# BMW
brand     = 'bmw'
model     = '3er-(alle)'
#model     = '5er-(alle)'

# Mercedes
#brand = 'mercedes-benz'
#model = 'c-klasse-(alle)'
#model = 'e-klasse-(alle)'

# Skoda
#brand     = 'skoda'
#model     = 'octavia'

# Volkswagen
#brand     = 'volkswagen'
#model     = 'golf'
#model     = 'passat-variant'

# Volvo
#brand = 'volvo'
#model = 'v60'

data_filename = 'data_store_de/data_' + min_year + '_' + body_type + '_' + brand + '_' + model + '.csv'
fig_filename  = 'fig_store_de/fig_' + min_year + '_' + body_type + '_' + brand + '_' + model + '.png'


# ======================================================= 
# Selected car parameters 
# ======================================================= 

price_min = 00.
price_max = 28.
km_min    = 0.
km_max    = 90.
power_min = 151.
power_max = 500.
year_min  = 2018
year_max  = 2023
