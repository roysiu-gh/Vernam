---
# Vernam 2.0.0

### Synopsis
A simple vernam (or OTP) encryption / decription program in python

---
### Code Example
Encode message "super_secret_message" with key "very_secret_key", store in variable "encoded", and print as a list.
~~~
encoded = vernam("super_secret_message", "very_secret_key")
print( encoded )
~~~

Decode message stored in variable "encoded" with key "very_secret_key", store in variable "decoded", and print as a string.
~~~
decoded = vernam(encoded, "very_secret_key")
print( "".join(decoded) )
~~~
---
### Installation
Install:
~~~
>>> pip install vernam
~~~
Import:
~~~
>>> from vernam import vernam
~~~
---
### API Reference
1. Create an instance of class vernam
2. Run: 
instance.xor(key)
  * "key" must be a string or list, if the latter, each item must contain a single unicode character in string form
---
### License
[MIT Licence](https://choosealicense.com/licenses/mit/#)

---