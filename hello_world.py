#!/usr/bin/env python
# %%
import numpy as np
import pandas as pd
#import scipy as sp
import matplotlib.pyplot as plt
from matplotlib import cm
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import datetime
from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
#print ("loaded packages")

# %% 
basin_file = 'HUC_15060202_shapefile/WBDHU8'
#set a counding box for the map
llon = -113.00
rlon = -111.00
llat =   34.00
ulat =   36.00

# %% 
fig, ax1 = plt.subplots(1, 1, figsize=(6,6))
# create polar stereographic Basemap instance.
# add 0.5 degrees to bounding box to add geographical context
m = Basemap(llcrnrlon=llon-.5,llcrnrlat=llat-.5,urcrnrlon=rlon+.5,urcrnrlat=ulat+.5,
            resolution='i', projection='mill',ax=ax1, epsg=4269)

#server="http://server.arcgisonline.com/ArcGIS",
m.arcgisimage(service='ESRI_Imagery_World_2D', xpixels = 2000, verbose= True, ax=ax1)

# add .shp file of the catchment
m.readshapefile(basin_file,'Verde Basin',linewidth=1.5,color='k')

# draw coastlines, state and country boundaries, edge of map.
m.drawcoastlines()
m.drawstates()
#m.drawcounties()
m.drawcountries()
# draw parallels.
parallels = np.arange(-120,120,1.)
m.drawparallels(parallels,labels=[1,0,0,0],fontsize=8)
# draw meridians
meridians = np.arange(0.,420.,1.)
m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=8)

# add Camp Verde point
x1,y1 = m(-111.8543, 34.5636)
ax1.scatter(x1,y1, marker='o', c='w',edgecolor='k')
ax1.annotate("Camp Verde", color='w', xy=(210, 145), xycoords='figure points',
            fontsize=12,fontweight='bold')
# add Prescott point
x2,y2 = m(-112.4685,34.5400)
ax1.scatter(x2,y2, marker='o', c='w',edgecolor='k')
ax1.annotate("Prescott", color='w', xy=(107, 145), xycoords='figure points',
            fontsize=12,fontweight='bold')
# add Flagstaff point
x3,y3 = m(-111.6513,35.1983)
ax1.scatter(x3,y3, marker='o', c='w',edgecolor='k')
ax1.annotate("Flagstaff", color='w', xy=(250, 230), xycoords='figure points',
            fontsize=12,fontweight='bold')


plt.tight_layout()
#plt.show()
plotfile = 'map_of_study_area.png'
sf = fig.savefig(plotfile, dpi=300) # ,dpi=300)

# %%