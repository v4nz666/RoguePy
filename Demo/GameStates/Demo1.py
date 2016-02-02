'''
DemoOne GameState
'''
import RoguePy.State.GameState as GameState
from RoguePy.libtcod import libtcod
from RoguePy.UI import Elements

class Demo1(GameState):
  
  def __init__(self,name, manager, ui):
    super(self.__class__, self).__init__(name, manager, ui)
    
    self._setupView()
    self._setupInputs()
  
  ###
  # Initialisation
  ###
  
  def _setupView(self):
    
    view = self.getView()
    
    self.element = self.view.addElement(Elements.Element(0, 0, view.width, view.height))
    self.element.draw = self.draw
    
    self.view.addElement(Elements.Label(3, self.view.height - 1, "ESC - Quit"))
    self.view.addElement(Elements.Label(35, self.view.height - 1, "Spc - Next"))
    
  def draw(self):
    title = "View and Elements"
    x = self.element.width / 6
    y = self.element.height / 4
    w = x * 4
    h = y * 2
    str = \
      "The fundamental part of the UI is the View. It represents the entire visible screen. " + \
      "You can build up an interface using different Elements. You may create a basic Element " + \
      "object, and use the libtcod drawing functions to draw directly to its console. Create " + \
      "your object and, replace its draw() method with one of your own. The element's console " + \
      "will be cleared, and your draw method will be called, every time you call your state " + \
      "manager's doTick() method."
    
    libtcod.console_print(self.element.console, (self.element.width - len(title)) / 2, y - 2, title)
    libtcod.console_print_rect(self.element.console, x, y, w, h, str)
    
  def _setupInputs(self):
    self.view.setInputs({
      'quit': {
        'key':libtcod.KEY_ESCAPE,
        'ch': None,
        'fn': self.quit
      },
      'step': {
        'key':libtcod.KEY_SPACE,
        'ch': None,
        'fn': self.next
      }
    })
  
  ###
  # Input callbacks
  ###
  
  def next(self):
    self._manager.setNextState('demo2')
  def quit(self):
    self._manager.setNextState('quit')
