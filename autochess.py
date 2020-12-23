import random
import config as cf

class Player:
    def __init__(self):
        self.hand = []
        self.bench = []
        self.gold = cf.starting_gold
        self.level = cf.starting_level
    def deal_summon(self, pool):
        """Choices accpets lists as arguments so we convert the dictionary to lists of the
        appropriate type, values and keys. It also returns a list of the single number
        selected so we need to use [0] at the end to grab just the integer 1-5. This could be
        reduced to a line or two but I chose to break it out to make it easier to read.
        """
        draw_percent = cf.draw_percentages[self.level]
        random_tier = random.choices(list(draw_percent.keys()), weights=list(draw_percent.values()))
        tier_chosen = pool[random_tier[0] - 1]
        random.shuffle(tier_chosen)
        self.hand.append(tier_chosen.pop())
    def increase_level(self):
        self.level += 1
                      
class Summon:
    def __init__(self, name, tier):
        self.name = name
        self.tier = tier
        self.cost = self.tier
    def __repr__(self):
        return f"{self.tier}{self.name}"

def create_pool():
    tier1_summons=[]
    tier2_summons=[]
    tier3_summons=[]
    tier4_summons=[]
    tier5_summons=[]
    for summon in cf.tier1_summon_names:
        for x in range(cf.tier1_summon_quantity):
            tier1_summons.append(Summon(summon, 1))
    for summon in cf.tier2_summon_names:
        for x in range(cf.tier2_summon_quantity):
            tier2_summons.append(Summon(summon, 2))
    for summon in cf.tier3_summon_names:
        for x in range(cf.tier3_summon_quantity):
            tier3_summons.append(Summon(summon, 3))
    for summon in cf.tier4_summon_names:
        for x in range(cf.tier4_summon_quantity):
            tier4_summons.append(Summon(summon, 4))
    for summon in cf.tier5_summon_names:
        for x in range(cf.tier5_summon_quantity):
            tier5_summons.append(Summon(summon, 3))
    pool = [tier1_summons, tier2_summons, tier3_summons, tier4_summons, tier5_summons]
    return pool

def main():
    player1 = Player()                    
    pool = create_pool()
    print(len(pool[0]))
    print(len(pool[1]))
    for x in range(5): 
        player1.deal_summon(pool)
    print(player1.hand)
    player1.increase_level()
    for _ in range(5):
        player1.deal_summon(pool)
    print(player1.hand)
    print(len(pool[0]))
    print(len(pool[1]))
if __name__ == '__main__':
    main()
