# HyTools

HyTools is a python library for processing imaging spectroscopy data,
with a focus on terrestrial scenes.  At it's core it consists of a
series of functions for reading and writing ENVI-formatted images and
reading NEON AOP HDF files. Built on top of these functions are a
series of higher level processing tools for data analysis which
include spectral resampling, topographic and BRDF correction, spectral
transforms, maskings and more.

For complete documentation see: [https://hytools.readthedocs.org/](https://readthedocs.org/)


## Dependencies
- numpy
- h5py
- scipy
- gdal, optional for exporting GeoTIFFs

## Installation
To install run:

```python
python setup.py install
```

## Basic usage
```python
import hytools as ht

#Read an ENVI file
hyObj = ht.open_envi('envi_file.bin')
#Map image data to numpy memmap object
hyObj.load_data()

#Calculate NDVI, retrieves closest wavelength to input lambda in nm
ir = hy_obj.get_wave(900)
red = hy_obj.get_wave(660)
ndvi = (ir-red)/(ir+red)

#Other options for retrieving data
band = hy_obj.get_band(10)
column = hy_obj.get_column(1)
line = hy_obj.get_line(234)
chunk = hy_obj.get_chunk(x1,x2,y1,y2)

# Create a writer object to write to new file
writer = ht.io.WriteENVI('output_envi.bin',hy_obj.header_dict)

#Create an iterator object to cycle though image
iterator = hy_obj.iterate(by = 'line')

# Cycle line by line, read from original data
while not iterator.complete:  
   #Read next line
   line = iterator.read_next() 

   #Do some calculations.......
   radiance = line * gain + offset

   #Write line to file
   writer.write_line(radiance,iterator.current_line)
	
writer.close()  
```
