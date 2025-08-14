import asteroid
from constants import *
import math

class Stats:
    def __init__(self, score=0, total_kills=0, sm_kills=0, med_kills=0, big_kills=0, total_shot=0):
        self.score = score
        self.kills = total_kills
        self.total_shot = total_shot
        self.sm_kills = sm_kills
        self.med_kills = med_kills
        self.big_kills = big_kills

    
    

    def got_kill(self, aster):
        if aster.radius == ASTEROID_MAX_RADIUS: 
            self.score += 3
            self.big_kills += 1
        elif aster.radius != ASTEROID_MIN_RADIUS:
            self.score += 2
            self.med_kills += 1
        else: 
            self.score += 1
            self.sm_kills += 1

        self.kills += 1

    def shot_bullet(self):
        self.total_shot += 1

    def get_final_score(self):
        return f"Total Final Score: {self.score} | Got a total of {self.kills} kills | {self.sm_kills} Were small, {self.med_kills} were medium, {self.big_kills} total were big targets.\n {self.total_shot} Bullets. Accuracy Rating of {math.floor((self.kills / self.total_shot) * 100)}%"
    
player_stats = Stats()