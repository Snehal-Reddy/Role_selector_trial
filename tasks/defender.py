import math
from utils.config import *
from utils.geometry import *
from skills import skills_union
from skills import sGoToPoint
from skills import sGoToBall
from skills import sKickToPoint

#VERY IMPORTANT -
# take into consideration that there can be more than 2 defenders

class TDefender(object):
	def __init__(self):
		super(TDefender, self).__init__()

	def getTargetPos(self,state,play=-1):
        #blocking potential shots to goal
		ballPos = Vector2D(int(state.ballPos.x), int(state.ballPos.y))
		attacker_id = state.opp_bot_closest_to_ball
        attacker_pos = Vector2D (int(state.awayPos[attacker_id].x),int(state.awayPos[attacker_id].y))
		x = -HALF_FIELD_MAXX+DBOX_WIDTH+BOT_RADIUS
        if (ballPos.x-attacker_pos.x) != 0 :
            y = ballPos.y + (ballPos.y-attacker_pos.y)*abs((-HALF_FIELD_MAXX+2*BOT_RADIUS-ballPos.x)/(ballPos.x-attacker_pos.x))
        else :
            y = ballPos.y
        y = min(y,OUR_GOAL_MAXY - BOT_RADIUS)
        y = max(y,OUR_GOAL_MINY + BOT_RADIUS)
        if y - OUR_GOAL_MINY <= 2*BOT_RADIUS :
            y = y + 4.4*BOT_RADIUS
        elif OUR_GOAL_MAXY - y <= 2*BOT_RADIUS :
            y = y - 1.7*BOT_RADIUS
        else :
            y = y + 2.4*BOT_RADIUS
        finalPos = Vector2D(x,y)

        return finalPos