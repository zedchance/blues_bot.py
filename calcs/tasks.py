# Slayer task calculator

from helpers.hiscore import Hiscore
from calcs.experience import level_to_xp, LEVEL_99

class Tasks(Hiscore):
    """ Calculates the estimated slayer tasks left to level up """
    
    def __init__(self, username, tasks):
        super().__init__(username)
        self.tasks = int(tasks)
    
    def xp_needed_to_level_up(self):
        """ Returns xp needed to level up """
        return level_to_xp(self.slayer_level + 1) - self.slayer_xp
    
    def avg_xp_per_task(self):
        """ Returns average xp per task """
        return self.slayer_xp // self.tasks
    
    def tasks_to_level_up(self):
        """ Returns tasks needed to level up based on average """
        return self.xp_needed_to_level_up() // self.avg_xp_per_task()
    
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