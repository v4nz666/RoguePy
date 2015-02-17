'''
MenuItem Element

@package RoguePy.UI
'''
from RoguePy.libtcod import libtcod
from RoguePy.UI.Elements import List
from RoguePy.UI.Elements import MenuItem

class Menu(List):
  
  def __init__(self, x, y, w, h, menuItems={}):
    
    self.selected = 0
    
    self.menuItems = []
    itemStrings = []
    _y = 0
    for i in menuItems:
      label = i.keys()[0]
      fn = i[label]
      
      #if self.align == CENTER:
      _x = (w - len(label)) / 2
      #elif self.align == LEFT:
      #x = 0
      self.menuItems.append(MenuItem(_x, _y, label, fn))
      itemStrings.append(label)
    
    self.setWrap(True)
    
    super(Menu, self).__init__(x, y, w, h, itemStrings)
  
  def setWrap(self, wrap):
    self._wrap = wrap
  def getWrap(self):
    return self._wrap
  
  def selectFn(self):
    # Call the associated callback, and pass the index that's just been selected.
    self.menuItems[self.selected].fn(self.selected)
  
  def selectUp(self):
    self._moveSelect(-1)
    
  def selectDown(self):
    self._moveSelect(1)
  
  def _moveSelect(self, step):
    newIndex = self.selected + step
    if self._wrap:
      if newIndex < 0:
        newIndex = len(self.menuItems ) + step
      elif newIndex >= len(self.menuItems):
        newIndex = 0
    else:
      if newIndex < 0:
        newIndex = 0
      elif newIndex >= len(self.menuItems):
        newIndex = len(self.menuItems) + step
    self.selected = newIndex
    
    if self.selected + self._offset > self.height - 1:
      self.scrollDown()
    elif self.selected < self._offset:
      self.scrollUp()
    
  
  def draw(self):
    super(Menu, self).draw()
    y = self.selected - self._offset
    for x in range(len(self.menuItems[self.selected].getLabel())):
      selectedFg = libtcod.console_get_char_background(self.console, x, y)
      selectedBg = libtcod.console_get_char_foreground(self.console, x, y)
      libtcod.console_set_char_foreground(self.console, x, y, selectedFg)
      libtcod.console_set_char_background(self.console, x, y, selectedBg) 