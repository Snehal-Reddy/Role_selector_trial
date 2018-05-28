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
	def getTargetPos(self,state,play=-1,number):
		ballPos = Vector2D(int(state.ballPos.x), int(state.ballPos.y))
		goalPos  = Vector2D(-HALF_FIELD_MAXX,0)
		Ball_handler_threshold = 0.08
		#update with new rules
		Ball_handler_distance_free_kick = 500

		#taking a free kick or penalty
		if play == 0 or play ==4 or play ==2:
			return Vector2D(state.ballPos.x,state.ballPos.y)	

		# block shots but maintain distance
		elif play == 1 or play == 3:
			x = ballPos.x + Ball_handler_distance_free_kick*((goalPos.x - ballPos.x)/ballPos.dist(goalPos))
			y = ballPos + Ball_handler_distance_free_kick*((goalPos.y - ballPos.y)/ballPos.dist(goalPos))
			finalPos = Vector2D(x,y)

			return finalPos

		#block shots standing close to ball
		else:
			x = ballPos.x + Ball_handler_threshold*(goalPos.x - ballPos.x)
			y = ballPos + Ball_handler_threshold*(goalPos.y - ballPos.y)
			finalPos = Vector2D(x,y)

			return finalPos

		