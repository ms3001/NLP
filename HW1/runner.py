from load import load
from generate import generate

# Function to run the program as needed

def main(filename, n):
	rules = load(filename)

main('grammar.gr', 1)