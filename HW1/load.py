
# Function to load in a given grammar
def load(filename):
	gramm = open(filename, "r")
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
		rules.setdefault(lhs,[])
		rules[lhs].append([relodds rhs])
	gramm.close()	

	# Turn relodds into probabilities

	print rules
	return rules




