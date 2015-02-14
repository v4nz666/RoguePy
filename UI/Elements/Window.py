'''
Documentation, License etc.

@package RoguePy.UI
'''
from RoguePy.libtcod import libtcod
from RoguePy.UI import View
from RoguePy.UI.Elements import Frame


class Window(Frame):
  
  def __init__(self, x, y, w, h):
    super(Window, self).__init__(x, y, w, h)
    self.setTitle("")
    
  def setTitle(self, title):
    if len(title) > self.width-2:
      title = title[:self.width-2]
    self._title = title
  
  def draw(self):
    Frame.draw(self)
    libtcod.console_print(self.console, 1, 0, self._title)
    