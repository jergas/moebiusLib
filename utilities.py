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
	retrograde, inverse and retrograd-inverse and transpositions.
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
	
	
	def intervalsToSeries(self, intervals, start, modulo=12):
		""" Constructs a list of values from a list of intervals.
		intervals	---> a list of intervals.
		start		---> the starting ponit of the returned series.
		modulo		---> optional arg. Don't use when working with PCS
		return		-->> a list
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
		(i.e. inverse[0] = original[0]).
		return	-->> the inverse identity of self.originalSeries
		"""
		origin				= self.originalSeries[0]
		intervals			= self.seriesToIntervals(self.originalSeries)
		invertedIntervals	= []
		for interval in intervals:
			interval *= -1
			invertedIntervals.append(interval)
		inverse		= self.intervalsToSeries(invertedIntervals, origin)
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
	 	pass
