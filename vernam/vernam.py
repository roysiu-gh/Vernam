#!/usr/bin/env python3

def vernam(text, key):
    bintext = [ ord(x) for x in text ]
    binkey = [ ord(x) for x in key ]
    
    for i in range(len(bintext)):
        binkey.append( binkey[i] )
    
    result = [ bintext[i] ^ binkey[i] for i in range(len(bintext)) ]
    
    for index, item in enumerate(result):
        result[index] = chr(item)
    return result

encoded = vernam("super_secret_message", "very_secret_key")
print( encoded )

decoded = vernam(encoded, "very_secret_key")
print( "".join(decoded) )
