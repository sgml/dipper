#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name='Dipper',
      version='1.0',
      description='Data Ingest Pipeline',
      packages=find_packages(),
      install_requires=['psycopg2', 'rdflib', 'isodate', 'roman', 'python-docx', 'pyyaml']
      )