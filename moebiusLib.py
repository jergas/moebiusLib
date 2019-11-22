# -*- coding: UTF-8 -*-


# Copyright Ernesto Illescas-Peláez 2006, Ernesto Illescas-Peláez and Edgar
# Becerra-Santillan 2013 

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

"""
Classes that generate \"Moebius Progressions\" and transposition
matrixes as conceived by composer Ernesto Illescas-Peláez in his
Master's thesis \"An Organizing Tide of Chaos - Resonances of Chaos
Theory in a Composer's Craftsmanship\".
"""
__author__	=  'Ernesto Illescas-Pelaez and Edgar Becerra-Santillan'
__date__	= '20 February 2013'
__version__=  'Dev'


# Import Python native modules.
import collections
import numpy
import sys
# Import user modules
import utilities

Identities = utilities.Identities

class Progression(Identities):
	""" Generates a Moebius progression and related attributes.
	__init__() Takes 2 integer arguments, which are converted to 
	their remainder modulo 12: startPitch and missingPitch. Contains
	attributes and methods useful for working with the progression.
	
	Available attributes are:
	chromaticSet    --- (0, 1, 2, ... 11)
	pitches         --- deque object containing the chromatic set minus
                       missingPitch
	complete        --- one loop of the progression (without repeating
                       startPitch)
	nonLooping      --- the non-looping part of the progression. If the
                       progression lacks it, None
	loopingStart    --- the looping section of the progression
	
	Useful inherited methods are:
	original()          --- returns complete
	retrograde()        --- returns the retrograde of complete
	inverse()           --- returns the inverse of complete
	retrogradeInverse() --- returns the retrograde-inverse of complete
	transposition()     --- needs startPitch argument, and optionally
                           identitiy=\'original\'. Transposes to
                           startPitch.
	"""
	
	def __init__(self, startPitch, missingPitch):
		""" Set the initial conditions for generating a Moebius pitch
		progression, and generate the tone-row. Pitches are represented
		by integers: C = 0, C# = 1, D = 2, etc. Uses the Identities()
		super-class to make available the following methods for the
		whole progression: original(), retrograde(), inverse() and
		retrogradeInverse().
		startPitch      ---> The first note of the progression
		missingPitch    ---> A missing pitch in the chromatic set
		"""
		# Test whether initialization data is valid. If not raise an error.
		if isinstance(startPitch, int) and isinstance(missingPitch, int):
			self.startPitch		= startPitch   % 12
			self.missingPitch	= missingPitch % 12
			if self.startPitch == self.missingPitch:
				raise RuntimeError('startPitch and missingPitch can not be equivalent modulo 12')
		else:
			raise RuntimeError('startPitch and missingPitch must be integers!')

		# Tuple representing the chromatic scale (C= 0).
		self.chromaticSet	= (0, 1, 2, 3, 4 , 5, 6 , 7, 8, 9, 10 , 11)
		# Generate the Classes attributes.
		self.processInitialConditions() # defines self.pitches
		self.makeProgression() # defines self.complete
		self.determineNonLoopingNLoopingSections()	# defines
													# self.nonLooping
													# and self.looping
		# Initialize the Identites() superclass that makes the
		# original(), retrograde(), inverse(), retrogradeInverse() and
		# transposition() methods available (for self.complete).
		Identities.__init__(self, self.complete)
	
	
	def processInitialConditions(self):
		""" Rotates the chromatic set until self.startingPitch is the
			first element of the list, removes missingPitch from the
			list, and records the list as the self.pitches attribute.
		"""
		pitches	= collections.deque(self.chromaticSet)
		pitches.remove(self.missingPitch)
		while pitches[0] != self.startPitch:
			lastPitch = pitches.popleft()
			pitches.append(lastPitch)
		self.pitches = pitches
		print """
Applied initial conditions:
	startPitch        = {0}
	missingPitch      = {1}
self.pitches set to:
	{2}
			""".format(self.startPitch, self.missingPitch, self.pitches)
	
	
	def makeProgression(self):
		""" Constructs a Moebius tone-row by iterating the function
		2x = y inside a mod11 system until it starts repeating itself.
		x is self.startPitch, and y the new x for the following
		iteration. Records the list as the self.complete attribute.
		"""
		newIndex	= 0
		newPitch	= self.startPitch
		toneRow		= []
		while True:
			newPitch = self.pitches[newIndex]
			if toneRow.count(newPitch):
				# When tone-row starts repeating, record where for
				# future reference.
				self.loopingStart	= newPitch
				break
			toneRow.append(newPitch)
			# Next line equal to 2x = mod11(y)
			newIndex	= (newPitch + newIndex) % 11
		self.complete = toneRow
		print """
Constructed the following tone-row:
	{0}
			""".format(self.complete)
		
		
	def determineNonLoopingNLoopingSections(self):
		""" Determine whether self.complete has a non-looping section.
		If so, make it available to the class through
		self.nonLoopingSection attribute; else attribute will be None.
		Also determine the tone-row's looping section, and make it
		available through self.loopingSection.
		"""
		toggle		= 0
		self.nonLooping	= []
		self.looping		= []
		for pitch in self.complete:
			if pitch == self.loopingStart:
				toggle = 1
			if not toggle:
				self.nonLooping.append(pitch)
			else:
				self.looping.append(pitch)
		if not len(self.nonLooping):
			self.nonLooping = None
		if self.nonLooping:
			print """
The progression's nonLooping section is:
	{0}
The progression's looping section is:
	{1}
				""".format(self.nonLooping, self.looping)
		else:
			print """
The progression lacks a non-looping section.
The progression's looping section is:
	{0}
			""".format(self.looping)



class Matrix(Progression):
	""" Constructs a transposition matrix with the original tone-row (or
	an identity) as the first row of the matrix, and its inverse as
	first note for the subsequent transpositions. __init__() takes 2
	mandatory integer arguments, which are converted to  their remainder
	modulo 12: startPitch and missingPitch; and to optional ones
	identity ('original', 'retrograde', 'inverse', 'retrogradeInverse')
	and transposeTo.
	
	Available attributes are:
	matrix    --- a matrix object with the 'identity' tone row as first
                 row, and its inverse as the first column. e.g.:
			[[ 1  2  4  8  5 10  9  7  3  6]
			 [ 0  1  3  7  4  9  8  6  2  5]
			 [10 11  1  5  2  7  6  4  0  3]
			 [ 6  7  9  1 10  3  2  0  8 11]
			 [ 9 10  0  4  1  6  5  3 11  2]
			 [ 4  5  7 11  8  1  0 10  6  9]
			 [ 5  6  8  0  9  2  1 11  7 10]
			 [ 7  8 10  2 11  4  3  1  9  0]
			 [11  0  2  6  3  8  7  5  1  4]
			 [ 8  9 11  3  0  5  4  2 10  1]]
	"""
	
	def __init__(self, startPitch, missingPitch, identity='original',
					transposeTo=None):
		""" Uses the Progression superclass to generate a moebius
		tone-row and the optional argument to set the origin of the
		Matrix. Constructs a transposition matrix.
		startPitch      ---> The first note of the progression
		missingPitch    ---> A missing pitch in the chromatic set
		identity        ---> Optionally use 'retrograde', 'inverse', or
		                    'retrogradeInverse' to construct the
		                    matrix
		transposeTO     ---> Optionally start row1 with this value
		"""
		Progression.__init__(self, startPitch, missingPitch)
		# Test to see if the identity attribute is valid. if so, define
		# self.row1
		try:
			# Transpse the tone row if necessary.
			if transposeTo != None:
				self.row1 = self.transposition(transposeTo, identity)
				print """ The tone-row has been transposed  so that it starts with {0}.
					""".format(transposeTo)
			else:
				self.row1 = getattr(self, identity)()
		except AttributeError:
			raise AttributeError('identity must be the name of a method of Identities() in utilities.py!')
			return
		print """ The {0} tone-row will be used to generate a
transposition matrix. row 1 will be: {1}
			""".format(identity, self.row1)
		# Re-initialize the Identites() superclass that makes the
		# original(), retrograde(), inverse(), retrogradeInverse() and
		# transposition() methods available for self.row1, instead of
		# for Progresion.complete.
		Identities.__init__(self, self.row1)
		print """ Its inverse will be column 1: {0}
			""".format(self.inverse())
		self.constructMatrix() # Generates the self.matrix attribute
		print """ Generated the following transposition matrix:

{0}
			""".format(self.matrix)
	
	
	def constructMatrix(self):
		""" Constructs the transposition matrix with self.row1 as row 1,
		and its inverse identity as column 1.
		"""
		column1	= self.inverse()
		matrix	= []
		for rowStart in column1:
			row = self.transposition(rowStart)
			matrix.append(row)
		self.matrix = numpy.matrix(matrix)
