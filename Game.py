
import UI
import State

class Game:
    def __init__(self, title, width, height, fullscreen):
        print title, width, height, fullscreen
        self.ui = UI.UI()
        self.ui.init(width, height, fullscreen, title)
        self.stateManager = State.StateManager()

    def addState(self, state):
        state._manager = self.stateManager
        state._initUi(self.ui)
        # Only necessary because we're janking in the view above, and initialization requires a view...
        state.init()
        self.stateManager.addState(state)

    def run(self, stateName):
        self.stateManager.setCurrentState(stateName)
        while not self.ui.is_closed():
            self.stateManager.doTick()
