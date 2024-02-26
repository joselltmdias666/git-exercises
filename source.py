
import sys

def main(argv):
        if len(argv) > 1: 
                print(f"Hello {argv[1]}")
        else:
                print("USage: python hello.py [arg0]")

if _name_ == "_main_":
        main(sys.argv[1:])





