# Advent of code
# Day 1: Cube Conundrum
import re

with open('Day2_input.txt') as file:
	lines = file.read().splitlines()

# part 1
total = (1+len(lines))*len(lines)/2

for line in lines:
	found = False
	entry = line.split(":")
	game_full = entry[0]
	game = int(re.search(r'\d+', game_full).group())
	data = entry[1]
	members = data.split(";")
	for member in members:
		set_game = member.split(",")
		for color in set_game:
			match = int(re.search(r'\d+', color).group())
			if match > 12:
				color_code = re.search(r'[a-z]', color).group()
				if color_code == 'r':
					total -= game
					found = True
					break
				elif color_code == 'g' and match > 13:
					total -= game
					found = True
					break
				elif color_code == 'b' and match > 14:
					total -= game
					found = True
					break
		if found:
			break
print("Part 1: ", total)

#part 2
total = 0
for line in lines:
	data = line.split(":")[1]
	draws = data.split(";")
	green = 0
	blue = 0
	red = 0
	for draw in draws:
		color_draws = draw.split(",")
		for color_draw in color_draws:
			color_code = re.search(r'[a-z]', color_draw).group()
			num = int(re.search(r'\d+', color_draw).group())
			if color_code == 'g' and num > green:
				green = num;
			elif color_code == 'r' and num > red:
				red = num;
			elif color_code == 'b' and num > blue:
				blue = num;
	total += green*red*blue
print("Part 2: ", total)