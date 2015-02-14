'''
Documentation, License etc.

@package RoguePy.UI
'''
from RoguePy.libtcod import libtcod
from RoguePy.UI import View

class Element(View):
  #TODO we should be calling View.__init__  :/
  def __init__(self, x, y, w, h):
    self.x = x
    self.y = y
    self.width = w
    self.height = h
    
    self.active = True
    
    self.console = libtcod.console_new(w, h)
    
    self.setDefaultColors()
    self.clearConsole()
    
    self._elements = []
    self._inputs = {}
    
  def draw(self):
    pass
  
  def toggleActive(self):
    self.active = not self.active
  