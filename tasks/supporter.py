import math
from utils.config import *
from utils.geometry import *
from skills import skills_union
from skills import sGoToPoint
from skills import sGoToBall
from skills import sKickToPoint

#VERY IMPORTANT -
# take into consideration that there can be more than 2 supporters

class TSupporter(object):
	def __init__(self):
		super(TSupporter, self).__init__()
	def getTargetPos(self,state,play=-1,number):
		pass
		