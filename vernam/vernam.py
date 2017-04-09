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
    
    
    #def xor(self, key: Union[list, str]) -> list:
    def xor(self, key):
        binkey = [ ord(x) for x in key ]

        for i in range(len(self.bintext)):
            binkey.append( binkey[i] )

        result = [ x for x in [ self.bintext[i] ^ binkey[i] for i in range(len(self.bintext)) ] ]
        
        for index, item in enumerate(result):
            result[index] = unichr(item)
        return result