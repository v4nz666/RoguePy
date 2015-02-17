'''
Documentation, License etc.

@package RoguePy.UI
'''
from RoguePy.libtcod import libtcod
from RoguePy.UI.Elements import Element

class Label(Element):
  
  def __init__(self, x, y, label=""):
    super(Label, self).__init__(x, y, len(label), 1)
    self._label = label
  
  def setLabel(self, label):
    self.label = label
  def getLabel(self):
    return self._label
  
  def draw(self):
    libtcod.console_print(self.console, 0, 0, self._label)
      