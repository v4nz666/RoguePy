from RoguePy.libtcod import libtcod
from RoguePy.UI.Elements import Element
from collections import namedtuple
from .. import Colors

CellView = namedtuple('CellView', ['char', 'fg', 'bg'])

class Map(Element):
  def __init__(self, x, y, w, h, _map):
    super(Map, self).__init__(x, y, w, h)
    self._map = _map
    self._offsetX = 0
    self._offsetY = 0
    self.halfW = self.width / 2
    self.halfH = self.height / 2

  def center(self, x, y):
    """
    Centers the view-port of the ui element around coordinates x, y of the map. If the coordinate is near the edge of
    the map, the actual center of the view-port will differ from those passed in. 
    
    See also: onScreen() - Return the onscreen coordinates of a given x, y pair accounting for centering.
    
    :param x: X coordinate to center view around
    :param y: Y coordinate to center view around
    :return: self
    """
    if x < self.halfW:
      self._offsetX = 0
    elif x < self._map.width - self.halfW:
      self._offsetX = x - self.halfW
    else:
      self._offsetX = self._map.width - self.width
    
    if y < self.halfH:
      self._offsetY = 0
    elif y < self._map.height - self.halfH:
      self._offsetY = y - self.halfH
    else:
      self._offsetY = self._map.height - self.height
    self.setDirty()
    return self


  def onScreen(self, x, y):
    """
    Return the onscreen coordinates of a given x, y pair accounting for centering.

    :param x: int   The actual map X coordinate to calculate the onscreen coordinate of.
    :param y: int   The actual map X coordinate to calculate the onscreen coordinate of.
    :return: tuple  Adjusted (x, y) coordinates
    """
    return (x - self._offsetX, y - self._offsetY)
  
  def draw(self):
    for sy in range(self.height):
      for sx in range(self.width):
        x = sx + self._offsetX
        y = sy + self._offsetY
        if (x >= 0 and x < self._map.width and y >= 0 and y < self._map.height):
          c = self._map.getCell(x, y)
          cv = self.cellToView(c)
          libtcod.console_put_char_ex(self.console, sx, sy, cv.char, cv.fg, cv.bg)

    self.setDirty(False)

  def cellToView(self, c):
    result = CellView(c.terrain.char, c.terrain.fg, c.terrain.bg)
    if c.entity != None:
      result = CellView(c.entity.ch, c.entity.fg, result.bg)
    elif c.items:
      pass
    return result
