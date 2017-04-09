#!/usr/bin/env python
#from typing import Union

class vernam(object):
    def __init__(self, text):
        self.text = text
        self.bintext = [ ord(x) for x in text ]
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __repr__(self):
        return self.__dict__
    
    
    #def vernam(self, key: Union[list, str]) -> list:
    def vernam(self, key):
        binkey = [ ord(x) for x in key ]
        
        """
        app = 0
        while len(binkey) < len(self.bintext):
            binkey.append( binkey[app] )
            app += 1
        """
        
        for i in range(len(self.bintext)):
            binkey.append( binkey[i] )
        
        """
        result = []
        for i in range(len(self.bintext)):
            result.append( self.bintext[i] ^ binkey[i] )
        """
        result = [ x for x in [ self.bintext[i] ^ binkey[i] for i in range(len(self.bintext)) ] ]
        
        for index, item in enumerate(result):
            result[index] = unichr(item)
        return result

#"""
foo = vernam("abcd6z")
x = (foo.vernam("abczz"))
print( x )
bar = vernam(x)
y = "".join(bar.vernam(["a","b","c","z","z"]))
print( y )
#"""