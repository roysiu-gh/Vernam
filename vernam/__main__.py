#!/usr/bin/env python3
from py_vernam import vernam
import sys

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Encrypt a message using the Vernam cipher')
    parser.add_argument('vals', metavar='vals', type=str, nargs='+',help='cipher arguments') #only 2
    
    parser.add_argument('--list', dest='return_str', action='store_false', help='return as string (default: return list)')
    parser.add_argument('--string', dest='return_str', action='store_true', help='return as string (default: return list)')
    
    parser.add_argument('--long', dest='return_long', action='store_true', help='encrypt with longest value (default: length of first val)')
    parser.add_argument('--short', dest='return_long', action='store_false', help='encrypt with shortest value (default: length of first val)')
    
    args = parser.parse_args()
    print( vernam( *args.vals, return_str=args.return_str, return_long=args.return_long ) )

if __name__ == "__main__":
    main()