import math
from utils.config import *
from utils.geometry import *
from skills import skills_union
from skills import sGoToPoint
from skills import sGoToBall
from skills import sKickToPoint




class TAttacker(object):
	def __init__(self):
		super(TAttacker, self).__init__()
	def getTargetPos(self,state,play):
		ballPos = Vector2D(int(state.ballPos.x), int(state.ballPos.y))
		x = ballPos.x
		y = ballPos.y
		finalPos = Vector2D(x,y)

        return finalPos
			