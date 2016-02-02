"""
ui-test-bed
"""
import sys
sys.path.append('../..')
import RoguePy
import GameStates

# Never want to exceed 60fps
RoguePy.setFps(60)
ui = RoguePy.UI.UI()
ui.init(48, 32, False)

stateManager = RoguePy.State.StateManager()
stateManager.ui = ui

s_splash = GameStates.SplashScreen('splash', stateManager)
s_demo1 = GameStates.Demo1('demo1', stateManager)
s_demo2 = GameStates.Demo2('demo2', stateManager)
s_demo3 = GameStates.Demo3('demo3', stateManager)
s_demo4 = GameStates.Demo4('demo4', stateManager)
s_demo5 = GameStates.Demo5('demo5', stateManager)
s_quit = GameStates.Quit('quit', stateManager)

stateManager.addState(s_splash)
stateManager.addState(s_demo1)
stateManager.addState(s_demo2)
stateManager.addState(s_demo3)
stateManager.addState(s_demo4)
stateManager.addState(s_demo5)
stateManager.addState(s_quit)

stateManager.setCurrentState('splash')

while not ui.is_closed():
  stateManager.doTick()

  
  
