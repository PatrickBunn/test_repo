# Week 8: Working with Gridded and Hierarchical data – Raster, NetCDF, xarray
Forecasting the timing and severity of a flood event is near impossible by just looking at historical streamflow or rain gauge observations. We must use precipitation forecast data from atmospheric models. This week we will enhance our streamflow forecast methodology by using gridded precipitation forecast data.
____

## Table of Contents:
1. [Instructions](#instructions)
    - [Set environment and get packages](#conda)
    - [Download Verde Basin shapefile](#raster)
    - [Download precipitation forecast data](#netcdf)
    - [Make forecast maps and basin averages](#maps)
2. [Assignment Questions](#assignment)
___
<a name="instructions"></a>
## Instructions

<a name="conda"></a>
#### 1. Set envrionment and get packages
- clone 'hastools' but use python 3.6 this time
- download the following packages to this new environment:
```
maplotlib=3.1.1
basemap=1.2.0
basemap-high-res=1.2.0
netcdf
```

<a name="raster"></a>
#### 2. Download Verde Basin shapefile
- Get shapefile for the Verde Basin (HUC-15060202) from the [USGS Watershed Boundary Dataset](https://viewer.nationalmap.gov/basic/?basemap=b1&category=nhd&title=NHD%20Viewextract). Extract the .zip in the same directory as the script you are working on this week. 

<a name="netcdf"></a>
#### 3. Download precipitation forecast data
- Create an account and/or sign in to the [Research Data Archive](https://rda.ucar.edu/). Search for NCEP GFS 0.25 Degree Global Forecast Grids Historical Archive. 

- On the Data Access tab, use the "Get a subset" tool. Use the following options to request a custom subset:
  - Initialization time: yesterday @ 0000 to yesterday +14 days @ 0000
  - Parameter: Total Precipitation ()
  - Output Format: Convert to netCDF 
  - For Gridded Product: select all variables
  - Spatial selection: use a bounding box 
  - Use the .gzip data compression and web download option. 

  Now you can **submit** your request.

- Receive the email from RDA with your subset of precipitation forecast data. 
- Download it using the python pre-populated script. Run that python script (enter RDA account password) and then use the following set of commands to decompress and unzip the files:
  ```
  tar -xvf filename.gz.tar
  gunzip filename.gz
  ```
  This should give you the netcdf file with the .nc extension: **filename.nc**

<a name="netcdf"></a>
#### 4. Make forecast maps and basin averages
- Set your envrionment, open a new python script, and read in the packages you installed before at [ Step #1](#conda). 
- Set path names to .shp file and .nc file. 
- Use netCDF4.Dataset() to read in the data file and find the dimensions of variables. Use ```print(netCDF4.Dataset().variables)```

- Create a matplotlib figure:
  - plot a basemap
  ```
  m = Basemap(llcrnrlon= llcrnrlat=, urcrnrlon=,      urcrnrlat=, resolution=, projection=,ax=)
  ``` 
  - then the add the shapefile 
  ```
   m.readshapefile(shapefile, name)
  ```
  - finally add the forecast precip data. 
  ```
  m.pcolormesh(x,y,data)
  ```
- Plot map for +7days accumulated precipiation, and for +14 days. 
- Calculate a basin-wide mean precipitation accumulation for both forecast hours by a slicing the data to lat/lon box around the basin. 

<a name="assignment"></a>
#### Assignment questions

1. Is there a precipitation event forecast in the next 14 days and what does this mean for forecasting streamflow at Camp Verde for the next two weeks? 

2. How much confidence do you have that the forecast precipitation (or lack of) will actually occur? (We are plotting accumulated precpitation over 7-14 days, so timing and location in the basin aren't that important)

3. How will you incorporate this estimate of precipitation input to the Verde Basin into your streamflow forecast for this week?
