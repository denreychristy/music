# Music - Main

# ================================================================================================ #
# Imports

from modules.chord	import Chord
from modules.note	import Note
from modules.scale	import Scale

# ================================================================================================ #

note = Note(60)
scale = Scale(note, 'major')
chord = Chord.from_scale(note, scale)