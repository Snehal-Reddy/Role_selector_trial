import math
from utils.config import *
from utils.geometry import *
from skills import skills_union
from skills import sGoToPoint
from skills import sGoToBall
from skills import sKickToPoint

class TClearer(object):
	def __init__(self, arg):
		super(TClearer, self).__init__()
	def getTargetPos(self,state,play=-1,number):
		return Vector2D(int(state.ballPos.x),int(state.ballPos.y))