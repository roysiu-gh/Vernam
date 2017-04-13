#!/usr/bin/env python3
import sys
from typing import Union, List

#def vernam(text:Union[list, str], key:Union[list, str]) -> list:
def vernam(text, key):
    bintext = [ ord(x) for x in text ]
    binkey = [ ord(x) for x in key ]
    
    i = 0
    while len(binkey) < len(bintext):
        binkey.append( binkey[i] )
        i += 1
    
    result = [ bintext[i] ^ binkey[i] for i in range(len(bintext)) ]
    
    for index, item in enumerate(result):
        result[index] = chr(item)
    return result

def usage():
    print( "Usage: {} {} {}".format(sys.argv[0], "<message>", "<key>") )

if __name__ == "__main__":
    try:
        print( vernam( sys.argv[1], sys.argv[2] ) )
    except (TypeError, IndexError):
        usage()