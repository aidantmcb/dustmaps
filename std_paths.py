#!/usr/bin/env python
#
# std_paths.py
# Defines a set of paths used by scripts in the dustmaps module.
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

import os

script_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.abspath(os.path.join(script_dir, 'data'))
test_dir = os.path.abspath(os.path.join(script_dir, 'test'))
output_dir = os.path.abspath(os.path.join(script_dir, 'output'))