from utils.geometry import Vector2D
from itertools import combinations
from itertools import permutations

"""
botL --> list of available botID's
taskD --> Dictionary with keys as taks names and values as the position to go ( as an object of the class Vector2D )
"""

class optimalAssignment(object):
    def __init__(self, state, botL, taskD):
        self.Mat = self.assign(state, botL, taskD)

    def assign( self, state, botL, taskD):
        Mat = {}
        for x in botL:
            Mat[x] = {}
            botPos = Vector2D(state.homePos[x].x, state.homePos[x].y)
            for y in taskD.keys():
                Mat[x][y] = botPos.dist(taskD[y])
        return Mat
    def decider( self, botL, taskD):
        no_of_bot = len(botL)
        no_of_task = len(taskD)
        # no_of_bot >= no_of_task .... inherent assumption in the STOx's paper
        # thus exhaustion is optimal as no_of_bot <= 6
        bot_Comb = list(combinations(botL, no_of_task))
        task_Comb = list(permutations(taskD.keys(), no_of_task))
        min_val = 99999
        for x in bot_Comb:
            for y in task_Comb:
                comb = zip(x, y)
                comb.sort( key = lambda a : self.Mat[a[0]][a[1]] )
                if min_val > self.Mat[comb[-1][0]][comb[-1][1]]:
                    min_val = self.Mat[comb[-1][0]][comb[-1][1]]
                    bot_comb_index = bot_Comb.index(x)
                    task_comb_index = task_Comb.index(y)
                    s = 0
                    for t in comb:
                        s = s + self.Mat[t[0]][t[1]]
                    sum_of_val = s
                elif min_val == self.Mat[comb[-1][0]][comb[-1][1]]:
                    s = 0
                    for t in comb:
                        s = s + self.Mat[t[0]][t[1]]
                    if s < sum_of_val:
                        bot_comb_index = bot_Comb.index(x)
                        task_comb_index = task_Comb.index(y)
                        sum_of_val = s
                    else:
                        pass
                else:
                    pass
        return zip(bot_Comb[bot_comb_index], task_Comb[task_comb_index])
