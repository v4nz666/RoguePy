'''
Documentation, License etc.

@package RoguePy.UI
'''
from RoguePy.libtcod import libtcod

class View(object):

  def __init__(self, ui):
    self.x = 0
    self.y = 0
    self.width = ui.getWidth()
    self.height = ui.getHeight()
    
    self._elements = []
    
    self._console = libtcod.console_new(self.width, self.height)
  
  def getElements(self):
    return self._elements
  
  def getConsole(self):
    return self._console
  
  def addElement(self, el):
    self._elements.append(el)
    return el
  
  def setDefaultColors(self, fg = libtcod.white, bg = libtcod.black):
    libtcod.console_set_default_foreground(self._console,fg)
    libtcod.console_set_default_background(self._console,bg)
  
  def clearConsole(self):
    libtcod.console_clear(self._console)
  
  def renderElement(self, el, drawToSelf=True):
    el.draw()
    print "rendering " + str(vars(el))
    for e in el.getElements():
      self.renderElement(e, False)
      print "RECURSE rendering " + str(vars(e))
      print "blitting e.console to " + str((e.x, e.y)) + " on " + str(el.getConsole())
      libtcod.console_blit(e.getConsole(), 0, 0, e.width, e.height, el.getConsole(), e.x, e.y)
    if drawToSelf:
      print "blitting el.console to " + str((el.x, el.y)) + " on " + str(self._console)
      libtcod.console_blit(el.getConsole(), 0, 0, el.width, el.height, self._console, el.x, el.y)