import random
import config as cf

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.bench = []
        self.in_play = []
        self.offer = []
        self.gold = cf.starting_gold
        self.level = cf.starting_level
    
    def deal_summon(self, pool):
        draw_percent = cf.draw_percentages[self.level]
        random_tier = random.choices(list(draw_percent.keys()), weights=list(draw_percent.values()))
        tier_chosen = pool[random_tier[0] - 1]
        random.shuffle(tier_chosen)
        self.hand.append(tier_chosen.pop())
    
    def increase_level(self):
        self.level += 1

    def __repr__(self):
        return self.name

class AI(Player):
    def __repr__(self):
        return self.name
    
class Summon:
    def __init__(self, name, tier):
        self.name = name
        self.tier = tier
        self.cost = self.tier
    
    def __repr__(self):
        return f"{self.tier}{self.name}"

class Game:
    def __init__(self):
        self.pool = self.create_pool()
        self.players = self.add_players()

    def create_pool(self):
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
                tier5_summons.append(Summon(summon, 5))
        pool = [tier1_summons, tier2_summons, tier3_summons, tier4_summons, tier5_summons]
        return pool

    def add_players(self):
        players = []
        players.append(Player("Player"))
        for x in range(7):
            players.append(AI(f"AI {x+1}"))
        return players

def main():
    game = Game()
    
    print(len(game.pool[0]))
    print(len(game.pool[1]))
    for x in range(5): 
        game.players[0].deal_summon(game.pool)
    print(game.players[0].hand)
    for x in range(9):
        game.players[0].increase_level()
    for x in range(5):
        game.players[0].deal_summon(game.pool)
    print(game.players[0].hand)
    print(len(game.pool[0]))
    print(len(game.pool[1]))
    print(len(game.pool[2]))
    print(len(game.pool[3]))
    print(len(game.pool[4]))
    print(game.pool[4])
    print(game.players)
if __name__ == '__main__':
    main()
