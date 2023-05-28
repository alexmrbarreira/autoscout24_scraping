
from parameters_de import *

# ======================================================= 
# Load searched car data 
# ======================================================= 
df    = pd.read_csv(data_filename)

price = df.loc[:,'Price'].tolist()
km    = df.loc[:,'Km'].tolist()
power = df.loc[:,'Power'].tolist()
year  = df.loc[:,'Year'].tolist()
gas   = df.loc[:,'Gas'].tolist()
trans = df.loc[:,'Transmission'].tolist()
url   = df.loc[:,'URL'].tolist()

# =======================================================
# List a few desired URLs 
# =======================================================

print_URL = True
#print_URL = False

open_URL = True
#open_URL = False

price_min = 00.
price_max = 25.
km_min    = 0.
km_max    = 75.
power_min = 150.
power_max = 500.
year_min  = 2019
year_max  = 2023

if(print_URL):
    print ('')
    print ('Selected URLs for:')
    print ('Price in [', price_min, price_max,']')
    print ('Km in    [', km_min   , km_max   ,']')
    print ('Power in [', power_min, power_max,']')
    print ('Year in  [', year_min , year_max ,']')
    wc_url = np.where( (np.array(price) >= price_min) & (np.array(price) <= price_max) &
                       (np.array(km)    >= km_min)    & (np.array(km)    <= km_max)    &
                       (np.array(power) >= power_min) & (np.array(power) <= power_max) &
                       (np.array(year)  >= year_min)  & (np.array(year)  <= year_max)  )
    price_sel = np.array(price)[wc_url]
    km_sel    = np.array(km)[wc_url]
    for a in np.array(url)[wc_url]:
        print ('autoscout24.de' + a)

if(open_URL):
    print ('')
    print ('Opening selected URLs with firefox ... set open_URL=False to skip this.')
    string_of_urls = ''
    for url_now in np.array(url)[wc_url]:
        string_of_urls += 'autoscout24.de' + url_now + ' '
    os.system('firefox ' + string_of_urls)
    print ('')

# =======================================================
# Make plot
# =======================================================

def mark_selected(xx, yy):
    fontsize_here = 16
    for i in range(len(xx)):
        draw_circle(xx[i], yy[i])
    plt.annotate('Selection (circles):'                                         , xy = (0.55, 0.25), xycoords = 'axes fraction', c = 'k', fontsize = fontsize_here)
    plt.annotate(r'Price $\ \in$   ['   + str(int(price_min))  + ',' + str(int(price_max)) + ']', xy = (0.55, 0.20), xycoords = 'axes fraction', c = 'k', fontsize = fontsize_here)
    plt.annotate(r'Km    $\ \ \ \in$ [' + str(int(km_min))     + ',' + str(int(km_max))    + ']', xy = (0.55, 0.15), xycoords = 'axes fraction', c = 'k', fontsize = fontsize_here)
    plt.annotate(r'Power $\in$     ['   + str(int(power_min))  + ',' + str(int(power_max)) + ']', xy = (0.55, 0.10), xycoords = 'axes fraction', c = 'k', fontsize = fontsize_here)
    plt.annotate(r'Year  $\ \ \in$   [' + str(int(year_min))   + ',' + str(int(year_max))  + ']', xy = (0.55, 0.05), xycoords = 'axes fraction', c = 'k', fontsize = fontsize_here)
    return 0
def draw_circle(x0, y0):
    r   = 1.
    xx  = np.linspace(x0-r, x0+r, 100)
    yy1 =  np.sqrt( -(xx - x0)**2. + r**2. ) + y0
    yy2 = -np.sqrt( -(xx - x0)**2. + r**2. ) + y0
    plt.plot(xx, yy1, c = 'k', linestyle = 'solid', linewidth = 1)
    plt.plot(xx, yy2, c = 'k', linestyle = 'solid', linewidth = 1)
    return 0

labelsize   = 30
ticksize    = 30
ticklength_major  = 10.
ticklength_minor  = 5.
tickwidth   = 1.5
tickpad     = 6. 
title_font  = 30
text_font   = 20
legend_font = 20
alpha_c     = 0.4
cmap_use    = 'jet'

min_x = 0.
max_x = 150.
min_y = 0.
max_y = 50.

max_power_colors = 250
min_power_colors = 100
max_year_colors = 2023
min_year_colors = 2016

max_price_want = 25.
max_km_want    = 75.

fig1 = plt.figure(1, figsize=(17., 7.))
fig1.subplots_adjust(left=0.07, right=0.97, top=0.92, bottom=0.15, wspace = 0.35, hspace = 0.30)

# colors by power and symbols by transmission
panel = fig1.add_subplot(1,2,1)
plt.title('Search:' + min_year + ',' + body_type + ',' + brand + ',' + model, fontsize = title_font)
wc_1 = np.where(np.array(trans) == 'Schaltgetriebe')
wc_2 = np.where(np.array(trans) == 'Automatik')
plt.scatter(np.array(km)[wc_1], np.array(price)[wc_1], c = np.array(power)[wc_1], s = 40, marker = 'o', label = 'Manual', cmap = cmap_use, vmin = min_power_colors, vmax = max_power_colors)
plt.scatter(np.array(km)[wc_2], np.array(price)[wc_2], c = np.array(power)[wc_2], s = 40, marker = '^', label = 'Automatic', cmap = cmap_use, vmin = min_power_colors, vmax = max_power_colors)
plt.plot([0., max_km_want], [max_price_want, max_price_want], linewidth = 2., linestyle = 'dashed', c = 'k')
plt.plot([max_km_want, max_km_want], [0., max_price_want]   , linewidth = 2., linestyle = 'dashed', c = 'k')
mark_selected(np.array(km_sel), np.array(price_sel))
cb = plt.colorbar()
cb.set_label(r'Power (HP)', fontsize = labelsize-2)
cb.ax.tick_params(labelsize=ticksize-4)
plt.xlim(min_x, max_x)
plt.ylim(min_y, max_y)
plt.xlabel(r'Kilometers [1000]'  , fontsize = labelsize)
plt.ylabel(r'Price [1000 EUR]', fontsize = labelsize)
plt.tick_params(length=ticklength_major, width=tickwidth , bottom=True, top=True, left=True, right=True, direction = 'in', which = 'major', pad = tickpad, labelsize = ticksize)
params = {'legend.fontsize': legend_font}; plt.rcParams.update(params); plt.legend(loc = 'lower left', ncol = 1)

# colors by year and symbols by gas
panel = fig1.add_subplot(1,2,2)
plt.title('Country: Deutschland', fontsize = title_font)
wc_1 = np.where(np.array(gas) == 'Benzin')
wc_2 = np.where(np.array(gas) == 'Diesel')
plt.scatter(np.array(km)[wc_1], np.array(price)[wc_1], c = np.array(year)[wc_1], s = 40, marker = 'o', label = 'Gasoline', cmap = cmap_use, vmin = min_year_colors, vmax = max_year_colors)
plt.scatter(np.array(km)[wc_2], np.array(price)[wc_2], c = np.array(year)[wc_2], s = 40, marker = '^', label = 'Diesel', cmap = cmap_use, vmin = min_year_colors, vmax = max_year_colors)
plt.plot([0., max_km_want], [max_price_want, max_price_want], linewidth = 2., linestyle = 'dashed', c = 'k')
plt.plot([max_km_want, max_km_want], [0., max_price_want]   , linewidth = 2., linestyle = 'dashed', c = 'k')
mark_selected(np.array(km_sel), np.array(price_sel))
cb = plt.colorbar()
cb.set_label(r'Year', fontsize = labelsize-2)
cb.ax.tick_params(labelsize=ticksize-4)
plt.xlim(min_x, max_x)
plt.ylim(min_y, max_y)
plt.xlabel(r'Kilometers [1000]'  , fontsize = labelsize)
plt.ylabel(r'Price [1000 EUR]', fontsize = labelsize)
plt.tick_params(length=ticklength_major, width=tickwidth , bottom=True, top=True, left=True, right=True, direction = 'in', which = 'major', pad = tickpad, labelsize = ticksize)
params = {'legend.fontsize': legend_font}; plt.rcParams.update(params); plt.legend(loc = 'lower left', ncol = 1)


plt.savefig(fig_filename)
plt.show()
