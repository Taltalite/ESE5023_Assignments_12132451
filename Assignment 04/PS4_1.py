import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

def colorbar_tick(x, pos):
    return int(x*10)

us_eq = pd.read_csv('usgs_earthquakes.csv')

top50 = us_eq.sort_values('mag', ascending=False).head(50)[['latitude', 'longitude', 'mag']]

longitudes = top50['longitude']
latitudes = top50['latitude']

plt.figure(figsize=(10, 6), dpi=100)
proj = ccrs.Robinson(central_longitude=180)
ax = plt.axes(projection=proj)
ax.stock_img()
ax.set_title('Top 50 Earthquakes of 2014')
scat = ax.scatter(longitudes, latitudes, marker='o', c=top50['mag'], s=20, cmap='Reds', edgecolors='black',
           transform=ccrs.PlateCarree())

ticks = np.linspace(6.6, 8.2, num=9)
clb = plt.colorbar(scat, label='magnitude', orientation='vertical', fraction=0.01)
clb.set_ticks(ticks)
plt.show()
