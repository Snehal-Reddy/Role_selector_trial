import enum

class gameAnalyzer():
	class staticPlays(enum.Enum):
		FreeHomeKick = 0
		FreeAwayKick = 1
		IndirectHomeKick = 2
		IndirectAwayKick = 3
		HomePenalty = 4
		AwayPenalty = 5

	def __init__(self, tasklist, state, play=None):
		# tasklist -> list of available tactics
		# state -> belief state
		# play -> static play, if it is None means we have decide it dynamically
		self.tasklist = tasklist
		self.state = state
		self.play = play
		self.home_yellow = state.isteamyellow

	def availableBots():
		# return list of available bots using state
		bots = []
		for i in xrange(len(state.homePos)):
			if state.homeDetected[i]:
				bots.append(i)

		return bots

	def targetPoints(tasks):
		# input -> list of tasks(Tactics)
		# ouput -> a dict, keyword -> tasks name, value -> their target point

		#assuming class names for tactics are TBallHandler , TMarker etc.
		task_dict = {'Defender':TDefender,'BallHandler':TBallHandler,'Marker':TMarker,'Supporter':TSupporter,'Attacker':TAttacker,'Distractor':TDistractor,'Clearer':TClearer}
		required_task_dict = {}
		for i in xrange(len(tasks)):
			obj = task_dict[tasks[i]]()
			required_task_dict[tasks[i]] = obj.getTargetPos(state,play)

		return required_task_dict

	def staticPlays():
		curPlay = -1
		for play in staticPlays:
			if play.value == self.play:
				curPlay = play.value
				break
		if curPlay > -1:
			if curPlay == 0:
				# our direct free Kick
				requiredTasks = ['BallHandler','Attacker','Supporter','Supporter','Defender']  # add more task here
				tasks = self.intersection(requiredTasks, self.tasklist)
				# task is dict, keyword -> tasks name, value -> their target point
				tasks = self.targetPoints(tasks)
				bots = self.availableBots()
				return tasks, bots

			elif curPlay == 1:
				# their direct free Kick
				requiredTasks = ['Distractor','Clearer','Marker','Marker','Defender']
				tasks = self.intersection(requiredTasks, self.tasklist)
				tasks = self.targetPoints(tasks)
				bots = self.availableBots()

			elif curPlay == 2:
				#our indirect free kick
				requiredTasks = ['BallHandler','Attacker','Supporter','Defender','Distractor']
				tasks = self.intersection(requiredTasks, self.tasklist)
				tasks = self.targetPoints(tasks)
				bots = self.availableBots()

			elif curPlay == 3:
				#their indirect free kick
				requiredTasks = ['Distractor','Defender','Marker','Marker','Defender']
				tasks = self.intersection(requiredTasks, self.tasklist)
				tasks = self.targetPoints(tasks)
				bots = self.availableBots()

			elif curPlay == 4:
				#our penalty
				requiredTasks = ['BallHandler','Attacker','Supporter','Distractor','Defender']
				tasks = self.intersection(requiredTasks, self.tasklist)
				# task is dict, keyword -> tasks name, value -> their target point
				tasks = self.targetPoints(tasks)
				bots = self.availableBots()

			elif curPlay == 5:
				#their penalty
				requiredTasks = ['Distractor','Clearer','Marker','Marker','Defender']
				tasks = self.intersection(requiredTasks, self.tasklist)
				# task is dict, keyword -> tasks name, value -> their target point
				tasks = self.targetPoints(tasks)
				bots = self.availableBots()

		else:
			print("this static play is not available!!")

	def dynamicPlays():
		ballPos = Vector2D(int(state.ballPos.x), int(state.ballPos.y))
		if state.ball_in_our_possession :

			#clearing under complete defence 
			if ballPos.x < -4500 + OUR_DBOX_MAXX:
				#ball in our D
				if ballPos.y < OUR_DBOX_MAXY + 200 and ballPos.y > OUR_DBOX_MINY - 200 :
					requiredTasks = ['Distractor','Clearer','Marker','Defender','Defender']
					tasks = self.intersection(requiredTasks, self.tasklist)
					# task is dict, keyword -> tasks name, value -> their target point
					tasks = self.targetPoints(tasks)
					bots = self.availableBots()
				#ball not in our D but still very close to goal
				else:
					requiredTasks = ['Distractor','Attacker','Marker','Defender','Defender']
					tasks = self.intersection(requiredTasks, self.tasklist)
					# task is dict, keyword -> tasks name, value -> their target point
					tasks = self.targetPoints(tasks)
					bots = self.availableBots()


			#prepare for attack
			elif ballPos.x < 1000  and ballPos.x > -1000 :
				requiredTasks = ['Distractor','Defender','Attacker','Supporter','Defender']
				tasks = self.intersection(requiredTasks, self.tasklist)
				# task is dict, keyword -> tasks name, value -> their target point
				tasks = self.targetPoints(tasks)
				bots = self.availableBots()

			#attack
			elif ballPos.x > 1000 and ballPos.x < 4500 - OUR_DBOX_MAXX:
				requiredTasks = ['Distractor','Distractor','Attacker','Supporter','Defender']
				tasks = self.intersection(requiredTasks, self.tasklist)
				# task is dict, keyword -> tasks name, value -> their target point
				tasks = self.targetPoints(tasks)
				bots = self.availableBots()	

			#complete attack
			elif ballPos.x > 4500 - OUR_DBOX_MAXX :
				requiredTasks = ['Distractor','Supporter','Attacker','Supporter','Defender']
				tasks = self.intersection(requiredTasks, self.tasklist)
				# task is dict, keyword -> tasks name, value -> their target point
				tasks = self.targetPoints(tasks)
				bots = self.availableBots()	

			#neutral play in our half
			else:
				requiredTasks = ['Distractor','Distractor','Attacker','Supporter','Defender']
				tasks = self.intersection(requiredTasks, self.tasklist)
				# task is dict, keyword -> tasks name, value -> their target point
				tasks = self.targetPoints(tasks)
				bots = self.availableBots()		





