'''
GameState
'''
from RoguePy import Input
from RoguePy import UI
from TickHandler import TickHandler


class GameState(object):
  def __init__(self, name, manager, ui):
    self._name = name
    self._manager = manager
    self.inputHandler = Input.KeyboardHandler()

    self.tickHandlers = {}
    self.handlerQueue = []

    self.view = UI.View(ui)
    self.ui = ui

  @property
  def inputHandler(self):
    return self.__inputHandler

  @inputHandler.setter
  def inputHandler(self, h):
    if isinstance(h, Input.InputHandler):
      self.__inputHandler = h

  def getName(self):
    return self._name
  
  def getView(self):
    return self.view

  def addHandler(self, name, interval, handler):
    if not name in self.tickHandlers:
      self.tickHandlers[name] = TickHandler(interval, handler)
  def removeHandler(self, name):
    self.handlerQueue.append(name)

  def purgeHandlers(self):
    for name in self.handlerQueue:
      if name in self.tickHandlers:
        del self.tickHandlers[name]
    self.handlerQueue = []

  ######
  # The good stuff
  ######
  def processInput(self):
    inputs = self.view.getActiveInputs()
    self.inputHandler.setInputs(inputs)
    self.inputHandler.handleInput()
  
  def beforeLoad(self):
    pass
  def beforeUnload(self):
    pass
