import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import math
from scipy import integrate

TOA = xr.open_dataset("CERES_EBAF-TOA_200003-201701.nc", engine="netcdf4")

"""
problem 2-1
"""

plot_datas = [TOA.toa_sw_all_mon.mean(dim='time'), TOA.toa_lw_all_mon.mean(dim='time'), TOA.solar_mon.mean(dim='time'),
              TOA.toa_net_all_mon.mean(dim='time')]
plot_titles = ['TOA shortwave radiation', 'TOA longwave radiation', 'TOA solar radiation', 'TOA net radiation flux']

x = TOA.toa_sw_all_mon.lon
y = TOA.toa_sw_all_mon.lat

fig, axs = plt.subplots(2, 2)
axs = axs.flatten()

for i in range(len(axs)):
    z = plot_datas[i]
    axs[i].set_xlabel('Longitude')
    axs[i].set_ylabel('Latitude')
    axs[i].set_title(plot_titles[i])
    if i == len(axs) - 1:
        cntr = axs[i].contourf(x, y, z, levels=30, cmap=cm.coolwarm)
    else:
        cntr = axs[i].contourf(x, y, z, levels=30, cmap=cm.viridis)
    fig.colorbar(cntr, ax=axs[i])

fig, ax = plt.subplots(1, 1)
x = TOA.toa_sw_all_mon.lon
y = TOA.toa_sw_all_mon.lat
z = TOA.solar_mon.mean(dim='time') - (TOA.toa_lw_all_mon.mean(dim='time') + TOA.toa_sw_all_mon.mean(dim='time'))
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('TOA solar - (lw + sw)')
cntr = ax.contourf(x, y, z, levels=30, cmap=cm.coolwarm)
fig.colorbar(cntr, ax=ax)

"""
problem 2-2
"""

print('computing incoming solar, outgoing longwave and outgoing shortwave...')


def lon_func(x):
    return 2 * np.pi * 6371 * math.sin(np.pi / 2 - x / 180 * np.pi) / 360


m_solar = TOA.solar_mon.mean(dim='time')
m_lw = TOA.toa_lw_all_mon.mean(dim='time')
m_sw = TOA.toa_sw_all_mon.mean(dim='time')
cnt = (len(m_solar.lat) - 1) * (len(m_solar.lon) - 1)
sum_solar = np.array(np.zeros(cnt))
sum_lw = np.array(np.zeros(cnt))
sum_sw = np.array(np.zeros(cnt))
sum_area = np.array(np.zeros(cnt))
k = 0
for i in range(len(m_solar.lat) - 1):
    area, err = integrate.quad(lon_func, float(m_solar[i].lat.values), float(m_solar[i + 1].lat.values))
    if i % 30 == 0:
        print('completed %.2f %%' % ((k / cnt) * 100))
    if i == len(m_solar.lat) - 2:
        print('completed 100.00 %')
    for j in range(len(m_solar.lon) - 1):
        avg_solar = (float(m_solar[i][j].values) + float(m_solar[i + 1][j].values) + float(
            m_solar[i][j + 1].values) + float(
            m_solar[i + 1][j + 1].values)) / 4
        avg_lw = (float(m_lw[i][j].values) + float(m_lw[i + 1][j].values) + float(m_lw[i][j + 1].values) + float(
            m_lw[i + 1][j + 1].values)) / 4
        avg_sw = (float(m_sw[i][j].values) + float(m_sw[i + 1][j].values) + float(m_sw[i][j + 1].values) + float(
            m_sw[i + 1][j + 1].values)) / 4
        sum_solar[k] = avg_solar
        sum_sw[k] = avg_sw
        sum_lw[k] = avg_lw
        sum_area[k] = area
        k += 1

incoming_solar = np.average(sum_solar, weights=sum_area)
outgoing_lw = np.average(sum_lw, weights=sum_area)
outgoing_sw = np.average(sum_sw, weights=sum_area)
print('incoming_solar: ', incoming_solar)
print('outgoing_longwave: ', outgoing_lw)
print('outgoing_shortwave: ', outgoing_sw)

"""
problem 2-3
"""

plt.figure(3)
ax = plt.axes()

ax.plot(TOA.lat, TOA.toa_net_all_mon.mean(dim=['time', 'lon']), label='total net radiation')
ax.set_ylabel('Net radiation $W m^{-2}$')
ax.set_xlabel('Latitude')
plt.grid()
plt.legend()

"""
problem 2-4
"""

low_cld_sw_mean = TOA.where(TOA.cldarea_total_daynight_mon <= 25).toa_sw_all_mon.mean(dim="time")
low_cld_lw_mean = TOA.where(TOA.cldarea_total_daynight_mon <= 25).toa_lw_all_mon.mean(dim="time")
low_cld_comps_mean = low_cld_sw_mean + low_cld_lw_mean

high_cld_sw_mean = TOA.where(TOA.cldarea_total_daynight_mon >= 75).toa_sw_all_mon.mean(dim="time")
high_cld_lw_mean = TOA.where(TOA.cldarea_total_daynight_mon >= 75).toa_lw_all_mon.mean(dim="time")
high_cld_comps_mean = high_cld_sw_mean + high_cld_lw_mean

fig, (ax1, ax2) = plt.subplots(1, 2)
x = TOA.toa_sw_all_mon.lon
y = TOA.toa_sw_all_mon.lat
z1 = low_cld_comps_mean
z2 = high_cld_comps_mean

ax1.set_xlabel('Longitude')
ax1.set_ylabel('Latitude')
ax1.set_title('Low Cloud Area lw + sw radiation')
cntr1 = ax1.contourf(x, y, z1, levels=100, cmap=cm.viridis)
fig.colorbar(cntr1, ax=ax1)

ax2.set_xlabel('Longitude')
ax2.set_ylabel('Latitude')
ax2.set_title('High Cloud Area lw + sw radiation')
cntr2 = ax2.contourf(x, y, z2, levels=100, cmap=cm.viridis)
fig.colorbar(cntr2, ax=ax2)

"""
problem 2-5
"""

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
x = TOA.toa_sw_all_mon.lon
y = TOA.toa_sw_all_mon.lat
z1 = low_cld_lw_mean
z2 = low_cld_sw_mean
z3 = high_cld_lw_mean
z4 = high_cld_sw_mean

ax1.set_xlabel('Longitude')
ax1.set_ylabel('Latitude')
ax1.set_title('Low Cloud Area LW radiation')
cntr1 = ax1.contourf(x, y, z1, levels=50, cmap=cm.viridis)
fig.colorbar(cntr1, ax=ax1)

ax2.set_xlabel('Longitude')
ax2.set_ylabel('Latitude')
ax2.set_title('Low Cloud Area SW radiation')
cntr2 = ax2.contourf(x, y, z2, levels=50, cmap=cm.viridis)
fig.colorbar(cntr2, ax=ax2)

ax3.set_xlabel('Longitude')
ax3.set_ylabel('Latitude')
ax3.set_title('High Cloud Area LW radiation')
cntr3 = ax3.contourf(x, y, z3, levels=50, cmap=cm.viridis)
fig.colorbar(cntr3, ax=ax3)

ax4.set_xlabel('Longitude')
ax4.set_ylabel('Latitude')
ax4.set_title('High Cloud Area SW radiation')
cntr4 = ax4.contourf(x, y, z4, levels=50, cmap=cm.viridis)
fig.colorbar(cntr4, ax=ax4)

plt.show()
