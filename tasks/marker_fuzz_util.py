import sys
import rospy
from krssg_ssl_msgs.msg import BeliefState
from krssg_ssl_msgs.msg import gr_Commands
import thread
import time
from std_msgs.msg import Int8
from utils.geometry import Vector2D
import math 
from utils.config import *
from utils.geometry import *
RATIO = MAX_BALL_SPEED*1.0/MAX_BOT_SPEED

# UTILITY FILE FOR FUZZY_ULTRA
class pass_analysis(object):
	
	def __init__(self, bot_id, state):
		self.bot_id = bot_id

	def line( self, opp, bot_id, reciever_id, state):
		if (state.awayPos[bot_id].x - state.awayPos[reciever_id].x) != 0:
			slope = (state.awayPos[bot_id].y - state.awayPos[reciever_id].y)*1.0/(state.awayPos[bot_id].x - state.awayPos[reciever_id].x)
		else:
			return math.fabs((state.awayPos[bot_id].x-state.homePos[opp].x)*1.0/(state.awayPos[bot_id].y - state.awayPos[reciever_id].y))
		up = math.fabs((state.homePos[opp].y - state.awayPos[bot_id].y) - slope*(state.homePos[opp].x - state.awayPos[bot_id].x))
		low = (1 + slope**2)**0.5
		return up*1.0/low		

	def evr_params( self, state, reciever_id, bp, rp, sp):
		global RATIO
		ourteam = [x for x in xrange(6)]
		botPos = bp
		recieverPos = rp
		sep = sp
		nearness_ratio = -1
		intercept_ratio = -1
		count1 = 0
		count2 = 0
		print "#"*50
		print "PLAYER: ", reciever_id, "     in_line_dist     sep    sep_from_rival      perp_dist     in_line_dist2"
		for player in ourteam:
			distance = botPos.dist(Vector2D(state.homePos[player].x, state.homePos[player].y))
			distance2 = recieverPos.dist(Vector2D(state.homePos[player].x, state.homePos[player].y))
			if distance2 > HALF_FIELD_MAXX*0.5 and distance > HALF_FIELD_MAXX*0.75:
				continue
			dist = self.line(player, self.bot_id, reciever_id, state)
			in_line_dist = (distance**2-dist**2)**(0.5)
			in_line_dist2 = (distance2**2-dist**2)**(0.5)
			if in_line_dist > sep or in_line_dist2 > sep:
				if nearness_ratio < sep*1.0/distance2:
					nearness_ratio = sep*1.0/distance2
				if sep*1.0/distance2 > RATIO*0.75:
					count1 = count1 + 1
			else:
				if intercept_ratio < in_line_dist*1.0/dist:
					intercept_ratio = in_line_dist*1.0/dist
				# if self.prod(in_line_dist, dist, sep) < 0:
				# 	count2 = count2 + 1
			print "DETAILS--> ",player, in_line_dist, sep, distance2, dist, in_line_dist2
		if intercept_ratio == -1 and nearness_ratio == -1:
			return 0.1, 0
		if intercept_ratio > 400.0/27:
			intercept_ratio = 400.0/27
		if nearness_ratio > 400.0/27:
			nearness_ratio = 400.0/27
		if intercept_ratio > nearness_ratio:
			return intercept_ratio, count1+count2
		else:
			return nearness_ratio, count2+count1

