import math
from utils.config import *
from utils.geometry import *
from skills import skills_union
from skills import sGoToPoint
from skills import sGoToBall
from skills import sKickToPoint


#VERY IMPORTANT -
# take into consideration that there can be more than 2 Distractors

class TDistractor(object):
	def __init__(self, arg):
		super(TDistractor, self).__init__()
		self.arg = arg
	def getTargetPos(self,state,play=-1,number):
		x = 0
		y = 1300
		finalPos = Vector2D(x,y)

		return finalPos