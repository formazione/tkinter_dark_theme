
# coding: utf-8

'''
this modile provide a function that switch tk style to 'azure dark'
'''

import os
import tkinter.ttk

def apply_theme(widget):
	'''load and set 'azure dark' theme to a tk widget'''
	widget.tk.call('source', os.path.join(os.path.dirname(__file__), 'azure dark.tcl'))
	tkinter.ttk.Style(widget).theme_use('azure')

