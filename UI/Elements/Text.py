'''
Documentation, License etc.

@package RoguePy.UI
'''
from RoguePy.libtcod import libtcod
from RoguePy.UI import Element

class Text(Element):
  
  def __init__(self, x, y, w, h, text):
    super(Text, self).__init__(x, y, w, h)
    self._text = text
  
  def draw(self):
    libtcod.console_print_rect(self._console, 0, 0, self.width, self.height, self._text)
