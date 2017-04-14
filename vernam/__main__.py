#!/usr/bin/env python3
from py_vernam import vernam, usage
import sys

def main():
    try:
        print( vernam( sys.argv[1], sys.argv[2] ) )
    except (TypeError, IndexError):
        usage()

if __name__ =="__main__":
    main()