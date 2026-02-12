# Music - Chord

# ================================================================================================ #
# Imports

from typing import Optional

from .note	import Note
from .scale	import Scale

# ================================================================================================ #

class Chord:
	def __init__(self, root: Note, chord_tones: list[Note]):
		self.__root: Note = root
		self.__notes: list[Note] = chord_tones
	
	# ================================================== #
	# Class Methods

	@classmethod
	def from_intervals(cls, root: Note, intervals: list[int]) -> 'Chord':
		root_midi = root.generic_midi
		return cls(
			root = root,
			chord_tones = [Note(root_midi + x) for x in intervals]
		)
	
	@classmethod
	def from_scale(cls, root: Note, scale: Scale, degrees: list[int] = [1, 3, 5]) -> Optional['Chord']:
		if not scale.contains(root): return None
		root_scale_degree: Optional[int] = scale.get_diatonic_degree(root)
		if root_scale_degree is None: return None
		chord_degrees = [root_scale_degree + d for d in degrees]
		chord_tones = [scale.get_note_from_degree(d) for d in chord_degrees]
		chord_tones = [c for c in chord_tones if c is not None]

		return cls(
			root = root,
			chord_tones = chord_tones
		)
	
	@classmethod
	def all_chords_from_scale(cls, scale: Scale) -> list['Chord']:
		chord_types = [[1]]
		for i in range(2, 8):
			chord_types += [c + [i] for c in chord_types]
		
		result = []
		for note in scale:
			for chord in chord_types:
				result.append(cls.from_scale(root = note, scale = scale, degrees = chord))
		
		return result

	# ================================================== #
	# Dunder Methods

	def __str__(self) -> str:
		return str([note.generic_name for note in self.__notes])

	# ================================================== #
	# Property Methods

	# ================================================== #
	# Set Methods

	# ================================================== #
	# Other Methods

	def contains(self, note: Note) -> bool:
		return any(note.generic_midi == chord_note.generic_midi for chord_note in self.__notes)

# ================================================================================================ #