#!/usr/bin/env python
#
# plot_bayestar.py
# An example of how to query the "Bayestar" dust map of
# Green, Schlafly, Finkbeiner et al. (2015).
#
# Copyright (C) 2016  Gregory M. Green
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

from __future__ import print_function

import numpy as np
import os.path

try:
    import PIL
except ImportError as error:
    print('This example requires Pillow or PIL.\n'
          'See <http://pillow.readthedocs.io/en/stable/installation.html>.')
    raise error

from astropy.coordinates import SkyCoord
import astropy.units as u

from ..bayestar import BayestarQuery
from .. import std_paths

def numpy2pil(a, vmin, vmax):
    a = np.clip((a - vmin) / (vmax - vmin), 0., 1.)
    a = (254.99 * a).astype('u1')
    return PIL.Image.fromarray(a)


def main():
    # Set up Bayestar query object
    bayestar = BayestarQuery(max_samples=1)

    # Create a grid of coordinates
    l = np.arange(-180., 180.1, 5.)
    b = np.arange(-90., 90.1, 5.)
    l,b = np.meshgrid(l,b)
    d = 5.    # We'll query integrated reddening to a distance of 5 kpc
    coords = SkyCoord(l*u.deg, b*u.deg, d*u.kpc, frame='galactic')

    # Get the dust median reddening at each coordinate
    ebv = bayestar.query(coords, mode='median')

    # Convert the output array to a PIL image and save
    img = numpy2pil(ebv[::-1,::-1], 0., 1.5)
    fname = os.path.join(std_paths.output_dir, 'bayestar.png')
    img.save(fname)

    return 0


if __name__ == '__main__':
    main()