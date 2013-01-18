# -*- coding: UTF-8 -*-

#	Classes that generate "Moebius Progressions" and transposition
# matrixes as conceived by composer Ernesto Illescas-Peláez in his
# Master's thesis "An Organizing Tide of Chaos - Resonances of Chaos
# Theory in a Composer's Craftsmanship".
#
#	Coded by Edgar Becerra-Santillán and Ernesto Illescas-Peláez.

# Import Python native modules.
import collections
import sys

class Progression(object):
	""" Generates a Moebius progression and related attributes. Contains
	methods useful for working with the progression.
	"""
	
	def __init__(self, startPitch, missingPitch):
		""" Set the initial conditions for generating a Moebius pitch
		progression, and generate the tone-row. Pitches are represented
		by integers: C = 0, C# = 1, D = 2, etc.
		startPitch		---> The first note of the progression
		missingPitch	---> A missing pitch in the chromatic set
		"""
		# Test whether initialization data is valid. If not raise error.
		if isinstance(startPitch, int) and isinstance(missingPitch, int):
			if startPitch >=0 and startPitch <=11:
				if missingPitch >=0 and missingPitch <=11:
					if startPitch != missingPitch:
						self.startPitch		= startPitch
						self.missingPitch	= missingPitch
					else:
						raise RuntimeError('startPitch and missingPitch can not be equal')
				else:
					raise RuntimeError('missingPitch must be >= 0 and <=11!')
			else:
				raise RuntimeError('startPitch must be >= 0 and <=11!')
		else:
			raise RuntimeError('startPitch AND missingPitch must be integers!')
		# List representing the chromatic scale (C= 0).
		self.chromaticSet	= (0, 1, 2, 3, 4 , 5, 6 , 7, 8, 9, 10 , 11)
		# Generate the Classes attributes.
		self.processInitialConditions() # defines self.pitches
		self.makeProgression() # defines self.complete
		self.determineNonLoopingNLoopingSections()	# defines
													# self.nonLooping
													# and self.looping
	
	
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
