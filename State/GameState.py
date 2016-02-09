'''
GameState
'''
from RoguePy import Input
from RoguePy import UI
from TickHandler import TickHandler


class GameState(object):
  def __init__(self, name, manager = None):
    self.name = name
    self.manager = manager
    self.inputHandler = Input.KeyboardHandler()

    self.tickHandlers = {}
    self.handlerQueue = []
    self.view = None

    self.focused = None

  def initView(self, ui):
    self.view = UI.View(ui)
  
  @property
  def name(self):
    return self.__name
  @name.setter
  def name(self,name):
    self.__name = name
  
  @property
  def manager(self):
    return self.__manager
  @manager.setter
  def manager(self,manager):
    self.__manager = manager
  
  @property
  def inputHandler(self):
    return self.__inputHandler
  @inputHandler.setter
  def inputHandler(self, h):
    if isinstance(h, Input.InputHandler):
      self.__inputHandler = h

  @property
  def view(self):
    return self.__view
  @view.setter
  def view(self,view):
    self.__view = view

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

  def processInput(self):
    inputs = {}
    if self.view.inputsEnabled:
      inputs.update(self.view.getInputs())
    if self.focused is not None:
      inputs.update(self.focused.getInputs())
    self.inputHandler.setInputs(inputs)
    self.inputHandler.handleInput()

  def setFocus(self, el):
    self.focused = el

  def blur(self):
    self.focused = None

  def beforeLoad(self):
    pass
  def beforeUnload(self):
    pass
