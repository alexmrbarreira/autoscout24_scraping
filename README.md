# car_website_scraping
Simple set of python scripts that gather data from car websites and plots a few car properties together. Useful to rapidly browse available car offers and visualize market trends.

### Table of contents
- [Dependencies](#dependencies)
- [Running the scripts](#running-the-scripts)
- [Results overview for different cars, same country](#results-overview-for-different-cars-same-country)

### Dependencies

- numpy and matplotlib
- pandas
- bs4 - python web scraping library

### Running the scripts
There are two sets of scripts: (i) one for offers in Germany from autoscout24.de and (ii) another for offers in Portugal from standvirtual.com. Their use is similar.

To get and plot data from autoscout24.de (German offers) simply:
- choose search car options in *parameters_de.py*. Check existing examples; to add more check brand/model names in autoscout24.de.
- run *python scrape_autoscout24_de.py*. This saves a car data table in *data_store_de/*.
- run *python plot_data_de.py*. This makes a plot with key car data; the figure is saved in *fig_store_de/*.

To get and plot data from standvirtual.com (Portuguese) simply:
- choose search car options in *parameters_pt.py*. Check existing examples; to add more check brand/model names in standvirtual.com
- run *python scrape_standvirtual_pt.py*. This saves a car data table in *data_store_pt/*.
- run *python plot_data_pt.py*. This makes a plot with key car data; the figure is saved in *fig_store_pt/*.

### Results overview for different cars same country
![fig_golf_de](./fig_store_de/fig_2016_kombi_volkswagen_golf.png)
