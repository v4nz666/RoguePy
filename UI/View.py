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
    self._inputs = {}
    
    self._storedEnabled = None
    self.console = libtcod.console_new(self.width, self.height)
    self.inputsEnabled = True
  
  def getElements(self):
    return self._elements
  
  def getConsole(self):
    return self.console
  
  def addElement(self, el):
    if el.x + el.width >= self.width:
      el.width = self.width - el.x
    if el.y + el.height>= self.height:
      el.height = self.height- el.y
    
    self._elements.append(el)
    return el
  
  def setInputs(self, inputs):
    self._inputs = inputs
  def getInputs(self):
    return self._inputs
  
  def storeState(self):
    self._storedEnabled = []
    index = 0
    for e in self._elements:
      if e.enabled:
        self._storedEnabled.append(index)
      index = index + 1
  def restoreState(self):
    if not self._storedEnabled:
      raise Exception("You must call storeState() before calling restoreState.")
    for index in self._storedEnabled:
      self._elements[index].enable()
  
  def disableAll(self):
    for e in self._elements:
      e.disable()
    self.disableInputs()
  
  def enableInputs(self):
    self.inputsEnabled = True
  def disableInputs(self):
    self.inputsEnabled = False
  
  def getActiveInputs(self, _inputs={}, el=None):
    if el == None:
      el = self
      inputs = {}
    else:
      inputs = _inputs
    if ( ( el == self ) or ( el.visible and el.enabled ) ):
      if el == self and self.inputsEnabled or el != self:
        newInputs = el.getInputs()
        inputs.update(newInputs)
        
      for e in el.getElements():
        self.getActiveInputs(inputs, e)
    if el == self:
      return inputs
  
  def setDefaultForeground(self, fg, cascade=False):
    libtcod.console_set_default_foreground(self.console,fg)
    if cascade:
      for e in self._elements:
        e.setDefaultForeground(fg, True)
  def setDefaultBackground(self, bg, cascade=False):
    libtcod.console_set_default_background(self.console,bg)
    if cascade:
      print "cascading"
      for e in self._elements:
        e.setDefaultBackground(bg, True)
  #TODO Convert fg, bg to a tuple
  def setDefaultColors(self, fg = libtcod.white, bg = libtcod.black, cascade=False):
    self.fg = fg
    self.bg = bg
    self.setDefaultForeground(fg, cascade)
    self.setDefaultBackground(bg, cascade)
  
  def getDefaultColors(self):
    return (self.fg, self.bg)
  
  def clearConsole(self):
    libtcod.console_clear(self.console)
  
  def renderElements(self):
    for e in self._elements:
      e.clearConsole()
      if not e.visible:
        continue
      e.draw()
      e.renderElements()
      if not e.enabled:
        self.renderOverlay(e)
      libtcod.console_blit(e.getConsole(), 0, 0, e.width, e.height, self.console, e.x, e.y)

  
  def renderOverlay(self, el):
    con = libtcod.console_new(el.width, el.height)
    libtcod.console_set_default_background(con, libtcod.black)
    libtcod.console_blit(con, 0, 0, el.width, el.height, el.console, 0, 0, 0.0, 0.4)
    