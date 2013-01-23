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
class Identities(object):
	""" Contains methods to generate and work with series identites:
	retrograde, inverse and inverse-retrograde.
	"""
	def __init__(self, original):
		""" Set the original series as the self.original attribute.
		original	---> a list: the original series
		"""
		self.original	= original
		
		
	def seriesToIntervals(self, points):
		""" Converts a list of points into a list of intervals.
		points	---> a list of points.
		return	-->> a list of intervals.
		"""
		intervals	= []
		a			= points[0]
		for x in points:
			newInterval = x - a
			intervals.append(newInterval)
			a = x
		intervals.pop(0)
		return intervals
	
	
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
	
	
	def retrograde(self):
		""" Returns the reversed original without affecting
		self.original.
		return	-->> the retrograde identity of self.original
		"""
		retrograde = list(reversed(self.original))
		return retrograde
