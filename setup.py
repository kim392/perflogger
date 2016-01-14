import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup (
    name = "perflogger",
    version = "1.0",
   
    # Project uses elasticsearch to insert data into the ES DB
    install_requires = [
        'elasticsearch'
        ],

    # automatically pickup any packages found
    packages = find_packages(),
    
    # metadata for upload to PyPI
    author = "Sunwoo Kim",
    author_email = "kim392@illinois.edu",
    description = ("A command line utility to measure the performance of" 
                    "commands and other utilities"),
    keywords = "performance measure utility",
    url = "",
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2.7"
        ]
    )
