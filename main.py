# Imports.
import numpy as np
import pandas as pd
import random as rd
import os
import time
from termcolor import colored

# Array that contains most common intervals in all 12 keys.
interval_arr = np.array([
	['1',  '3',  'b3',  '5',  'b5',  '#5',  '6',  '(b)7', 'maj7', 'bb7',  '9',  'b9',  '#9',  '11', '#11', '13', 'b13'],
	['C',  'E',  'Eb',  'G',  'Gb',  'G#',  'A',  'Bb',   'B',    'Bbb',  'D',  'Db',  'D#',  'F',  'F#',  'A',  'Ab'], 
	['G',  'B',  'Bb',  'D',  'Db',  'D#',  'E',  'F',    'F#',   'Fb',   'A',  'Ab',  'A#',  'C',  'C#',  'E',  'Eb'], 
	['D',  'F#', 'F',   'A',  'Ab',  'A#',  'B',  'C',    'C#',   'Cb',   'E',  'Eb',  'E#',  'G',  'G#',  'B',  'Bb'], 
	['A',  'C#', 'C',   'E',  'Eb',  'E#',  'F#', 'G',    'G#',   'Gb',   'B',  'Bb',  'B#',  'D',  'D#',  'F#', 'F'], 
	['E',  'G#', 'G',   'B',  'Bb',  'B#',  'C#', 'D',    'D#',   'Db',   'F#', 'F',   'F##', 'A',  'A#',  'C#', 'C'], 
	['B',  'D#', 'D',   'F#', 'F',   'F##', 'G#', 'A',    'A#',   'Ab',   'C#', 'C',   'C##', 'E',  'E#',  'G#', 'G'],
	['Cb', 'Eb', 'Ebb', 'Gb', 'Gbb', 'G',   'Ab', 'Bbb',  'Bb',   'Bbbb', 'Db', 'Dbb', 'D',   'Fb', 'F',   'Ab', 'Abb'],
	['F#', 'A#', 'A',   'C#', 'C',   'C##', 'D#', 'E',    'E#',   'Eb',   'G#', 'G',   'G##', 'B',  'B#',  'D#', 'D'],
	['Gb', 'Bb', 'Bbb', 'Db', 'Dbb', 'D',   'Eb', 'Fb',   'F',    'Fbb',  'Ab', 'Abb', 'A',   'Cb', 'C',   'Eb', 'Ebb'],
	['C#', 'E#', 'E',   'G#', 'G',   'G##', 'A#', 'B',    'B#',   'Bb',   'D#', 'D',   'D##', 'F#', 'F##', 'A#', 'A'], 	
	['Db', 'F',  'Fb',  'Ab', 'Abb', 'A',   'Bb', 'Cb',   'C',    'Cbb',  'Eb', 'Ebb', 'E',   'Gb', 'G',   'Bb', 'Bbb'],	
	['Ab', 'C',  'Cb',  'Eb', 'Ebb', 'E',   'F',  'Gb',   'G',    'Gbb',  'Bb', 'Bbb', 'B',   'Db', 'D',   'F',  'Fb'], 
	['Eb', 'G',  'Cb',  'Bb', 'Bbb', 'B',   'C',  'Db',   'D',    'Dbb',  'F',  'Fb',  'F#',  'Ab', 'A',   'C',  'Cb'],
	['Bb', 'D',  'Db',  'F',  'Fb',  'F#',  'G',  'Ab',   'A',    'Abb',  'C',  'Cb',  'C#',  'Eb', 'E',   'G',  'Gb'],
	['F',  'A',  'Ab',  'C',  'Cb',  'C#',  'D',  'Eb',   'E',    'Ebb',  'G',  'Gb',  'B#',  'Bb', 'B',   'D',  'Db']
	])

s1 = ' ██╗   ██╗ █████╗     ██╗     ██╗██╗  ██╗███████╗         ██╗ █████╗ ███████╗███████╗██████╗\n'
s2 = ' ╚██╗ ██╔╝██╔══██╗    ██║     ██║██║ ██╔╝██╔════╝         ██║██╔══██╗╚══███╔╝╚══███╔╝╚════██╗\n'
s3 = '  ╚████╔╝ ███████║    ██║     ██║█████╔╝ █████╗           ██║███████║  ███╔╝   ███╔╝   ▄███╔╝\n'
s4 = '   ╚██╔╝  ██╔══██║    ██║     ██║██╔═██╗ ██╔══╝      ██   ██║██╔══██║ ███╔╝   ███╔╝    ▀▀══╝\n'
s5 = '    ██║   ██║  ██║    ███████╗██║██║  ██╗███████╗    ╚█████╔╝██║  ██║███████╗███████╗  ██╗\n'
s6 = '    ╚═╝   ╚═╝  ╚═╝    ╚══════╝╚═╝╚═╝  ╚═╝╚══════╝     ╚════╝ ╚═╝  ╚═╝╚══════╝╚══════╝  ╚═╝\n'
s7 = s1 + s2 + s3 + s4 + s5 + s6

s8 = ' ┬┌┐┌┬┐┌─┐┬─┐┬  ┬┌─┐┬    ┌─┐┬─┐┌─┐┌─┐┌┬┐┬┌─┐┌─┐\n │││││ ├┤ ├┬┘└┐┌┘├─┤│    ├─┘├┬┘├─┤│   │ ││  ├┤\n ┴┘└┘┴ └─┘┴└─ └┘ ┴ ┴┴─┘  ┴  ┴└─┴ ┴└─┘ ┴ ┴└─┘└─┘\n'

# Convert numpy array to Pandas dataframe.
interval_df = pd.DataFrame(data=interval_arr[1:], columns=interval_arr[0])

# Function that will ask you the questions
def ask_interval(arr, choice):
	# This function will check if your answer is correct.
	def check_answer(arr, key, interval, interval_answer):
		if interval_answer == arr.iloc[key, interval]: return True
		elif interval_answer != arr.iloc[key, interval]: return False

	def choose_key_menu():
		os.system('cls' if os.name == 'nt' else 'clear')
		print(''); print(s8)

		print('Choose from the following list of keys.\n')
		print(" Scale  Number of sharps/flats\n C\n G      #\n D      ##\n A      ###\n E      ####\n B      #####\n Cb     bbbbbbb\n F#     ######\n Gb     bbbbbb\n C#     #######\n Db     bbbbb\n Ab     bbbb\n Eb     bbb\n Bb     bb\n F      b\n")

		key_choice = input('Key choice: ')

		if key_choice == 'C': return 0
		if key_choice == 'G': return 1
		if key_choice == 'D': return 2
		if key_choice == 'A': return 3
		if key_choice == 'E': return 4
		if key_choice == 'B': return 5
		if key_choice == 'Cb': return 6
		if key_choice == 'F#': return 7
		if key_choice == 'Gb': return 8
		if key_choice == 'C#': return 9
		if key_choice == 'Db': return 10
		if key_choice == 'Ab': return 11
		if key_choice == 'Eb': return 12
		if key_choice == 'Bb': return 13
		if key_choice == 'F': return 14
		if key_choice == 'q': interval_menu()

	if choice == '2':
		key_choice = choose_key_menu()

	question_counter = 0
	correct_counter = 0

	while True:
		os.system('cls' if os.name == 'nt' else 'clear')
		print(''); print(s8)

		# Randomly obtain a musical key.
		key = rd.randint(0, arr.shape[0]-1)
		if choice == '2':
			key = key_choice

		# Randomly obtain an interval.
		interval = rd.randint(1, arr.shape[1]-1)

		# Ask the question.
		if question_counter == 0: print(f' Q: In the key of {arr.iloc[key, 0]}, what is the {arr.columns.values[interval]} interval?')
		elif question_counter > 0 and question_counter < 6: print(f' Q: Key: {arr.iloc[key, 0]}, Interval: {arr.columns.values[interval]}')
		else: print(f' Q: {arr.iloc[key, 0]} | {arr.columns.values[interval]}')

		# Your answer
		interval_answer = input(' A: ')
		question_counter += 1

		if interval_answer == 'q': interval_menu()

		# Check answer.
		if check_answer(arr, key, interval, interval_answer):
			correct_counter += 1
			print(colored('\nCorrect!', 'green'))
			print(f'{correct_counter}/{question_counter}, {int(correct_counter/question_counter*100):.1f}% correct.\n')
			delay = 1 - question_counter*0.03;
			if question_counter >= 10: delay = 0.7
		else:
			print(colored('\nIncorrect!', 'red'))
			print(f'The correct answer is {arr.iloc[key, interval]}')
			print(f'{correct_counter}/{question_counter}, {int(correct_counter/question_counter*100):.1f}% correct.\n')
			delay = 2

		# Timer before the next question appears.
		now = time.time(); future = now + delay
		while time.time() < future: pass

		# Clear terminal.
		os.system('cls' if os.name == 'nt' else 'clear')


def interval_menu():
	os.system('cls' if os.name == 'nt' else 'clear')
	print(''); print(s8)

	print('Do you want to practice all scales or one scale?\n')
	print(" [1] All scales")
	print(" [2] One scale")
	print(" [q] Back to main menu")

	choice = input('\nChoice: ')

	if choice == '1' or choice == '2': ask_interval(interval_df, choice)
	elif choice == 'q': main_menu()


def main_menu():
	while True:
		os.system('cls' if os.name == 'nt' else 'clear')
		print(''); print(s7)

		print(" ===> Welcome to Auke's musical flashcard software! Choose your practice mode.\n")
		print(" [1] Interval exercises")
		print(" [2] ii-V-I exercises")

		choice = input('\nWhat do you want to practice? ')

		if choice == '1': interval_menu()
		if choice == '2': pass
		if choice == 'q': quit()

def main():
	main_menu()

main()