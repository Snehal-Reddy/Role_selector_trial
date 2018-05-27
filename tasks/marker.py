import math
from utils.config import *
from utils.geometry import *
from skills import skills_union
from skills import sGoToPoint
from skills import sGoToBall
from skills import sKickToPoint
import marker_fuzz

class TMarker(object):
	def __init__(self):
		super(TMarker, self).__init__()
	def getTargetPos(self,state):
		#fuzzy logic for opponents
        ballPos = Vector2D(int(state.ballPos.x), int(state.ballPos.y))
        attacker_id = state.opp_bot_closest_to_ball
        p = get_all(state,attacker_id)
        x = (state.awayPos[attacker_id].x)*0.9 + (ballPos.x)*0.1
        y = (state.awayPos[attacker_id].y)*0.9 + (ballPos.y)*0.1

        finalPos = Vector2D(x,y)

        return finalPos