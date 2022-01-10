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

s.fast_forward_in_beats(600)

# build instruments
flute = s.new_part("Flute")

flute_midi = [66, 64, 67,
				66, 64, 67,
				64, 63, 67,
				66, 67, 64]
flute_durations = [1.5, 1.5, 2.5]
flute_rests = [0.25, 0.25, 1]

s.start_transcribing()

s.wait(1)

i = 0
for midi in flute_midi:
	flute.play_note(midi - 12, volume = 0.1, length = flute_durations[i % len(flute_durations)])
	s.wait(flute_rests[i % len(flute_rests)])
	i += 1

# -------

for _ in range(0, 3):
	flute.play_note(67 - 12, volume = 0.1, length = 2.5)
	s.wait(1)

# -------

flute_midi = [67, 61, 65,
				64, 67, 65,
				68, 68, 68, 68]
i = 0
for midi in flute_midi:
	flute.play_note(midi - 12, volume = 0.1, length = flute_durations[i % len(flute_durations)])
	s.wait(flute_rests[i % len(flute_rests)])
	i += 1

# -------

performance = s.stop_transcribing()
score = performance.to_score(bar_line_locations = [4, 7.5, 11.5,
													15, 18,
													21.5, 24.5, 28,
													32.5, 37, 41.5,
													45, 48, 51.5, 54.5,
													59, 63.5, 68],

							max_divisor = 6,
							title = "Adrift", 
							composer = "Alex Stephenson")
score.show()

