import numpy as np
import random as rd
from collections import namedtuple

Mode = namedtuple('Mode', 'start_key intervals')

ionian = Mode('C', [1,1,0.5,1,1,1,0.5])
dorian = Mode('D', [1,0.5,1,1,1,0.5,1])
phrygian = Mode('E', [0.5,1,1,1,0.5,1,1])
lydian = Mode('F',[1,1,1,0.5,1,1,0.5])
mixolydian = Mode('G', [1,1,0.5,1,1,0.5,1])
aeolian = Mode('A', [1,0.5,1,1,0.5,1,1])
locrian = Mode('B', [0.5,1,1,0.5,1,1,1])

modes = [ionian, dorian, phrygian, lydian, mixolydian, aeolian, locrian]

keys_sharp = np.array(['C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C',
	'C#','D','D#','E','F','F#','G','G#','A','A#','B'])
keys_flat = np.array(['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B','C',
	'Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B'])
quinten = np.array(['Cb','Gb','Db','Ab','Eb','Bb',
	'F' ,'C' ,'G' ,'D' ,'A' ,'E' ,'B',
	'F#','C#','G#','D#','A#','E#','B#'])

thirds_filter = np.array([0, 2, 4, 6, 1, 3, 5])

def sharp_or_flat(key, mode):
	index = np.where(quinten == key)[0][0]
	ref_point = np.where(quinten == mode.start_key)[0][0]
	
	if index - ref_point < 0:	return False
	else:	return True

def get_scales(start_key, mode):
	keys_arr = keys_sharp
	if sharp_or_flat(start_key, mode) == False:
		keys_arr = keys_flat
	
	start_index = np.where(keys_arr == start_key)[0][0]

	scale, scale_2 = [], []
	sum_interval = 0
	scale.append(keys_arr[start_index])

	for i in range(len(mode.intervals)):
		sum_interval += int(mode.intervals[i]*2)
		scale.append(keys_arr[start_index + sum_interval])

	for i in range(len(thirds_filter)):
		scale_2.append(scale[thirds_filter[i]])

	#print(scale, scale_2)
	return scale, scale_2

def thirds_exercise():
	mode = np.random(modes)
	print(mode)
	

scale, scale_2 = get_scales('B', ionian)


