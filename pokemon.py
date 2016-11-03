import pygame, math, random
from pokemon_types import *


class Move():
    all_moves = []
    def __init__(self, power, name, move_type, contact, priority=0, effect=None):

        self.power = power
        self.name = name
        self.type = move_type
        self.contact = contact
        if self.contact == "physical":
            self.contact_image = pygame.image.load('images/physical.png')
        elif self.contact == "special":
            self.contact_image = pygame.image.load('images/special.png')
        self.priority = priority
        self.effect = effect
        Move.all_moves.append(self)

class Hidden_Power(Move):

    def __init__(self, move_type):
        Move.__init__(self, power=60, name="Hidden Power", move_type = move_type, contact="special")

# Normal
double_edge = Move(120, "Double Edge", Normal, "physical", 0, "recoil")
fake_out = Move(40, "Fake Out", Normal, "physical", 3, "flinch")
feint = Move(30, "Feint", Normal, "physical", 2)
quick_attack = Move(40, "Quick Attack", Normal, "physical", 1)
extreme_speed = Move(40, "Extreme Speed", Normal, "physical", 2)
tri_attack = Move(80, "Tri Attack", Normal, "special")
mega_kick = Move(120, "Mega Kick", Normal, "physical")
boomburst = Move(140, "Boomburst", Normal, "special")
tackle = Move(50, "Return", Normal, "physical")
scratch = Move(40, "Scratch", Normal, "physical")
thrash = Move(90, "Return", Normal, "physical")
hyper_voice = Move(90, "Hyper Voice", Normal, "special")
Return = Move(102, "Return", Normal, "physical")
### F I G H T
drain_punch = Move(75, "Drain Punch", Fight, "physical", 0, "drain")
mach_punch = Move(40, "Mach Punch", Fight, "physical", 1)
vacuum_wave = Move(40, "Vacuum Wave", Fight, "special", 1)
sky_uppercut = Move(85, "Sky Uppercut", Fight, "physical")
jump_kick = Move(100, "Jump Kick", Fight, "physical")
cross_chop = Move(100, "Cross Chop", Fight, "physical")
hidden_power_fight = Hidden_Power(Fight)
brick_break = Move(75, "Brick Break", Fight, "physical")
#### F L Y I N G
brave_bird = Move(120, "Brave Bird", Flying, "physical", 0, "recoil")
air_cutter = Move(60, "Air Cutter", Flying, "special")
hurricane = Move(110, "Hurricane", Flying, "special")
hidden_power_flying = Hidden_Power(Flying)
aeroblast = Move(100, "Aeroblast", Flying, "special")
air_slash = Move(75, "Air Slash", Flying, "special")
aerial_ace = Move(60, "Aerial Ace", Flying, "physical")
drill_peck = Move(80, "Drill Peck", Flying, "physical")
### P O I S O N
sludge_wave = Move(95, "Sludge Wave", Poison, "special")
sludge_bomb = Move(90, "Sludge Bomb", Poison, "special")
poison_jab = Move(80, "Poison Jab", Poison, "physical")
# Ground
drill_run = Move(80, "Drill Run", Ground, "physical")
hidden_power_ground = Hidden_Power(Ground)
earthquake = Move(100, "Earthquake", Ground, "physical")
earth_power = Move(90, "Earth Power", Ground, "special")
#### R O C K
stone_edge = Move(100, "Stone Edge", Rock, "physical")
hidden_power_rock = Hidden_Power(Rock)
power_gem = Move(80, "Power Gem", Rock, "special")
ancient_power = Move(60, "Ancient Power", Rock, "special")
rock_slide = Move(75, "Rock Slide", Rock, "physical")
#### B U G
u_turn = Move(70, "U-Turn", Bug, "physical", 0, "switch")
megahorn = Move(120, "Megahorn", Bug, "physical")
bug_buzz = Move(90, "Bug Buzz", Bug, "special")
signal_beam = Move(75, "Signal Beam", Bug, "special")
x_scissor = Move(80, "X-Scissor", Bug, "physical")
# Ghost
shadow_sneak = Move(40, "Shadow Sneak", Ghost, "physical", 1)
shadow_ball = Move(80, "Shadow Ball", Ghost, "special")
shadow_claw = Move(70, "Shadow Claw", Ghost, "physical")
shadow_punch = Move(60, "Shadow Punch", Ghost, "physical")
### S T E E L
bullet_punch = Move(40, "Bullet Punch", Steel, "physical", 1)
steel_wing = Move(70, "Steel Wing", Steel, "physical")
iron_head = Move(80, "Iron Head", Steel, "physical")
flash_cannon = Move(80, "Flash Cannon", Steel, "special")
iron_tail = Move(100, "Iron Tail", Steel, "physical")
#### F I R E
flare_blitz = Move(120, "Flare Blitz", Fire, "physical", 0, "recoil")
heat_wave = Move(95, "Heat Wave", Fire, "special")
blaze_kick = Move(85, "Blaze Kick", Fire, "physical")
flame_wheel = Move(60, "Flame Wheel", Fire, "physical")
fire_fang = Move(65, "Fire Fang", Fire, "physical")
hidden_power_fire = Hidden_Power(Fire)
fire_punch = Move(75, "Fire Punch", Fire, "physical")
flamethrower = Move(90, "Flamethrower", Fire, "special")
#### W A T E R
aqua_jet = Move(40, "Aqua Jet", Water, "physical", 1)
crabhammer = Move(100, "Crabhammer", Water, "physical")
razor_shell = Move(75, "Razor Shell", Water, "physical")
aqua_tail = Move(90, "Aqua Tail", Water, "physical")
water_gun = Move(40, "Water Gun", Water, "special")
waterfall = Move(80, "Waterfall", Water, "physical")
surf = Move(90, "Surf", Water, "special")
hidden_power_water = Hidden_Power(Water)
### G R A S S
wood_hammer = Move(120, "Wood Hammer", Grass, "physical", 0, "recoil")
magical_leaf = Move(60, "Magical Leaf", Grass, "special")
power_whip = Move(120, "Power Whip", Grass, "physical")
seed_bomb = Move(80, "Seed Bomb", Grass, "physical")
hidden_power_grass = Hidden_Power(Grass)
leaf_blade = Move(90, "Leaf Blade", Grass, "physical")
energy_ball = Move(90, "Energy Ball", Grass, "special")
### E L E C T R I C
volt_tackle = Move(120, "Volt Tackle", Electric, "physical", 0, "recoil")
wild_charge = Move(90, "Wild Charge", Electric, "physical", 0, "recoil")
spark = Move(65, "Spark", Electric, "physical")
thunderbolt = Move(90, "Thunderbolt", Electric, "special")
thunder_punch = Move(75, "Thunder Punch", Electric, "physical")
thunder_fang = Move(65, "Thunder Fang", Electric, "physical")
# Psychic
zen_headbutt = Move(80, "Zen Headbutt", Psychic, "physical")
psychic = Move(90, "Psychic", Psychic, "special")
### I C E
ice_shard = Move(40, "Ice Shard", Ice, "special", 1)
icicle_spear = Move(87, "Icicle Spear", Ice, "physical")
hidden_power_ice = Hidden_Power(Ice)
ice_punch = Move(75, "Ice Punch", Ice, "physical")
ice_beam = Move(90, "Ice Beam", Ice, "special")
ice_fang = Move(65, "Ice Fang", Ice, "physical")
### D R A G O N
dragon_rush = Move(100, "Dragon Rush", Dragon, "physical")
dragon_pulse = Move(70, "Dragon Pulse", Dragon, "special")
dragon_claw = Move(80, "Dragon Claw", Dragon, "physical")
#### D A R K
sucker_punch = Move(80, "Sucker Punch", Dark, "physical", 1, "sucker_punch")
night_slash = Move(70, "Night Slash", Dark, "physical")
dark_pulse = Move(80, "Dark Pulse", Dark, "special")
hidden_power_dark = Hidden_Power(Dark)
bite = Move(60, "Bite", Dark, "physical")
crunch = Move(80, "Crunch", Dark, "physical")
# Fairy
hidden_power_fairy = Hidden_Power(Fairy)
moonblast = Move(95, "Moonblast", Fairy, "special")
dazzling_gleam = Move(80, "Dazzling Gleam", Fairy, "special")
play_rough = Move(90, "Play Rough", Fairy, "physical")

def stat_calc(base_stat, points=0):
    stat = (2 * base_stat + points) + 18
    return stat
def hp_calc(base_stat, points=0):
    hp = (2 * base_stat + points) + 34
    return hp


class Pokemon():

    All_Pokemon = []
    Pokeball = pygame.image.load('images/pokeball.png')
    icon_x = pygame.image.load('images/icon_x.png')

    def __init__(self, health, attack, defense, special_attack, special_defense, speed,
    ptype1, name, front_image, back_image, ptype2=None):

        self.base_health = health
        self.base_attack = attack
        self.base_defense = defense
        self.base_special_attack = special_attack
        self.base_special_defense = special_defense
        self.base_speed = speed
        self.max_health = hp_calc(health)
        self.current_health = self.max_health
        self.attack = stat_calc(attack)
        self.defense = stat_calc(defense)
        self.special_attack = stat_calc(special_attack)
        self.special_defense = stat_calc(special_defense)
        self.speed = stat_calc(speed)
        self.move_set = []
        self.move1 = None
        self.move2 = None
        self.move3 = None
        self.move4 = None
        self.name = name
        self.fainted = False
        self.points = 15
        self.type = ptype1
        self.move_list = []
        self.move1_number = 0
        self.move2_number = 1
        self.move3_number = 2
        self.move4_number = 3
        self.type2 = ptype2
        self.front_image = pygame.image.load(front_image)
        self.back_image = pygame.image.load(back_image)
        self.health_points = 0
        self.attack_points = 0
        self.defense_points = 0
        self.special_attack_points = 0
        self.special_defense_points = 0
        self.speed_points = 0
        self.first_turn = True
        #Pokemon.All_Pokemon.append(self)

    @staticmethod
    def update():
        for pokemon in Pokemon.All_Pokemon:
            pokemon.points = 15
            pokemon.points -= pokemon.health_points
            pokemon.points -= pokemon.attack_points
            pokemon.points -= pokemon.defense_points
            pokemon.points -= pokemon.special_attack_points
            pokemon.points -= pokemon.special_defense_points
            pokemon.points -= pokemon.speed_points
            pokemon.max_health = hp_calc(pokemon.base_health, pokemon.health_points)
            pokemon.attack = stat_calc(pokemon.base_attack, pokemon.attack_points)
            pokemon.defense = stat_calc(pokemon.base_defense, pokemon.defense_points)
            pokemon.special_attack = stat_calc(pokemon.base_special_attack, pokemon.special_attack_points)
            pokemon.special_defense = stat_calc(pokemon.base_special_defense, pokemon.special_defense_points)
            pokemon.speed = stat_calc(pokemon.base_speed, pokemon.speed_points)


class Team():
    teams = []
    def __init__(self, pokemon, number=0):
        self.list = pokemon
        self.pokemon_number = number
        self.pokemon = pokemon[number]
        Team.teams.append(self)


class Opponent():
    opponents = []
    All_Pokemon = []
    def __init__(self, pokemon, number=0):
        self.list = pokemon
        self.pokemon_number = number
        self.pokemon = pokemon[number]
        Opponent.opponents.append(self)


class Gym_Leader(Opponent):
    s = []
    def __init__(self, pokemon, name):
        Opponent.__init__(self, pokemon)
        self.name = name
        Gym_Leader.s.append(self)


class Bulbasaur(Pokemon):
    front_image = 'images/bulbasaur_front.png'
    back_image = 'images/bulbasaur_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=21, attack=23, defense=23, special_attack=31, special_defense=31, speed=21,
        ptype1=Grass, name="Bulbasaur", front_image=Bulbasaur.front_image, back_image=Bulbasaur.back_image, ptype2=Poison)
        self.move1 = energy_ball
        self.move2 = sludge_bomb
        self.move3 = ancient_power
        self.move4 = iron_tail
        self.move_list = [Return, iron_tail, energy_ball, sludge_bomb, ancient_power]
        self.move_set = [energy_ball, sludge_bomb, ancient_power, iron_tail]


class Ivysaur(Pokemon):
    front_image = 'images/ivysaur_front.png'
    back_image = 'images/ivysaur_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=22, attack=23, defense=23, special_attack=30, special_defense=30, speed=22,
        ptype1=Grass, name="Ivysaur", front_image=Ivysaur.front_image, back_image=Ivysaur.back_image, ptype2=Poison)
        self.move1 = energy_ball
        self.move2 = sludge_bomb
        self.move3 = ancient_power
        self.move4 = iron_tail
        self.move_list = [Return, iron_tail, energy_ball, sludge_bomb, ancient_power]
        self.move_set = [energy_ball, sludge_bomb, ancient_power, iron_tail]


class Venasaur(Pokemon):
    front_image = 'images/venasaur_front.png'
    back_image = 'images/venasaur_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=23, attack=23, defense=23, special_attack=29, special_defense=29, speed=23,
        ptype1=Grass, name="Venasaur", front_image=Venasaur.front_image, back_image=Venasaur.back_image, ptype2=Poison)
        self.move1 = energy_ball
        self.move2 = sludge_bomb
        self.move3 = earthquake
        self.move4 = iron_tail
        self.move_list = [earthquake, iron_tail, energy_ball, sludge_bomb, ancient_power]
        self.move_set = [energy_ball, sludge_bomb, earthquake, iron_tail]


class Squirtle(Pokemon):
    front_image = 'images/squirtle_front.png'
    back_image = 'images/squirtle_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=21, attack=23, defense=31, special_attack=24, special_defense=30, speed=21,
        ptype1=Water, name="Squirtle", front_image=Squirtle.front_image, back_image=Squirtle.back_image)
        self.move1 = aqua_jet
        self.move2 = surf
        self.move3 = ice_beam
        self.move4 = iron_tail
        self.move_list = [iron_tail, surf, waterfall, ice_punch, ice_beam, water_gun, brick_break, Return]
        self.move_set = [aqua_jet, surf, ice_beam, iron_tail]


class Wartortle(Pokemon):
    front_image = 'images/wartortle_front.png'
    back_image = 'images/wartortle_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=22, attack=23, defense=30, special_attack=24, special_defense=30, speed=21,
        ptype1=Water, name="Wartortle", front_image=Wartortle.front_image, back_image=Wartortle.back_image)
        self.move1 = waterfall
        self.move2 = surf
        self.move3 = ice_punch
        self.move4 = iron_tail
        self.move_list = [iron_tail, surf, waterfall, ice_punch, ice_beam, water_gun, brick_break, Return]
        self.move_set = [waterfall, surf, ice_punch, iron_tail]


class Blastoise(Pokemon):
    front_image = 'images/blastoise_front.png'
    back_image = 'images/blastoise_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=22, attack=24, defense=28, special_attack=24, special_defense=30, speed=22,
        ptype1=Water, name="Blastoise", front_image=Blastoise.front_image, back_image=Blastoise.back_image)
        self.move1 = waterfall
        self.move2 = surf
        self.move3 = ice_punch
        self.move4 = iron_tail
        self.move_list = [iron_tail, surf, waterfall, ice_punch, ice_beam, water_gun, brick_break, Return]
        self.move_set = [waterfall, surf, ice_punch, iron_tail]


class Charmander(Pokemon):
    front_image = 'images/charmander_front.png'
    back_image = 'images/charmander_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=19, attack=25, defense=21, special_attack=29, special_defense=24, speed=32,
        ptype1=Fire, name="Charmander", front_image=Charmander.front_image, back_image=Charmander.back_image)
        self.move1 = flamethrower
        self.move2 = ancient_power
        self.move3 = crunch
        self.move4 = thunder_punch
        self.move_list = [scratch, flamethrower, crunch, thunder_punch, aerial_ace, ancient_power, brick_break, dragon_claw]
        self.move_set = [flamethrower, ancient_power, crunch, thunder_punch]


class Charmeleon(Pokemon):
    front_image = 'images/charmeleon_front.png'
    back_image = 'images/charmeleon_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=21, attack=24, defense=21, special_attack=30, special_defense=24, speed=30,
        ptype1=Fire, name="Charmeleon", front_image=Charmeleon.front_image, back_image=Charmeleon.back_image)
        self.move1 = flamethrower
        self.move2 = ancient_power
        self.move3 = crunch
        self.move4 = thunder_punch
        self.move_list = [scratch, flamethrower, crunch, thunder_punch, aerial_ace, ancient_power, brick_break, dragon_claw]
        self.move_set = [flamethrower, ancient_power, crunch, thunder_punch]


class Charizard(Pokemon):
    front_image = 'images/charizard_front.png'
    back_image = 'images/charizard_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=22, attack=23, defense=22, special_attack=31, special_defense=24, speed=28,
        ptype1=Fire, name="Charizard", front_image=Charizard.front_image, back_image=Charizard.back_image, ptype2=Flying)
        self.move1 = flamethrower
        self.move2 = ancient_power
        self.move3 = earthquake
        self.move4 = thunder_punch
        self.move_list = [scratch, flamethrower, crunch, thunder_punch, aerial_ace, ancient_power, brick_break, dragon_claw, air_slash, crunch, earthquake, iron_tail]
        self.move_set = [flamethrower, ancient_power, earthquake, thunder_punch]


class Butterfree(Pokemon):
    move_list = [air_slash, bug_buzz, aerial_ace, energy_ball, psychic, shadow_ball, signal_beam, Return]
    move1 = air_slash
    move2 = bug_buzz
    move3 = energy_ball
    move4 = psychic
    move_set = [move1, move2, move3, move4]
    front_image = 'images/butterfree_front.png'
    back_image = 'images/butterfree_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=23, attack=17, defense=19, special_attack=34, special_defense=30, speed=27,
        ptype1=Bug, name="Butterfree", front_image=Butterfree.front_image, back_image=Butterfree.back_image, ptype2=Flying)
        self.move1 = Butterfree.move1
        self.move2 = Butterfree.move2
        self.move3 = Butterfree.move3
        self.move4 = Butterfree.move4
        self.move_list = Butterfree.move_list
        self.move_set = Butterfree.move_set


class Beedrill(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=25, attack=34, defense=15, special_attack=17, special_defense=30, speed=29,
        ptype1=Bug, name="Beedrill", front_image="images/beedrill_front.png", back_image="images/beedrill_back.png", ptype2=Poison)
        self.move1 = poison_jab
        self.move2 = x_scissor
        self.move3 = brick_break
        self.move4 = Return
        self.move_list = [poison_jab, x_scissor, brick_break, Return]
        self.move_set = [poison_jab, x_scissor, brick_break, Return]


class Mega_Beedrill(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=20, attack=45, defense=12, special_attack=5, special_defense=24, speed=44,
        ptype1=Bug, name="Mega-Beedrill", front_image="images/mega_beedrill_front.png", back_image="images/mega_beedrill_back.png", ptype2=Poison)
        self.move1 = poison_jab
        self.move2 = x_scissor
        self.move3 = brick_break
        self.move4 = Return
        self.move_list = [poison_jab, x_scissor, brick_break, Return]
        self.move_set = [poison_jab, x_scissor, brick_break, Return]


class Pidgey(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=24, attack=27, defense=24, special_attack=21, special_defense=21, speed=33,
        ptype1=Normal, name="Pidgey", front_image="images/pidgey_front.png", back_image="images/pidgey_back.png", ptype2=Flying)
        self.move1 = Return
        self.move2 = aerial_ace
        self.move3 = hidden_power_ground
        self.move4 = u_turn
        self.move_list = [Return, aerial_ace, hidden_power_ground, u_turn, boomburst, air_slash, scratch]
        self.move_set = [Return, aerial_ace, hidden_power_ground, u_turn]


class Pidgeotto(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=27, attack=26, defense=24, special_attack=21, special_defense=21, speed=31,
        ptype1=Normal, name="Pidgeotto", front_image="images/pidgeotto_front.png", back_image="images/pidgeotto_back.png", ptype2=Flying)
        self.move1 = Return
        self.move2 = aerial_ace
        self.move3 = hidden_power_ground
        self.move4 = boomburst
        self.move_list = [Return, aerial_ace, hidden_power_ground, boomburst, air_slash, scratch]
        self.move_set = [Return, aerial_ace, hidden_power_ground, boomburst]


class Pidgeot(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=26, attack=25, defense=23, special_attack=22, special_defense=22, speed=32,
        ptype1=Normal, name="Pidgeot", front_image="images/pidgeot_front.png", back_image="images/pidgeot_back.png", ptype2=Flying)
        self.move1 = Return
        self.move2 = aerial_ace
        self.move3 = hidden_power_ground
        self.move4 = boomburst
        self.move_list = [Return, aerial_ace, hidden_power_ground, boomburst, air_slash, scratch]
        self.move_set = [Return, aerial_ace, hidden_power_ground, boomburst]


class Mega_Pidgeot(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=21, attack=21, defense=21, special_attack=35, special_defense=21, speed=31,
        ptype1=Normal, name="Mega-Pidgeot", front_image="images/mega_pidgeot_front.png", back_image="images/mega_pidgeot_back.png", ptype2=Flying)
        self.move1 = boomburst
        self.move2 = aeroblast
        self.move3 = hidden_power_ground
        self.move4 = iron_tail
        self.move_list = [boomburst, aeroblast, hidden_power_ground, iron_tail, Return, aerial_ace, air_slash, scratch]
        self.move_set = [self.move1, self.move2, self.move3, self.move4]


class Rattata(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=18, attack=33, defense=21, special_attack=15, special_defense=21, speed=42,
        ptype1=Normal, name="Rattata", front_image="images/rattata_front.png", back_image="images/rattata_back.png")
        self.move1 = Return
        self.move2 = crunch
        self.move3 = fire_fang
        self.move4 = u_turn
        self.move_list = [Return, crunch, fire_fang, u_turn, zen_headbutt, bite, Return, scratch, boomburst, hidden_power_ground]
        self.move_set = [Return, crunch, fire_fang, u_turn]


class Raticate(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=20, attack=29, defense=22, special_attack=18, special_defense=25, speed=35,
        ptype1=Normal, name="Raticate", front_image="images/raticate_front.png", back_image="images/raticate_back.png")
        self.move1 = Return
        self.move2 = crunch
        self.move3 = fire_fang
        self.move4 = u_turn
        self.move_list = [Return, crunch, fire_fang, u_turn, zen_headbutt, bite, Return, scratch, boomburst, hidden_power_ground]
        self.move_set = [Return, crunch, fire_fang, u_turn]


class Spearow(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=23, attack=34, defense=17, special_attack=18, special_defense=18, speed=40,
        ptype1=Normal, name="Spearow", front_image="images/spearow_front.png", back_image="images/spearow_back.png", ptype2=Flying)
        self.move1 = drill_peck
        self.move2 = Return
        self.move3 = drill_run
        self.move4 = hidden_power_rock
        self.move_list = [drill_peck, Return, drill_run, hidden_power_rock, air_slash, aerial_ace]
        self.move_set = [drill_peck, Return, drill_run, hidden_power_rock]


class Fearow(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=22, attack=30, defense=22, special_attack=21, special_defense=21, speed=34,
        ptype1=Normal, name="Fearow", front_image="images/fearow_front.png", back_image="images/fearow_back.png", ptype2=Flying)
        self.move1 = drill_peck
        self.move2 = Return
        self.move3 = drill_run
        self.move4 = hidden_power_rock
        self.move_list = [drill_peck, Return, drill_run, hidden_power_rock, air_slash, aerial_ace]
        self.move_set = [drill_peck, Return, drill_run, hidden_power_rock]


class Ekans(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=18, attack=31, defense=23, special_attack=21, special_defense=28, speed=29,
        ptype1=Poison, name="Ekans", front_image="images/ekans_front.png", back_image="images/ekans_back.png")
        self.move1 = poison_jab
        self.move2 = earthquake
        self.move3 = fire_fang
        self.move4 = crunch
        self.move_list = [poison_jab, earthquake, fire_fang, crunch]
        self.move_set = [poison_jab, earthquake, fire_fang, crunch]


class Arbok(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=21, attack=29, defense=24, special_attack=22, special_defense=27, speed=27,
        ptype1=Poison, name="Arbok", front_image="images/arbok_front.png", back_image="images/arbok_back.png")
        self.move1 = poison_jab
        self.move2 = earthquake
        self.move3 = fire_fang
        self.move4 = crunch
        self.move_list = [poison_jab, earthquake, fire_fang, crunch]
        self.move_set = [poison_jab, earthquake, fire_fang, crunch]


class Pichu(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=14, attack=29, defense=11, special_attack=26, special_defense=26, speed=44,
        ptype1=Electric, name="Pichu", front_image="images/pichu_front.png", back_image="images/pichu_back.png")
        self.move1 = thunder_punch
        self.move2 = iron_tail
        self.move3 = surf
        self.move4 = hidden_power_ground
        self.move_list = [thunder_punch, iron_tail, surf, hidden_power_ground, signal_beam, mega_kick, thunderbolt]
        self.move_set = [thunder_punch, iron_tail, surf, hidden_power_ground]


class Light_Ball_Pikachu(Pokemon):
    move_list = [brick_break, iron_tail, thunderbolt, signal_beam, surf]
    move1 = thunderbolt
    move2 = signal_beam
    move3 = surf
    move4 = iron_tail
    move_set = [thunderbolt, signal_beam, surf, iron_tail]
    front_image = 'images/pikachu_front.png'
    back_image = 'images/pikachu_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=12, attack=39, defense=14, special_attack=35, special_defense=18, speed=32,
        ptype1=Electric, name="Light Ball Pikachu", front_image=Pikachu.front_image, back_image=Pikachu.back_image)
        self.move1 = Pikachu.move1
        self.move2 = Pikachu.move2
        self.move3 = Pikachu.move3
        self.move4 = Pikachu.move4
        self.move_set = Pikachu.move_set
        self.move_list = Pikachu.move_list


class Pikachu(Pokemon):
    move_list = [brick_break, iron_tail, thunderbolt, signal_beam, surf]
    move1 = thunderbolt
    move2 = signal_beam
    move3 = surf
    move4 = iron_tail
    move_set = [thunderbolt, signal_beam, surf, iron_tail]
    front_image = 'images/pikachu_front.png'
    back_image = 'images/pikachu_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=17, attack=26, defense=19, special_attack=23, special_defense=23, speed=42,
        ptype1=Electric, name="Pikachu", front_image=Pikachu.front_image, back_image=Pikachu.back_image)
        self.move1 = Pikachu.move1
        self.move2 = Pikachu.move2
        self.move3 = Pikachu.move3
        self.move4 = Pikachu.move4
        self.move_set = Pikachu.move_set
        self.move_list = Pikachu.move_list


class Raichu(Pokemon):
    move_list = [brick_break, iron_tail, thunderbolt, signal_beam, surf]
    move1 = thunderbolt
    move2 = signal_beam
    move3 = surf
    move4 = iron_tail
    move_set = [thunderbolt, signal_beam, surf, iron_tail]
    front_image = 'images/raichu_front.png'
    back_image = 'images/raichu_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=18, attack=28, defense=17, special_attack=28, special_defense=25, speed=34,
        ptype1=Electric, name="Raichu", front_image=Raichu.front_image, back_image=Raichu.back_image)
        self.move1 = Raichu.move1
        self.move2 = Raichu.move2
        self.move3 = Raichu.move3
        self.move4 = Raichu.move4
        self.move_list = Raichu.move_list
        self.move_set = Raichu.move_set


class Sandshrew(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=25, attack=38, defense=43, special_attack=9, special_defense=15, speed=20,
        ptype1=Ground, name="Sandshrew", front_image="images/sandshrew_front.png", back_image="images/sandshrew_back.png")
        self.move1 = earthquake
        self.move2 = rock_slide
        self.move3 = iron_tail
        self.move4 = brick_break
        self.move_list = [earthquake, rock_slide, iron_tail, brick_break, aerial_ace, scratch]
        self.move_set = [earthquake, rock_slide, iron_tail, brick_break]


class Sandslash(Pokemon):
    move_list = [earthquake, aerial_ace, iron_tail, brick_break, scratch]
    move1 = earthquake
    move2 = aerial_ace
    move3 = iron_tail
    move4 = brick_break
    move_set = [move1, move2, move3, move4]
    front_image = 'images/sandslash_front.png'
    back_image = 'images/sandslash_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=25, attack=33, defense=37, special_attack=15, special_defense=18, speed=22,
        ptype1=Ground, name="Sandslash", front_image=Sandslash.front_image, back_image=Sandslash.back_image)
        self.move1 = Sandslash.move1
        self.move2 = Sandslash.move2
        self.move3 = Sandslash.move3
        self.move4 = Sandslash.move4
        self.move_set = Sandslash.move_set
        self.move_list = Sandslash.move_list


class NidoranF(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=30, attack=26, defense=28, special_attack=22, special_defense=22, speed=22,
        ptype1=Poison, name="Nidoran-F", front_image="images/nidoranf_front.png", back_image="images/nidoranf_back.png")
        self.move1 = poison_jab
        self.move2 = Return
        self.move3 = iron_tail
        self.move4 = crunch
        self.move_list = [poison_jab, Return, iron_tail, crunch]
        self.move_set = [poison_jab, Return, iron_tail, crunch]


class Nidorina(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=29, attack=25, defense=27, special_attack=23, special_defense=23, speed=23,
        ptype1=Poison, name="Nidorina", front_image="images/nidorina_front.png", back_image="images/nidorina_back.png")
        self.move1 = poison_jab
        self.move2 = Return
        self.move3 = iron_tail
        self.move4 = crunch
        self.move_list = [poison_jab, Return, iron_tail, crunch]
        self.move_set = [poison_jab, Return, iron_tail, crunch]


class Nidoqueen(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=27, attack=27, defense=26, special_attack=22, special_defense=25, speed=23,
        ptype1=Poison, name="Nidoqueen", front_image="images/nidoqueen_front.png", back_image="images/nidoqueen_back.png", ptype2=Ground)
        self.move1 = poison_jab
        self.move2 = earthquake
        self.move3 = ice_punch
        self.move4 = thunder_punch
        self.move_list = [poison_jab, earthquake, ice_punch, thunder_punch, Return, iron_tail, crunch]
        self.move_set = [poison_jab, earthquake, ice_punch, thunder_punch]


class NidoranM(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=25, attack=31, defense=22, special_attack=22, special_defense=22, speed=28,
        ptype1=Poison, name="Nidoran-M", front_image="images/nidoranm_front.png", back_image="images/nidoranm_back.png")
        self.move1 = poison_jab
        self.move2 = Return
        self.move3 = iron_tail
        self.move4 = crunch
        self.move_list = [poison_jab, Return, iron_tail, crunch]
        self.move_set = [poison_jab, Return, iron_tail, crunch]


class Nidorino(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=25, attack=29, defense=23, special_attack=23, special_defense=23, speed=27,
        ptype1=Poison, name="Nidorino", front_image="images/nidorino_front.png", back_image="images/nidorino_back.png")
        self.move1 = poison_jab
        self.move2 = Return
        self.move3 = iron_tail
        self.move4 = crunch
        self.move_list = [poison_jab, Return, iron_tail, crunch]
        self.move_set = [poison_jab, Return, iron_tail, crunch]


class Nidoking(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=24, attack=30, defense=23, special_attack=25, special_defense=22, speed=25,
        ptype1=Poison, name="Nidoking", front_image="images/nidoking_front.png", back_image="images/nidoking_back.png", ptype2=Ground)
        self.move1 = poison_jab
        self.move2 = earthquake
        self.move3 = ice_punch
        self.move4 = thunder_punch
        self.move_list = [poison_jab, earthquake, ice_punch, thunder_punch, Return, iron_tail, crunch]
        self.move_set = [poison_jab, earthquake, ice_punch, thunder_punch]


class Cleffa(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=35, attack=17, defense=19, special_attack=31, special_defense=38, speed=10,
        ptype1=Fairy, name="Cleffa", front_image="images/cleffa_front.png", back_image="images/cleffa_back.png")
        self.move1 = flamethrower
        self.move2 = magical_leaf
        self.move3 = psychic
        self.move4 = hidden_power_fairy
        self.move_list = [flamethrower, magical_leaf, psychic, hidden_power_fairy, iron_tail, mega_kick, shadow_ball, signal_beam, zen_headbutt]
        self.move_set = [flamethrower, magical_leaf, psychic, hidden_power_fairy]


class Clefairy(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=33, attack=21, defense=22, special_attack=28, special_defense=30, speed=16,
        ptype1=Fairy, name="Clefairy", front_image="images/clefairy_front.png", back_image="images/clefairy_back.png")
        self.move1 = moonblast
        self.move2 = flamethrower
        self.move3 = ice_beam
        self.move4 = thunderbolt
        self.move_list = [moonblast, flamethrower, ice_beam, thunderbolt]
        self.move_set = [moonblast, flamethrower, ice_beam, thunderbolt]


class Clefable(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=28, attack=22, defense=23, special_attack=30, special_defense=28, speed=19,
        ptype1=Fairy, name="Clefable", front_image="images/clefable_front.png", back_image="images/clefable_back.png")
        self.move1 = moonblast
        self.move2 = flamethrower
        self.move3 = ice_beam
        self.move4 = thunderbolt
        self.move_list = [moonblast, flamethrower, ice_beam, thunderbolt]
        self.move_set = [moonblast, flamethrower, ice_beam, thunderbolt]


class Vulpix(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=19, attack=20, defense=20, special_attack=25, special_defense=33, speed=33,
        ptype1=Fire, name="Vulpix", front_image="images/vulpix_front.png", back_image="images/vulpix_back.png")
        self.move1 = flamethrower
        self.move2 = psychic
        self.move3 = dark_pulse
        self.move4 = shadow_ball
        self.move_list = [flamethrower, psychic, dark_pulse, shadow_ball]
        self.move_set = [flamethrower, psychic, dark_pulse, shadow_ball]


class Ninetails(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=22, attack=22, defense=22, special_attack=24, special_defense=30, speed=30,
        ptype1=Fire, name="Ninetails", front_image="images/ninetails_front.png", back_image="images/ninetails_back.png")
        self.move1 = flamethrower
        self.move2 = psychic
        self.move3 = dark_pulse
        self.move4 = shadow_ball
        self.move_list = [flamethrower, psychic, dark_pulse, shadow_ball]
        self.move_set = [flamethrower, psychic, dark_pulse, shadow_ball]


class Igglybuff(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=64, attack=21, defense=11, special_attack=29, special_defense=14, speed=11,
        ptype1=Normal, name="Igglybuff", front_image="images/igglybuff_front.png", back_image="images/igglybuff_back.png", ptype2=Fairy)
        self.move1 = flamethrower
        self.move2 = hyper_voice
        self.move3 = mega_kick
        self.move4 = hidden_power_fairy
        self.move_list = [flamethrower, hyper_voice, mega_kick, hidden_power_fairy, psychic, shadow_ball]
        self.move_set = [flamethrower, hyper_voice, mega_kick, hidden_power_fairy]


class Jigglypuff(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=64, attack=25, defense=11, special_attack=25, special_defense=14, speed=11,
        ptype1=Normal, name="Jigglypuff", front_image="images/jigglypuff_front.png", back_image="images/jigglypuff_back.png", ptype2=Fairy)
        self.move1 = moonblast
        self.move2 = hyper_voice
        self.move3 = ice_punch
        self.move4 = thunder_punch
        self.move_list = [moonblast, hyper_voice, ice_punch, thunder_punch, ice_beam, thunderbolt]
        self.move_set = [moonblast, hyper_voice, ice_punch, thunder_punch]


class Wigglytuff(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=48, attack=24, defense=16, special_attack=29, special_defense=17, speed=16,
        ptype1=Normal, name="Wigglytuff", front_image="images/wigglytuff_front.png", back_image="images/wigglytuff_back.png", ptype2=Fairy)
        self.move1 = moonblast
        self.move2 = hyper_voice
        self.move3 = ice_punch
        self.move4 = thunder_punch
        self.move_list = [moonblast, hyper_voice, ice_punch, thunder_punch, ice_beam, thunderbolt]
        self.move_set = [moonblast, hyper_voice, ice_punch, thunder_punch]


class Zubat(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=24, attack=28, defense=22, special_attack=18, special_defense=24, speed=34,
        ptype1=Poison, name="Zubat", front_image="images/zubat_front.png", back_image="images/zubat_back.png", ptype2=Flying)
        self.move1 = aerial_ace
        self.move2 = poison_jab
        self.move3 = bite
        self.move4 = fire_fang
        self.move_list = [aerial_ace, poison_jab, bite, fire_fang, x_scissor]
        self.move_set = [aerial_ace, poison_jab, bite, fire_fang]


class Golbat(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=25, attack=26, defense=23, special_attack=21, special_defense=25, speed=30,
        ptype1=Poison, name="Golbat", front_image="images/golbat_front.png", back_image="images/golbat_back.png", ptype2=Flying)
        self.move1 = aerial_ace
        self.move2 = poison_jab
        self.move3 = bite
        self.move4 = fire_fang
        self.move_list = [aerial_ace, poison_jab, bite, fire_fang, x_scissor]
        self.move_set = [aerial_ace, poison_jab, bite, fire_fang]


class Crobat(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=24, attack=25, defense=22, special_attack=20, special_defense=22, speed=37,
        ptype1=Poison, name="Crobat", front_image="images/crobat_front.png", back_image="images/crobat_back.png", ptype2=Flying)
        self.move1 = aerial_ace
        self.move2 = poison_jab
        self.move3 = bite
        self.move4 = fire_fang
        self.move_list = [aerial_ace, poison_jab, bite, fire_fang, x_scissor]
        self.move_set = [aerial_ace, poison_jab, bite, fire_fang]


class Oddish(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=21, attack=23, defense=26, special_attack=35, special_defense=31, speed=14,
        ptype1=Grass, name="Oddish", front_image="images/oddish_front.png", back_image="images/oddish_back.png", ptype2=Poison)
        self.move1 = energy_ball
        self.move2 = sludge_bomb
        self.move3 = hidden_power_fire
        self.move4 = Return
        self.move_list = [energy_ball, sludge_bomb, hidden_power_fire, Return]
        self.move_set = [energy_ball, sludge_bomb, hidden_power_fire, Return]


class Gloom(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=23, attack=25, defense=27, special_attack=32, special_defense=28, speed=15,
        ptype1=Grass, name="Gloom", front_image="images/gloom_front.png", back_image="images/gloom_back.png", ptype2=Poison)
        self.move1 = energy_ball
        self.move2 = sludge_bomb
        self.move3 = hidden_power_fire
        self.move4 = Return
        self.move_list = [energy_ball, sludge_bomb, hidden_power_fire, Return]
        self.move_set = [energy_ball, sludge_bomb, hidden_power_fire, Return]


class Vileplume(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=23, attack=24, defense=26, special_attack=34, special_defense=28, speed=15,
        ptype1=Grass, name="Vileplume", front_image="images/vileplume_front.png", back_image="images/vileplume_back.png", ptype2=Poison)
        self.move1 = energy_ball
        self.move2 = sludge_bomb
        self.move3 = hidden_power_fire
        self.move4 = Return
        self.move_list = [energy_ball, sludge_bomb, hidden_power_fire, Return]
        self.move_set = [energy_ball, sludge_bomb, hidden_power_fire, Return]


class Paras(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=18, attack=37, defense=29, special_attack=24, special_defense=29, speed=13,
        ptype1=Bug, name="Paras", front_image="images/paras_front.png", back_image="images/paras_back.png", ptype2=Grass)
        self.move1 = leaf_blade
        self.move2 = x_scissor
        self.move3 = poison_jab
        self.move4 = hidden_power_ground
        self.move_list = [leaf_blade, x_scissor, poison_jab, hidden_power_ground]
        self.move_set = [leaf_blade, x_scissor, poison_jab, hidden_power_ground]


class Parasect(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=22, attack=35, defense=30, special_attack=22, special_defense=30, speed=11,
        ptype1=Bug, name="Parasect", front_image="images/parasect_front.png", back_image="images/parasect_back.png", ptype2=Grass)
        self.move1 = leaf_blade
        self.move2 = x_scissor
        self.move3 = poison_jab
        self.move4 = hidden_power_ground
        self.move_list = [leaf_blade, x_scissor, poison_jab, hidden_power_ground]
        self.move_set = [leaf_blade, x_scissor, poison_jab, hidden_power_ground]


class Venonat(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=30, attack=27, defense=25, special_attack=20, special_defense=25, speed=23,
        ptype1=Bug, name="Venonat", front_image="images/venonat_front.png", back_image="images/venonat_back.png", ptype2=Poison)
        self.move1 = poison_jab
        self.move2 = x_scissor
        self.move3 = fire_fang
        self.move4 = hidden_power_ground
        self.move_list = [poison_jab, x_scissor, fire_fang, hidden_power_ground, Return]
        self.move_set = [poison_jab, x_scissor, fire_fang, hidden_power_ground]


class Venomoth(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=23, attack=22, defense=20, special_attack=30, special_defense=25, speed=30,
        ptype1=Bug, name="Venomoth", front_image="images/venomoth_front.png", back_image="images/venomoth_back.png", ptype2=Poison)
        self.move1 = bug_buzz
        self.move2 = sludge_bomb
        self.move3 = psychic
        self.move4 = hidden_power_ground
        self.move_list = [bug_buzz, sludge_bomb, psychic, hidden_power_ground, poison_jab, x_scissor, fire_fang, Return]
        self.move_set = [bug_buzz, sludge_bomb, psychic, hidden_power_ground, poison_jab, x_scissor, fire_fang]


class Diglett(Pokemon):
    move_list = [earthquake, rock_slide, aerial_ace, Return]
    move1 = earthquake
    move2 = rock_slide
    move3 = aerial_ace
    move4 = Return
    move_set = [move1, move2, move3, move4]
    front_image = 'images/diglett_front.png'
    back_image = 'images/diglett_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=6, attack=31, defense=14, special_attack=20, special_defense=25, speed=54,
        ptype1=Ground, name="Diglett", front_image=Diglett.front_image, back_image=Diglett.back_image)
        self.move1 = Diglett.move1
        self.move2 = Diglett.move2
        self.move3 = Diglett.move3
        self.move4 = Diglett.move4
        self.move_list = Diglett.move_list
        self.move_set = Diglett.move_set


class Dugtrio(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=13, attack=30, defense=19, special_attack=19, special_defense=25, speed=44,
        ptype1=Ground, name="Dugtrio", front_image="images/dugtrio_front.png", back_image="images/dugtrio_back.png")
        self.move1 = earthquake
        self.move2 = rock_slide
        self.move3 = aerial_ace
        self.move4 = hidden_power_ice
        self.move_list = [earthquake, rock_slide, aerial_ace, hidden_power_ice]
        self.move_set = [earthquake, rock_slide, aerial_ace, hidden_power_ice]


class Meowth(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=20, attack=23, defense=18, special_attack=21, special_defense=21, speed=47,
        ptype1=Normal, name="Meowth", front_image="images/meowth_front.png", back_image="images/meowth_back.png")
        self.move1 = Return
        self.move2 = hyper_voice
        self.move3 = bite
        self.move4 = hidden_power_ground
        self.move_list = [Return, hyper_voice, bite, hidden_power_ground, fire_fang]
        self.move_set = [Return, hyper_voice, bite, hidden_power_ground]


class Persian(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=22, attack=24, defense=21, special_attack=22, special_defense=22, speed=39,
        ptype1=Normal, name="Persian", front_image="images/persian_front.png", back_image="images/persian_back.png")
        self.move1 = Return
        self.move2 = fake_out
        self.move3 = bite
        self.move4 = feint
        self.move_list = [Return, fake_out, bite, feint, hyper_voice, hidden_power_ground, fire_fang]
        self.move_set = [Return, fake_out, bite, feint]


class Psyduck(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=23, attack=24, defense=23, special_attack=31, special_defense=23, speed=26,
        ptype1=Water, name="Psyduck", front_image="images/psyduck_front.png", back_image="images/psyduck_back.png")
        self.move1 = surf
        self.move2 = ice_beam
        self.move3 = psychic
        self.move4 = hidden_power_grass
        self.move_list = [surf, ice_beam, psychic, hidden_power_grass, hidden_power_ground]
        self.move_set = [surf, ice_beam, psychic, hidden_power_grass]


class Golduck(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=24, attack=24, defense=23, special_attack=29, special_defense=24, speed=26,
        ptype1=Water, name="Golduck", front_image="images/golduck_front.png", back_image="images/golduck_back.png")
        self.move1 = surf
        self.move2 = ice_beam
        self.move3 = psychic
        self.move4 = hidden_power_grass
        self.move_list = [surf, ice_beam, psychic, hidden_power_grass, hidden_power_ground]
        self.move_set = [surf, ice_beam, psychic, hidden_power_grass]


class Mankey(Pokemon):
    move_list = [cross_chop, brick_break, earthquake, ice_punch, thunder_punch, fire_punch]
    move1 = cross_chop
    move2 = fire_punch
    move3 = thunder_punch
    move4 = ice_punch
    move_set = [move1, move2, move3, move4]
    front_image = 'images/mankey_front.png'
    back_image = 'images/mankey_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=20, attack=39, defense=17, special_attack=17, special_defense=22, speed=35,
        ptype1=Fight, name="Mankey", front_image=Mankey.front_image, back_image=Mankey.back_image)
        self.move1 = Mankey.move1
        self.move2 = Mankey.move2
        self.move3 = Mankey.move3
        self.move4 = Mankey.move4
        self.move_list = Mankey.move_list
        self.move_set = Mankey.move_set


class Primeape(Pokemon):
    move_list = [cross_chop, brick_break, earthquake, ice_punch, thunder_punch, fire_punch]
    move1 = cross_chop
    move2 = fire_punch
    move3 = thunder_punch
    move4 = ice_punch
    move_set = [move1, move2, move3, move4]
    front_image = 'images/primeape_front.png'
    back_image = 'images/primeape_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=21, attack=35, defense=20, special_attack=20, special_defense=23, speed=31,
        ptype1=Fight, name="Primeape", front_image=Primeape.front_image, back_image=Primeape.back_image)
        self.move1 = Primeape.move1
        self.move2 = Primeape.move2
        self.move3 = Primeape.move3
        self.move4 = Primeape.move4
        self.move_set = Primeape.move_set
        self.move_list = Primeape.move_list


class Growlithe(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=24, attack=30, defense=19, special_attack=30, special_defense=21, speed=26,
        ptype1=Fire, name="Growlithe", front_image="images/growlithe_front.png", back_image="images/growlithe_back.png")
        self.move1 = flamethrower
        self.move2 = spark
        self.move3 = fire_fang
        self.move4 = hidden_power_ground
        self.move_list = [flamethrower, spark, fire_fang, hidden_power_ground, hidden_power_rock]
        self.move_set = [flamethrower, spark, fire_fang, hidden_power_ground]


class Arcanine(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=24, attack=30, defense=22, special_attack=26, special_defense=22, speed=26,
        ptype1=Fire, name="Arcanine", front_image="images/arcanine_front.png", back_image="images/arcanine_back.png")
        self.move1 = flamethrower
        self.move2 = spark
        self.move3 = fire_fang
        self.move4 = hidden_power_ground
        self.move_list = [flamethrower, spark, fire_fang, hidden_power_ground, hidden_power_rock]
        self.move_set = [flamethrower, spark, fire_fang, hidden_power_ground]


class Poliwag(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=20, attack=25, defense=20, special_attack=20, special_defense=20, speed=45,
        ptype1=Water, name="Poliwag", front_image="images/poliwag_front.png", back_image="images/poliwag_back.png")
        self.move1 = waterfall
        self.move2 = Return
        self.move3 = ice_beam
        self.move4 = psychic
        self.move_list = [waterfall, Return, ice_beam, psychic, hidden_power_grass, hidden_power_fire]
        self.move_set = [waterfall, Return, ice_beam, psychic]


class Poliwhirl(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=25, attack=25, defense=25, special_attack=20, special_defense=20, speed=35,
        ptype1=Water, name="Poliwhirl", front_image="images/poliwhirl_front.png", back_image="images/poliwhirl_back.png")
        self.move1 = waterfall
        self.move2 = brick_break
        self.move3 = ice_punch
        self.move4 = hidden_power_grass
        self.move_list = [waterfall, brick_break, ice_punch, hidden_power_grass, Return, ice_beam, psychic, hidden_power_fire]
        self.move_set = [waterfall, brick_break, ice_punch, hidden_power_grass]



class Poliwrath(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=27, attack=25, defense=29, special_attack=21, special_defense=27, speed=21,
        ptype1=Water, name="Poliwrath", front_image="images/poliwrath_front.png", back_image="images/poliwrath_back.png", ptype2=Fight)
        self.move1 = waterfall
        self.move2 = brick_break
        self.move3 = ice_beam
        self.move4 = hidden_power_grass
        self.move_list = [waterfall, brick_break, ice_punch, hidden_power_grass, Return, ice_beam, psychic, hidden_power_fire]
        self.move_set = [waterfall, brick_break, ice_punch, hidden_power_grass]


class Abra(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=12, attack=9, defense=7, special_attack=51, special_defense=27, speed=44,
        ptype1=Psychic, name="Abra", front_image="images/abra_front.png", back_image="images/abra_back.png")
        self.move1 = psychic
        self.move2 = signal_beam
        self.move3 = energy_ball
        self.move4 = hidden_power_ground
        self.move_list = [psychic, signal_beam, energy_ball, hidden_power_ground, shadow_ball, dazzling_gleam]
        self.move_set = [psychic, signal_beam, energy_ball, hidden_power_ground]


class Kadabra(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=15, attack=12, defense=11, special_attack=45, special_defense=26, speed=40,
        ptype1=Psychic, name="Kadabra", front_image="images/kadabra_front.png", back_image="images/kadabra_back.png")
        self.move1 = psychic
        self.move2 = signal_beam
        self.move3 = energy_ball
        self.move4 = hidden_power_ground
        self.move_list = [psychic, signal_beam, energy_ball, hidden_power_ground, shadow_ball, dazzling_gleam]
        self.move_set = [psychic, signal_beam, energy_ball, hidden_power_ground]


class Alakazam(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=17, attack=13, defense=14, special_attack=41, special_defense=29, speed=36,
        ptype1=Psychic, name="Alakazam", front_image="images/alakazam_front.png", back_image="images/alakazam_back.png")
        self.move1 = psychic
        self.move2 = signal_beam
        self.move3 = energy_ball
        self.move4 = hidden_power_ground
        self.move_list = [psychic, signal_beam, energy_ball, hidden_power_ground, shadow_ball, dazzling_gleam]
        self.move_set = [psychic, signal_beam, energy_ball, hidden_power_ground]


class Machop(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=35, attack=39, defense=25, special_attack=17, special_defense=17, speed=17,
        ptype1=Fight, name="Machop", front_image="images/machop_front.png", back_image="images/machop_back.png")
        self.move1 = cross_chop
        self.move2 = rock_slide
        self.move3 = poison_jab
        self.move4 = earthquake
        self.move_list = [cross_chop, rock_slide, poison_jab, earthquake, brick_break, fire_punch, ice_punch, thunder_punch]
        self.move_set = [cross_chop, rock_slide, poison_jab, earthquake]


class Machoke(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=30, attack=37, defense=26, special_attack=18, special_defense=22, speed=17,
        ptype1=Fight, name="Machoke", front_image="images/machoke_front.png", back_image="images/machoke_back.png")
        self.move1 = cross_chop
        self.move2 = rock_slide
        self.move3 = poison_jab
        self.move4 = earthquake
        self.move_list = [cross_chop, rock_slide, poison_jab, earthquake, brick_break, fire_punch, ice_punch, thunder_punch]
        self.move_set = [cross_chop, rock_slide, poison_jab, earthquake]


class Machamp(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=27, attack=39, defense=24, special_attack=19, special_defense=25, speed=16,
        ptype1=Fight, name="Machamp", front_image="images/machamp_front.png", back_image="images/machamp_back.png")
        self.move1 = cross_chop
        self.move2 = rock_slide
        self.move3 = poison_jab
        self.move4 = earthquake
        self.move_list = [cross_chop, rock_slide, poison_jab, earthquake, brick_break, fire_punch, ice_punch, thunder_punch]
        self.move_set = [cross_chop, rock_slide, poison_jab, earthquake]


class Bellsprout(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=25, attack=38, defense=17, special_attack=35, special_defense=15, speed=20,
        ptype1=Grass, name="Bellsprout", front_image="images/bellsprout_front.png", back_image="images/bellsprout_back.png", ptype2=Poison)
        self.move1 = energy_ball
        self.move2 = sludge_bomb
        self.move3 = power_whip
        self.move4 = hidden_power_ground
        self.move_list = [energy_ball, sludge_bomb, power_whip, hidden_power_ground, Return, seed_bomb]
        self.move_set = [energy_ball, sludge_bomb, power_whip, hidden_power_ground]


class Weepinbell(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=25, attack=35, defense=19, special_attack=33, special_defense=17, speed=21,
        ptype1=Grass, name="Weepinbell", front_image="images/weepinbell_front.png", back_image="images/weepinbell_back.png", ptype2=Poison)
        self.move1 = energy_ball
        self.move2 = sludge_bomb
        self.move3 = power_whip
        self.move4 = hidden_power_ground
        self.move_list = [energy_ball, sludge_bomb, power_whip, hidden_power_ground, Return, seed_bomb]
        self.move_set = [energy_ball, sludge_bomb, power_whip, hidden_power_ground]


class Victreebel(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=25, attack=32, defense=20, special_attack=31, special_defense=21, speed=21,
        ptype1=Grass, name="Victeebel", front_image="images/victreebel_front.png", back_image="images/victreebel_back.png", ptype2=Poison)
        self.move1 = energy_ball
        self.move2 = sludge_bomb
        self.move3 = power_whip
        self.move4 = hidden_power_ground
        self.move_list = [energy_ball, sludge_bomb, power_whip, hidden_power_ground, Return, seed_bomb, leaf_blade]
        self.move_set = [energy_ball, sludge_bomb, power_whip, hidden_power_ground]


class Tentacool(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=18, attack=18, defense=16, special_attack=22, special_defense=45, speed=31,
        ptype1=Water, name="Tentacool", front_image="images/tentacool_front.png", back_image="images/tentacool_back.png", ptype2=Poison)
        self.move1 = sludge_bomb
        self.move2 = surf
        self.move3 = ice_beam
        self.move4 = hidden_power_ground
        self.move_list = [sludge_bomb, surf, ice_beam, hidden_power_ground, waterfall, poison_jab, Return, dazzling_gleam]
        self.move_set = [sludge_bomb, surf, ice_beam, hidden_power_ground]


class Tentacruel(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=23, attack=20, defense=19, special_attack=23, special_defense=35, speed=30,
        ptype1=Water, name="Tentacruel", front_image="images/tentacruel_front.png", back_image="images/tentacruel_back.png", ptype2=Poison)
        self.move1 = sludge_bomb
        self.move2 = surf
        self.move3 = ice_beam
        self.move4 = hidden_power_ground
        self.move_list = [sludge_bomb, surf, ice_beam, hidden_power_ground, waterfall, poison_jab, Return, dazzling_gleam]
        self.move_set = [sludge_bomb, surf, ice_beam, hidden_power_ground]


class Geodude(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=20, attack=40, defense=50, special_attack=15, special_defense=15, speed=10,
        ptype1=Ground, name="Geodude", front_image="images/geodude_front.png", back_image="images/geodude_back.png", ptype2=Rock)
        self.move1 = earthquake
        self.move2 = rock_slide
        self.move3 = fire_punch
        self.move4 = thunder_punch
        self.move_list = [earthquake, rock_slide, fire_punch, thunder_punch, brick_break, Return, ancient_power, earth_power, flamethrower]
        self.move_set = [earthquake, rock_slide, fire_punch, thunder_punch]


class Graveler(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=21, attack=37, defense=44, special_attack=17, special_defense=17, speed=14,
        ptype1=Ground, name="Graveler", front_image="images/graveler_front.png", back_image="images/graveler_back.png", ptype2=Rock)
        self.move1 = earthquake
        self.move2 = rock_slide
        self.move3 = fire_punch
        self.move4 = thunder_punch
        self.move_list = [earthquake, rock_slide, fire_punch, thunder_punch, brick_break, Return, ancient_power, earth_power, flamethrower]
        self.move_set = [earthquake, rock_slide, fire_punch, thunder_punch]


class Golem(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=24, attack=36, defense=39, special_attack=17, special_defense=20, speed=14,
        ptype1=Ground, name="Golem", front_image="images/golem_front.png", back_image="images/golem_back.png", ptype2=Rock)
        self.move1 = earthquake
        self.move2 = rock_slide
        self.move3 = fire_punch
        self.move4 = thunder_punch
        self.move_list = [earthquake, rock_slide, fire_punch, thunder_punch, brick_break, Return, ancient_power, earth_power, flamethrower]
        self.move_set = [earthquake, rock_slide, fire_punch, thunder_punch]


class Ponyta(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=18, attack=31, defense=20, special_attack=24, special_defense=24, speed=33,
        ptype1=Fire, name="Ponyta", front_image="images/ponyta_front.png", back_image="images/ponyta_back.png")
        self.move1 = flame_wheel
        self.move2 = spark
        self.move3 = iron_tail
        self.move4 = hidden_power_ground
        self.move_list = [flame_wheel, spark, iron_tail, hidden_power_ground, flamethrower, Return]
        self.move_set = [flame_wheel, spark, iron_tail, hidden_power_ground]


class Rapidash(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=19, attack=30, defense=21, special_attack=24, special_defense=24, speed=32,
        ptype1=Fire, name="Rapidash", front_image="images/rapidash_front.png", back_image="images/rapidash_back.png")
        self.move1 = flame_wheel
        self.move2 = spark
        self.move3 = drill_run
        self.move4 = megahorn
        self.move_list = [flame_wheel, spark, drill_run, megahorn, poison_jab, iron_tail, hidden_power_ground, flamethrower, Return]
        self.move_set = [flame_wheel, spark, drill_run, megahorn]


class Slowpoke(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=43, attack=31, defense=31, special_attack=19, special_defense=19, speed=7,
        ptype1=Psychic, name="Slowpoke", front_image="images/slowpoke_front.png", back_image="images/slowpoke_back.png", ptype2=Water)
        self.move1 = aqua_tail
        self.move2 = zen_headbutt
        self.move3 = earthquake
        self.move4 = flamethrower
        self.move_list = [aqua_tail, zen_headbutt, earthquake, flamethrower, surf, psychic, signal_beam, shadow_ball, Return, ice_beam]
        self.move_set = [aqua_tail, zen_headbutt, earthquake, flamethrower]


class Slowbro(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=29, attack=23, defense=34, special_attack=31, special_defense=24, speed=9,
        ptype1=Psychic, name="Slowbro", front_image="images/slowbro_front.png", back_image="images/slowbro_back.png", ptype2=Water)
        self.move1 = surf
        self.move2 = psychic
        self.move3 = ice_beam
        self.move4 = flamethrower
        self.move_list = [surf, psychic, ice_beam, flamethrower, aqua_tail, zen_headbutt, earthquake, signal_beam, shadow_ball, Return]
        self.move_set = [surf, psychic, ice_beam, flamethrower]


class Slowking(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=29, attack=23, defense=24, special_attack=31, special_defense=34, speed=9,
        ptype1=Psychic, name="Slowking", front_image="images/slowking_front.png", back_image="images/slowking_back.png", ptype2=Water)
        self.move1 = surf
        self.move2 = psychic
        self.move3 = ice_beam
        self.move4 = flamethrower
        self.move_list = [surf, psychic, ice_beam, flamethrower, aqua_tail, zen_headbutt, earthquake, signal_beam, shadow_ball, Return]
        self.move_set = [surf, psychic, ice_beam, flamethrower]


class Magnemite(Pokemon):
    move_list = [flash_cannon, signal_beam, thunderbolt, Return]
    move1 = flash_cannon
    move2 = thunderbolt
    move3 = signal_beam
    move4 = hidden_power_ground
    move_set = [move1, move2, move3, move4]
    front_image = 'images/magnemite_front.png'
    back_image = 'images/magnemite_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=12, attack=16, defense=32, special_attack=44, special_defense=25, speed=21,
        ptype1=Electric, name="Magnemite", front_image=Magnemite.front_image, back_image=Magnemite.back_image, ptype2=Steel)
        self.move1 = Magnemite.move1
        self.move2 = Magnemite.move2
        self.move3 = Magnemite.move3
        self.move4 = Magnemite.move4
        self.move_list = Magnemite.move_list
        self.move_set = Magnemite.move_set


class Magneton(Pokemon):
    move_list = [flash_cannon, signal_beam, thunderbolt, Return]
    move1 = flash_cannon
    move2 = thunderbolt
    move3 = signal_beam
    move4 = hidden_power_ground
    move_set = [move1, move2, move3, move4]
    front_image = 'images/magneton_front.png'
    back_image = 'images/magneton_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=16, attack=19, defense=31, special_attack=39, special_defense=23, speed=23,
        ptype1=Electric, name="Magneton", front_image=Magneton.front_image, back_image=Magneton.back_image, ptype2=Steel)
        self.move1 = Magneton.move1
        self.move2 = Magneton.move2
        self.move3 = Magneton.move3
        self.move4 = Magneton.move4
        self.move_list = Magneton.move_list
        self.move_set = Magneton.move_set


class Magnezone(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=20, attack=20, defense=32, special_attack=36, special_defense=25, speed=17,
        ptype1=Electric, name="Magnezone", front_image="images/magnezone_front.png", back_image="images/magnezone_back.png", ptype2=Steel)
        self.move1 = flash_cannon
        self.move2 = thunderbolt
        self.move3 = signal_beam
        self.move4 = hidden_power_ground
        self.move_list = [flash_cannon, thunderbolt, signal_beam, hidden_power_ground, hidden_power_fire, iron_head, Return, spark]
        self.move_set = [flash_cannon, thunderbolt, signal_beam, hidden_power_ground]


class Farfetchd(Pokemon):
    move_list = [aerial_ace, air_slash, leaf_blade, iron_tail, poison_jab]
    move1 = aerial_ace
    move2 = air_slash
    move3 = leaf_blade
    move4 = iron_tail
    move_set = [move1, move2, move3, move4]
    front_image = 'images/farfetchd_front.png'
    back_image = 'images/farfetchd_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=22, attack=28, defense=23, special_attack=25, special_defense=26, speed=26,
        ptype1=Flying, name="Farfetch'd", front_image=Farfetchd.front_image, back_image=Farfetchd.back_image, ptype2=Normal)
        self.move1 = Farfetchd.move1
        self.move2 = Farfetchd.move2
        self.move3 = Farfetchd.move3
        self.move4 = Farfetchd.move4
        self.move_list = Farfetchd.move_list
        self.move_set = Farfetchd.move_set


class Doduo(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=17, attack=41, defense=22, special_attack=17, special_defense=17, speed=36,
        ptype1=Flying, name="Doduo", front_image="images/doduo_front.png", back_image="images/doduo_back.png", ptype2=Normal)
        self.move1 = drill_peck
        self.move2 = Return
        self.move3 = steel_wing
        self.move4 = hidden_power_ground
        self.move_list = [drill_peck, Return, steel_wing, hidden_power_ground]
        self.move_set = [drill_peck, Return, steel_wing, hidden_power_ground]


class Dodrio(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=20, attack=36, defense=23, special_attack=19, special_defense=19, speed=33,
        ptype1=Flying, name="Dodrio", front_image="images/dodrio_front.png", back_image="images/dodrio_back.png", ptype2=Normal)
        self.move1 = drill_peck
        self.move2 = Return
        self.move3 = steel_wing
        self.move4 = hidden_power_ground
        self.move_list = [drill_peck, Return, steel_wing, hidden_power_ground]
        self.move_set = [drill_peck, Return, steel_wing, hidden_power_ground]


class Seel(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=30, attack=21, defense=25, special_attack=21, special_defense=32, speed=21,
        ptype1=Water, name="Seel", front_image="images/seel_front.png", back_image="images/seel_back.png")
        self.move1 = surf
        self.move2 = ice_beam
        self.move3 = drill_run
        self.move4 = iron_tail
        self.move_list = [surf, ice_beam, drill_run, iron_tail, waterfall, aqua_tail, Return, signal_beam]
        self.move_set = [surf, ice_beam, drill_run, iron_tail]


class Dewgong(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=29, attack=22, defense=25, special_attack=22, special_defense=30, speed=22,
        ptype1=Water, name="Dewgong", front_image="images/dewgong_front.png", back_image="images/dewgong_back.png", ptype2=Ice)
        self.move1 = surf
        self.move2 = ice_beam
        self.move3 = drill_run
        self.move4 = iron_tail
        self.move_list = [surf, ice_beam, drill_run, iron_tail, waterfall, aqua_tail, Return, signal_beam]
        self.move_set = [surf, ice_beam, drill_run, iron_tail]


class Grimer(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=37, attack=37, defense=23, special_attack=18, special_defense=23, speed=12,
        ptype1=Poison, name="Grimer", front_image="images/grimer_front.png", back_image="images/grimer_back.png")
        self.move1 = poison_jab
        self.move2 = fire_punch
        self.move3 = shadow_punch
        self.move4 = hidden_power_ground
        self.move_list = [poison_jab, fire_punch, shadow_punch, hidden_power_ground, thunder_punch, ice_punch, sludge_bomb, shadow_ball, thunderbolt, flamethrower, Return]
        self.move_set = [poison_jab, fire_punch, shadow_punch, hidden_power_ground]


class Muk(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=32, attack=32, defense=23, special_attack=19, special_defense=30, speed=14,
        ptype1=Poison, name="Muk", front_image="images/muk_front.png", back_image="images/muk_back.png")
        self.move1 = poison_jab
        self.move2 = fire_punch
        self.move3 = shadow_punch
        self.move4 = hidden_power_ground
        self.move_list = [poison_jab, fire_punch, shadow_punch, hidden_power_ground, brick_break, dark_pulse, thunder_punch, ice_punch, sludge_bomb, shadow_ball, thunderbolt, flamethrower, Return, rock_slide]
        self.move_set = [poison_jab, fire_punch, shadow_punch, hidden_power_ground]


class Shellder(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=15, attack=32, defense=49, special_attack=22, special_defense=12, speed=20,
        ptype1=Water, name="Shellder", front_image="images/shellder_front.png", back_image="images/shellder_back.png")
        self.move1 = razor_shell
        self.move2 = icicle_spear
        self.move3 = Return
        self.move4 = hidden_power_ground
        self.move_list = [razor_shell, icicle_spear, Return, hidden_power_ground, surf, ice_beam]
        self.move_set = [razor_shell, icicle_spear, Return, hidden_power_ground]



class Cloyster(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=14, attack=27, defense=52, special_attack=24, special_defense=13, speed=20,
        ptype1=Water, name="Cloyster", front_image="images/cloyster_front.png", back_image="images/cloyster_back.png", ptype2=Ice)
        self.move1 = razor_shell
        self.move2 = icicle_spear
        self.move3 = Return
        self.move4 = hidden_power_ground
        self.move_list = [razor_shell, icicle_spear, Return, hidden_power_ground, surf, ice_beam]
        self.move_set = [razor_shell, icicle_spear, Return, hidden_power_ground]


class Ghastly(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=15, attack=16, defense=15, special_attack=48, special_defense=17, speed=39,
        ptype1=Ghost, name="Ghastly", front_image="images/ghastly_front.png", back_image="images/ghastly_back.png", ptype2=Poison)
        self.move1 = shadow_ball
        self.move2 = sludge_bomb
        self.move3 = psychic
        self.move4 = hidden_power_ground
        self.move_list = [shadow_ball, sludge_bomb, psychic, hidden_power_ground, dark_pulse, thunderbolt, signal_beam]
        self.move_set = [shadow_ball, sludge_bomb, psychic, hidden_power_ground]


class Haunter(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=17, attack=18, defense=17, special_attack=43, special_defense=20, speed=35,
        ptype1=Ghost, name="Haunter", front_image="images/haunter_front.png", back_image="images/haunter_back.png", ptype2=Poison)
        self.move1 = shadow_ball
        self.move2 = sludge_bomb
        self.move3 = psychic
        self.move4 = hidden_power_ground
        self.move_list = [shadow_ball, sludge_bomb, psychic, hidden_power_ground, dark_pulse, thunderbolt, signal_beam]
        self.move_set = [shadow_ball, sludge_bomb, psychic, hidden_power_ground]


class Gengar(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=18, attack=19, defense=18, special_attack=39, special_defense=23, speed=33,
        ptype1=Ghost, name="Gengar", front_image="images/gengar_front.png", back_image="images/gengar_back.png", ptype2=Poison)
        self.move1 = shadow_ball
        self.move2 = sludge_bomb
        self.move3 = psychic
        self.move4 = hidden_power_ground
        self.move_list = [shadow_ball, sludge_bomb, psychic, hidden_power_ground, dark_pulse, thunderbolt, signal_beam]
        self.move_set = [shadow_ball, sludge_bomb, psychic, hidden_power_ground]


class Onix(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=14, attack=18, defense=62, special_attack=11, special_defense=18, speed=27,
        ptype1=Ground, name="Onix", front_image="images/onix_front.png", back_image="images/onix_back.png", ptype2=Rock)
        self.move1 = earthquake
        self.move2 = rock_slide
        self.move3 = iron_tail
        self.move4 = hidden_power_grass
        self.move_list = [earthquake, rock_slide, iron_tail, hidden_power_grass]
        self.move_set = [earthquake, rock_slide, iron_tail, hidden_power_grass]


class Steelix(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=22, attack=25, defense=59, special_attack=16, special_defense=19, speed=9,
        ptype1=Ground, name="Steelix", front_image="images/steelix_front.png", back_image="images/steelix_back.png", ptype2=Steel)
        self.move1 = earthquake
        self.move2 = iron_tail
        self.move3 = aqua_tail
        self.move4 = crunch
        self.move_list = [earthquake, iron_tail, aqua_tail, crunch, fire_fang, Return, rock_slide, dragon_pulse]
        self.move_set = [earthquake, iron_tail, aqua_tail, crunch]


class Drowzee(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=27, attack=22, defense=21, special_attack=20, special_defense=41, speed=19,
        ptype1=Psychic, name="Drowzee", front_image="images/drowzee_front.png", back_image="images/drowzee_back.png")
        self.move1 = zen_headbutt
        self.move2 = fire_punch
        self.move3 = ice_punch
        self.move4 = thunder_punch
        self.move_list = [zen_headbutt, fire_punch, ice_punch, thunder_punch]
        self.move_set = [zen_headbutt, fire_punch, ice_punch, thunder_punch]


class Hypno(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=26, attack=23, defense=22, special_attack=23, special_defense=35, speed=21,
        ptype1=Psychic, name="Hypno", front_image="images/hypno_front.png", back_image="images/hypno_back.png")
        self.move1 = psychic
        self.move2 = fire_punch
        self.move3 = ice_punch
        self.move4 = thunder_punch
        self.move_list = [psychic, fire_punch, ice_punch, thunder_punch, zen_headbutt]
        self.move_set = [psychic, fire_punch, ice_punch, thunder_punch, zen_headbutt]


class Krabby(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=14, attack=48, defense=42, special_attack=11, special_defense=12, speed=23,
        ptype1=Water, name="Krabby", front_image="images/krabby_front.png", back_image="images/krabby_back.png")
        self.move1 = crabhammer
        self.move2 = rock_slide
        self.move3 = brick_break
        self.move4 = x_scissor
        self.move_list = [crabhammer, rock_slide, brick_break, x_scissor]
        self.move_set = [crabhammer, rock_slide, brick_break, x_scissor]


class Kingler(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=17, attack=41, defense=36, special_attack=16, special_defense=16, speed=24,
        ptype1=Water, name="Kingler", front_image="images/kingler_front.png", back_image="images/kingler_back.png")
        self.move1 = crabhammer
        self.move2 = rock_slide
        self.move3 = brick_break
        self.move4 = x_scissor
        self.move_list = [crabhammer, rock_slide, brick_break, x_scissor]
        self.move_set = [crabhammer, rock_slide, brick_break, x_scissor]


class Voltorb(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=18, attack=14, defense=23, special_attack=25, special_defense=25, speed=45,
        ptype1=Electric, name="Voltorb", front_image="images/voltorb_front.png", back_image="images/voltorb_back.png")
        self.move1 = thunderbolt
        self.move2 = signal_beam
        self.move3 = Return
        self.move4 = hidden_power_ground
        self.move_list = [thunderbolt, signal_beam, Return, hidden_power_ground]
        self.move_set = [thunderbolt, signal_beam, Return, hidden_power_ground]


class Electrode(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=19, attack=15, defense=22, special_attack=25, special_defense=25, speed=44,
        ptype1=Electric, name="Electrode", front_image="images/electrode_front.png", back_image="images/electrode_back.png")
        self.move1 = thunderbolt
        self.move2 = signal_beam
        self.move3 = Return
        self.move4 = hidden_power_ground
        self.move_list = [thunderbolt, signal_beam, Return, hidden_power_ground]
        self.move_set = [thunderbolt, signal_beam, Return, hidden_power_ground]


class Exeggcute(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=28, attack=18, defense=37, special_attack=28, special_defense=21, speed=18,
        ptype1=Grass, name="Exeggcute", front_image="images/exeggcute_front.png", back_image="images/exeggcute_back.png", ptype2=Psychic)
        self.move1 = psychic
        self.move2 = energy_ball
        self.move3 = sludge_bomb
        self.move4 = hidden_power_ground
        self.move_list = [psychic, energy_ball, sludge_bomb, hidden_power_ground, ancient_power]
        self.move_set = [psychic, energy_ball, sludge_bomb, hidden_power_ground]


class Exeggutor(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=27, attack=27, defense=25, special_attack=36, special_defense=19, speed=16,
        ptype1=Grass, name="Exeggutor", front_image="images/exeggutor_front.png", back_image="images/exeggutor_back.png", ptype2=Psychic)
        self.move1 = psychic
        self.move2 = energy_ball
        self.move3 = sludge_bomb
        self.move4 = hidden_power_ground
        self.move_list = [psychic, energy_ball, sludge_bomb, hidden_power_ground, ancient_power]
        self.move_set = [psychic, energy_ball, sludge_bomb, hidden_power_ground]


class Cubone(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=23, attack=23, defense=45, special_attack=19, special_defense=23, speed=17,
        ptype1=Ground, name="Cubone", front_image="images/cubone_front.png", back_image="images/cubone_back.png")
        self.move1 = earthquake
        self.move2 = rock_slide
        self.move3 = thunder_punch
        self.move4 = fire_punch
        self.move_list = [earthquake, rock_slide, thunder_punch, fire_punch, aerial_ace, brick_break, flamethrower, ice_beam, iron_tail, Return]
        self.move_set = [earthquake, rock_slide, thunder_punch, fire_punch]


class Thick_Club_Cubone(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=20, attack=41, defense=39, special_attack=16, special_defense=20, speed=14,
        ptype1=Ground, name="Thick Club Cubone", front_image="images/cubone_front.png", back_image="images/cubone_back.png")
        self.move1 = earthquake
        self.move2 = rock_slide
        self.move3 = thunder_punch
        self.move4 = fire_punch
        self.move_list = [earthquake, rock_slide, thunder_punch, fire_punch, aerial_ace, brick_break, flamethrower, ice_beam, iron_tail, Return]
        self.move_set = [earthquake, rock_slide, thunder_punch, fire_punch]


class Marowak(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=21, attack=28, defense=39, special_attack=18, special_defense=28, speed=16,
        ptype1=Ground, name="Marowak", front_image="images/Marowak_front.png", back_image="images/Marowak_back.png")
        self.move1 = earthquake
        self.move2 = rock_slide
        self.move3 = thunder_punch
        self.move4 = fire_punch
        self.move_list = [earthquake, rock_slide, thunder_punch, fire_punch, aerial_ace, brick_break, flamethrower, ice_beam, iron_tail, Return]
        self.move_set = [earthquake, rock_slide, thunder_punch, fire_punch]


class Thick_Club_Marowak(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=18, attack=48, defense=33, special_attack=14, special_defense=24, speed=13,
        ptype1=Ground, name="Thick Club Marowak", front_image="images/Marowak_front.png", back_image="images/Marowak_back.png")
        self.move1 = earthquake
        self.move2 = rock_slide
        self.move3 = thunder_punch
        self.move4 = fire_punch
        self.move_list = [earthquake, rock_slide, thunder_punch, fire_punch, aerial_ace, brick_break, flamethrower, ice_beam, iron_tail, Return]
        self.move_set = [earthquake, rock_slide, thunder_punch, fire_punch]


class Hitmonlee(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=16, attack=40, defense=17, special_attack=12, special_defense=36, speed=29,
        ptype1=Fight, name="Hitmonlee", front_image="images/hitmonlee_front.png", back_image="images/hitmonlee_back.png")
        self.move1 = jump_kick
        self.move2 = blaze_kick
        self.move3 = earthquake
        self.move4 = poison_jab
        self.move_list = [jump_kick, blaze_kick, earthquake, poison_jab, rock_slide, Return]
        self.move_set = [jump_kick, blaze_kick, earthquake, poison_jab]


class Hitmonchan(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=16, attack=35, defense=26, special_attack=12, special_defense=36, speed=25,
        ptype1=Fight, name="Hitmonchan", front_image="images/hitmonchan_front.png", back_image="images/hitmonchan_back.png")
        self.move1 = sky_uppercut
        self.move2 = earthquake
        self.move3 = ice_punch
        self.move4 = thunder_punch
        self.move_list = [sky_uppercut, earthquake, ice_punch, thunder_punch, fire_punch, rock_slide, Return]
        self.move_set = [sky_uppercut, earthquake, ice_punch, thunder_punch]


class Hitmontop(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=16, attack=31, defense=31, special_attack=12, special_defense=36, speed=24,
        ptype1=Fight, name="Hitmontop", front_image="images/hitmontop_front.png", back_image="images/hitmontop_back.png")
        self.move1 = brick_break
        self.move2 = earthquake
        self.move3 = rock_slide
        self.move4 = aerial_ace
        self.move_list = [brick_break, earthquake, rock_slide, aerial_ace, Return]
        self.move_set = [brick_break, earthquake, rock_slide, aerial_ace]


class Lickitung(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=35, attack=22, defense=29, special_attack=23, special_defense=29, speed=12,
        ptype1=Normal, name="Lickitung", front_image="images/lickitung_front.png", back_image="images/lickitung_back.png")
        self.move1 = mega_kick
        self.move2 = earthquake
        self.move3 = thunderbolt
        self.move4 = ice_beam
        self.move_list = [mega_kick, earthquake, thunderbolt, ice_beam, aqua_tail, brick_break, flamethrower, fire_punch, ice_punch, iron_tail, power_whip, rock_slide, shadow_ball, surf, thunder_punch, zen_headbutt]
        self.move_set = [mega_kick, earthquake, thunderbolt, ice_beam]


class Lickilicky(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=32, attack=25, defense=28, special_attack=23, special_defense=28, speed=14,
        ptype1=Normal, name="Lickilicky", front_image="images/lickilicky_front.png", back_image="images/lickilicky_back.png")
        self.move1 = mega_kick
        self.move2 = earthquake
        self.move3 = thunderbolt
        self.move4 = ice_beam
        self.move_list = [mega_kick, earthquake, thunderbolt, ice_beam, aqua_tail, brick_break, flamethrower, fire_punch, ice_punch, iron_tail, power_whip, rock_slide, shadow_ball, surf, thunder_punch, zen_headbutt]
        self.move_set = [mega_kick, earthquake, thunderbolt, ice_beam]


class Koffing(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=18, attack=29, defense=42, special_attack=27, special_defense=20, speed=15,
        ptype1=Poison, name="Koffing", front_image="images/koffing_front.png", back_image="images/koffing_back.png")
        self.move1 = sludge_wave
        self.move2 = flamethrower
        self.move3 = thunderbolt
        self.move4 = hidden_power_ground
        self.move_list = [sludge_wave, flamethrower, thunderbolt, hidden_power_ground, dark_pulse, shadow_ball, Return]
        self.move_set = [sludge_wave, flamethrower, thunderbolt, hidden_power_ground]


class Weezing(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=20, attack=28, defense=37, special_attack=26, special_defense=21, speed=18,
        ptype1=Poison, name="Weezing", front_image="images/Weezing_front.png", back_image="images/Weezing_back.png")
        self.move1 = sludge_wave
        self.move2 = flamethrower
        self.move3 = thunderbolt
        self.move4 = hidden_power_ground
        self.move_list = [sludge_wave, flamethrower, thunderbolt, hidden_power_ground, dark_pulse, shadow_ball, Return]
        self.move_set = [sludge_wave, flamethrower, thunderbolt, hidden_power_ground]


class Rhyhorn(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=35, attack=37, defense=41, special_attack=13, special_defense=13, speed=11,
        ptype1=Ground, name="Rhyhorn", front_image="images/rhyhorn_front.png", back_image="images/rhyhorn_back.png", ptype2=Rock)
        self.move1 = earthquake
        self.move2 = rock_slide
        self.move3 = aqua_tail
        self.move4 = megahorn
        self.move_list = [earthquake, rock_slide, aqua_tail, megahorn, ice_fang, thunder_fang, ancient_power, crunch, dragon_pulse, earth_power, flamethrower, ice_beam, iron_tail, fire_fang, poison_jab, Return, thunderbolt]
        self.move_set = [earthquake, rock_slide, aqua_tail, megahorn]


class Rhydon(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=33, attack=40, defense=37, special_attack=14, special_defense=14, speed=12,
        ptype1=Ground, name="Rhydon", front_image="images/rhydon_front.png", back_image="images/rhydon_back.png", ptype2=Rock)
        self.move1 = earthquake
        self.move2 = rock_slide
        self.move3 = aqua_tail
        self.move4 = megahorn
        self.move_list = [earthquake, rock_slide, aqua_tail, megahorn, brick_break, fire_punch, thunder_punch, ice_punch, fire_fang, ice_fang, thunder_fang, ancient_power, crunch, dragon_pulse, earth_power, flamethrower, ice_beam, iron_tail, poison_jab, Return, thunderbolt]
        self.move_set = [earthquake, rock_slide, aqua_tail, megahorn]


class Rhyperior(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=32, attack=39, defense=36, special_attack=16, special_defense=16, speed=11,
        ptype1=Ground, name="Rhyperior", front_image="images/rhyperior_front.png", back_image="images/rhyperior_back.png", ptype2=Rock)
        self.move1 = earthquake
        self.move2 = rock_slide
        self.move3 = aqua_tail
        self.move4 = megahorn
        self.move_list = [earthquake, rock_slide, aqua_tail, megahorn, brick_break, fire_punch, thunder_punch, ice_punch, fire_fang, ice_fang, thunder_fang, ancient_power, crunch, dragon_pulse, earth_power, flamethrower, ice_beam, iron_tail, poison_jab, Return, thunderbolt]
        self.move_set = [earthquake, rock_slide, aqua_tail, megahorn]


class Chansey(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=83, attack=1, defense=2, special_attack=12, special_defense=35, speed=17,
        ptype1=Normal, name="Chansey", front_image="images/chansey_front.png", back_image="images/chansey_back.png")
        self.move1 = hyper_voice
        self.move2 = ice_beam
        self.move3 = thunderbolt
        self.move4 = psychic
        self.move_list = [hyper_voice, ice_beam, thunderbolt, flamethrower, psychic, dazzling_gleam, shadow_ball]
        self.move_set = [hyper_voice, ice_beam, thunderbolt, flamethrower]


class Blissey(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=71, attack=3, defense=3, special_attack=21, special_defense=37, speed=15,
        ptype1=Normal, name="Blissey", front_image="images/Blissey_front.png", back_image="images/Blissey_back.png")
        self.move1 = hyper_voice
        self.move2 = ice_beam
        self.move3 = thunderbolt
        self.move4 = psychic
        self.move_list = [hyper_voice, ice_beam, thunderbolt, flamethrower, psychic, dazzling_gleam, shadow_ball]
        self.move_set = [hyper_voice, ice_beam, thunderbolt, flamethrower]


class Tangela(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=22, attack=19, defense=40, special_attack=34, special_defense=14, speed=21,
        ptype1=Grass, name="Tangela", front_image="images/tangela_front.png", back_image="images/tangela_back.png")
        self.move1 = energy_ball
        self.move2 = sludge_bomb
        self.move3 = ancient_power
        self.move4 = hidden_power_fire
        self.move_list = [energy_ball, sludge_bomb, ancient_power, hidden_power_fire, dark_pulse, hidden_power_ice]
        self.move_set = [energy_ball, sludge_bomb, ancient_power, hidden_power_fire]


class Tangrowth(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=28, attack=28, defense=35, special_attack=31, special_defense=14, speed=14,
        ptype1=Grass, name="Tangrowth", front_image="images/tangrowth_front.png", back_image="images/tangrowth_back.png")
        self.move1 = energy_ball
        self.move2 = sludge_bomb
        self.move3 = earthquake
        self.move4 = hidden_power_fire
        self.move_list = [energy_ball, sludge_bomb, earthquake, hidden_power_fire, ancient_power, dark_pulse, hidden_power_ice, aerial_ace, brick_break, poison_jab, power_whip, rock_slide, Return]
        self.move_set = [energy_ball, sludge_bomb, earthquake, hidden_power_fire]


class Kangaskhan(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=32, attack=29, defense=24, special_attack=13, special_defense=24, speed=28,
        ptype1=Normal, name="Kangaskhan", front_image="images/kangaskhan_front.png", back_image="images/kangaskhan_back.png")
        self.move1 = double_edge
        self.move2 = drain_punch
        self.move3 = sucker_punch
        self.move4 = fake_out
        self.move_list = [double_edge, drain_punch, sucker_punch, fake_out, earthquake, mega_kick, brick_break, iron_tail, Return, scratch, shadow_claw, fire_punch, thunder_punch, ice_punch]
        self.move_set = [double_edge, drain_punch, sucker_punch, fake_out]


class Horsea(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=15, attack=19, defense=36, special_attack=36, special_defense=13, speed=31,
        ptype1=Water, name="Horsea", front_image="images/horsea_front.png", back_image="images/horsea_back.png")
        self.move1 = surf
        self.move2 = ice_beam
        self.move3 = hidden_power_ground
        self.move4 = Return
        self.move_list = [surf, ice_beam, hidden_power_ground, Return, flash_cannon, dragon_pulse, hidden_power_grass, signal_beam, waterfall]
        self.move_set = [surf, ice_beam, hidden_power_ground, Return]


class Seadra(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=19, attack=22, defense=32, special_attack=32, special_defense=16, speed=29,
        ptype1=Water, name="Seadra", front_image="images/Seadra_front.png", back_image="images/Seadra_back.png")
        self.move1 = surf
        self.move2 = ice_beam
        self.move3 = hidden_power_ground
        self.move4 = Return
        self.move_list = [surf, ice_beam, hidden_power_ground, Return, flash_cannon, dragon_pulse, hidden_power_grass, signal_beam, waterfall]
        self.move_set = [surf, ice_beam, hidden_power_ground, Return]


class Kingdra(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=22, attack=26, defense=26, special_attack=26, special_defense=26, speed=24,
        ptype1=Water, name="Kingdra", front_image="images/Kingdra_front.png", back_image="images/Kingdra_back.png", ptype2=Dragon)
        self.move1 = surf
        self.move2 = ice_beam
        self.move3 = hidden_power_ground
        self.move4 = dragon_pulse
        self.move_list = [surf, ice_beam, hidden_power_ground, dragon_pulse, Return, flash_cannon, hidden_power_grass, signal_beam, waterfall]
        self.move_set = [surf, ice_beam, hidden_power_ground, dragon_pulse]


class Goldeen(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=21, attack=31, defense=28, special_attack=16, special_defense=24, speed=30,
        ptype1=Water, name="Goldeen", front_image="images/goldeen_front.png", back_image="images/goldeen_back.png")
        self.move1 = aqua_tail
        self.move2 = drill_run
        self.move3 = megahorn
        self.move4 = poison_jab
        self.move_list = [aqua_tail, drill_run, megahorn, poison_jab, ice_beam, signal_beam, surf]
        self.move_set = [aqua_tail, drill_run, megahorn, poison_jab]


class Seaking(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=27, attack=31, defense=21, special_attack=21, special_defense=26, speed=23,
        ptype1=Water, name="Seaking", front_image="images/Seaking_front.png", back_image="images/Seaking_back.png")
        self.move1 = aqua_tail
        self.move2 = drill_run
        self.move3 = megahorn
        self.move4 = poison_jab
        self.move_list = [aqua_tail, drill_run, megahorn, poison_jab, ice_beam, signal_beam, surf]
        self.move_set = [aqua_tail, drill_run, megahorn, poison_jab]


class Staryu(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=13, attack=20, defense=24, special_attack=31, special_defense=24, speed=38,
        ptype1=Water, name="Staryu", front_image="images/staryu_front.png", back_image="images/staryu_back.png")
        self.move1 = surf
        self.move2 = ice_beam
        self.move3 = thunderbolt
        self.move4 = psychic
        self.move_list = [surf, ice_beam, thunderbolt, psychic, dazzling_gleam, flash_cannon, power_gem, Return, signal_beam, waterfall]
        self.move_set = [surf, ice_beam, thunderbolt, psychic]


class Starmie(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=17, attack=21, defense=25, special_attack=29, special_defense=25, speed=33,
        ptype1=Water, name="Starmie", front_image="images/starmie_front.png", back_image="images/starmie_back.png", ptype2=Psychic)
        self.move1 = surf
        self.move2 = ice_beam
        self.move3 = thunderbolt
        self.move4 = psychic
        self.move_list = [surf, ice_beam, thunderbolt, psychic, dazzling_gleam, flash_cannon, power_gem, Return, signal_beam, waterfall]
        self.move_set = [surf, ice_beam, thunderbolt, psychic]


class MimeJr(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=10, attack=12, defense=22, special_attack=34, special_defense=43, speed=29,
        ptype1=Psychic, name="Mime Jr.", front_image="images/mrmimejr_front.png", back_image="images/mrmimejr_back.png", ptype2=Fairy)
        self.move1 = psychic
        self.move2 = signal_beam
        self.move3 = thunderbolt
        self.move4 = hidden_power_ground
        self.move_list = [psychic, signal_beam, thunderbolt, hidden_power_ground, hidden_power_fight, brick_break, Return, shadow_ball]
        self.move_set = [psychic, signal_beam, thunderbolt, hidden_power_ground]


class MrMime(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=13, attack=15, defense=21, special_attack=33, special_defense=39, speed=29,
        ptype1=Psychic, name="Mr. Mime", front_image="images/mrmime_front.png", back_image="images/mrmime_back.png", ptype2=Fairy)
        self.move1 = psychic
        self.move2 = dazzling_gleam
        self.move3 = thunderbolt
        self.move4 = hidden_power_ground
        self.move_list = [psychic, dazzling_gleam, thunderbolt, hidden_power_ground, signal_beam, hidden_power_fight, brick_break, shadow_ball, aerial_ace, energy_ball, fire_punch, ice_punch, mega_kick, thunder_punch, zen_headbutt]
        self.move_set = [psychic, dazzling_gleam, thunderbolt, hidden_power_ground]


class Scyther(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=21, attack=33, defense=24, special_attack=16, special_defense=24, speed=32,
        ptype1=Bug, name="Scyther", front_image="images/scyther_front.png", back_image="images/scyther_back.png", ptype2=Flying)
        self.move1 = aerial_ace
        self.move2 = x_scissor
        self.move3 = brick_break
        self.move4 = u_turn
        self.move_list = [aerial_ace, x_scissor, brick_break, u_turn, night_slash, Return, bug_buzz, air_slash, steel_wing]
        self.move_set = [aerial_ace, x_scissor, brick_break, u_turn]


class Scizor(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=21, attack=39, defense=30, special_attack=16, special_defense=24, speed=20,
        ptype1=Bug, name="Scizor", front_image="images/scizor_front.png", back_image="images/scizor_back.png", ptype2=Steel)
        self.move1 = iron_head
        self.move2 = x_scissor
        self.move3 = brick_break
        self.move4 = night_slash
        self.move_list = [iron_head, x_scissor, brick_break, night_slash, aerial_ace, Return, bug_buzz, air_slash, steel_wing]
        self.move_set = [iron_head, x_scissor, brick_break, night_slash]


class Smoochum(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=22, attack=15, defense=7, special_attack=42, special_defense=32, speed=32,
        ptype1=Ice, name="Smoochum", front_image="images/smoochum_front.png", back_image="images/smoochum_back.png", ptype2=Psychic)
        self.move1 = ice_beam
        self.move2 = psychic
        self.move3 = signal_beam
        self.move4 = hidden_power_ground
        self.move_list = [ice_beam, psychic, signal_beam, hidden_power_ground, ice_punch, mega_kick, shadow_ball, zen_headbutt]
        self.move_set = [ice_beam, psychic, signal_beam, hidden_power_ground]


class Jynx(Pokemon):
    move_list = [ice_beam, ice_punch, psychic, signal_beam, brick_break, energy_ball, shadow_ball]
    move1 = ice_beam
    move2 = psychic
    move3 = signal_beam
    move4 = energy_ball
    move_set = [ice_beam, psychic, signal_beam, energy_ball]
    front_image = 'images/jynx_front.png'
    back_image = 'images/jynx_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=21, attack=16, defense=12, special_attack=38, special_defense=31, speed=31,
        ptype1=Ice, name="Jynx", front_image=Jynx.front_image, back_image=Jynx.back_image, ptype2=Psychic)
        self.move1 = Jynx.move1
        self.move2 = Jynx.move2
        self.move3 = Jynx.move3
        self.move4 = Jynx.move4
        self.move_set = Jynx.move_set
        self.move_list = Jynx.move_list


class Elekid(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=19, attack=26, defense=15, special_attack=27, special_defense=23, speed=40,
        ptype1=Electric, name="Elekid", front_image="images/elekid_front.png", back_image="images/elekid_back.png")
        self.move1 = thunderbolt
        self.move2 = cross_chop
        self.move3 = fire_punch
        self.move4 = hidden_power_grass
        self.move_list = [thunderbolt, cross_chop, fire_punch, hidden_power_grass, hidden_power_ground, fire_punch, ice_punch, mega_kick, signal_beam, thunder_punch]
        self.move_set = [thunderbolt, cross_chop, fire_punch, hidden_power_grass]


class Electabuzz(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=20, attack=25, defense=18, special_attack=29, special_defense=26, speed=32,
        ptype1=Electric, name="Electabuzz", front_image="images/electabuzz_front.png", back_image="images/electabuzz_back.png")
        self.move1 = thunderbolt
        self.move2 = cross_chop
        self.move3 = fire_punch
        self.move4 = hidden_power_grass
        self.move_list = [thunderbolt, cross_chop, fire_punch, hidden_power_grass, hidden_power_ground, fire_punch, ice_punch, mega_kick, signal_beam, thunder_punch, iron_tail]
        self.move_set = [thunderbolt, cross_chop, fire_punch, hidden_power_grass]


class Electivire(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=21, attack=34, defense=19, special_attack=26, special_defense=24, speed=26,
        ptype1=Electric, name="Electivire", front_image="images/electivire_front.png", back_image="images/electivire_back.png")
        self.move1 = thunderbolt
        self.move2 = earthquake
        self.move3 = flamethrower
        self.move4 = hidden_power_grass
        self.move_list = [thunderbolt, earthquake, flamethrower, hidden_power_grass, cross_chop, hidden_power_ground, fire_punch, ice_punch, mega_kick, signal_beam, thunder_punch, iron_tail]
        self.move_set = [thunderbolt, earthquake, flamethrower, hidden_power_grass]


class Magby(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=18, attack=31, defense=15, special_attack=29, special_defense=23, speed=34,
        ptype1=Fire, name="Magby", front_image="images/magby_front.png", back_image="images/magby_back.png")
        self.move1 = fire_punch
        self.move2 = thunder_punch
        self.move3 = cross_chop
        self.move4 = mega_kick
        self.move_list = [fire_punch, thunder_punch, cross_chop, mega_kick, heat_wave, iron_tail, psychic]
        self.move_set = [fire_punch, thunder_punch, cross_chop, mega_kick]


class Magmar(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=20, attack=29, defense=17, special_attack=30, special_defense=26, speed=28,
        ptype1=Fire, name="Magmar", front_image="images/magmar_front.png", back_image="images/magmar_back.png")
        self.move1 = heat_wave
        self.move2 = thunder_punch
        self.move3 = cross_chop
        self.move4 = mega_kick
        self.move_list = [heat_wave, thunder_punch, cross_chop, mega_kick, fire_punch, iron_tail, psychic]
        self.move_set = [heat_wave, thunder_punch, cross_chop, mega_kick]


class Magmortar(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=21, attack=26, defense=19, special_attack=35, special_defense=26, speed=23,
        ptype1=Fire, name="Magmortar", front_image="images/magmortar_front.png", back_image="images/magmortar_back.png")
        self.move1 = heat_wave
        self.move2 = thunderbolt
        self.move3 = earthquake
        self.move4 = hidden_power_grass
        self.move_list = [heat_wave, thunderbolt, earthquake, hidden_power_grass, thunder_punch, cross_chop, mega_kick, fire_punch, iron_tail, psychic]
        self.move_set = [heat_wave, thunderbolt, earthquake, hidden_power_grass]


class Pinsir(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=19, attack=38, defense=30, special_attack=16, special_defense=21, speed=26,
        ptype1=Bug, name="Pinsir", front_image="images/pinsir_front.png", back_image="images/pinsir_back.png")
        self.move1 = x_scissor
        self.move2 = earthquake
        self.move3 = rock_slide
        self.move4 = brick_break
        self.move_list = [x_scissor, earthquake, rock_slide, brick_break, Return]
        self.move_set = [x_scissor, earthquake, rock_slide, brick_break]


class Tauros(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=23, attack=31, defense=29, special_attack=12, special_defense=21, speed=34,
        ptype1=Normal, name="Tauros", front_image="images/tauros_front.png", back_image="images/tauros_back.png")
        self.move1 = Return
        self.move2 = earthquake
        self.move3 = iron_tail
        self.move4 = zen_headbutt
        self.move_list = [Return, earthquake, iron_tail, zen_headbutt, flamethrower, ice_beam, rock_slide, surf, thunderbolt]
        self.move_set = [Return, earthquake, iron_tail, zen_headbutt]


class Gyarados(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=26, attack=35, defense=22, special_attack=16, special_defense=28, speed=23,
        ptype1=Water, name="Gyarados", front_image="images/gyarados_front.png", back_image="images/gyarados_back.png", ptype2=Flying)
        self.move1 = aqua_tail
        self.move2 = earthquake
        self.move3 = stone_edge
        self.move4 = flamethrower
        self.move_list = [aqua_tail, earthquake, stone_edge, flamethrower, crunch, dark_pulse, dragon_pulse, ice_beam, ice_fang, iron_tail, surf, thunderbolt]
        self.move_set = [aqua_tail, earthquake, stone_edge, flamethrower]


class Lapras(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=36, attack=24, defense=22, special_attack=24, special_defense=27, speed=17,
        ptype1=Water, name="Lapras", front_image="images/lapras_front.png", back_image="images/lapras_back.png", ptype2=Ice)
        self.move1 = surf
        self.move2 = ice_beam
        self.move3 = thunderbolt
        self.move4 = signal_beam
        self.move_list = [surf, ice_beam, thunderbolt, signal_beam, aqua_tail, dragon_pulse, drill_run, iron_tail, psychic, Return, zen_headbutt]
        self.move_set = [surf, ice_beam, thunderbolt, signal_beam]


class Vaporeon(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=37, attack=19, defense=17, special_attack=31, special_defense=27, speed=19,
        ptype1=Water, name="Vaporeon", front_image="images/vaporeon_front.png", back_image="images/vaporeon_back.png")
        self.move1 = surf
        self.move2 = ice_beam
        self.move3 = signal_beam
        self.move4 = hidden_power_ground
        self.move_list = [surf, ice_beam, signal_beam, hidden_power_ground, hidden_power_grass, aqua_tail, bite, iron_tail, Return, shadow_ball, hyper_voice]
        self.move_set = [surf, ice_beam, signal_beam, hidden_power_ground]


class Jolteon(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=19, attack=19, defense=17, special_attack=31, special_defense=27, speed=37,
        ptype1=Electric, name="Jolteon", front_image="images/Jolteon_front.png", back_image="images/Jolteon_back.png")
        self.move1 = thunderbolt
        self.move2 = signal_beam
        self.move3 = hidden_power_grass
        self.move4 = iron_tail
        self.move_list = [thunderbolt, signal_beam, hidden_power_grass, iron_tail, hidden_power_ground, bite, ]
        self.move_set = [thunderbolt, signal_beam, hidden_power_grass, iron_tail]


class Flareon(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=19, attack=37, defense=17, special_attack=27, special_defense=31, speed=19,
        ptype1=Fire, name="Flareon", front_image="images/Flareon_front.png", back_image="images/Flareon_back.png")
        self.move1 = fire_fang
        self.move2 = heat_wave
        self.move3 = iron_tail
        self.move4 = hidden_power_grass
        self.move_list = [fire_fang, heat_wave, iron_tail, hidden_power_grass, bite, hyper_voice, Return, shadow_ball]
        self.move_set = [fire_fang, heat_wave, iron_tail, hidden_power_grass]


class Espeon(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=19, attack=19, defense=17, special_attack=37, special_defense=27, speed=31,
        ptype1=Psychic, name="Espeon", front_image="images/Espeon_front.png", back_image="images/Espeon_back.png")
        self.move1 = psychic
        self.move2 = dazzling_gleam
        self.move3 = shadow_ball
        self.move4 = hidden_power_ground
        self.move_list = [psychic, dazzling_gleam, shadow_ball, hidden_power_ground, iron_tail, hidden_power_grass, bite, hyper_voice, Return, zen_headbutt, signal_beam]
        self.move_set = [psychic, dazzling_gleam, shadow_ball, hidden_power_ground]


class Umbreon(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=27, attack=19, defense=31, special_attack=17, special_defense=37, speed=19,
        ptype1=Dark, name="Umbreon", front_image="images/Umbreon_front.png", back_image="images/Umbreon_back.png")
        self.move1 = bite
        self.move2 = iron_tail
        self.move3 = hidden_power_ground
        self.move4 = Return
        self.move_list = [bite, iron_tail, Return, hidden_power_ground, hidden_power_grass, hyper_voice, dark_pulse, shadow_ball]
        self.move_set = [bite, iron_tail, Return, hidden_power_ground]


class Leafeon(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=19, attack=31, defense=37, special_attack=17, special_defense=19, speed=27,
        ptype1=Grass, name="Leafeon", front_image="images/Leafeon_front.png", back_image="images/Leafeon_back.png")
        self.move1 = leaf_blade
        self.move2 = iron_tail
        self.move3 = hidden_power_ground
        self.move4 = x_scissor
        self.move_list = [leaf_blade, iron_tail, x_scissor, hidden_power_ground, hyper_voice, shadow_ball, Return, bite, energy_ball]
        self.move_set = [leaf_blade, iron_tail, x_scissor, hidden_power_ground]


class Glaceon(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=19, attack=17, defense=31, special_attack=37, special_defense=27, speed=19,
        ptype1=Ice, name="Glaceon", front_image="images/Glaceon_front.png", back_image="images/Glaceon_back.png")
        self.move1 = ice_beam
        self.move2 = shadow_ball
        self.move3 = hidden_power_ground
        self.move4 = signal_beam
        self.move_list = [ice_beam, shadow_ball, signal_beam, hidden_power_ground, hyper_voice, Return, bite, iron_tail, ice_fang]
        self.move_set = [ice_beam, shadow_ball, signal_beam, hidden_power_ground]


class Porygon(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=25, attack=23, defense=27, special_attack=32, special_defense=28, speed=15,
        ptype1=Normal, name="Porygon", front_image="images/porygon_front.png", back_image="images/porygon_back.png")
        self.move1 = tri_attack
        self.move2 = psychic
        self.move3 = ice_beam
        self.move4 = thunderbolt
        self.move_list = [tri_attack, psychic, ice_beam, thunderbolt, aerial_ace, iron_tail, shadow_ball, signal_beam, zen_headbutt]
        self.move_set = [tri_attack, psychic, ice_beam, thunderbolt]


class Porygon2(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=25, attack=23, defense=26, special_attack=31, special_defense=28, speed=17,
        ptype1=Normal, name="Porygon2", front_image="images/porygon2_front.png", back_image="images/porygon2_back.png")
        self.move1 = tri_attack
        self.move2 = psychic
        self.move3 = ice_beam
        self.move4 = thunderbolt
        self.move_list = [tri_attack, psychic, ice_beam, thunderbolt, aerial_ace, iron_tail, shadow_ball, signal_beam, zen_headbutt]
        self.move_set = [tri_attack, psychic, ice_beam, thunderbolt]


class PorygonZ(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=25, attack=23, defense=26, special_attack=31, special_defense=28, speed=17,
        ptype1=Normal, name="Porygon-Z", front_image="images/porygon-z_front.png", back_image="images/porygon-z_back.png")
        self.move1 = tri_attack
        self.move2 = psychic
        self.move3 = ice_beam
        self.move4 = thunderbolt
        self.move_list = [tri_attack, psychic, ice_beam, thunderbolt, aerial_ace, iron_tail, shadow_ball, signal_beam, zen_headbutt]
        self.move_set = [tri_attack, psychic, ice_beam, thunderbolt]


class Omanyte(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=15, attack=17, defense=42, special_attack=38, special_defense=23, speed=15,
        ptype1=Rock, name="Omanyte", front_image="images/omanyte_front.png", back_image="images/omanyte_back.png", ptype2=Water)
        self.move1 = surf
        self.move2 = ancient_power
        self.move3 = ice_beam
        self.move4 = earth_power
        self.move_list = [surf, ancient_power, ice_beam, earth_power, bite, rock_slide, Return, waterfall]
        self.move_set = [surf, ancient_power, ice_beam, earth_power]
        self.move_set = [tri_attack, psychic, ice_beam, thunderbolt]


class Omastar(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=15, attack=17, defense=42, special_attack=38, special_defense=23, speed=15,
        ptype1=Rock, name="Omastar", front_image="images/omastar_front.png", back_image="images/omastar_back.png", ptype2=Water)
        self.move1 = surf
        self.move2 = ancient_power
        self.move3 = ice_beam
        self.move4 = earth_power
        self.move_list = [surf, ancient_power, ice_beam, earth_power, bite, stone_edge, Return, waterfall]
        self.move_set = [surf, ancient_power, ice_beam, earth_power]


class Kabuto(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=13, attack=34, defense=38, special_attack=23, special_defense=19, speed=23,
        ptype1=Rock, name="Kabuto", front_image="images/Kabuto_front.png", back_image="images/Kabuto_back.png", ptype2=Water)
        self.move1 = waterfall
        self.move2 = rock_slide
        self.move3 = ice_beam
        self.move4 = earth_power
        self.move_list = [waterfall, rock_slide, ice_beam, earth_power, bite, surf, ancient_power, Return, aerial_ace]
        self.move_set = [waterfall, rock_slide, ice_beam, earth_power]


class Kabutops(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=18, attack=35, defense=32, special_attack=20, special_defense=21, speed=24,
        ptype1=Rock, name="Kabutops", front_image="images/Kabutops_front.png", back_image="images/Kabutops_back.png", ptype2=Water)
        self.move1 = aqua_tail
        self.move2 = stone_edge
        self.move3 = ice_beam
        self.move4 = earth_power
        self.move_list = [aqua_tail, stone_edge, ice_beam, earth_power, bite, surf, mega_kick, aerial_ace, x_scissor, brick_break, night_slash]
        self.move_set = [aqua_tail, stone_edge, ice_beam, earth_power]


class Aerodactyl(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=23, attack=31, defense=19, special_attack=17, special_defense=22, speed=38,
        ptype1=Rock, name="Aerodactyl", front_image="images/aerodactyl_front.png", back_image="images/aerodactyl_back.png", ptype2=Flying)
        self.move1 = stone_edge
        self.move2 = earthquake
        self.move3 = aerial_ace
        self.move4 = aqua_tail
        self.move_list = [stone_edge, earthquake, aerial_ace, aqua_tail, dragon_pulse, dragon_claw, iron_tail, ice_fang, fire_fang, thunder_fang, heat_wave, earth_power, crunch, ancient_power]
        self.move_set = [stone_edge, earthquake, aerial_ace, aqua_tail]


class Munchlax(Pokemon):
    move_list = [iron_tail, surf, waterfall, thunder_punch, fire_punch, ice_punch, ice_beam, water_gun, brick_break, Return, crunch, mega_kick, crunch, hyper_voice, Return, shadow_ball, thunder_fang]
    move1 = mega_kick
    move2 = earthquake
    move3 = ice_punch
    move4 = thunder_punch    
    move_set = [move1, move2, move3, move4]
    front_image = 'images/munchlax_front.png'
    back_image = 'images/munchlax_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=52, attack=33, defense=15, special_attack=15, special_defense=33, speed=2,
        ptype1=Normal, name="Munchlax", front_image=Munchlax.front_image, back_image=Munchlax.back_image)
        self.move1 = Munchlax.move1
        self.move2 = Munchlax.move2
        self.move3 = Munchlax.move3
        self.move4 = Munchlax.move4
        self.move_list = Munchlax.move_list
        self.move_set = Munchlax.move_set


class Snorlax(Pokemon):
    move1 = earthquake
    move2 = surf
    move3 = mega_kick
    move4 = ice_punch
    move_list = [iron_tail, surf, waterfall, thunder_punch, fire_punch, ice_punch, ice_beam, water_gun, brick_break, Return, crunch, mega_kick, crunch]
    move_set = [move1, move2, move3, move4]
    front_image = 'images/snorlax_front.png'
    back_image = 'images/snorlax_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=44, attack=31, defense=18, special_attack=18, special_defense=31, speed=8,
        ptype1=Normal, name="Snorlax", front_image=Snorlax.front_image, back_image=Snorlax.back_image)
        self.move1 = Snorlax.move1
        self.move2 = Snorlax.move2
        self.move3 = Snorlax.move3
        self.move4 = Snorlax.move4
        self.move_list = Snorlax.move_list
        self.move_set = Snorlax.move_set


class Articuno(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=23, attack=22, defense=26, special_attack=25, special_defense=32, speed=22,
        ptype1=Ice, name="Articuno", front_image="images/articuno_front.png", back_image="images/articuno_back.png", ptype2=Flying)
        self.move1 = ice_beam
        self.move2 = hurricane
        self.move3 = ancient_power
        self.move4 = hidden_power_ground
        self.move_list = [ice_beam, hurricane, ancient_power, hidden_power_ground, aerial_ace, Return, steel_wing, signal_beam]
        self.move_set = [ice_beam, hurricane, ancient_power, hidden_power_ground]


class Zapdos(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=23, attack=23, defense=22, special_attack=33, special_defense=23, speed=26,
        ptype1=Electric, name="Zapdos", front_image="images/Zapdos_front.png", back_image="images/Zapdos_back.png", ptype2=Flying)
        self.move1 = thunderbolt
        self.move2 = air_cutter
        self.move3 = heat_wave
        self.move4 = hidden_power_grass
        self.move_list = [thunderbolt, air_cutter, heat_wave, hidden_power_grass, hidden_power_ice, aerial_ace, ancient_power, drill_peck, Return, signal_beam]
        self.move_set = [thunderbolt, air_cutter, heat_wave, hidden_power_grass]


class Moltres(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=23, attack=26, defense=23, special_attack=33, special_defense=22, speed=23,
        ptype1=Fire, name="Moltres", front_image="images/Moltres_front.png", back_image="images/Moltres_back.png", ptype2=Flying)
        self.move1 = flamethrower
        self.move2 = hurricane
        self.move3 = ancient_power
        self.move4 = hidden_power_grass
        self.move_list = [flamethrower, hurricane, ancient_power, hidden_power_grass, hidden_power_ice, aerial_ace, drill_peck, Return, steel_wing]
        self.move_set = [flamethrower, hurricane, ancient_power, hidden_power_grass]


class Dratini(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=21, attack=32, defense=22, special_attack=25, special_defense=25, speed=25,
        ptype1=Dragon, name="Dratini", front_image="images/dratini_front.png", back_image="images/dratini_back.png")
        self.move1 = dragon_rush
        self.move2 = aqua_tail
        self.move3 = iron_tail
        self.move4 = flamethrower
        self.move_list = [dragon_rush, aqua_tail, iron_tail, flamethrower, dragon_pulse, ice_beam, Return, thunderbolt, surf]
        self.move_set = [dragon_rush, aqua_tail, iron_tail, flamethrower]


class Dragonair(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=22, attack=30, defense=23, special_attack=25, special_defense=25, speed=25,
        ptype1=Dragon, name="Dragonair", front_image="images/dragonair_front.png", back_image="images/dragonair_back.png")
        self.move1 = dragon_rush
        self.move2 = aqua_tail
        self.move3 = iron_tail
        self.move4 = flamethrower
        self.move_list = [dragon_rush, aqua_tail, iron_tail, flamethrower, dragon_pulse, ice_beam, Return, thunderbolt, surf]
        self.move_set = [dragon_rush, aqua_tail, iron_tail, flamethrower]


class Dragonite(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=23, attack=33, defense=24, special_attack=25, special_defense=25, speed=20,
        ptype1=Dragon, name="Dragonite", front_image="images/dragonite_front.png", back_image="images/dragonite_back.png", ptype2=Flying)
        self.move1 = dragon_rush
        self.move2 = earthquake
        self.move3 = fire_punch
        self.move4 = iron_tail
        self.move_list = [dragon_rush, earthquake, fire_punch, iron_tail, aqua_tail, heat_wave, dragon_pulse, ice_beam, Return, thunderbolt, surf, aerial_ace, hurricane, ice_punch, stone_edge, thunder_punch]
        self.move_set = [dragon_rush, earthquake, iron_tail, fire_punch]


class Mewtwo(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=23, attack=24, defense=20, special_attack=34, special_defense=20, speed=29,
        ptype1=Psychic, name="Mewtwo", front_image="images/mewtwo_front.png", back_image="images/mewtwo_back.png")
        self.move1 = psychic
        self.move2 = ice_beam
        self.move3 = thunderbolt
        self.move4 = earth_power
        self.move_list = [psychic, ice_beam, thunderbolt, earth_power, flamethrower, shadow_punch, dark_pulse]
        self.move_set = [psychic, ice_beam, thunderbolt, earth_power]


class Mew(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=25, attack=25, defense=25, special_attack=25, special_defense=25, speed=25,
        ptype1=Psychic, name="Mew", front_image="images/mew_front.png", back_image="images/mew_back.png")
        self.move_list = []
        for move in Move.all_moves:
            self.move_list.append(move)
        self.move1 = random.choice(self.move_list)
        self.move2 = random.choice(self.move_list)
        self.move3 = random.choice(self.move_list)
        self.move4 = random.choice(self.move_list)
        self.move_set = [self.move1, self.move2, self.move3, self.move4]


class Chikorita(Pokemon):
    move_list = [energy_ball, ancient_power, Return, iron_tail]
    move1 = energy_ball
    move2 = ancient_power
    move3 = Return
    move4 = iron_tail
    move_set = [energy_ball, ancient_power, Return, iron_tail]
    front_image = 'images/chikorita_front.png'
    back_image = 'images/chikorita_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=21, attack=23, defense=31, special_attack=23, special_defense=31, speed=21,
        ptype1=Grass, name="Chikorita", front_image=Chikorita.front_image, back_image=Chikorita.back_image)
        self.move1 = Chikorita.move1
        self.move2 = Chikorita.move2
        self.move3 = Chikorita.move3
        self.move4 = Chikorita.move4
        self.move_list = Chikorita.move_list
        self.move_set = Chikorita.move_set


class Bayleef(Pokemon):
    def __init__(self):
        Pokemon.__init__(self, health=22, attack=23, defense=30, special_attack=23, special_defense=30, speed=22,
        ptype1=Grass, name="Bayleef", front_image="images/bayleef_front.png", back_image="images/bayleef_back.png")
        self.move1 = energy_ball
        self.move2 = earthquake
        self.move3 = ancient_power
        self.move4 = iron_tail
        self.move_list = [energy_ball, ancient_power, earthquake, iron_tail]
        self.move_set = [energy_ball, ancient_power, earthquake, iron_tail]


class Meganium(Pokemon):
    move_list = [energy_ball, ancient_power, Return, iron_tail, earthquake]
    move1 = energy_ball
    move2 = ancient_power
    move3 = earthquake
    move4 = iron_tail
    move_set = [energy_ball, ancient_power, earthquake, iron_tail]
    front_image = 'images/meganium_front.png'
    back_image = 'images/meganium_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=23, attack=23, defense=29, special_attack=23, special_defense=29, speed=23,
        ptype1=Grass, name="Meganium", front_image=Meganium.front_image, back_image=Meganium.back_image)
        self.move1 = Meganium.move1
        self.move2 = Meganium.move2
        self.move3 = Meganium.move3
        self.move4 = Meganium.move4
        self.move_list = Meganium.move_list
        self.move_set = Meganium.move_set


class Bonsly(Pokemon):
    move_list=[brick_break, earth_power, earthquake, fire_punch, ice_punch, rock_slide, thunder_punch]
    move1 = rock_slide
    move2 = earthquake
    move3 = thunder_punch
    move4 = ice_punch
    move_set = [move1, move2, move3, move4]
    front_image='images/bonsly_front.png'
    back_image='images/bonsly_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=26, attack=42, defense=49, special_attack=5, special_defense=23, speed=5,
        ptype1=Rock, name="Bonsly", front_image=Bonsly.front_image, back_image=Bonsly.back_image)
        self.move1 = Bonsly.move1
        self.move2 = Bonsly.move2
        self.move3 = Bonsly.move3
        self.move4 = Bonsly.move4
        self.move_list = Bonsly.move_list
        self.move_set = Bonsly.move_set


class Sudowoodo(Pokemon):
    move_list=[brick_break, earth_power, earthquake, fire_punch, ice_punch, rock_slide, thunder_punch]
    move1 = rock_slide
    move2 = earthquake
    move3 = thunder_punch
    move4 = ice_punch
    move_set = [move1, move2, move3, move4]
    front_image='images/sudowoodo_front.png'
    back_image='images/sudowoodo_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=26, attack=36, defense=42, special_attack=11, special_defense=24, speed=11,
        ptype1=Rock, name="Sudowoodo", front_image=Sudowoodo.front_image, back_image=Sudowoodo.back_image)
        self.move1 = Sudowoodo.move1
        self.move2 = Sudowoodo.move2
        self.move3 = Sudowoodo.move3
        self.move4 = Sudowoodo.move4
        self.move_list = Sudowoodo.move_list
        self.move_set = Sudowoodo.move_set


bulbasaur = Bulbasaur()
opponent_bulbasaur = Bulbasaur()
ivysaur = Ivysaur()
opponent_ivysaur = Ivysaur()
venasaur = Venasaur()
opponent_venasaur = Venasaur()
squirtle = Squirtle()
opponent_squirtle = Squirtle()
wartortle = Wartortle()
opponent_wartortle = Wartortle()
blastoise = Blastoise()
opponent_blastoise = Blastoise()
charmander = Charmander()
opponent_charmander = Charmander()
charmeleon = Charmeleon()
opponent_charmeleon = Charmeleon()
charizard = Charizard()
opponent_charizard = Charizard()
butterfree = Butterfree()
opponent_butterfree = Butterfree()
beedrill = Beedrill()
opponent_beedrill = Beedrill()
mega_beedrill = Mega_Beedrill()
opponent_mega_beedrill = Mega_Beedrill()
pidgey = Pidgey()
opponent_pidgey = Pidgey()
pidgeotto = Pidgeotto()
opponent_pidgeotto = Pidgeotto()
pidgeot = Pidgeot()
opponent_pidgeot = Pidgeot()
mega_pidgeot = Mega_Pidgeot()
opponent_mega_pidgeot = Mega_Pidgeot()
rattata = Rattata()
opponent_rattata = Rattata()
raticate = Raticate()
opponent_raticate = Raticate()
spearow = Spearow()
opponent_spearow = Spearow()
fearow = Fearow()
opponent_fearow = Fearow()
ekans = Ekans()
opponent_ekans = Ekans()
arbok = Arbok()
opponent_arbok = Arbok()
pichu, opponent_pichu = Pichu(), Pichu()
pikachu = Pikachu()
light_ball_pikachu, opponent_light_ball_pikachu = Light_Ball_Pikachu(), Light_Ball_Pikachu()
opponent_pikachu = Pikachu()
raichu = Raichu()
opponent_raichu = Raichu()
sandshrew, opponent_sandshrew = Sandshrew(), Sandshrew()
sandslash = Sandslash()
opponent_sandslash = Sandslash()
nidoranf, opponent_nidoranf = NidoranF(), NidoranF()
nidorina, opponent_nidorina = Nidorina(), Nidorina()
nidoqueen, opponent_nidoqueen = Nidoqueen(), Nidoqueen()
nidoranm, opponent_nidoranm = NidoranM(), NidoranM()
nidorino, opponent_nidorino = Nidorino(), Nidorino()
nidoking, opponent_nidoking = Nidoking(), Nidoking()
cleffa, opponent_cleffa = Cleffa(), Cleffa()
clefairy, opponent_clefairy = Clefairy(), Clefairy()
clefable, opponent_clefable = Clefable(), Clefable()
vulpix, opponent_vulpix = Vulpix(), Vulpix()
ninetails, opponent_ninetails = Ninetails(), Ninetails()
igglybuff, opponent_igglybuff = Igglybuff(), Igglybuff()
jigglypuff, opponent_jigglypuff = Jigglypuff(), Jigglypuff()
wigglytuff, opponent_wigglytuff = Wigglytuff(), Wigglytuff()
zubat, opponent_zubat = Zubat(), Zubat()
golbat, opponent_golbat = Golbat(), Golbat()
crobat, opponent_crobat = Crobat(), Crobat()
oddish, opponent_oddish = Oddish(), Oddish()
gloom, opponent_gloom = Gloom(), Gloom()
vileplume, opponent_vileplume = Vileplume(), Vileplume()
paras, opponent_paras = Paras(), Paras()
parasect, opponent_parasect = Parasect(), Parasect()
venonat, opponent_venonat = Venonat(), Venonat()
venomoth, opponent_venomoth = Venomoth(), Venomoth()
diglett = Diglett()
opponent_diglett = Diglett()
dugtrio, opponent_dugtrio = Dugtrio(), Dugtrio()
meowth, opponent_meowth = Meowth(), Meowth()
persian, opponent_persian = Persian(), Persian()
psyduck, opponent_psyduck = Psyduck(), Psyduck()
golduck, opponent_golduck = Golduck(), Golduck()
mankey = Mankey()
opponent_mankey = Mankey()
primeape = Primeape()
opponent_primeape = Primeape()
growlithe, opponent_growlithe = Growlithe(), Growlithe()
arcanine, opponent_arcanine = Arcanine(), Arcanine()
poliwag, opponent_poliwag = Poliwag(), Poliwag()
poliwhirl, opponent_poliwhirl = Poliwhirl(), Poliwhirl()
poliwrath, opponent_poliwrath = Poliwrath(), Poliwrath()
abra, opponent_abra = Abra(), Abra()
kadabra, opponent_kadabra = Kadabra(), Kadabra()
alakazam, opponent_alakazam = Alakazam(), Alakazam()
machop, opponent_machop = Machop(), Machop()
machoke, opponent_machoke = Machoke(), Machoke()
machamp, opponent_machamp = Machamp(), Machamp()
bellsprout, opponent_bellsprout = Bellsprout(), Bellsprout()
weepinbell, opponent_weepinbell = Weepinbell(), Weepinbell()
victreebel, opponent_victreebel = Victreebel(), Victreebel()
tentacool, opponent_tentacool = Tentacool(), Tentacool()
tentacruel, opponent_tentacruel = Tentacruel(), Tentacruel()
geodude, opponent_geodude = Geodude(), Geodude()
graveler, opponent_graveler = Graveler(), Graveler()
golem, opponent_golem = Golem(), Golem()
ponyta, opponent_ponyta = Ponyta(), Ponyta()
rapidash, opponent_rapidash = Rapidash(), Rapidash()
slowpoke, opponent_slowpoke = Slowpoke(), Slowpoke()
slowbro, opponent_slowbro = Slowbro(), Slowbro()
slowking, opponent_slowking = Slowking(), Slowking()
magnemite = Magnemite()
opponent_magnemite = Magnemite()
magneton = Magneton()
opponent_magneton = Magneton()
magnezone, opponent_magnezone = Magnezone(), Magnezone()
farfetchd = Farfetchd()
opponent_farfetchd = Farfetchd()
doduo, opponent_doduo = Doduo(), Doduo()
dodrio, opponent_dodrio = Dodrio(), Dodrio()
seel, opponent_seel = Seel(), Seel()
dewgong, opponent_dewgong = Dewgong(), Dewgong()
grimer, opponent_grimer = Grimer(), Grimer()
muk, opponent_muk = Muk(), Muk()
shellder, opponent_shellder = Shellder(), Shellder()
cloyster, opponent_cloyster = Cloyster(), Cloyster()
ghastly = Ghastly()
opponent_ghastly = Ghastly()
haunter, opponent_haunter = Haunter(), Haunter(),
gengar, opponent_gengar = Gengar(), Gengar()
onix, opponent_onix = Onix(), Onix()
steelix, opponent_steelix = Steelix(), Steelix()
drowzee, opponent_drowzee = Drowzee(), Drowzee()
hypno, opponent_hypno = Hypno(), Hypno()
krabby, opponent_krabby = Krabby(), Krabby()
kingler, opponent_kingler = Kingler(), Kingler()
voltorb, opponent_voltorb = Voltorb(), Voltorb()
electrode, opponent_electrode = Electrode(), Electrode()
exeggcute, opponent_exeggcute = Exeggcute(), Exeggcute()
exeggutor, opponent_exeggutor = Exeggutor(), Exeggutor()
cubone, opponent_cubone = Cubone(), Cubone()
thick_club_cubone, opponent_thick_club_cubone = Thick_Club_Cubone(), Thick_Club_Cubone()
marowak, opponent_marowak = Marowak(), Marowak()
thick_club_marowak, opponent_thick_club_marowak = Thick_Club_Marowak(), Thick_Club_Marowak()
hitmonlee, opponent_hitmonlee = Hitmonlee(), Hitmonlee()
hitmonchan, opponent_hitmonchan = Hitmonchan(), Hitmonchan()
hitmontop, opponent_hitmontop = Hitmontop(), Hitmontop()
lickitung, opponent_lickitung = Lickitung(), Lickitung()
lickilicky, opponent_lickilicky = Lickilicky(), Lickilicky()
koffing, opponent_koffing = Koffing(), Koffing()
weezing, opponent_weezing = Weezing(), Weezing()
rhyhorn, opponent_rhyhorn = Rhyhorn(), Rhyhorn()
rhydon, opponent_rhydon = Rhydon(), Rhydon()
rhyperior, opponent_rhyperior = Rhyperior(), Rhyperior()
chansey, opponent_chansey = Chansey(), Chansey()
blissey, opponent_blissey = Blissey(), Blissey()
tangela = Tangela()
opponent_tangela = Tangela()
tangrowth, opponent_tangrowth = Tangrowth(), Tangrowth()
kangaskhan = Kangaskhan()
opponent_kangaskhan = Kangaskhan()
horsea, opponent_horsea = Horsea(), Horsea()
seadra, opponent_seadra = Seadra(), Seadra()
kingdra, opponent_kingdra = Kingdra(), Kingdra()
goldeen, opponent_goldeen = Goldeen(), Goldeen()
seaking, opponent_seaking = Seaking(), Seaking()
staryu, opponent_staryu = Staryu(), Staryu()
starmie, opponent_starmie = Starmie(), Starmie()
mimejr, opponent_mimejr = MimeJr(), MimeJr()
mrmime, opponent_mrmime = MrMime(), MrMime()
scyther, opponent_scyther = Scyther(), Scyther()
scizor, opponent_scizor = Scizor(), Scizor()
smoochum, opponent_smoochum = Smoochum(), Smoochum()
jynx = Jynx()
opponent_jynx = Jynx()
elekid, opponent_elekid = Elekid(), Elekid()
electabuzz, opponent_electabuzz = Electabuzz(), Electabuzz()
electivire, opponent_electivire = Electivire(), Electivire()
magby, opponent_magby = Magby(), Magby()
magmar, opponent_magmar = Magmar(), Magmar()
magmortar, opponent_magmortar = Magmortar(), Magmortar()
pinsir, opponent_pinsir = Pinsir(), Pinsir()
tauros, opponent_tauros = Tauros(), Tauros()
gyarados, opponent_gyarados = Gyarados(), Gyarados()
lapras, opponent_lapras = Lapras(), Lapras()
vaporeon, opponent_vaporeon = Vaporeon(), Vaporeon()
jolteon, opponent_jolteon = Jolteon(), Jolteon()
flareon, opponent_flareon = Flareon(), Flareon()
espeon, opponent_espeon = Espeon(), Espeon()
umbreon, opponent_umbreon = Umbreon(), Umbreon()
leafeon, opponent_leafeon = Leafeon(), Leafeon()
glaceon, opponent_glaceon = Glaceon(), Glaceon()
porygon, opponent_porygon = Porygon(), Porygon()
porygon2, opponent_porygon2 = Porygon2(), Porygon2()
porygonz, opponent_porygonz = PorygonZ(), PorygonZ()
omanyte, opponent_omanyte = Omanyte(), Omanyte()
omastar, opponent_omastar = Omastar(), Omastar()
kabuto, opponent_kabuto = Kabuto(), Kabuto()
kabutops, opponent_kabutops = Kabutops(), Kabutops()
aerodactyl, opponent_aerodactyl = Aerodactyl(), Aerodactyl()
munchlax = Munchlax()
opponent_munchlax = Munchlax()
snorlax = Snorlax()
opponent_snorlax = Snorlax()
articuno, opponent_articuno = Articuno(), Articuno()
zapdos, opponent_zapdos = Zapdos(), Zapdos()
moltres, opponent_moltres = Moltres(), Moltres()
dratini, opponent_dratini = Dratini(), Dratini()
dragonair, opponent_dragonair = Dragonair(), Dragonair()
dragonite, opponent_dragonite = Dragonite(), Dragonite()
mewtwo = Mewtwo()
opponent_mewtwo = Mewtwo()
mew, opponent_mew = Mew(), Mew()
chikorita = Chikorita()
opponent_chikorita = Chikorita()
meganium = Meganium()
opponent_meganium = Meganium()
bonsly = Bonsly()
opponent_bonsly = Bonsly()
sudowoodo = Sudowoodo()
opponent_sudowoodo = Sudowoodo()

Pokemon.All_Pokemon = [
    bulbasaur, ivysaur, venasaur,
    squirtle, wartortle, blastoise,
    charmander, charmeleon, charizard,
    butterfree,
    beedrill, mega_beedrill,
    pidgey, pidgeotto, pidgeot, mega_pidgeot,
    rattata, raticate,
    spearow, fearow,
    ekans, arbok,
    pichu, pikachu, light_ball_pikachu, raichu,
    sandshrew, sandslash,
    nidoranf, nidorina, nidoqueen,
    nidoranm, nidorino, nidoking,
    cleffa, clefairy, clefable,
    vulpix, ninetails,
    igglybuff, jigglypuff, wigglytuff,
    zubat, golbat, crobat,
    oddish, gloom, vileplume,
    paras, parasect,
    venonat, venomoth,
    diglett, dugtrio,
    meowth, persian,
    psyduck, golduck,
    mankey, primeape,
    growlithe, arcanine,
    poliwag, poliwhirl, poliwrath,
    abra, kadabra, alakazam,
    machop, machoke, machamp,
    bellsprout, weepinbell, victreebel,
    tentacool, tentacruel,
    geodude, graveler, golem,
    ponyta, rapidash,
    slowpoke, slowbro, slowking,
    magnemite, magneton, magnezone,
    farfetchd,
    doduo, dodrio,
    seel, dewgong,
    grimer, muk,
    shellder, cloyster,
    ghastly, haunter, gengar,
    onix, steelix,
    drowzee, hypno,
    krabby, kingler,
    voltorb, electrode,
    exeggcute, exeggutor,
    cubone, thick_club_cubone, marowak, thick_club_marowak,
    hitmonlee, hitmonchan, hitmontop,
    lickitung, lickilicky,
    koffing, weezing,
    rhyhorn, rhydon, rhyperior,
    chansey, blissey,
    tangela, tangrowth,
    kangaskhan,
    horsea, seadra, kingdra,
    goldeen, seaking,
    staryu, starmie,
    mimejr, mrmime,
    scyther, scizor,
    smoochum, jynx,
    elekid, electabuzz, electivire,
    magby, magmar, magmortar,
    pinsir, 
    tauros,
    gyarados,
    lapras,
    vaporeon, jolteon, flareon, espeon, umbreon, leafeon, glaceon,
    omanyte, omastar,
    kabuto, kabutops,
    aerodactyl,
    munchlax, snorlax,
    articuno, zapdos, moltres,
    dratini, dragonair, dragonite,
    mewtwo, mew,
    chikorita, meganium,
    bonsly, sudowoodo,
]
Opponent.All_Pokemon = [
    opponent_bulbasaur, opponent_ivysaur, opponent_venasaur,
    opponent_squirtle, opponent_wartortle, opponent_blastoise,
    opponent_charmander, opponent_charmeleon, opponent_charizard,
    opponent_butterfree,
    opponent_beedrill, opponent_mega_beedrill,
    opponent_pidgey, opponent_pidgeotto, opponent_pidgeot, opponent_mega_pidgeot,
    opponent_rattata, opponent_raticate,
    opponent_spearow, opponent_fearow,
    opponent_ekans, opponent_arbok,
    opponent_pichu, opponent_pikachu, opponent_light_ball_pikachu, opponent_raichu,
    opponent_sandshrew, opponent_sandslash,
    opponent_nidoranf, opponent_nidorina, opponent_nidoqueen,
    opponent_nidoranm, opponent_nidorino, opponent_nidoking,
    opponent_cleffa, opponent_clefairy, opponent_clefable,
    opponent_vulpix, opponent_ninetails,
    opponent_igglybuff, opponent_jigglypuff, opponent_wigglytuff,
    opponent_zubat, opponent_golbat, opponent_crobat,
    opponent_oddish, opponent_gloom, opponent_vileplume,
    opponent_paras, opponent_parasect,
    opponent_venonat, opponent_venomoth,
    opponent_diglett, opponent_dugtrio,
    opponent_meowth, opponent_persian,
    opponent_psyduck, opponent_golduck,
    opponent_mankey, opponent_primeape,
    opponent_growlithe, opponent_arcanine,
    opponent_poliwag, opponent_poliwhirl, opponent_poliwrath,
    opponent_abra, opponent_kadabra, opponent_alakazam,
    opponent_machop, opponent_machoke, opponent_machamp,
    opponent_bellsprout, opponent_weepinbell, opponent_victreebel,
    opponent_tentacool, opponent_tentacruel,
    opponent_geodude, opponent_graveler, opponent_golem,
    opponent_ponyta, opponent_rapidash,
    opponent_slowpoke, opponent_slowbro, opponent_slowking,
    opponent_magnemite, opponent_magneton, opponent_magnezone,
    opponent_farfetchd,
    opponent_doduo, opponent_dodrio,
    opponent_seel, opponent_dewgong,
    opponent_grimer, opponent_muk,
    opponent_shellder, opponent_cloyster,
    opponent_ghastly, opponent_haunter, opponent_gengar,
    opponent_onix, opponent_steelix,
    opponent_drowzee, opponent_hypno,
    opponent_krabby, opponent_kingler,
    opponent_voltorb, opponent_electrode,
    opponent_exeggcute, opponent_exeggutor,
    opponent_cubone, opponent_thick_club_cubone, opponent_marowak, opponent_thick_club_marowak,
    opponent_hitmonlee, opponent_hitmonchan, opponent_hitmontop,
    opponent_lickitung, opponent_lickilicky,
    opponent_koffing, opponent_weezing,
    opponent_rhyhorn, opponent_rhydon, opponent_rhyperior,
    opponent_chansey, opponent_blissey,
    opponent_tangela, opponent_tangrowth,
    opponent_kangaskhan,
    opponent_horsea, opponent_seadra, opponent_kingdra,
    opponent_goldeen, opponent_seaking,
    opponent_staryu, opponent_starmie,
    opponent_mimejr, opponent_mrmime,
    opponent_scyther, opponent_scizor,
    opponent_smoochum, opponent_jynx,
    opponent_elekid, opponent_electabuzz, opponent_electivire,
    opponent_magby, opponent_magmar, opponent_magmortar,
    opponent_pinsir, 
    opponent_tauros,
    opponent_gyarados,
    opponent_lapras,
    opponent_vaporeon, opponent_jolteon, opponent_flareon, opponent_espeon, opponent_umbreon, opponent_leafeon, opponent_glaceon,
    opponent_omanyte, opponent_omastar,
    opponent_kabuto, opponent_kabutops,
    opponent_aerodactyl,
    opponent_munchlax, opponent_snorlax,
    opponent_articuno, opponent_zapdos, opponent_moltres,
    opponent_dratini, opponent_dragonair, opponent_dragonite,
    opponent_mewtwo, opponent_mew,
    opponent_chikorita, opponent_meganium,
    opponent_bonsly, opponent_sudowoodo
]

# Player teams
test_team = Team([scyther, chikorita, raticate, cleffa, starmie])

ezpz_team = Team([machamp, slowpoke, kangaskhan, magnemite, abra])
first_tean = Team([squirtle, chikorita, charmander, jynx, pikachu])
slow_team = Team([bonsly, munchlax, magnemite, sandslash, squirtle])
blue = Team([pikachu, magnemite, farfetchd, jynx, primeape])
starter_team = Team([venasaur, charizard, blastoise, raichu, meganium])
# Opponent teams
test_opponent = Opponent([opponent_abra, opponent_clefable, opponent_nidoranm, opponent_rhyperior, opponent_flareon])

challenge = Opponent([opponent_geodude, opponent_mankey, opponent_munchlax, opponent_slowpoke, opponent_ghastly])
challenge2 = Opponent([opponent_munchlax, opponent_mankey, opponent_ghastly, opponent_spearow, opponent_diglett])
babies = Opponent([opponent_bulbasaur, opponent_charmander, opponent_squirtle, opponent_pikachu, opponent_chikorita])
rival = Opponent([opponent_blastoise, opponent_venasaur, opponent_charizard, opponent_butterfree, opponent_pikachu])
red = Opponent([opponent_butterfree, opponent_magneton, opponent_snorlax, opponent_sudowoodo, opponent_sandslash])
opponent = Opponent([opponent_diglett, opponent_snorlax, opponent_bulbasaur, opponent_sandslash, opponent_primeape])
# Gym Leader teams
fight_gym = Gym_Leader([opponent_hitmonlee, opponent_hitmonchan, opponent_mankey, opponent_machamp, opponent_poliwrath], "Fight")
normal_gym = Gym_Leader([opponent_tauros, opponent_kangaskhan, opponent_munchlax, opponent_spearow, opponent_rattata], "Normal")
ice_gym = Gym_Leader([opponent_dewgong, opponent_cloyster, opponent_articuno, opponent_jynx, opponent_lapras], "Ice")
poison_gym = Gym_Leader([opponent_gengar, opponent_golbat, opponent_haunter, opponent_arbok, opponent_ghastly], "Poison")
ground_gym = Gym_Leader([opponent_rhyhorn, opponent_dugtrio, opponent_nidoqueen, opponent_nidoking, opponent_rhydon], "Ground")
fire_gym = Gym_Leader([opponent_growlithe, opponent_ponyta, opponent_rapidash, opponent_arcanine, opponent_moltres], "Fire")
psychic_gym = Gym_Leader([opponent_kadabra, opponent_mrmime, opponent_alakazam, opponent_abra, opponent_espeon], "Psychic")
grass_gym = Gym_Leader([opponent_victreebel, opponent_tangela, opponent_vileplume, opponent_tangrowth, opponent_oddish], "Grass")
electric_gym = Gym_Leader([opponent_voltorb, opponent_electabuzz, opponent_raichu, opponent_light_ball_pikachu, opponent_magneton], "Electric")
blue_gym = Gym_Leader([opponent_pidgeot, opponent, alakazam, opponent_rhydon, opponent_exeggutor, opponent_gyarados], "Blue")
better_blue_gym = Gym_Leader([opponent_mega_pidgeot, opponent_abra, opponent_rhydon, opponent_exeggutor, opponent_gyarados], "Blue 2")









