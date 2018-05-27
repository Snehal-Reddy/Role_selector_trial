import gameAnalyzer
import optimalAssignment

play = 0


def bs_callback():
	global play 
	task_list = ['Defender','BallHandler','Marker','Supporter','Attacker','Distractor','Clearer']
	obj = GameAnalyser(task_list,state,play)

def refree_callback(msg):
 	global play
 	if (self.home_yellow and msg.command == 8) or ((not self.home_yellow) and msg.command == 9) :
 		#our direct freekick
 		play = 0
 	elif msg.command == 8 or msg.command == 9 :
 		#their direct freekick
 		play = 1
 	elif (self.home_yellow and msg.command == 10) or ((not self.home_yellow) and msg.command == 11) :
 		#our indirect freekick
 		play = 2
 	elif msg.command == 10 or msg.command == 11 :
 		#their indirect free kick
 		play = 3
 	elif (self.home_yellow and msg.command == 6) or ((not self.home_yellow) and msg.command == 7) :
 		#our penalty
 		play = 4
 	elif msg.command == 6 or msg.command == 7 :
 		#their penalty
 		play = 5

def main():
    global pub
    rospy.Subscriber('/ref_data',Refree,obj.refree_callback,queue_size=1000)
    rospy.Subscriber('/belief_state', BeliefState, bs_callback, queue_size=1000)
    rospy.spin()

if __name__=='__main__':
    # rospy.init_node('skill_py_node',anonymous=False)
    main()
