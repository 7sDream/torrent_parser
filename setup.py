#!/usr/bin/env python
# coding=utf-8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import torrent_parser

setup(
    name='torrent_parser',
    keywords=['file', 'torrent', 'JSON', 'parser'],
    version=torrent_parser.__version__,
    py_modules=['torrent_parser'],
    url='https://github.com/7sDream/torrent_parser',
    license='MIT',
    author='7sDream',
    author_email='7seconddream@gmail.com',
    description='A .torrent file parser for both Python 2 and 3',
    install_requires=[],
    entry_points={
        'console_scripts': ['pytp=torrent_parser:__main']
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Multimedia',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
