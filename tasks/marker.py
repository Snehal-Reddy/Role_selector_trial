import math
from utils.config import *
from utils.geometry import *
from skills import skills_union
from skills import sGoToPoint
from skills import sGoToBall
from skills import sKickToPoint
import marker_fuzz

#VERY IMPORTANT -
# take into consideration that there can be more than 2 markers

class TMarker(object):
	def __init__(self):
		super(TMarker, self).__init__()
	def getTargetPos(self,state,play=-1,number,fuzzy_list):
		#fuzzy logic for opponents
		ballPos = Vector2D(int(state.ballPos.x), int(state.ballPos.y))
		oppPos = Vector2D(state.awayPos[fuzzy_list[number]].x,state.awayPos[fuzzy_list[number]].y)
		
		x = ballPos.x*0.1 + 0.9*oppPos.x
		y = ballPos.y*0.1 + 0.9*oppPos.y

		finalPos = Vector2D(x,y)

		return finalPos