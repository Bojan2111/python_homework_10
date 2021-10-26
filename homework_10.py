##############################
# Homework no. 10 for Pirple #
#    Python is Easy Course   #
#      Import modules        #
# Created by:                #
# Bojan Adzic aka Coder::Owl #
##############################

'''
	This task is about importing one library and put it to practice.
	I have decided to go with the Statistics library and showcase the
	possibilities with managing statistical data analysis.

	In statistics, mean, mode, standard deviation and variance are
	most commonly used methods to describe the importance or certain
	aspects of data.

	Lucky for us, Python offers a built in library for this. For more
	advanced data analysis, especially with big data, consider using
	pandas open source library.

	Potential use is with analyzing user input.
'''
import os
os.system('color')
import sys
from termcolor import colored, cprint
import statistics as s

# Fast, floating point arithmetic mean.
print("Floating point arithmetic mean:", s.fmean([3.5, 4.0, 5.25]))

# Geometric mean of data.
print("Geometric mean:", round(s.geometric_mean([54, 24, 36]), 1))

# Harmonic mean of data.
print("Harmonic mean 1:", s.harmonic_mean([40, 60]))
print("Harmonic mean 2:", s.harmonic_mean([2.5, 3, 10]))

# Median (middle value) of data.
print("Median (middle value) 1:", s.median([1, 3, 5]))
print("Median (middle value) 2:", s.median([1, 3, 5, 7]))

# Low median of data.
print("Low median 1:", s.median_low([1, 3, 5]))
print("Low median 2:", s.median_low([1, 3, 5, 7]))

# High median of data.
print("High median 1:", s.median_high([1, 3, 5]))
print("High median 2:", s.median_high([1, 3, 5, 7]))

# Median, or 50th percentile, of grouped data.
print("Median, or 50th percentile 1:", s.median_grouped([52, 52, 53, 54]))
print("Median, or 50th percentile 2:", s.median_grouped([1, 2, 2, 3, 4, 4, 4, 4, 4, 5]))
print("Median, or 50th percentile 3:", s.median_grouped([1, 3, 3, 5, 7], interval=1))
print("Median, or 50th percentile 4:", s.median_grouped([1, 3, 3, 5, 7], interval=2))

# Single mode (most common value) of discrete or nominal data.
print("Single mode (most common value) - integers:", s.mode([1, 1, 2, 3, 3, 3, 3, 4]))
print("Single mode (most common value) - strings:", s.mode(["red", "blue", "blue", "red", "green", "red", "red"]))

# List of modes (most common values) of discrete or nomimal data.
print("List of modes (most common values):", s.multimode('aabbbbccddddeeffffgg'))

# Population standard deviation of data.
print("Population standard deviation:", s.pstdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75]))

# Population variance of data.
data = [0.0, 0.25, 0.25, 1.25, 1.5, 1.75, 2.75, 3.25]
print("Population variance of data:", s.pvariance(data))

# Population variance of data with precalculated  arithmetic mean (“average”) of data.
mu = s.mean(data)
print("Population variance of data with precalculated  arithmetic mean:", s.pvariance(data, mu))

# Sample standard deviation of data.
print("Sample standard deviation:", s.stdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75]))

# Sample variance of data.
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print("Sample variance:", s.variance(data))

print("\n======================================\n")
print("\nAnd now for something completely different...\n")
print("\n======================================\n")

def printData(data):
	print("\n======================================\n")
	print("Arithmetic mean:", s.mean(data))
	print("Fast float mean:", s.fmean(data))
	print("Geometric mean:", s.geometric_mean(data))
	print("Harmonic mean:", s.harmonic_mean(data))
	print("Median value:", s.median(data))
	print("Low median:", s.median_low(data))
	print("High median:", s.median_high(data))
	print("Groupped median:", s.median_grouped(data))
	print("Most common value:", s.mode(data))
	print("Most commons list:", s.multimode(data))
	print("Quantiles:", s.quantiles(data))
	print("Population standard deviation:", s.pstdev(data))
	print("Population variance:", s.pvariance(data))
	print("Standard deviation:", s.stdev(data))
	print("Variance:", s.variance(data))
	print("\n======================================\n")

while True:
	data = []
	dataType = input("What type of data will you enter?\nType 's' for strings, 'i' for integers and 'f' for floats: ")
	if dataType == 's':
		while True:
			stringInput = input("Enter strings here. Leave empty to quit program. ")
			print(chr(27) + "[2J")
			if stringInput == "":
				break
			else:
				data.append(stringInput)
				if len(data) > 1:
					print("Most common string in your data entry is: ", s.mode(data))
				else:
					print("Data list not long enough to calculate. Enter more data.")
					print("I can only tell you the most common values in this string list:", s.multimode(data))
	elif dataType == 'i':
		while True:
			intInput = int(input("Enter numbers here. Leave empty to quit program. "))
			print(chr(27) + "[2J")
			if intInput == '':
				break
			else:
				data.append(intInput)
				if len(data) > 2:
					printData(data)
				else:
					print("Data list not long enough to calculate. Enter more data.")
	elif dataType == 'f':
		while True:
			intInput = float(input("Enter numbers here. Leave empty to quit program. "))
			print(chr(27) + "[2J")
			if intInput == None:
				break
			else:
				data.append(intInput)
				if len(data) > 2:
					printData(data)
				else:
					print("Data list not long enough to calculate. Enter more data.")
	else:
		break