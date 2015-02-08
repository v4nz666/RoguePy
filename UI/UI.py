'''
Documentation, License etc.

@package RoguePy
'''
import os
import sys
from RoguePy.libtcod import libtcod

class UI:
  _path = ''
  
  def __init__(self):
    self._rootPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    self._font = self._rootPath + b'/libtcod/lucida12x12_gs_tc.png'
    self._renderer = libtcod.RENDERER_GLSL;
  
  def init(self, w, h, fs):
    self.width = w
    self.height = h
    libtcod.console_set_custom_font(self._font, libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    libtcod.console_set_default_foreground(0, libtcod.white)
    libtcod.console_set_default_background(0, libtcod.black)
    libtcod.console_init_root(w, h, b'title', fs, self._renderer)
  
  def refresh(self, gameState):
    
    libtcod.console_flush()
  
  def is_closed(self):
    closed = libtcod.console_is_window_closed()
    return closed