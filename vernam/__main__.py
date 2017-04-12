#!/usr/bin/env python3
import vernam
import sys

def main():
    try:
        print( vernam.vernam( sys.argv[1], sys.argv[2] ) )
    except (TypeError, IndexError):
        vernam.usage()

if __name__ =="__main__":
    main()