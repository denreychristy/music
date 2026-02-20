# Music - Main

# ================================================================================================ #
# Imports

from modules.chord	import Chord
from modules.note	import Note
from modules.scale	import Scale

# ================================================================================================ #

class Song:
	def __init__(self):
		self.__sections: list[Section] = []

class Section:
	def __init__(self):
		self.__measures: list[Measure] = []

class Measure:
	def __init__(self):
		pass

# ================================================================================================ #

note = Note(60)
scale = Scale(note, 'major')
chord = Chord.from_scale(note, scale)