# Music - Scale

# ================================================================================================ #
# Imports

from typing	import Optional, Union

from .note	import Note

# ================================================================================================ #
# Constants

DEGREE_NAMES: list[str] = ['1', 'b2', '2', 'b3', '3', '4', 'b5', '5', 'b6', '6', 'b7', '7']

# ================================================================================================ #

class Scale:
	def __init__(self, root: Note, name: str):
		self.__root: Note = root
		self.__half_steps: Optional[list[int]] = self.get_half_steps(name)

		self.__notes: Optional[list[Note]] = None
		if self.__half_steps is not None:
			root_midi = self.__root.generic_midi
			self.__notes: Optional[list[Note]] = [Note(root_midi + x) for x in self.__half_steps]
	
	# ================================================== #
	# Class Methods

	"""
	Returns the list of integer half step pattern values that make up the given Scale, i.e. [0, 2,
	4, 5, 7, 9, 11] for a Major Scale.
	"""
	@classmethod
	def get_half_steps(cls, name: str) -> Optional[list[int]]:
		if name.lower() == 'major':
			return [0, 2, 4, 5, 7, 9, 11]
	
	# ================================================== #
	# Dunder Methods

	"""
	Allows the iteration over the Scale.__notes list.
	"""
	def __iter__(self):
		if self.__notes is None: return None
		for note in self.__notes:
			yield note

	"""
	Returns a string list of all the Note.generic_names in the Scale.__notes list.
	"""
	def __str__(self) -> str:
		if self.__notes is None: return ""

		return str([note.generic_name for note in self.__notes])

	# ================================================== #
	# Property Methods

	"""
	Returns the list of integer half step pattern values that make up the Scale, i.e. [0, 2, 4, 5,
	7, 9, 11] for a Major Scale.
	"""
	@property
	def half_steps(self) -> Optional[list[int]]:
		return self.__half_steps

	# ================================================== #
	# Set Methods

	# ================================================== #
	# Other Methods

	"""
	Returns True if a given note is in the Scale.__notes list, else False.
	"""
	def contains(self, note: Note) -> bool:
		if self.__notes is None: return False
		return any(note.generic_midi == scale_note.generic_midi for scale_note in self.__notes)

	"""
	Return the string 'name' from DEGREE_NAMES of a given note relative to the Scale.
	"""
	def get_degree_name(self, note: Note) -> str:
		half_steps_from_root: int = (note.generic_midi - self.__root.generic_midi) % 12
		return DEGREE_NAMES[half_steps_from_root]
	
	"""
	Returns the integer scale degree of the given Note if it is in the Scale, else None.
	"""
	def get_diatonic_degree(self, note: Note) -> Optional[int]:
		if self.__notes is None: return None
		if not self.contains(note): return None
		generic_midi_list: list[int] = [scale_note.generic_midi for scale_note in self.__notes]
		return generic_midi_list.index(note.generic_midi)
	
	"""
	Returns the Note implied by the given integer degree, or the string degree name as found in
	DEGREE_NAMES.
	"""
	def get_note_from_degree(self, degree: Union[int, str]) -> Optional[Note]:
		if self.__notes is None: return None
		if isinstance(degree, int): return self.__notes[(degree - 1) % len(self.__notes)]
		if degree not in DEGREE_NAMES: return None
		half_steps_from_root: int = DEGREE_NAMES.index(degree)
		root_midi: int = self.__root.generic_midi
		return Note(root_midi + half_steps_from_root)

# ================================================================================================ #