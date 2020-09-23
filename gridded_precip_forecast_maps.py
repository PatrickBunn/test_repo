#!/usr/bin/env python
# %%
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import BoundaryNorm
from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset

# %% 
basin_file = 'HUC_15060202_shapefile/WBDHU8'

# %%
# set filename
precip_forecast_file = 'gfs_precip_data/gfs.0p25.2020091500.f336.grib2.bunn447532.nc'
# use netCDF4.Dataset to read in .nc file 
precip_forecast_data = Dataset(precip_forecast_file)
# find varibale names and dimesions
precip_forecast_data.variables
# extract specific variables: lats, lons and precip
precip_forecast = precip_forecast_data.variables['APCP_P8_L1_GLL0_acc336h']
lat = precip_forecast_data.variables['lat_0'][:]
lon = precip_forecast_data.variables['lon_0'][:]

# %%
# calculate a mean value in a bounding box (e.g. Verde catchment)
mean_precip_verde = np.mean(precip_forecast[0,(lat>=34.5)&(lat<=35.5),(lon>=360-112.5)&(lon<=360-111.5)])

# %% 
# start a figure named fig, set axis and dimesions of fig
fig, ax1 = plt.subplots(1, 1, figsize=(6,6))
# create a Basemap to plot data onto
m = Basemap(llcrnrlon=np.min(lon)-360.,llcrnrlat=np.min(lat),urcrnrlon=np.max(lon)-360.,urcrnrlat=np.max(lat),
            resolution='i', projection='mill',ax=ax1, epsg=4269)

# add satellite image to background of map
#m.arcgisimage(service='ESRI_Imagery_World_2D', xpixels = 2000, verbose= True, ax=ax1)

# draw coastlines, state and country boundaries, edge of map.
m.drawcounties(zorder=2,linewidth=.25)

# add .shp file of the catchment
m.readshapefile(basin_file,'Verde Basin',linewidth=1.5,color='k')

# draw parallels.
parallels = np.arange(-120,120,1.)
m.drawparallels(parallels,labels=[1,0,0,0],fontsize=8)
# draw meridians
meridians = np.arange(0.,420.,1.)
m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=8)

ny = len(lat); nx = len(lon) # find lat/lon dimensions ny,nx
lons, lats = m.makegrid(nx, ny) # make evenly spaced grid on basemap m of ny by nx 
x, y = m(lons, lats) # compute map projection coordinates

# draw mesh of data (no contouring with low res data)
cmap = plt.get_cmap('Blues') # pick the desired colormap, 
levs = np.arange(0,5,0.25)   # sensible levels,
norm = BoundaryNorm(levs, ncolors=cmap.N, clip=True) #and define a normalization
cs = m.pcolormesh(x,y,precip_forecast[0,:,:],cmap=cmap,norm=norm)

# add colorbar",
cbar = m.colorbar(cs,location='bottom',pad="6%")
cbar.ax.set_xticklabels(cbar.ax.get_xticklabels(),rotation=30)
cbar.set_label('GFS forecast 14 day Accumulated Precipitation [$\\mathrm{mm}]$ \n Basin Mean = '+str(mean_precip_verde)+' [$\mathrm{mm}]$',size=10)

# add some reference locations to map
x1,y1 = m(-111.8543, 34.5636) # add Camp Verde point
x2,y2 = m(-112.4685,34.5400) # add Prescott point
x3,y3 = m(-111.6513,35.1983) # add Flagstaff point
locations = ["Camp Verde","Prescott","Flagstaff"]
coords = [[x1,y1],[x2,y2],[x3,y3]]
xy_s = [(220, 175),(130, 165),(280, 285)]
#xy_s = [(250, 125),(110, 110),(295, 245)] # for sat. map

for loc,coord,xy in zip(locations,coords,xy_s):
    ax1.scatter(coord[0],coord[1], marker='o', c='k',edgecolor='k')
    ax1.annotate(loc, color='k', xy=xy, xycoords='figure points',
                fontsize=12,fontweight='bold')

plt.tight_layout()
plotfile = 'forecast_14_days_precip_accu.png'
#plotfile = 'map_of_study_area.png'
sf = fig.savefig(plotfile, dpi=300) # ,dpi=300)
# %%
