"""
DemoFive GameState
"""

from RoguePy.Map.Map import Map
from RoguePy.Map.Terrain import Terrain
from RoguePy.Map.Entity import Entity
from RoguePy.Map import terrains

import RoguePy.State.GameState as GameState
from RoguePy.libtcod import libtcod
from RoguePy.UI import Elements

class Demo5(GameState):

  def __init__(self,name, manager):

    super(self.__class__, self).__init__(name, manager)

    self.addHandler('updateUi', 1, self.updateUi)

    grid = [
      "               XXXXXXXXX ",
      "  XXXXXX   XXXXX-------X ",
      "  X----XXXXX---X-------X ",
      "  X------------X-------X ",
      "  X----XXXXX---X-------X ",
      "  XX-XXX   X---XXXXXX-XX ",
      "   X-X     X---X    X-X  ",
      "   X-X     XXX-X  XXX-X  ",
      " XXX-XXXXXXX X-XXXX---X  ",
      " X---------X X--------X  ",
      " X--~~~~---X XXXXXX---X  ",
      " X---------X      XXXXX  ",
      " XXXXXXXXXXX             ",
      ]

    water = Terrain(True, False, 'Pool of water') \
      .setChar('~') \
      .setColors(libtcod.blue, libtcod.darker_blue)

    # This initialises a new empty map
    self.map = Map(len(grid[0]), len(grid))

    statue = Entity('Golden Statue')
    statue.setChar('&')
    statue.setColor(libtcod.gold)

    self.map.addEntity(statue, 20, 9)

    for y in range(len(grid)):
      row = grid[y]
      for x in range(len(row)):
        char = row[x]

        if char == "X":
          self.map.getCell(x, y).setTerrain(terrains.WALL)
        elif char == "-":
          self.map.getCell(x, y).setTerrain(terrains.FLOOR)
        elif char == "~":
          self.map.getCell(x, y).setTerrain(water)
        else:
          self.map.getCell(x, y).setTerrain(terrains.EMPTY)


  def beforeLoad(self):
    self._setupView()
    self._setupInputs()
    self.selectedX = 0
    self.selectedY = 0

  def _setupView(self):

    frame = Elements.Frame(0, 0, self.view.width, self.view.height)
    frame.setTitle("The Map")
    self.view.addElement(frame)
    frame.addElement(Elements.Label(3, frame.height - 1, "ESC - Quit"))
    frame.addElement(Elements.Label(35, frame.height - 1, "Spc - Next"))
    self.frame = frame

    str = \
      "The Map Element, along with the RoguePy.Map package allow you to easily define and display " + \
      "the game world. The Map Element allows you to draw a portion of the map, centered around a " + \
      "given coordinate, and allows you to easily navigate between on-map and on-screen coordinates.\n\n" + \
      "Maps are fundamentally made up of terrain. There are a few pre-made terrain definitions EMPTY, " + \
      "WALL, and FLOOR for instance) but you may add as many as you like. Each terrain type has " + \
      "a character, fg and bg color, and may be transparent and/or passable.\n\n"
    str2 = \
      "Move the + around with the arrow keys, and examine the different terrain types.\n\n" + \
      "The crosshair effect is achieved by adding a raw Element to the Map element, setting the " + \
      "background opacity to 0, then simply drawing the + at the onscreen coordinates each frame."

    self.view.addElement(Elements.Text(1, 2, 30, 20, str))
    self.view.addElement(Elements.Text(1, 23, 46, 8, str2))


    self.mapFrame = self.frame.addElement(Elements.Frame(32, 2, 15, 15)).setTitle('Map')
    self.mapElement = self.mapFrame.addElement(Elements.Map(1, 1, 13, 13, self.map))
    self.mapOverlay = self.mapElement.addElement(Elements.Element(0, 0, 13, 13))
    self.mapOverlay.bgOpacity = 0
    self.mapOverlay.draw = self.drawOverlay

    self.fpsLabel = self.mapFrame.addElement(Elements.Label(8, 0, ""))

    self.cellLabel = self.frame.addElement(Elements.Label(32, 18, ""))
    self.cellDesc = self.frame.addElement(Elements.Text(32, 20, 14, 1)).setDefaultColors(libtcod.darker_green)
    self.cellItems = self.frame.addElement(Elements.List(32, 21, 14, 1)).setDefaultColors(libtcod.gold)

  def _setupInputs(self):
    self.view.setInputs({
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
    })
    self.mapElement.setInputs({
      'selectionUp': {
        'key': libtcod.KEY_UP,
        'ch' : None,
        'fn' : self.moveSelectionUp
      },
      'selectionDn': {
        'key': libtcod.KEY_DOWN,
        'ch' : None,
        'fn' : self.moveSelectionDown
      },
      'selectionLeft': {
        'key': libtcod.KEY_LEFT,
        'ch' : None,
        'fn' : self.moveSelectionLeft
      },
      'selectionRight': {
        'key': libtcod.KEY_RIGHT,
        'ch' : None,
        'fn' : self.moveSelectionRight
      }
    })

  ###
  # Game Loop stuff
  ###

  def updateUi(self):
    m = self.mapElement
    m.center(self.selectedX, self.selectedY)
    self.updateCellDesc()
    self.updateCellItems()
    self.fpsLabel.setLabel("FPS:" + str(libtcod.sys_get_fps()))

  def drawOverlay(self):
    onScreen = self.mapElement.onScreen(self.selectedX, self.selectedY)
    self.mapOverlay.clear()
    self.mapOverlay.putCh(onScreen[0], onScreen[1], '+', libtcod.light_green, libtcod.black)

  def updateCellDesc(self):
    self.cellLabel.setLabel('Cell:' + str((self.selectedX, self.selectedY)))
    cellTerrain = self.map.getTerrain(self.selectedX, self.selectedY)
    self.cellDesc.setText(cellTerrain.desc)
  def updateCellItems(self):
    items = self.map.getCell(self.selectedX, self.selectedY).entities
    itemNames = []

    for i in range(len(items)):
      itemNames.append(items[i].name)
    self.cellItems.setItems(itemNames)


  ###
  # Input callbacks
  ###

  def moveSelectionUp(self):
    if self.selectedY > 0:
      self.selectedY -= 1

  def moveSelectionDown(self):
    if self.selectedY < self.map.height - 1:
      self.selectedY += 1

  def moveSelectionLeft(self):
    if self.selectedX > 0:
      self.selectedX -= 1

  def moveSelectionRight(self):
    if self.selectedX < self.map.width - 1:
      self.selectedX += 1

  def next(self):
    self._manager.setNextState('demo1')
  def quit(self):
    self._manager.setNextState('quit')