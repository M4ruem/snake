from pytimedinput import timedInput
import os
from random import randint
from colorama import Fore, init

def print_field():
	for cell in CELLS:
		if cell in snake_body:
			print(Fore.GREEN + 'S', end = '')
		elif cell[0] in (0, WIDTH - 1) or cell[1] in (0, HEIGHT - 1):
			print(Fore.BLUE + '#', end = '')
		elif cell == apple_pos:
			print(Fore.RED + '@', end = '')
		else:
			print(' ', end = '')
		if cell[0] == WIDTH - 1:
			print('')

def update_snake():
	global eaten
	head = snake_body[0][0] + movement[0], snake_body[0][1] + movement[1]
	snake_body.insert(0,head)
	if not eaten:
		snake_body.pop(-1)
	eaten = False

def apple_collision():
	global apple_pos, eaten
	if apple_pos == snake_body[0]:
		apple_pos = place_apple()
		eaten = True

def place_apple():
	col = randint(1, WIDTH - 2)
	row = randint(1, HEIGHT - 2)
	while (col,row) in snake_body:
		col = randint(1, WIDTH - 2)
		row = randint(1, HEIGHT - 2)

	return (col, row)

init(autoreset = True)

WIDTH = 32
HEIGHT = 16
CELLS = [(col, row) for row in range(HEIGHT) for col in range(WIDTH)]

snake_body = [(5, HEIGHT // 2),(4, HEIGHT // 2),(3, HEIGHT // 2)]
MOVEMENT = {'left': (-1,0), 'right': (1, 0), 'up': (0, -1), 'down': (0,1)}
movement = MOVEMENT['right']
eaten = False

apple_pos = place_apple()

while True:
	os.system('clear')
	print_field()
	txt,_ = timedInput('',timeout = 0.3)
	if txt == 'w':
		movement = MOVEMENT['up']
	elif txt == 'a':
		movement = MOVEMENT['left']
	elif txt == 's':
		movement = MOVEMENT['down']
	elif txt == 'd':
		movement = MOVEMENT['right']
	elif txt == 'q':
		os.system('clear')
		break
	update_snake()
	apple_collision()

	if	snake_body[0][0] in (0, WIDTH - 1) or \
		snake_body[0][1] in (0, HEIGHT - 1) or \
		snake_body[0] in snake_body[1:]:
		os.system('clear')
		break
