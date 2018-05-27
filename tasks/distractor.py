import math
from utils.config import *
from utils.geometry import *
from skills import skills_union
from skills import sGoToPoint
from skills import sGoToBall
from skills import sKickToPoint

number_of_distractors = 0

class TDistractor(object):
	def __init__(self, arg):
		super(TDistractor, self).__init__()
		self.arg = arg
	def getTargetPos(self,state):
		global number_of_distractors 
		number_of_distractors=number_of_distractors+1
		x = 0
		y = pow(-1,number_of_distractors)*1300*number_of_distractors
		finalPos = Vector2D(x,y)

		return finalPos