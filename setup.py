#!/usr/bin/env python3

from setuptools import setup, find_packages
import os
import subprocess

directory = os.path.dirname(os.path.abspath(__file__))

# long_description
readme_path = os.path.join(directory, 'README.md')
try:
    # copied from dhimmel/obonet:
    # Try to create an reStructuredText long_description from README.md
    args = 'pandoc', '--from', 'markdown', '--to', 'rst', readme_path
    long_description = subprocess.check_output(args)
    long_description = long_description.decode()
except Exception as error:
    # Fallback to markdown (unformatted on PyPI) long_description
    print('README.md conversion to reStructuredText failed. Error:')
    print(error)
    with open(readme_path) as read_file:
        long_description = read_file.read()



setup(
    name='dipper',
    version='0.1.0',
    author='Kent Shefchek',
    author_email='kshefchek@gmail.com',
    url='https://github.com/monarch-initiative/dipper',
    description='Library for transforming data from open genomic databases to RDF',
    packages=find_packages(),
    license='BSD',
    install_requires=[
        'psycopg2', 'rdflib', 'isodate', 'roman', 'python-docx', 'pyyaml',
        'pysftp', 'beautifulsoup4', 'GitPython', 'intermine', 'pandas'],
    include_package_data=True,

    keywords='ontology graph obo owl sparql rdf',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Visualization'
    ],
    scripts=['./dipper.py']
)

