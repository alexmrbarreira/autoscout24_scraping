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
max_page  = 20 
min_year  = '2016'

# Audi
#brand = 'audi'
#model = 'a4-avant'

# BMW
#brand = 'bmw'
#model = 'serie-3'
#model = 'serie-5'

# Mercedes
#brand = 'mercedes-benz'
#model = 'classe-c'
#model = 'classe-e'

# Skoda
#brand     = 'skoda'
#model     = 'octavia-break'
#model     = 'superb-break'

# Volkswagen
brand = 'vw'
model = 'golf-variant'
#model = 'passat-variant'

# Volvo
#brand = 'volvo'
#model = 'v60'


data_filename = 'data_store_pt/data_' + min_year + '_' + brand + '_' + model + '.csv'
fig_filename  = 'fig_store_pt/fig_' + min_year + '_' + brand + '_' + model + '.png'
