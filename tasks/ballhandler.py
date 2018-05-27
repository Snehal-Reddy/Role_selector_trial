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
	def getTargetPos(self,state,play=-1):
		#taking a free kick or penalty
		if play == 0 or play ==4 or play ==2:
			return Vector2D(state.ballPos.x,state.ballPos.y)	
		

		