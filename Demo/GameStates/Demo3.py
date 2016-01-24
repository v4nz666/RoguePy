'''
DemoThree GameState
'''
import RoguePy.State.GameState as GameState
from RoguePy.libtcod import libtcod
from RoguePy.UI import Elements

class Demo3(GameState):
 
  def __init__(self,name, manager, ui):
    super(self.__class__, self).__init__(name, manager, ui)
   
    self.setBlocking(True)
    self._setupView()
    self._setupInputs()
    
 
  ###
  # Initialisation
  ###
 
  def _setupView(self):
   
    frame = Elements.Frame(0, 0, self.view.width, self.view.height)
    frame.setTitle("Interactive elements")
    self.frame = frame
    self.view.addElement(frame)
    frame.addElement(Elements.Label(3, frame.height - 1, "ESC - Quit"))
    frame.addElement(Elements.Label(35, frame.height - 1, "Spc - Next"))
    
    str = \
      "The Menu element accepts list of dicts. Each key is an item in the menu, and the values " + \
      "are callbacks. The callback will be called when the user selects an option, and will be " + \
      "passed the index of the item that was selected. Press Up/Down/Enter to select a backgroud " + \
      "color for the main frame Element and all of its children.\n\n" + \
      "Sliders allow the user to choose a value within a specified range, and call a callback when " + \
      "their selected value changes.\n\n" + \
      "Press R, G, or B to select the appropriate slider, and the left and right arrows to adjust " + \
      "the values. The sliders' values range from 0 to 255."
    
    halfX = self.view.width / 2
    halfY = self.view.height / 2
    self.frame.addElement(Elements.Text(2, 2, self.view.width - 4, halfY + 1, str))
    
    str2 = \
      "Press TAB to pop up a modal dialog. Modal elements disable all other elements when their " + \
      "show() method is called. Control is returned when the modal's hide() method is called. " + \
      "You must pass your view object to the show and hide methods so the modal may trigger " + \
      "it to disable the other elements."
    self.frame.addElement(Elements.Text(14, halfY + 4, 32, 10, str2))
    
    menuItems = [
      {'Black' : self.menuOnSelect},
      {'White' : self.menuOnSelect},
      {'Red'   : self.menuOnSelect},
      {'Blue'  : self.menuOnSelect},
      {'Green' : self.menuOnSelect}
    ]
    self.menuFrame = self.frame.addElement(Elements.Frame(1, halfY + 4, 12, 6))
    self.menuFrame.setTitle("Bg Color")
    self.menu = self.menuFrame.addElement(Elements.Menu(1, 1, 10, 4, menuItems))
    
    self.sliderFrame = self.frame.addElement(Elements.Frame(1, halfY + 10, 12, 5))
    self.sliderFrame.setTitle("Fg Color")
    
    self.labelR = self.sliderFrame.addElement(Elements.Label(1,1,"R"))
    rVal = libtcod.console_get_default_foreground(self.frame.console).r
    self.sliderR = self.sliderFrame.addElement(Elements.Slider(3, 1, 8, 0, 255, rVal, 8))
    self.sliderR.onChange = self.changeForeground
    
    self.labelG = self.sliderFrame.addElement(Elements.Label(1,2,"G"))
    gVal = libtcod.console_get_default_foreground(self.frame.console).g
    self.sliderG = self.sliderFrame.addElement(Elements.Slider(3, 2, 8, 0, 255, gVal, 8))
    self.sliderG.onChange = self.changeForeground
    self.sliderG.disable()
    
    self.labelB = self.sliderFrame.addElement(Elements.Label(1,3,"B"))
    bVal = libtcod.console_get_default_foreground(self.frame.console).b
    self.sliderB = self.sliderFrame.addElement(Elements.Slider(3, 3, 8, 0, 255, bVal, 8))
    self.sliderB.onChange = self.changeForeground
    self.sliderB.disable()
    
    modalText = \
      "The Modal element is simply a wrapper. It has no visual components, but allows you to nest " + \
      "Elements within it. The inputs associated with the modal, and its descendants, will be the " + \
      "only ones processed while the modal is visible. You must bind the Input associated with " + \
      "the modal's hide() method directly to the modal element, rather than, say to the View as " + \
      "even Inputs bound directly to the View are unavailable when a modal is present.\n\n" + \
      "Notice how Space and ESC are no longer available. You may proceed once you've closed this " + \
      "modal and thus re-enabled the View-bound Inputs."
    
    modalX = halfX / 4 - 1
    modalY = halfY / 4
    modalW = halfX * 3 / 2 + 2
    modalH = halfY * 3 / 2
    
    self.modal = self.view.addElement(Elements.Modal(modalX, modalY, modalW, modalH))
    self.modaleFrame = self.modal.addElement(Elements.Frame(0, 0, modalW, modalH))
    self.modaleFrame.setTitle("Modal Elements")
    self.modalText = self.modal.addElement(Elements.Text(2, 2, modalW - 4, modalH - 4, modalText))
    self.modalLabel  = self.modal.addElement(Elements.Label(3, modalH - 1, "TAB - Back"))
    self.modal.onClose = self.modalClosed
    
    
  def _setupInputs(self):
    self.frame.setInputs({
      'quit': {
        'key': libtcod.KEY_ESCAPE,
        'ch' : None,
        'fn' : self.quit
      },
      'step': {
        'key': libtcod.KEY_SPACE,
        'ch' : None,
        'fn' : self.next
      },
      'showModal': {
        'key': libtcod.KEY_TAB,
        'ch' : None,
        'fn' : self.toggleModal
      }
    })
    
    self.modal.setInputs({
      'showModal': {
        'key': libtcod.KEY_TAB,
        'ch' : None,
        'fn' : self.toggleModal
      }
    })
    
    self.menu.setInputs({
      'menuScrollUp': {
        'key' : libtcod.KEY_UP,
        'ch'  : None,
        'fn'  : self.menu.selectUp
      },
      'menuScrollDn': {
        'key' : libtcod.KEY_DOWN,
        'ch'  : None,
        'fn'  : self.menu.selectDown
      },
      'menuSelect': {
        'key' : libtcod.KEY_ENTER,
        'ch'  : None,
        'fn'  : self.menu.selectFn
      }
    })
    
    self.sliderFrame.setInputs({
      'selectR': {
        'key': None,
        'ch' : "r",
        'fn' : self.selectR
      },
      'selectG': {
        'key': None,
        'ch' : "g",
        'fn' : self.selectG
      },
      'selectB': {
        'key': None,
        'ch' : "b",
        'fn' : self.selectB
      }
    })
    
    self.sliderR.setInputs({
      'sliderR-left': {
        'key' : libtcod.KEY_LEFT,
        'ch'  : None,
        'fn'  : self.sliderR.left
      },
      'sliderR-right': {
        'key' : libtcod.KEY_RIGHT,
        'ch'  : None,
        'fn'  : self.sliderR.right
      }
    })
    
    self.sliderG.setInputs({
      'sliderG-left': {
        'key' : libtcod.KEY_LEFT,
        'ch'  : None,
        'fn'  : self.sliderG.left
      },
      'sliderG-right': {
        'key' : libtcod.KEY_RIGHT,
        'ch'  : None,
        'fn'  : self.sliderG.right
      }
    })
    
    self.sliderB.setInputs({
      'sliderB-left': {
        'key' : libtcod.KEY_LEFT,
        'ch'  : None,
        'fn'  : self.sliderB.left
      },
      'sliderB-right': {
        'key' : libtcod.KEY_RIGHT,
        'ch'  : None,
        'fn'  : self.sliderB.right
      }
    })
  
  ###
  # Input callbacks
  ###

  def menuOnSelect(self, index):
    if index == 0:
      self.frame.setDefaultBackground(libtcod.black, True)
    elif index == 1:
      self.frame.setDefaultBackground(libtcod.white, True)
    elif index == 2:
      self.frame.setDefaultBackground(libtcod.red, True)
    elif index == 3:
      self.frame.setDefaultBackground(libtcod.green, True)
    elif index == 4:
      self.frame.setDefaultBackground(libtcod.blue, True)
  
  def changeForeground(self):
    r = self.sliderR.getVal()
    g = self.sliderG.getVal()
    b = self.sliderB.getVal()
    color = libtcod.Color(r, g, b)
    self.frame.setDefaultForeground(color, True)
  
  def selectR(self):
    self.sliderR.enable()
    self.sliderG.disable()
    self.sliderB.disable()
  def selectG(self):
    self.sliderR.disable()
    self.sliderG.enable()
    self.sliderB.disable()
  def selectB(self):
    self.sliderR.disable()
    self.sliderG.disable()
    self.sliderB.enable()
  
  def toggleModal(self):
    if self.modal.enabled:
      self.modal.hide(self.view)
    else:
      self.modal.show(self.view)
  def modalClosed(self):
    print "Called back from Modal onClose"

  def next(self):
    self._manager.setNextState('demo4')
  def quit(self):
    self._manager.setNextState('quit')