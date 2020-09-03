#!/usr/bin/env python
# %%
import numpy as np
import pandas as pd
#import scipy as sp
import matplotlib.pyplot as plt
from matplotlib import cm
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
#import datetime
from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
#print ("loaded packages")

# %% 

#set a counding box for the map
llon = -122.57
rlon = -119.13
llat =   38.50
ulat =   41.50

fig, ax1 = plt.subplots(1, 1, figsize=(6,6))
# create polar stereographic Basemap instance.
# add 0.5 degrees to bounding box to add geographical context
m = Basemap(llcrnrlon=llon-.5,llcrnrlat=llat-.5,urcrnrlon=rlon+.5,urcrnrlat=ulat+.5,
            resolution='i', projection='mill',ax=ax1, epsg=4269)

#server="http://server.arcgisonline.com/ArcGIS",
m.arcgisimage(service='ESRI_Imagery_World_2D', xpixels = 2000, verbose= True, ax=ax1)

# add .shp file of the catchment
#m.readshapefile(basin_file,'Feather Basin',linewidth=1.5,color='k')

# draw coastlines, state and country boundaries, edge of map.
m.drawcoastlines()
m.drawstates()
m.drawcountries()
# draw parallels.
parallels = np.arange(-120,120,1.)
m.drawparallels(parallels,labels=[1,0,0,0],fontsize=8)
# draw meridians
meridians = np.arange(0.,420.,1.)
m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=8)

# draw a polygon to highlight area of interest
x1,y1 = m(llon,llat)
x2,y2 = m(rlon,llat)
x3,y3 = m(rlon,ulat)
x4,y4 = m(llon,ulat)
poly = Polygon([(x1,y1),(x2,y2),(x3,y3),(x4,y4)],facecolor='none',edgecolor='gray',linewidth=3)
plt.gca().add_patch(poly)

# add oroville dam point
x5,y5 = m(-121.4920,39.5426)
ax1.scatter(x5,y5, marker='o', c='red',edgecolor='k')
ax1.annotate("Oroville Dam", color='red', xy=(138, 158), xycoords='figure points',
            fontsize=12,fontweight='bold')
plt.tight_layout()
#plt.show()
plotfile = 'map_of_study_area.png'
sf = fig.savefig(plotfile, dpi=300) # ,dpi=300)

# %%