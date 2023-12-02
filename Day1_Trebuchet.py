# Advent of code
# Day 1: Trebuchet?!
# part 1
import re

with open('Day1_input.txt') as file:
	lines = file.read().splitlines()

final = 0

for line in lines:
	first = re.search(r'\d', line)
	last = re.search(r'(\d)(?!.*\d)', line)
	final += int(first.group()+last.group())

print("Part 1 final: ", final)

# part 2
def find_real_digits(line):
	num_dict = {'one':'1', 'two':'2', 'three':'3', \
	'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
	# find first digit
	first = re.search(r'\d', line)
	first_index = first.start()
	first_num = first.group()
	for num in num_dict.keys():
		match = re.search(num, line)
		if match:
			if match.start() < first_index:
				first_index = match.start() 
				first_num = num_dict[num]
	# find last digit
	last = re.search(r'(\d)(?!.*\d)', line)
	last_index = last.start()
	last_num = last.group()
	for num in num_dict.keys():
		if num in line:
			index = line.rfind(num)
			if index > last_index:
				last_index = index
				last_num = num_dict[num]
	return int(first_num+last_num)

final2 = 0 
for line in lines:
	final2 += find_real_digits(line)
	
print("Part 2 final: ", final2)