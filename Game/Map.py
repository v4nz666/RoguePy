
from .. import UI

class Map:
    def __init__(self, path):
        f = open(path)
        h = 0
        self.cells = []
        for line in f:
            # Minus one to account for newline.
            # TODO: Ensure all lines are the same length.
            w = len(line) - 1
            # TODO: Temporary hackishness.
            self.width = w
            for ch in line[:-1]:
                self.cells.append(self.charToCell(ch))
            h = h + 1
        self.height = h

    def getCell(self, x, y):
        # TODO: Bounds checking.
        return self.cells[x + y * self.width]

    def charToCell(self, ch):
        cell = {
            '#' : Cell('wall'),
            '.' : Cell('floor'),
        }.get(ch)
        if cell == None:
            raise Exception("Unknown cell token '" + ch + "'")
        return cell

class Cell:
    def __init__(self, type):
        self.type = type
        self.terrain = CellType.All[type]
        self.entities = []
        pass

class CellType:
    def __init__(self, char, fg, bg):
        self.char = char
        self.fg = fg
        self.bg = bg

CellType.All = {
    'wall'  : CellType('X', UI.Colors.Grey, UI.Colors.Black),
    'floor' : CellType('.', UI.Colors.Grey, UI.Colors.Black),
}

