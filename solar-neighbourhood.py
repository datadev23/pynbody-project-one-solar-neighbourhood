import pynbody
import pynbody.plot.sph as sph
import matplotlib.pylab as plt
from os import environ
import numpy
import pylab
import pynbody.units as units

#load data file

s = pynbody.load('../data/g15784.lr.01024.gz')

# load the halos catalogue

h = s.halos()

h1 = h[1]
print h1
# center the largest halo
pynbody.analysis.angmom.faceon(h1)

# set the units
s.physical_units()

# image

pynbody.plot.image(h1.s, width=100, cmap="Blues");

plt.show()
# apply the solar neighbourhood filter
"""
function that returns a filter which selects particles
    in a disc between radii `r1` and `r2` and thickness `height`.
"""

r1 = units.Unit("7.00e+00 kpc")
r2= units.Unit("9.00e+00 kpc")
height = units.Unit("16.00e+00 kpc")
filter =  pynbody.filt.SolarNeighborhood(r1, r2,height, cen=(0, 0, 0) )
