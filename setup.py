from setuptools import setup
# To use a consistent encoding
#from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open( path.join(path.abspath(path.dirname(__file__)) , 'README.md' )) as f:
    long_description = f.read()

setup(
    name = 'vernam',
    version = '2.0.0',

    description = 'Vernam cipher',
    long_description = long_description,

    url = 'https://github.com/roysoup/Vernam',

    author = 'Roy Siu',
    author_email = '',

    license = 'MIT Licence',

    classifiers = [
        'Development Status :: 5 - Production/Stable'
    ],
    
    install_requires = [''],
)