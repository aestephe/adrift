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

flute_midi = [65, 68, 66, 69, 60, 60, 60, 60]

s.start_transcribing()

s.wait(0.5)

for midi in flute_midi:
	flute.play_note(midi - 12, volume = 0.1, length = 2.5)
	s.wait(1.75)

performance = s.stop_transcribing()
score = performance.to_score(bar_line_locations = [3.5, 6.5, 10, 13.5, 16.5,
													21, 25, 29.5,
													32],
							max_divisor = 6,
							title = "Adrift", 
							composer = "Alex Stephenson")
score.show_xml()

