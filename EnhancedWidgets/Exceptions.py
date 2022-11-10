# -*- coding: utf-8 -*-

"""
EnhancedWidgets.Exceptions.py
Created : 2019-06-14
Last update : 2022-02-24
MIT License

Copyright (c) 2022 Benjamin Charron (CharronB12)

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

Contains exceptions used within the EnhancedWidgets module

Content
------
class Tracker(previous=(['Status Tracker is ready'], 1, ['[1] Status Tracker is ready']))
    Creates a tkinter-like widget where entries can easily be displayed to a user,
    including error codes and warning color-coded.
    
"""

class EW_FutureError(Exception):
    """
    Used to mark coding pathways in developement or planned for futur implementation.
    """
    pass


class EW_PlaceholderError(Exception):
    """
    Used for errors that do not have a specific name yet.  
    """
    pass

class EW_InputError(Exception):
    """
    Used for errors that do not have a specific name yet.  
    """
    pass