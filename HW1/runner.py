from load import load
from generate import generate

# Function to run the program as needed

def main(filename, n):
	rules = load(filename)
	for i in xrange(n):
		print generate(rules)

main('grammar.gr', 10)