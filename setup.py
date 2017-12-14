from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open( path.join(path.abspath(path.dirname(__file__)) , "README.md" )) as f:
    long_description = f.read()

setup(
    name = "vernam",
    version = "2.5.6",
    
    scripts=["vernam.py"],
    entry_points = {
        "console_scripts": ["vernam = vernam:cli"]
    },

    description = "Vernam cipher",
    long_description = long_description,

    url = "https://github.com/roysoup/Vernam",

    author = "Roy Siu",
    author_email = "",

    license = "MIT Licence",

    classifiers = [
        "Development Status :: 5 - Production/Stable"
    ],
    
    install_requires = ["Click"],
)