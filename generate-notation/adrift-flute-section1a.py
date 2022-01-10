import itertools
import math
from pyalex.chord import Chord
from pyalex.pitch import Pitch
from pyalex.polyphony import QueuedVoiceManager, VoiceId
from pyalex.rand import RandomizerGroup
from pyalex.utilities import Utilities, LengthMultiplier, LengthMultiplierManager
import random
import scamp
import statistics
import sys	

# -------------------------------------------------------------------------------------------------------------------------------------------

s = scamp.Session(tempo = 40)

s.fast_forward_to_beat(600)

# build instruments
flute = s.new_part("Flute")

flute_midi = [60, 67,
			  60, 67,
			  65, 65,
			  65, 64,
			  67, 61,
			  67, 61,
			  68, 68,
			  67, 70,
			  67, 68,
			  65, 68,
			  65, 62]

s.start_transcribing()

s.wait(2)

for midi in flute_midi:
	flute.play_note(midi - 12, volume = 0.1, length = 2.5)
	s.wait(1.75)

performance = s.stop_transcribing()
score = performance.to_score(bar_line_locations = [4, 8, 12, 16,
													20, 23.5, 27.5, 32,
													36.5, 40, 43.5, 47,
													50.5, 54, 57.5, 60.5,
													64, 67, 71, 74.5,
													78.5, 81, 84.5, 88],
							max_divisor = 6,
							title = "Adrift", 
							composer = "Alex Stephenson")
score.show_xml()

