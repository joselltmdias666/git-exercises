import sys

def greet(name):
	print(f'Hello {name}!')

if _name_ == "_main_":
	if len(sys.argv) !=2:
		print("Usage: puthon script.py <name>")
	else:
		name = sys.argv[1]
		greet(name)

