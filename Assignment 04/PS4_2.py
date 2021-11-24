import xarray as xr
import matplotlib.pyplot as plt
from matplotlib import cm
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.ticker as mticker
import numpy as np
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.feature as cfeat
from cartopy.io.shapereader import Reader

MERRA2 = xr.open_dataset("./MERRA2_400.tavg1_2d_chm_Nx.20210901.nc4", engine="netcdf4")

spe_time = MERRA2.time[12].values
tspe_time = str(spe_time).split('T')
date = tspe_time[0]
ttime = tspe_time[1].split('.')[0]

COCL = MERRA2.sel(time=spe_time).COCL

"""
problem 2-1
"""
plt.figure(figsize=(16, 9), dpi=100)

X = MERRA2.lon.values
Y = MERRA2.lat.values

# proj = ccrs.Robinson(central_longitude=0)
proj = ccrs.PlateCarree()
ax = plt.axes(projection=proj)

# ax.add_feature(cfeature.LAND, edgecolor='black', facecolor='grey', alpha=0.5, zorder=1)
ax.add_feature(cfeature.COASTLINE, edgecolor='black')

Z = COCL

cntr = ax.contourf(X, Y, Z, levels=20, cmap=cm.viridis, transform=ccrs.PlateCarree())

# Draw gridlines
gl = ax.gridlines(crs=ccrs.PlateCarree(), linewidth=1, color='black', alpha=0.8, draw_labels=True, linestyle='--')

# Manipulate latitude and longitude gridline numbers and spacing
gl.ylocator = mticker.FixedLocator(np.arange(-90, 90, 30))
gl.xlocator = mticker.FixedLocator(np.arange(-180, 180, 30))
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

gl.xlabel_style = {'size': 12, 'color': 'gray'}
gl.xlabel_style = {'color': 'gray', 'weight': 'bold'}

gl.ylabel_style = {'size': 12, 'color': 'gray'}
gl.ylabel_style = {'color': 'gray', 'weight': 'bold'}

ax.set_title('CO Column Burden in %s %s' % (date, ttime))

plt.colorbar(cntr, label='COCL', orientation='vertical', fraction=0.01)

"""
problem 2-2
"""

fig = plt.figure(figsize=(8, 8), dpi=100)

# Load the border data, CN-border-La.dat is download from
# https://gmt-china.org/data/CN-border-La.dat
with open('CN-border-La.dat') as src:
    context = src.read()
    blocks = [cnt for cnt in context.split('>') if len(cnt) > 0]
    borders = [np.fromstring(block, dtype=float, sep=' ') for block in blocks]

central_lon, central_lat = 100.0, 30.0  # Shanghai

X = MERRA2.lon.values
Y = MERRA2.lat.values

# proj = ccrs.Robinson(central_longitude=0)
proj = ccrs.Orthographic(central_lon, central_lat)
ax = plt.axes(projection=proj)

# Set figure extent
ax.set_extent([75, 135, 0, 55])

# Plot border lines
for line in borders:
    ax.plot(line[0::2], line[1::2], '-', lw=1, color='k',
            transform=ccrs.Geodetic())

# ax.add_feature(cfeature.LAND, edgecolor='black', facecolor='grey', alpha=0.5, zorder=1)
ax.add_feature(cfeature.COASTLINE, edgecolor='black')

Z = COCL

cntr = ax.contourf(X, Y, Z, levels=40, cmap=cm.viridis, transform=ccrs.PlateCarree())

# Draw gridlines
gl = ax.gridlines(crs=ccrs.PlateCarree(), linewidth=1, color='black', alpha=0.8, draw_labels=True, linestyle='--')

# Manipulate latitude and longitude gridline numbers and spacing
gl.ylocator = mticker.FixedLocator(np.arange(-90, 90, 30))
gl.xlocator = mticker.FixedLocator(np.arange(-180, 180, 30))
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER

gl.xlabel_style = {'size': 12, 'color': 'gray'}
gl.xlabel_style = {'color': 'gray', 'weight': 'bold'}

gl.ylabel_style = {'size': 12, 'color': 'gray'}
gl.ylabel_style = {'color': 'gray', 'weight': 'bold'}

ax.set_title('China CO Column Burden in %s %s' % (date, ttime))

plt.colorbar(cntr, label='COCL', orientation='vertical', fraction=0.01)

plt.show()
