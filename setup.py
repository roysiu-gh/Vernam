from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open( path.join(path.abspath(path.dirname(__file__)) , 'README.md' )) as f:
    long_description = f.read()

setup(
    name = 'vernam',
    version = '2.5.6',
    packages = ["vernam"],
    scripts=['vernam/__main__.py'],
    entry_points = {
        'console_scripts': ['vernam = vernam.__main__:main']
    },

    description = 'Vernam cipher',
    long_description = long_description,

    url = 'https://github.com/roysoup/Vernam',

    author = 'Roy Siu',
    author_email = '',

    license = 'MIT Licence',

    classifiers = [
        'Development Status :: 5 - Production/Stable'
    ],
    
    install_requires = ['typing'],
)