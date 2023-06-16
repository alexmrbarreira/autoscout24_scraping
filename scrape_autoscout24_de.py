
from parameters_de import *

# ======================================================= 
# Loop over autoscout24 search pages to collect URLs of individual car offers
# ======================================================= 
cars_URL = []
for page in range(1, max_page+1):
    print ('Collecting car URLs from autoscout24 page', page)
    # Call main URL from which to collect car URLs (save all links - a tags)
    try:
        url = 'https://www.autoscout24.de/lst/'+str(brand)+'/'+str(model)+'/bt_'+str(body_type)+'?atype=C&cy=D&damaged_listing=exclude&desc=0&fregfrom='+str(min_year)+'&lat=48.13913&lon=11.58022&ocs_listing=include&page='+str(page)+'&powertype=kw&search_id=2bepz5o1y9t&sort=standard&source=listpage_pagination&zipr=100'
        only_a_tags = SoupStrainer("a")
        soup = BeautifulSoup(requests.get(url).text,'lxml', parse_only=only_a_tags)
    except Exception as e:
        print("Call to main URL failed: " + str(e) +" "*50, end="\r")
        pass

    # From the soup objects, keep only URLs with "angebote" ("offers")
    for link in soup.find_all("a"):
        target_url = str(link.get("href"))
        if (r"/angebote/" in target_url) and (r"/leasing/" not in target_url): # include normal offers (exc. smyle offers -- autoscout online buying system)
            if( (brand not in target_url) or (model not in target_url)):
                print ('The brand/model strings do not appear in the car URLs; could signal that the search failed. Check input parameters.')
                print ('brand, model, URL = ', brand, model, target_url)
            cars_URL.append(target_url)

# Remove duplicates 
cars_URL = list(dict.fromkeys(cars_URL))

print ('Total number of car URLs', len(cars_URL))

# ======================================================= 
# Loop over car URLs and parse desired information (this part is very specific to the html of autoscout pages)
# ======================================================= 
cars_data = []
counter = 1
for url in cars_URL:
    dict_now = {}
    if (np.mod(counter, int(len(cars_URL)/10))==0):
        print ('Done collecting data for', counter, 'cars')

    try:
        car         = BeautifulSoup(requests.get('https://www.autoscout24.de' + url).text, 'lxml')
        price_parse = car.find_all("span", attrs={"class":"PriceInfo_price__JPzpT"})
        other_parse = car.find_all("div", attrs={"class":"VehicleOverview_itemText__V1yKT"})

        # Get the attributes: {price, km, transmission, year, gas, power} (playing string tricks here to get desired data)
        price = price_parse[0].text.split()[1].split(',')[0]
        km    = other_parse[0].text.split()[0]
        trans = other_parse[1].text
        year  = other_parse[2].text.split('/')[1]
        gas   = other_parse[3].text.split()[0]
        power = other_parse[4].text.split()[2].split('(')[1]

        cars_data.append([price, km, power, year, gas, trans, url])
        counter += 1

    except Exception as e:
        print ('Loading data failed for car URL', url, ':' + str(e) +" "*50, end="\r")
        counter += 1

# Save to file
df = pd.DataFrame(cars_data, columns=['Price', 'Km', 'Power', 'Year', 'Gas', 'Transmission', 'URL'])
df.to_csv(data_filename)

