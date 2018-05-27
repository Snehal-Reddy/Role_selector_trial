import math
from utils.config import *
from utils.geometry import *
from skills import skills_union
from skills import sGoToPoint
from skills import sGoToBall
from skills import sKickToPoint


class TBallHandler(object):
	def __init__(self, arg):
		super(TBallHandler, self).__init__()
		self.arg = arg
	def getTargetPos(self,state,play):
		#attacking a free kick
		if play == 0 or play ==4:
			return Vector2D(state.ballPos.x,state.ballPos.y)	
		#if we are defending a free kick
		if play == 1:
		    ballPos = Vector2D(int(state.ballPos.x), int(state.ballPos.y))
		    return Vector2D(0.3*ballPos.x + 0.7*4500,0.3*ballPos.y)

		