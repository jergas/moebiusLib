# -*- coding: UTF-8 -*-

#	Classes that generate "Moebius Progressions" and transposition
# matrixes as conceived by composer Ernesto Illescas-Peláez in his
# Master's thesis "An Organizing Tide of Chaos - Resonances of Chaos
# Theory in a Composer's Craftsmanship".
#
#	Coded by Edgar Becerra-Santillán and Ernesto Illescas-Peláez.

# Import Python native modules.
import sys

class Progression(object):
	""" Generates a Moebius progression, and associated methods.
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
		self.chromaticSet	= [0, 1, 2, 3, 4 , 5, 6 , 7, 8, 9, 10 , 11]
		# Generate the Classes attributes.
		self.pitches			= self.processInitialConditions()
		#self.complete			= self.makeProgression()
		#self.nonLoopingSection	= 
		#self.loopingSection	= 
	
	
	def processInitialConditions(self):
		""" Constructs a range(0, 12) list, rotates it until
			slef.startingPitch is the first element of the list, removes
			missingPitch from the list, and records the list as the
			self.pitches attribute.
		"""
		pitches	= self.chromaticSet
		pitches.remove(self.missingPitch)
		while pitches[0] != self.startPitch:
			lastPitch = pitches.pop(0)
			pitches.append(lastPitch)
		self.pitches = pitches
		print """Applied initial conditions
		startPitch        = {0}
		missingPitch      = {1}
		(rotated) pitches = {2}
				""".format(self.startPitch, self.missingPitch, self.pitches)
	
	def makeProgression(self):
		""" Constructs a Moebius tone-row.
		"""
		pass
