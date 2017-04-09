---
# Vernam 1.0.0

### Synopsis
A simple vernam (or OTP) encryption / decription program in python

---
### Code Example
Create an object with plaintext "abcd6z":
~~~
>>> foo = vernam("abcd6z
~~~
---
Encrypt with key "abczz", store in variable "encoded", and print:
~~~
>>> encoded = (foo.xor("abczz"))
>>> print( encoded )
[u'\x00', u'\x00', u'\x00', u'\x1e', u'L', u'\x1b']
~~~
---
Create object with ciphertext stored in "encoded":
~~~
>>> bar = vernam(encoded)
~~~
---
Decrypt with key "abczz", store in variable "decoded", and print (with list joined):
~~~
>>> decoded = bar.xor("abczz")
>>> print( "".join(decoded) )
abcd6z
~~~
---
### Installation
Install:
~~~
>>> pip install vernam
~~~
---
Import:
~~~
>>> from vernam import vernam
~~~
---
### API Reference
1. Create an instance of class vernam
2. Run: 
instance.xor(key) [^1]
---
### License
[MIT](https://choosealicense.com/licenses/mit/#)
---
[^1]: key must be a string or list, if the latter, each item must contain a single unicode character in string form