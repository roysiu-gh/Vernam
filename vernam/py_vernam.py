#!/usr/bin/env python3
import sys

def vernam(text, key, return_str=False, return_long=False):
    bintext = [ ord(x) for x in text ]
    binkey = [ ord(x) for x in key ]
    
    i = 0
    while len(binkey) < len(bintext):
        binkey.append( binkey[i] )
        i += 1
    
    vernamed = [ bintext[i] ^ binkey[i] for i in range(len(bintext)) ]
    result = [chr(i) for i in vernamed]
    
    if return_str:
        return "".join(result)
    
    return result

if __name__ == "__main__":
    import doctest
    doctest.testfile("py_vernam.doctest")