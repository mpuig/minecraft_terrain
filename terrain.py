import os, sys, time, gdal, numpy
from gdalconst import *

import mcpi.minecraft as minecraft
import mcpi.block as block
import server

mc = minecraft.Minecraft.create(server.address)

# register all of the drivers
gdal.AllRegister()

# open VRT created from the *.txt datasets
# http://www.gdal.org/gdalbuildvrt.html
ds = gdal.Open('montserrat.vrt', GA_ReadOnly)

if ds is None:
  print 'Could not open image'
  sys.exit(1)

# get georeference info
transform = ds.GetGeoTransform()
xOrigin = transform[0]
zOrigin = transform[3]
pixelWidth = transform[1]
pixelHeight = transform[5]
/
# 1-based index
band = ds.GetRasterBand(1)

# http://www.gdal.org/classGDALRasterBand.html#a6aa58b6f0a0c17722b9bf763a96ff069
minimum,maximum,mean,stddev = band.GetStatistics(True, True)

print 'minimum', minimum
print 'maximum', maximum
print 'XSize', band.XSize
print 'ZSize', band.YSize

# reset the space
#mc.setBlocks(0, 0, 0, band.XSize, int(maximum), band.YSize, block.AIR.id)

# read all band values and
data = band.ReadAsArray(0, 0, band.XSize, band.YSize)
counter = 0
for (x,z), value in numpy.ndenumerate(data):
  y = int((value-minimum) / 5)
  mc.setBlocks(x, 0, z, x, y, z, block.SANDSTONE)
  counter+=1
  if counter%20000 == 0:
    print counter
print 'done'