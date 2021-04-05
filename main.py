# Imports.
import numpy as np
import pandas as pd
import random as rd
import os
import time
from termcolor import colored

# Array that contains most common intervals in all 12 keys.
interval_arr = np.array([
	['1',  '3',  'b3',  '5',  'b5',  '#5',  '6',  '(b)7', 'maj7', 'bb7', '9',  'b9',  '#9',  '11', '#11', '13', 'b13'],
	['C',  'E',  'Eb',  'G',  'Gb',  'G#',  'A',  'Bb',   'B',    'Bbb',  'D',  'Db',  'D#',  'F', 'F#', 'A', 'Ab'], 
	['G',  'B',  'Bb',  'D',  'Db',  'D#',  'E',  'F',    'F#',   'Fb',   'A',  'Ab',  'A#',  'C', 'C#', '', ''], 
	['D',  'F#', 'F',   'A',  'Ab',  'A#',  'B',  'C',    'C#',   'Cb',   'E',  'Eb',  'E#',  'G', 'G#', '', ''], 
	['A',  'C#', 'C',   'E',  'Eb',  'E#',  'F#', 'G',    'G#',   'Gb',   'B',  'Bb',  'B#',  'D', 'D#', '', ''], 
	['E',  'G#', 'G',   'B',  'Bb',  'B#',  'C#', 'D',    'D#',   'Db',   'F#', 'F',   'F##', 'A', 'A#', '', ''], 
	['B',  'D#', 'D',   'F#', 'F',   'F##', 'G#', 'A',    'A#',   'Ab',   'C#', 'C',   'C##', 'E', 'E#', '', ''],
	['Cb', 'Eb', 'Ebb', 'Gb', 'Gbb', 'G',   'Ab', 'Bbb',  'Bb',   'Bbbb', 'Db', 'Dbb', 'D',   '', '', '', ''],
	['F#', 'A#', 'A',   'C#', 'C',   'C##', 'D#', 'E',    'E#',   'Eb',   'G#', 'G',   'G##', '', '', '', ''],
	['Gb', 'Bb', 'Bbb', 'Db', 'Dbb', 'D',   'Eb', 'Fb',   'F',    'Fbb',  'Ab', 'Abb', 'A',   '', '', '', ''],
	['C#', 'F',  'Fb',  'G#', 'G',   'G##', 'A#', 'B',    'B#',   'Bb',   'D#', 'D',   'D##', '', '', '', ''], 	
	['Db', 'F',  'Fb',  'Ab', 'Abb', 'A',   'Bb', 'Cb',   'C',    'Cbb',  'Eb', 'Ebb', 'E',   '', '', '', ''],	
	['Ab', 'C',  'Cb',  'Eb', 'Ebb', 'E',   'F',  'Gb',   'G',    'Gbb',  'Bb', 'Bbb', 'B',   '', '', '', ''], 
	['Eb', 'G',  'Cb',  'Bb', 'Bbb', 'B',   'C',  'Db',   'D',    'Dbb',  'F',  'Fb',  'F#',  '', '', '', ''],
	['Bb', 'D',  'Db',  'F',  'Fb',  'F#',  'G',  'Ab',   'A',    'Abb',  'C',  'Cb',  'C#',  '', '', '', ''],
	['F',  'A',  'Ab',  'C',  'Cb',  'C#',  'D',  'Eb',   'E',    'Ebb',  'G',  'Gb',  'B#',  '', '', '', '']
	])

# Convert numpy array to Pandas dataframe.
interval_df = pd.DataFrame(data=interval_arr[1:], columns=interval_arr[0])

# Function that will ask you the questions
def ask_interval(arr):
	# This function will check if your answer is correct.
	def check_answer(arr, key, interval, interval_answer):
		if interval_answer == arr.iloc[key, interval]: return True
		elif interval_answer != arr.iloc[key, interval]: return False

	question_counter = 0
	correct_counter = 0

	while True:
		# Randomly obtain a musical key.
		key = rd.randint(0, arr.shape[0]-1)

		# Randomly obtain an interval.
		interval = rd.randint(1, arr.shape[1]-1)

		# Ask the question.
		print(f'\n Q: In the key of {arr.iloc[key, 0]}, what is the {arr.columns.values[interval]} interval?')

		# Your answer
		interval_answer = input(' A: ')
		question_counter += 1

		# Check answer.
		if check_answer(arr, key, interval, interval_answer):
			correct_counter += 1
			print(colored('\nCorrect!', 'green'))
			print(f'{correct_counter}/{question_counter}, {int(correct_counter/question_counter*100):.1f}% correct.\n')
		else:
			print(colored('\nIncorrect!', 'red'))
			print(f'{correct_counter}/{question_counter}, {int(correct_counter/question_counter*100):.1f}% correct.\n')

		# Timer of 1 second before the next question appears.
		now = time.time(); delay = 1; future = now + delay
		while time.time() < future: pass

		# Clear terminal.
		os.system('cls' if os.name == 'nt' else 'clear')

# Clear terminal before question appears.
os.system('cls' if os.name == 'nt' else 'clear')

# Ask a question.
ask_interval(interval_df)