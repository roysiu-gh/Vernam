#!/usr/bin/env python3
import sys
import click

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

@click.command()
@click.argument("text")
@click.argument("key")
@click.option('--string/--list', '-s/-l', "return_str", default=False, help="return as string [default: list]")
@click.option('--return-long', default=False, help="WIP")
def _vernam_cli(*args, **kwargs): #text, key, return_str, return_long
    click.echo( vernam(*args, **kwargs) )

if __name__ == "__main__":
    #import doctest
    #doctest.testfile("vernam.doctest")
    _vernam_cli()