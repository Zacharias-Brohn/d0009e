import sys
import os
script_dir = os.path.dirname(__file__)
mymodule_path = os.path.join(script_dir,'..')
sys.path.insert(1, mymodule_path)
import Lab2.bounce
import Lab2.derivative

