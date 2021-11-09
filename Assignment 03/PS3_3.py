import xarray as xr
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.animation as animation
from celluloid import Camera

MERRA2 = xr.open_dataset("./MERRA2_400.tavg1_2d_chm_Nx.20210901.nc4", engine="netcdf4")

"""
problem 3-1
"""

fig, ax = plt.subplots(1, 1)
x = MERRA2.mean(dim=['lon']).sel(lat=['-0.5', '0.5']).mean(dim=['lat']).COEM.time
y = MERRA2.mean(dim=['lon']).sel(lat=['-0.5', '0.5']).mean(dim=['lat']).COEM
ax.set_xlabel('Time')
ax.set_ylabel('CO Emission $kg m^{-2} s^{-1}$')
ax.set_title('2021-09-01 CO Emission Time Series')
ax.plot(x, y)

"""
problem 3-2
"""
fig, ax = plt.subplots()
X = MERRA2.lon.values
Y = MERRA2.lat.values
camera = Camera(fig)

for time in MERRA2.time.values:
    Z = MERRA2.sel(time=time).COCL
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title('2021-09-01 CO Column Burden Time Series')
    cntr = ax.contourf(X, Y, Z, levels=40, cmap=cm.viridis)
    plt.text(-175, 80, '%s' % time, fontdict={'size': 8})
    camera.snap()
anim = camera.animate()
writergif = animation.PillowWriter(fps=2)
anim.save('2021-09-01 CO Column Burden Time Series.gif', writer=writergif)

plt.show()
