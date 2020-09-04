import random

class Player:
    def __init__(self):
        self.hand = []
        self.bench = []
        self.gold = 5
        self.level = 1
        self.draw_percentages = {'1':80, '2':20, '3':0, '4':0, '5':0} 
    def deal_summon(self, pool):
        tier_selection = random.choices(list(self.draw_percentages), weights=list(self.draw_percentages.values()))
        self.hand.append(random.choice(pool[int(tier_selection[0]) - 1]))
        
                      
class Summon:
    def __init__(self, name, tier):
        self.name = name
        self.tier = tier
        self.cost = self.tier
    def __repr__(self):
        return self.name

def create_pool():
    tier1_summon_names = ['Bomb', 'Flan', 'Cockatrice', 'Funguar', 'Goblin', 'Lamia', 'Basilisk', 'Ahirman', 'Coeurl']
    tier2_summon_names = ['Chocobo', 'Tonberry', 'Cactuar', 'Behemoth', 'Iron Giant', 'Marlboro', 'Ochu', 'Adamantoise']
    tier3_summon_names = ['Ramuh', 'Shiva', 'Ifrit', 'Carbuncle', 'Siren', 'Valefor', 'Titan']
    tier4_summon_names = ['Leviathan', 'Pheonix', 'Diablos', 'Odin', 'Alexander', 'Doomtrain']
    tier5_summon_names = ['Bahamut', 'Eden', 'Anima', 'Knights of the Round', 'Zodiark']
    tier1_summons=[]
    tier2_summons=[]
    tier3_summons=[]
    tier4_summons=[]
    tier5_summons=[]
    for summon in tier1_summon_names:
        for x in range(20):
            tier1_summons.append(Summon(summon, 1))
    for summon in tier2_summon_names:
        for x in range(18):
            tier2_summons.append(Summon(summon, 2))
    for summon in tier3_summon_names:
        for x in range(16):
            tier3_summons.append(Summon(summon, 3))
    for summon in tier4_summon_names:
        for x in range(14):
            tier4_summons.append(Summon(summon, 4))
    for summon in tier5_summon_names:
        for x in range(12):
            tier5_summons.append(Summon(summon, 3))
    pool = [tier1_summons, tier2_summons, tier3_summons, tier4_summons, tier5_summons]
    return pool

def main():
    player1 = Player()                    
    pool = create_pool()
    for x in range(5): player1.deal_summon(pool)
    print(player1.hand)

if __name__ == '__main__':
    main()
