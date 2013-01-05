# -*- coding: UTF-8 -*-

# Classes that generates a "Moebius Progressions" and transposition
#Matrixes as concieved by composer Ernesto Illescas-Peláez in his
#Master's thesis "An Organizing Tide of Chaos - Resonances of Chaos
#Theory in a Composer's Craftsmanship". Coded by Edgar Becerra-Santillán
#and Ernesto Illescas-Peláez

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
		# Generate the Classes attributes.
		self.complete			= self.makeProgression()
		#self.nonLooping Section	= 
		#self.loopingSection	= 
	
	
	def makeProgression(self):
		""" Constructs a Moebius town-row.
		"""
		pass