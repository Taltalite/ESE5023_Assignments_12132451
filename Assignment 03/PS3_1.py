import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

nino = xr.open_dataset("NOAA_NCDC_ERSST_v3b_SST.nc", engine="netcdf4")

nino_month_sst = nino.sst.groupby(nino.sst.time.dt.month).mean()

plt.figure(1)
for i in range(12):
    plt.subplot(3, 4, i + 1)
    nino_month_sst[i].plot()

nino_month_sst_anomalies = xr.DataArray(np.zeros(nino.sst.shape), coords=[nino.sst.time, nino.sst.lat, nino.sst.lon],
                                        dims=['time', 'lat', 'lon'])

for i in range(len(nino.sst)):
    nino_month_sst_anomalies[i] = nino.sst[i] - nino_month_sst.where(nino_month_sst.month == nino.sst[i].time.dt.month,
                                                                     drop=True).squeeze()

plt.figure(2)
nino_month_sst_anomalies[-1].plot()

# concat NINO 1+2, NINO 3, NINO 4
# nino_1_2 = nino_month_sst_anomalies.sel(time=slice('2000', '2016'), lat=slice(-10.0, -0.0), lon=slice(240, 250))
# nino_3 = nino_month_sst_anomalies.sel(time=slice('2000', '2016'), lat=slice(-5.0, 5.0), lon=slice(210, 250))
# nino_4 = nino_month_sst_anomalies.sel(time=slice('2000', '2016'), lat=slice(-5.0, 5.0), lon=slice(160, 210))
# nino_all = xr.concat([nino_1_2, nino_3, nino_4], dim='lon')

nino_34 = nino_month_sst_anomalies.sel(time=slice('2000', '2016'), lat=slice(-5.0, 5.0), lon=slice(190, 240))

nino_34_mean = np.mean(nino_34, axis=(1, 2))

el_nino_idx = np.zeros(len(nino_34_mean))
la_nina_idx = np.zeros(len(nino_34_mean))

i = 0
while i - 6 < len(nino_34_mean):
    if (nino_34_mean[i:i + 6] >= 0.4).all():
        el_nino_idx[i:i + 6] = nino_34_mean[i:i + 6]
    if (nino_34_mean[i:i + 6] <= -0.4).all():
        la_nina_idx[i:i + 6] = nino_34_mean[i:i + 6]
    i += 1

# plot figure

x = nino_34_mean.time.values

fig, ax=plt.subplots(1,1,figsize=(12,4))
ax.plot(x, nino_34_mean)
ax.set_ylim(-3, 3)
ax.set_title('SST Anomaly in Nino 3.4 Region')
ax.set_xlabel('Year')
ax.set_ylabel('Anomaly in Degrees C')
ax.grid()

fill_elnino = ax.fill_between(x, 0, el_nino_idx, color='r',label='El Niño Threshold')
fill_lanina = ax.fill_between(x, 0, la_nina_idx, color='b',label='La Niña Threshold')

el_nino_h = ax.axhline(y=0.5,color='r',ls='--')
la_nina_h = ax.axhline(y=-0.5,color='b',ls='--')

ax.legend([fill_elnino, fill_lanina,el_nino_h,la_nina_h], ['El Niño', 'La Niña','El Niño Threshold','La Niña Threshold'])

plt.show()
