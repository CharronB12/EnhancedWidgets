# -*- coding: utf-8 -*-
"""
Othala_setup.py
Created : 2019-05-29
Last update : 2022-02-24
MIT License

Copyright (c) 2021 Benjamin Charron (CharronB12)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from distutils.core import setup
from shutil import rmtree


import EnhancedWidgets
setup(name='EnhancedWidgets',
      version=EnhancedWidgets.__version__, #in init
      description=EnhancedWidgets.__doc__, #docstring at top of init
      author=EnhancedWidgets.__author__,
      author_email=EnhancedWidgets.__author_email__,
      url='https://github.com/CharronB12/EnhancedWidgets',
      packages=['EnhancedWidgets'],
      classifiers=[
        'Development Status :: Version 1 - Alpha',
        'Intended Audience :: myself',
        'License :: MIT',
        'Programming Language :: Python :: 3.8.8',
        'Topic :: advanced tkinter widgets',
        ],
      )

rmtree('build')



