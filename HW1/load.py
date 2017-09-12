
# Function to load a given grammar file into a dictionary
def load(filename):
	gramm = open(filename, "r")
	prerules = {}
	rules = {}
	while True:
		line = gramm.readline()
		if not line: # reached end of file
			break

		if(line.find('#') == 0): # is solely a commented line
			continue

		presplit = line.split('#') # To account for comments in line
		tokens = presplit[0].split() 

		if(len(tokens) == 0): # if empty line go next
			continue
	
		relodds = tokens[0]
		lhs = tokens[1]
		rhs = tokens[2::]
		prerules.setdefault(lhs,[])
		prerules[lhs].append([relodds, rhs])
		#rules[lhs].append(rhs)
	gramm.close()

	# Section below turn relative odds of occurence into probabilities
	for lhs in prerules:
		total = 0
		possibles = prerules[lhs]
		for occurence in possibles:
			total += float(occurence[0])
		for occurence in possibles:
			occurence[0] = float(occurence[0]) / total

	print prerules
	return rules




