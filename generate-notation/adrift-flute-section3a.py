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

s = scamp.Session(tempo = 36)

s.fast_forward_in_beats(600)

# build instruments
flute = s.new_part("Flute")

s.start_transcribing()

# flute_midi = [67, 65, 66,
# 				67, 65, 68,
# 				65, 64, 68,
# 				67, 68, 65,
# 				64, 65, 64,
# 				63, 60, 63,
# 				63, 60, 63]

flute_midi = [67, 65, 68,
				67, 65, 68]
flute_durations = [1.75, 1.75, 2.5]
flute_rests = [0, 0, 1]
i = 0
for midi in flute_midi:
	flute.play_note(midi - 12, volume = 0.1, length = flute_durations[i % len(flute_durations)])
	s.wait(flute_rests[i % len(flute_rests)])
	i += 1


flute_midi = [65, 64, 68, 67, 65]
flute_durations = [1.75, 1.75, 1, 1.75, 2.5]
flute_rests = [0, 0, 0, 0, 1]
i = 0
for midi in flute_midi:
	flute.play_note(midi - 12, volume = 0.1, length = flute_durations[i % len(flute_durations)])
	s.wait(flute_rests[i % len(flute_rests)])
	i += 1

flute_midi = [64, 67, 65, 64, 67, 68, 67]
flute_durations = [1.75, 1.75, 1.25, 1, 2, 1.25, 2.5]
flute_rests = [0, 0, 0, 0, 0, 0, 1]
i = 0
for midi in flute_midi:
	flute.play_note(midi - 12, volume = 0.1, length = flute_durations[i % len(flute_durations)])
	s.wait(flute_rests[i % len(flute_rests)])
	i += 1

s.wait(1)

flute_midi = [63, 60, 63,
				63, 60, 63]
flute_durations = [1.75, 1.75, 2.5]
flute_rests = [0, 0, 1]
i = 0
for midi in flute_midi:
	flute.play_note(midi - 12, volume = 0.1, length = 1.618 * flute_durations[i % len(flute_durations)])
	s.wait(flute_rests[i % len(flute_rests)])
	i += 1

flute_midi = [66, 69, 60, 69]
flute_durations = [1.75, 1.75, 1.25, 2.5]
flute_rests = [0, 0, 0, 1]
i = 0
for midi in flute_midi:
	flute.play_note(midi - 12, volume = 0.1, length = 1.618 * flute_durations[i % len(flute_durations)])
	s.wait(flute_rests[i % len(flute_rests)])
	i += 1

flute_midi = [66, 69, 60, 69, 72,
				66, 69, 70, 67, 70]
flute_durations = [1.75, 1.75, 1.25, 1.75, 2.5]
flute_rests = [0, 0, 0, 0, 1]
i = 0
for midi in flute_midi:
	flute.play_note(midi - 12, volume = 0.1, length = 1.618 * flute_durations[i % len(flute_durations)])
	s.wait(flute_rests[i % len(flute_rests)])
	i += 1

s.wait(0.5)

flute_midi = [67, 70, 69, 70]
flute_durations = [1.75, 1.75, 1.25, 2.5]
flute_rests = [0, 0, 0, 1]
i = 0
for midi in flute_midi:
	flute.play_note(midi - 12, volume = 0.1, length = 1.618 * flute_durations[i % len(flute_durations)])
	s.wait(flute_rests[i % len(flute_rests)])
	i += 1

s.wait(1)

flute_midi = [67, 78, 78,
				67, 78, 78]
flute_durations = [1.75, 1.75, 2.5]
flute_rests = [0, 0, 2]
i = 0
for midi in flute_midi:
	flute.play_note(midi - 12, volume = 0.1, length = 1.618 * flute_durations[i % len(flute_durations)])
	s.wait(flute_rests[i % len(flute_rests)])
	i += 1

flute_midi = [67, 79, 78, 79]
flute_durations = [1.75, 1.75, 1.75, 2.5]
flute_rests = [0, 0, 0, 2]
i = 0
for midi in flute_midi:
	flute.play_note(midi - 12, volume = 0.1, length = 1.618 * flute_durations[i % len(flute_durations)])
	s.wait(flute_rests[i % len(flute_rests)])
	i += 1

s.wait(0.75)

flute_midi = [80, 79, 80, 79, 81]
flute_durations = [1.75 * 0.382, 1.75 * 0.382, 1 * 0.382, 1.75 * 0.382, 2.5 * 0.382]
flute_rests = [0, 0, 0, 0, 0]
i = 0
for midi in flute_midi:
	flute.play_note(midi - 12, volume = 0.1, length = flute_durations[i % len(flute_durations)])
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
flute_durations = [1.75 * 0.382, 1.75 * 0.382, 1 * 0.382, 1.75 * 0.382, 1 * 0.382]
flute_rests = [0, 0, 0, 0, 0]
i = 0
for midi in flute_midi:
	flute.play_note(midi - 12, volume = 0.1, length = flute_durations[i % len(flute_durations)])
	s.wait(flute_rests[i % len(flute_rests)])
	i += 1

flute_midi = [84, 83, 85, 84,
				83, 85, 84, 86, 85]
flute_durations = [0.375]
flute_rests = [0]
i = 0
for midi in flute_midi:
	flute.play_note(midi - 12, volume = 0.1, length = flute_durations[i % len(flute_durations)])
	s.wait(flute_rests[i % len(flute_rests)])
	i += 1

performance = s.stop_transcribing()
score = performance.to_score(bar_line_locations = [4, 7.5, 11.5,
												15, 19, 22.5,
												27, 31, 35.5, 
												39, 42.5, 46, 49.5,
												52.5, 56, 60.5,
												64.5, 69, 73,
												76.5, 79.5, 83,
												86, 
												90.5, 95, 99.5, 104,
												107.5, 110.5, 114, 116.5, # 5/8 bar
												120],	
							max_divisor = 8,
							max_divisor_indigestibility = 5,
							title = "Adrift", 
							composer = "Alex Stephenson")
score.show_xml()

