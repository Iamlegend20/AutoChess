import random

class Player:
    def __init__(self):
        self.hand = []
        self.bench = []
        self.gold = 5

class Summon:
    def __init__(self, name, tier):
        self.name = name
        self.tier = tier
        self.cost = self.tier
    def __repr__(self):
        return self.name

def create_pool():
    pool = []
    tier1_summons = ['Ramuh', 'Shiva', 'Ifrit', 'Carbuncle', 'Cactuar', 'Chocobo', 'Tonberry']
    tier2_summons = ['Leviathan', 'Titan', 'Pheonix', 'Siren', 'Diablos', 'Odin', 'Alexander']
    tier3_summons = ['Bahamut', 'Eden', 'Anima', 'Knights of Round', 'Zodiark']
    for summon in tier1_summons:
        for x in range(10):
            pool.append(Summon(summon, 1))
    for summon in tier2_summons:
        for x in range(8):
            pool.append(Summon(summon, 2))
    for summon in tier3_summons:
        for x in range(6):
            pool.append(Summon(summon, 3))
    return pool
                    
pool = create_pool()        
