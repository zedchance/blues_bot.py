# Slayer task calculator

from helpers.hiscore import Hiscore
from calcs.experience import xp_to_next_level, level_to_xp, LEVEL_99

class Tasks():
    """ Calculates the estimated slayer tasks left to level up """
    
    def __init__(self, username, tasks):
        self.username = username
        self.tasks = int(tasks)
        user = Hiscore(username)
        self.slayer_level = int(user.slayer_level)
        self.slayer_xp = int(user.slayer_xp)
    
    def avg_xp_per_task(self):
        """ Returns average xp per task """
        return self.slayer_xp // self.tasks
    
    def tasks_to_level_up(self):
        """ Returns tasks needed to level up based on average """
        xp_needed = level_to_xp(self.slayer_level + 1) - self.slayer_xp
        return xp_needed // self.avg_xp_per_task()
    
    def tasks_to_level_99(self):
        """ Returns approx tasks needed to reach level 99 slayer """
        xp_needed = LEVEL_99 - self.slayer_xp
        return xp_needed // self.avg_xp_per_task()
    
    def estimated_total_tasks(self):
        """ Returns approx number of total tasks """
        return self.tasks_to_level_99() + self.tasks

# Test code
# blue = Tasks(bluetrane, 550)
# print("Avg:", blue.avg_xp_per_task())
# print("Tasks needed:", blue.tasks_to_level_up())