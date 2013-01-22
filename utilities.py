# -*- coding: UTF-8 -*-


# Copyright Ernesto Illescas-Peláez 2006 and 2009-2013, Ernesto Illescas-Peláez
# and Edgar Becerra-Santillan 2013 

# This file is part of moebiusLib.

# moebiusLib is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# moebiusLib is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
#along with moebiusLib.  If not, see <http://www.gnu.org/licenses/>.

## Contains classes that collect numeric utilities.

#	Classes that generate "Moebius Progressions" and transposition
# matrixes as conceived by composer Ernesto Illescas-Peláez in his
# Master's thesis "An Organizing Tide of Chaos - Resonances of Chaos
# Theory in a Composer's Craftsmanship".
#


# Import Python native modules.
class Identitis(object):
	""" Contains methods to generate and work with tone-row identites:
	retrograde, inverse and inverse-retrograde.
	"""
	def __init__(self):
		""" Initialization of the class.Does nothing.
		"""
		pass
	
	
	def seriesToIntervals(self, points):
		""" Converts a list of points into a list of intervals.
		points	---> a list of points.
		return	-->> a list of intervals.
		"""
		intrvals	= []
		a			= points[0]
		for x in points:
			newIntrval = x - a
			intrvals.append(newIntrval)
			a = x
		intrvals.pop(0)
		return intrvals
	
	
	def intervalsToSeries(self, intervals, start, modulo=None):
		""" Constructs a list of values from a list of intervals.
		intervals	---> a list of intervals.
		start		---> the starting ponit of the returned series.
		return		-->> a list
		"""
		series	= [start]
		for x in intervals:
			element = x + series[-1]
			if modulo:
				element = element % 12
			series.append(element)
		return series
