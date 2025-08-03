#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='pyurlquerycli',
      version='1.0',
      description='A simple script to interact with urlquery.net APIs from cli',
      long_description_content_type='text/markdown; charset=UTF-8;',
      long_description=open('./README.md').read(),
      url='https://github.com/maaaaz/pyurlquerycli',
      author='Thomas D.',
      author_email='tdebize@mail.com',
      license='LGPL',
      classifiers=[
        'Topic :: Security',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Programming Language :: Python :: 3'
      ],
      keywords='urlquery url malware phishing analyze sandbox',
      packages=find_packages(),
      install_requires=open('pyurlquerycli/requirements.txt').read().splitlines(),
      python_requires='>=3',
      entry_points={
        'console_scripts': ['pyurlquerycli=pyurlquerycli.pyurlquerycli:main'],
      },
      include_package_data=True)