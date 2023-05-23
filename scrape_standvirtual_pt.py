
from parameters_pt import *

# ======================================================= 
# Loop over standvirtual search pages to collect URLs of individual car offers
# ======================================================= 
cars_URL = []
for page in range(1, max_page+1):
    print ('Collecting car URLs from standvirtual page', page)
    # Call main URL from which to collect car URLs (save all links - a tags)
    try:
        if( (brand == 'bmw') or (brand == 'mercedes-benz') ):
            url = 'https://www.standvirtual.com/carros/'+str(brand)+'/desde-'+str(min_year)+'?search%5Bfilter_enum_engine_code%5D='+str(model)+'&page='+str(page)
        else:
            url = 'https://www.standvirtual.com/carros/'+str(brand)+'/'+str(model)+'/desde-'+str(min_year)+'?page='+str(page)
        only_a_tags = SoupStrainer("a")
        soup = BeautifulSoup(requests.get(url).text,'lxml', parse_only=only_a_tags)
    except Exception as e:
        print("Call to main URL failed: " + str(e) +" "*50, end="\r")
        pass

    # From the soup objects, keep only URLs with "anuncio" ("offers")
    for link in soup.find_all("a"):
        target_url = str(link.get("href"))
        #if (r"/anuncio/" in target_url) and (r"/leasing/" not in target_url): # this just removes some urls that contain angebote, but are not actual car offers
        if (r"/anuncio/" in target_url): 
            if( (brand not in target_url) or (model not in target_url)):
                print ('The brand/model strings to not appear in the car URLs; could signal that the search failed. Check input parameters.')
                print ('brand, model, URL = ', brand, model, target_url)
            cars_URL.append(target_url)

# Remove duplicates 
cars_URL = list(dict.fromkeys(cars_URL))

print ('Total number of car URLs', len(cars_URL))

# ======================================================= 
# Loop over car URLs and parse desired information (this part is very specific to the html of standvirtual pages)
# ======================================================= 
cars_data = []
counter = 1
for url in cars_URL:
    dict_now = {}
    if (np.mod(counter, int(len(cars_URL)/10))==0):
        print ('Done collecting data for', counter, 'cars')

    try:
        # Get the attributes: {price, km, transmission, year, gas, power} (playing string tricks here to get desired data)
        car           = BeautifulSoup(requests.get(url).text, 'lxml')
        price         = car.find("span", attrs={"class":"offer-price__number"}).find(text=True, recursive=False).replace(" ", "")
        details_parse = car.find_all("li", attrs={"class":"offer-params__item"})

        for details in details_parse:
            if (details.find("span").text == 'Quilómetros'):
                km    = details.find("div").text.replace(" ", "").split('km')[0].strip()
            if (details.find("span").text == 'Tipo de Caixa'):
                trans = details.find("div").text.replace(" ", "").strip()
            if (details.find("span").text == 'Ano'):
                year = details.find("div").text.replace(" ", "").strip()
            if (details.find("span").text == 'Combustível'):
                gas = details.find("div").text.replace(" ", "").strip()
            if (details.find("span").text == 'Potência'):
                power = details.find("div").text.replace(" ", "").split('cv')[0].strip()

        cars_data.append([price, km, power, year, gas, trans, url])
        counter += 1

    except Exception as e:
        print ('Loading data failed for car URL', url, ':' + str(e) +" "*50, end="\r")
        counter += 1

# Save to file
df = pd.DataFrame(cars_data, columns=['Price', 'Km', 'Power', 'Year', 'Gas', 'Transmission', 'URL'])
df.to_csv(data_filename)

