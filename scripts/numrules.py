import sys

if len(sys.argv) != 2:
	print("Usage: "+sys.argv[0]+" <INPUT>")
	exit(0)

filename = sys.argv[1]

with open(filename, 'r') as f:
	current_line = None
	counter = 0
	line_buffer = []
	for line in f:
		if current_line:
			line_buffer.append(line.replace("\n", ""))
			
			if len(line) > 1:
				counter = counter+1
			else:
				print(current_line.replace("{{BUILD.NUMRULES}}", str(counter)))
				for l in line_buffer:
					print(l)
				current_line = None
		else:
			if line.find("{{BUILD.NUMRULES}}") >= 0:
				line_buffer = []
				current_line = line.replace("\n", "")
				counter = 0
			else:
				print(line.replace("\n", ""))

