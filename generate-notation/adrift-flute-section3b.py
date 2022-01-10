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

s = scamp.Session(tempo = 72)

s.fast_forward_in_beats(600)

# build instruments
flute = s.new_part("Piccolo")

s.start_transcribing()

flute_midi = [79, 80, 79, 81]
flute_durations = [1.75 * 0.618, 1 * 0.618, 1.75 * 0.618, 2.5 * 0.618]
flute_rests = [0, 0, 0, 0]
i = 0
for midi in flute_midi:
	flute.play_note(midi + 12, volume = 0.1, length = flute_durations[i % len(flute_durations)])
	s.wait(flute_rests[i % len(flute_rests)])
	i += 1

flute_midi = [79, 80, 79, 81, 80,
				79, 81, 80, 82, 81,
				80,
				79, 81, 80, 82, 81,
				80, 82, 81, 83, 82,
				81, 83, 82, 84, 83,
				82
				]
flute_durations = [1.75 * 0.618, 1.75 * 0.618, 1 * 0.618, 1.75 * 0.618, 1 * 0.618]
flute_rests = [0, 0, 0, 0, 0]
i = 0
for midi in flute_midi:
	flute.play_note(midi + 12, volume = 0.1, length = flute_durations[i % len(flute_durations)])
	s.wait(flute_rests[i % len(flute_rests)])
	i += 1

flute_midi = [84, 83, 85, 84,
				83, 85, 84, 86, 85]
flute_durations = [0.75]
flute_rests = [0]
i = 0
for midi in flute_midi:
	flute.play_note(midi + 12, volume = 0.1, length = flute_durations[i % len(flute_durations)])
	s.wait(flute_rests[i % len(flute_rests)])
	i += 1

performance = s.stop_transcribing()
score = performance.to_score(bar_line_locations = [4, 7,
													11, 14,
													18, 21,
													25, 28,
													32, 35,
													39],
							max_divisor = 8,
							max_divisor_indigestibility = 5,
							title = "Adrift", 
							composer = "Alex Stephenson")
score.show_xml()

