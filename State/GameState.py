'''
GameState
'''
from RoguePy import Input
from RoguePy import UI

class GameState(object):
  def __init__(self, name, manager, ui):
    self._name = name
    self._manager = manager
    self._inputHandler = None
    self._view = UI.View(ui)
  
  def getName(self):
    return self._name
  
  def getView(self):
    return self._view
  
  def setBlocking(self, blocking):
    if blocking:
      self._inputHandler = Input.BlockingKeyboardHandler()
    else:
      self._inputHandler = Input.NonBlockingKeyboardHandler()
  
  def getInputHandler(self):
    return self._inputHandler
  
  ######
  # The good stuff
  ######
  def tick(self):
    pass
  
  def processInput(self):
    if isinstance(self._inputHandler, Input.InputHandler):
      inputs = self._view.getActiveInputs()
      self._inputHandler.setInputs(inputs)
      self._inputHandler.handleInput()
  