
"""
This is a test file for optimalAssignment
"""

from utils.geometry import Vector2D
from optimalAssignment import *


botL = [1,2,3,4,5]
taskD = { 't1': Vector2D(500,500), 't2': Vector2D(1000,1000), 't3': Vector2D(2000,2000) }

obj = optimalAssignment(state, botL, taskD) 
print obj.decider(botL, taskD)
