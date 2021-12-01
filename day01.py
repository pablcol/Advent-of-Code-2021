def main():
	#def sonar():
	input = [""]
	input = open("inputd1.txt").readlines()
	for lines in input:
		counter = 0
		if int(lines) < int(lines)+1:
			counter += 1
			print(counter)
	return

if __name__ == "__main__":
	main()
