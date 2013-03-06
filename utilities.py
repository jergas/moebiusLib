# -*- coding: UTF-8 -*-


# Copyright Ernesto Illescas-Peláez 2006 and 2013

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

"""
Utility classes for moebiusLib. Some of the code in this module was
taken from cascaBell: https://github.com/elerno/cascaBell
"""
__author__	=  'Ernesto Illescas-Pelaez'
__date__	= '20 February 2013'
__version__=  'Beta'


# Import Python native modules.
class Identities(object):
	""" Contains methods to return series identites, and to transpose
	them.
	"""
	def __init__(self, originalSeries):
		""" Set originalSeries as the self.originalSeries attribute.
		originalSeries	---> a list: the original series
		"""
		self.originalSeries	= originalSeries
		
		
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
		modulo		---> optional arg. 12 when working TET
		return		-->> a list of points
		"""
		series	= [start]
		for x in intervals:
			element = x + series[-1]
			if modulo:
				element = element % modulo
			series.append(element)
		return series
	
	
	def original(self):
		""" Returns the original series.
		return	-->> the original series
		"""
		return self.originalSeries
	
	
	def retrograde(self):
		""" Returns the retrograde series. No transposition takes place
		(i.e. retrograde[0] = original[-1]).
		return	-->> the retrograde identity of self.originalSeries
		"""
		retrograde = list(reversed(self.originalSeries))
		return retrograde
	
	
	def inverse(self):
		""" Returns the inverse series. No transposition takes place
		(i.e. inverse[0] = original[-1]).
		return	-->> the inverse identity of self.originalSeries
		"""
		origin				= self.originalSeries[0]
		intervals			= self.seriesToIntervals(self.originalSeries)
		invertedIntervals	= []
		for interval in intervals:
			interval *= -1
			invertedIntervals.append(interval)
		inverse		= self.intervalsToSeries(invertedIntervals, origin,
												modulo=12)
		return inverse
	
	
	def retrogradeInverse(self):
		""" Returns the retrograde of the inverse series. No
		transposition takes place (i.e. retrogradeInverse[0] =
		inverse[-1]).
		return	-->> the retrograde-inverse identity of
						self.originalSeries
		"""
		inverseSeries = self.inverse()
		retrogradeInverse	= list(reversed(inverseSeries))
		return retrogradeInverse
	
	
	def transposition(self, startPitch, identitiy='original'):
		""" Transposes self.original or the desired identity
		(retrograde, inverse, retrogradeInverse).
		startPitch	---> Series\'s starting pitch
		identity	---> optionally choose to return a transposed
							identity
		"""
		# Define which identity will be transposed.
		if identitiy == 'original':
			series = self.original()
		elif identitiy == 'retrograde':
			series = self.retrograde()
		elif identitiy == 'inverse':
			series = self.inverse()
		elif identitiy == 'retrogradeInverse':
			series = self.retrogradeInverse()
		# Make the transposition.
		intervals = self.seriesToIntervals(series)
		transposition = self.intervalsToSeries(intervals, startPitch, modulo=12)
		return transposition
