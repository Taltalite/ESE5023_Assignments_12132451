import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

TOA = xr.open_dataset("CERES_EBAF-TOA_200003-201701.nc", engine="netcdf4")

plot_datas = [TOA.toa_sw_all_mon.mean(dim='time'), TOA.toa_lw_all_mon.mean(dim='time'), TOA.solar_mon.mean(dim='time'),
              TOA.toa_net_all_mon.mean(dim='time')]
plot_titles = ['TOA shortwave radiation', 'TOA longwave radiation', 'TOA solar radiation', 'TOA net radiation flux']

x = TOA.toa_sw_all_mon.lon
y = TOA.toa_sw_all_mon.lat

fig, axs = plt.subplots(2, 2)
axs=axs.flatten()

for i in range(len(axs)):
    z = plot_datas[i]
    axs[i].set_xlabel('Longitude')
    axs[i].set_ylabel('Latitude')
    axs[i].set_title(plot_titles[i])
    if i == len(axs)-1:
        cntr = axs[i].contourf(x, y, z, levels=30, cmap=cm.coolwarm)
    else:
        cntr = axs[i].contourf(x, y, z, levels=30, cmap=cm.viridis)
    fig.colorbar(cntr, ax=axs[i])


fig, ax = plt.subplots(1,1)
x = TOA.toa_sw_all_mon.lon
y = TOA.toa_sw_all_mon.lat
z = TOA.solar_mon.mean(dim='time') - (TOA.toa_lw_all_mon.mean(dim='time') + TOA.toa_sw_all_mon.mean(dim='time'))
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('TOA solar - (lw + sw)')
cntr = ax.contourf(x, y, z, levels=30, cmap=cm.coolwarm)
fig.colorbar(cntr, ax=ax)
plt.show()
