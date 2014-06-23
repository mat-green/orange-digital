#  -*- coding: utf-8 -*- 
"""
Setup tools script for Orange Digital baby name application.
"""

import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

def required(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read().split('\n')

config = {
    "name" : "baby-names",
    "version" : "13.10.0",
    "namespace_packages" : [ ],
    "packages" : find_packages(exclude=[
                                         "*.tests", "*.tests.*", "tests.*", "tests",
                                         "*.ez_setup", "*.ez_setup.*", "ez_setup.*", "ez_setup",
                                         "*.examples", "*.examples.*", "examples.*", "examples",
                                       ]),
    "include_package_data" : True,
    "package_data" : {
                       "" : [ ],
                     },
    "data_files" : [],
    "scripts" : [ ],
    "entry_points" : { },
    "install_requires" : [  required('install-requires.txt') ],
    "tests_require" : [ required('install-test-requires.txt') ],
    "test_suite" : 'nose.collector',
    "zip_safe" : False,
    
    # Metadata for upload to PyPI
    "author" : 'Matthew Green',
    "author_email" : "matthew@newedgeengineering.com",
    "description" : "Rank the top 1000 male baby names between 1880 and 2010",
    "long_description" : """babynames is a command line application that queries 
http://www.socialsecurity.gov/OACT/babynames/ to retrieve top 1000 ranked male 
names between 1880 and 2010.""",
    "classifiers" : [
                      "Programming Language :: Python",
                    ],
    "license" : "",
    "keywords" : "",
    "url" : "",
}

setup(**config)
