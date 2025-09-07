import pygame

from stats import player_stats
from constants import *

class Upgrades():
    def __init__(self, speed=False, fire_rate=False, double_shot=False):
        self.speed = speed
        self.fire_rate = fire_rate
        self.double_shot = double_shot

    def Unlock(self, type):
        if type == 'speed':
            self.speed = True
        if type == 'fire_rate':
            self.fire_rate = True
        if type == 'double_shot':
            self.double_shot = True

    def CheckMilestone(self):
        if player_stats.kills >= FASTER_FIRE_RATE_UNLOCK and upgrades_obj.fire_rate == False:
            upgrades_obj.Unlock('fire_rate')
        if player_stats.kills >= UPGRADED_PLAYER_SPEED_UNLOCK and upgrades_obj.speed == False:
            upgrades_obj.Unlock('speed')
        if player_stats.kills >= PLAYER_DOUBLE_SHOT_UNLOCK and upgrades_obj.double_shot == False:
            upgrades_obj.Unlock('double_shot')

upgrades_obj = Upgrades()