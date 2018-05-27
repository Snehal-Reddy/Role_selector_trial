import math
from utils.config import *
from utils.geometry import *
from skills import skills_union
from skills import sGoToPoint
from skills import sGoToBall
from skills import sKickToPoint


#VERY IMPORTANT -
# take into consideration that there can be more than 2 attackers

class TAttacker(object):
	def __init__(self):
		super(TAttacker, self).__init__()
	def getTargetPos(self,state,play=-1):
		ballPos = Vector2D(int(state.ballPos.x), int(state.ballPos.y))
		x = ballPos.x
		y = ballPos.y
		finalPos = Vector2D(x,y)

        return finalPos
			