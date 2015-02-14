'''
Documentation, License etc.

@package RoguePy.UI
'''
from RoguePy.libtcod import libtcod
from RoguePy.UI import View

class Element(View):
  def __init__(self, x, y, w, h):
    self.x = x
    self.y = y
    self.width = w
    self.height = h
    
    self.active = True
    
    self._console = libtcod.console_new(w, h)
    
    self.setDefaultColors()
    self.clearConsole()
    
    self._elements = []
    self._inputs = {}
    
  def draw(self):
    pass
  
  def toggleActive(self):
    self.active = not self.active
  