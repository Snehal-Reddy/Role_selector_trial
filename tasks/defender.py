import math
from utils.config import *
from utils.geometry import *
from skills import skills_union
from skills import sGoToPoint
from skills import sGoToBall
from skills import sKickToPoint
import marker_fuzz

#VERY IMPORTANT -
# take into consideration that there can be more than 2 defenders

class TDefender(object):
	def __init__(self):
		super(TDefender, self).__init__()

	def getTargetPos(self,state,play=-1,number,fuzzy_list):
		#blocking potential shots to goal
		goalPos  = Vector2D(-HALF_FIELD_MAXX,0)
		oppPos = Vector2D(state.awayPos[fuzzy_list[number]].x,state.awayPos[fuzzy_list[number]].y)

		x = goalPos.x*0.1 + 0.9*oppPos.x
		y = goalPos.y*0.1 + 0.9*oppPos.y

		finalPos = Vector2D(x,y)

		return finalPos