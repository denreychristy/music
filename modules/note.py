# Music - Main

# ================================================================================================ #
# Imports

from typing import Optional, Union

# ================================================================================================ #

class Note:
	def __init__(self, note: Union[int, str]) -> None:
		if isinstance(note, int):
			self.__midi: int = note
			self.__generic_name: str = self.generic_name_from_midi(self.__midi)
			self.__octave: int = self.octave_from_midi(self.__midi)
			self.__name: str = self.name_from_midi(self.__midi, self.__generic_name, self.__octave)
		
		else:
			midi = self.midi_from_name(note)
			if midi is None: raise Exception('Note creation failed.')
			self.__midi = midi
			self.__generic_name: str = self.generic_name_from_midi(self.__midi)
			self.__octave: int = self.octave_from_midi(self.__midi)
			self.__name: str = note
	
	# ================================================== #
	# Class Methods

	@classmethod
	def enharmonic_equivalents(cls, note: str) -> Optional[list[str]]:
		equivalent_groups = [
			['A', 'G##', 'Bbb'],
			['A#', 'Bb', 'Cbb'],
			['B', 'A##', 'Cb'],
			['C', 'B#', 'Dbb'],
			['C#', 'B##', 'Db'],
			['D', 'C##', 'Ebb'],
			['D#', 'Eb', 'Fbb'],
			['E', 'D##', 'Fb'],
			['F', 'E#', 'Gbb'],
			['F#', 'E##', 'Gb'],
			['G', 'F##', 'Abb'],
			['G#', 'Ab']
		]
		for group in equivalent_groups:
			if note in group:
				return group
		return None

	@classmethod
	def generic_name_from_midi(cls, midi: int) -> str:
		notes: list[str] = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
		generic_name: str = notes[midi % 12]
		return generic_name
	
	@classmethod
	def midi_from_name(cls, name: str) -> Optional[int]:
		"""
		Expecting something of the form 'C' or 'C#4' or 'Cbb-1'.
		"""
		for midi in range(0, 128):
			octave = cls.octave_from_midi(midi)
			generic_name = cls.generic_name_from_midi(midi)
			enharmonic_equivalents = cls.enharmonic_equivalents(generic_name)
			if enharmonic_equivalents is None: return None
			for note_name in enharmonic_equivalents:
				if name == note_name + str(octave):
					return midi
	
	@classmethod
	def midi_to_frequency(cls, midi: int) -> float:
		return 440.0 * (2.0 ** ((midi - 69) / 12.0))

	@classmethod
	def name_from_midi(cls, midi: int, generic_name: Optional[str] = None,
		octave: Optional[int] = None) -> str:

		if generic_name is None:
			generic_name = cls.generic_name_from_midi(midi)
		if octave is None:
			octave = cls.octave_from_midi(midi)
		
		return generic_name + str(octave)
	
	@classmethod
	def octave_from_midi(cls, midi: int) -> int:
		return (midi // 12) - 1

	# ================================================== #
	# Dunder Methods

	def __add__(self, half_steps: int) -> 'Note':
		return Note(self.midi + half_steps)
	
	def __sub__(self, other: Union['Note', int]) -> Union['Note', int]:
		if isinstance(other, int):
			return Note(self.midi - other)
		else:
			return self.midi - other.midi

	def __eq__(self, value: object) -> bool:
		if not isinstance(value, 'Note'):
			return False
		
		return value.midi == self.midi

	def __repr__(self) -> str:
		return f'Note({self.__name}, {self.midi})'

	def __str__(self) -> str:
		return self.name

	# ================================================== #
	# Property Methods

	@property
	def generic_name(self) -> str:
		return self.__generic_name

	@property
	def midi(self) -> int:
		return self.__midi
	
	@property
	def name(self) -> str:
		return self.__name

	# ================================================== #
	# Set Methods

	# ================================================== #
	# Other Methods

# ================================================================================================ #