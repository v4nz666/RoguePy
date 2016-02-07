import Map

class Entity:

    def __init__(self, map, x, y):
        c = map.getCell(x, y)
        if ( c.entity != None ):
            raise Exception("Entity already present in map cell (%d,%d)" % (x, y))
        c.entity = self
        self.map = map
        self.x = x
        self.y = y

    def tryMove(self, dx, dy):
        if self.canMove(dx, dy):
            self.map.getCell(self.x, self.y).entity = None
            self.x += dx
            self.y += dy
            self.map.getCell(self.x, self.y).entity = self
            return True
        else:
            print "Bonk! (%s)" % self.map.getCell(self.x + dx, self.y + dy).type
            return False

    def canMove(self, dx, dy):
        c = self.map.getCell(self.x + dx, self.y + dy)
        return abs(dx) <= 1 and abs(dy) <= 1 and self.canEnter(c)

    def canEnter(self, cell):
        return cell.entity == None and cell.type == 'floor'
