import pygame
from pokemon_types import *


class Move():

    def __init__(self, power, name, move_type, contact):

        self.power = power
        self.name = name
        self.type = move_type
        self.contact = contact


# Normal
tackle = Move(50, "Tackle", Normal, "physical")
scratch = Move(40, "Scratch", Normal, "physical")
thrash = Move(100, "Thrash", Normal, "physical")
# Fight
brick_break = Move(75, "Brick Break", Fight, "physical")
# Flying
aerial_ace = Move(60, "Aerial Ace", Flying, "physical")
# Poison
sludge_bomb = Move(90, "Sludge Bomb", Poison, "special")
# Ground
earthquake = Move(100, "Earthquake", Ground, "physical")
# Rock
ancient_power = Move(60, "Ancient Power", Rock, "special")
# Bug
signal_beam = Move(75, "Signal Beam", Bug, "special")
# Ghost
shadow_ball = Move(80, "Shadow Ball", Ghost, "special")
# Steel
iron_tail = Move(100, "Iron Tail", Steel, "physical")
# Fire
fire_punch = Move(75, "Fire Punch", Fire, "physical")
flamethrower = Move(90, "Flamethrower", Fire, "special")
# Water
water_gun = Move(40, "Water Gun", Water, "special")
waterfall = Move(80, "Waterfall", Water, "physical")
surf = Move(90, "Surf", Water, "special")
# Grass
energy_ball = Move(90, "Energy Ball", Grass, "special")
# Electric
thunderbolt = Move(90, "Thunderbolt", Electric, "special")
thunder_punch = Move(75, "Thunder Punch", Electric, "physical")
# Psychic
psychic = Move(90, "Psychic", Psychic, "special")
# Ice
ice_punch = Move(75, "Ice Punch", Ice, "physical")
ice_beam = Move(90, "Ice Beam", Ice, "special")
# Dragon
dragon_claw = Move(80, "Dragon Claw", Dragon, "physical")
# Dark
crunch = Move(60, "Crunch", Dark, "physical")
# Fairy
dazzling_gleam = Move(80, "Dazzling Gleam", Fairy, "special")


class Pokemon():

    def __init__(self, health, attack, defense, special_attack, special_defense, speed, ptype1, name, ptype2=None):

        self.health = health
        self.current_health = health
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed
        self.move1 = None
        self.move2 = None
        self.move3 = None
        self.move4 = None
        self.name = name
        self.fainted = False
        self.points = (124 - health)
        self.points -= attack
        self.points -= defense
        self.points -= special_attack
        self.points -= special_defense
        self.points -= speed
        self.type = ptype1
        self.move_list = []
        self.move_set = []
        self.move1_number = 0
        self.move2_number = 1
        self.move3_number = 2
        self.move4_number = 3
        self.type2 = ptype2


class Opponent():

    def __init__(self, pokemon, number):

        self.list = pokemon
        self.pokemon_number = number
        self.pokemon = pokemon[number]


class Squirtle(Pokemon):

    move1 = iron_tail
    move2 = surf
    move3 = waterfall
    move4 = ice_punch
    move_list = [iron_tail, surf, waterfall, ice_punch, ice_beam, water_gun, brick_break, tackle]
    move_set = [iron_tail, surf, waterfall, ice_punch]

    def __init__(self):

        self.health = 32
        self.current_health = 32
        self.attack = 13
        self.defense = 30
        self.special_attack = 14
        self.special_defense = 29
        self.speed = 6
        self.move1 = Squirtle.move1
        self.move2 = Squirtle.move2
        self.move3 = Squirtle.move3
        self.move4 = Squirtle.move4
        self.name = "Squirtle"
        self.fainted = False
        self.points = 0
        self.type = Water
        self.move_list = Squirtle.move_list
        self.move_set = Squirtle.move_set
        self.move1_number = 0
        self.move2_number = 1
        self.move3_number = 2
        self.move4_number = 3
        self.type2 = None


class Snorlax(Pokemon):

    move1 = earthquake
    move2 = surf
    move3 = thrash
    move4 = ice_punch
    move_list = [iron_tail, surf, waterfall, ice_punch, ice_beam, water_gun, brick_break, tackle, crunch]
    move_set = [move1, move2, move3, move4]

    def __init__(self):

        self.health = 60
        self.current_health = 60
        self.attack = 36
        self.defense = 13
        self.special_attack = 1
        self.special_defense = 13
        self.speed = 1
        self.move1 = Snorlax.move1
        self.move2 = Snorlax.move2
        self.move3 = Snorlax.move3
        self.move4 = Snorlax.move4
        self.name = "Snorlax"
        self.fainted = False
        self.points = 0
        self.type = Normal
        self.move_list = Snorlax.move_list
        self.move_set = Snorlax.move_set
        self.move1_number = 0
        self.move2_number = 1
        self.move3_number = 2
        self.move4_number = 3
        self.type2 = None


class Charmander(Pokemon):

    def __init__(self):
        Pokemon.__init__(self, health=25, attack=19, defense=19, special_attack=19, special_defense=19, speed=19, ptype1=Fire, name="Charmander")


class Chikorita(Pokemon):

    def __init__(self):
        Pokemon.__init__(self, health=30, attack=10, defense=30, special_attack=11, special_defense=11, speed=4,
        ptype1=Grass, name="Chikorita")
class Pikachu(Pokemon):
    pass
class Bulbasaur(Pokemon):
    pass
class Jynx(Pokemon):
    pass
class Sandslash(Pokemon):
    move_list = [earthquake, aerial_ace, iron_tail, brick_break, scratch]
    move1 = earthquake
    move2 = aerial_ace
    move3 = iron_tail
    move4 = brick_break
    move_set = [move1, move2, move3, move4]
    def __init__(self):
        Pokemon.__init__(self, health=35, attack=30, defense=30, special_attack=1, special_defense=15, speed=13,
        ptype1=Ground, name="Sandslash")
        self.move1 = Sandslash.move1
        self.move2 = Sandslash.move2
        self.move3 = Sandslash.move3
        self.move4 = Sandslash.move4
        self.move_set = Sandslash.move_set
        self.move_list = Sandslash.move_list


class Primeape(Pokemon):
    move_list = [brick_break, earthquake, ice_punch, thunder_punch, fire_punch]
    move1 = brick_break
    move2 = fire_punch
    move3 = thunder_punch
    move4 = ice_punch
    move_set = [move1, move2, move3, move4]
    def __init__(self):
        Pokemon.__init__(self, health=25, attack=40, defense=15, special_attack=1, special_defense=15, speed=28,
        ptype1=Fight, name="Primeape")
        self.move1 = Primeape.move1
        self.move2 = Primeape.move2
        self.move3 = Primeape.move3
        self.move4 = Primeape.move4
        self.move_set = Primeape.move_set
        self.move_list = Primeape.move_list


squirtle = Squirtle()
opponent_squirtle = Squirtle()
snorlax = Snorlax()
sandslash = Sandslash()
primeape = Primeape()

Charmander = Charmander()
Charmander.move_set = [ancient_power, flamethrower, crunch, thunder_punch]
Charmander.move1 = ancient_power
Charmander.move2 = flamethrower
Charmander.move3 = crunch
Charmander.move4 = thunder_punch
Charmander.move_list = [scratch, flamethrower, crunch, thunder_punch, aerial_ace, ancient_power, brick_break, dragon_claw]

Chikorita = Chikorita()
Chikorita.move_list = [energy_ball, ancient_power, tackle, iron_tail]
Chikorita.move1 = energy_ball
Chikorita.move2 = ancient_power
Chikorita.move3 = tackle
Chikorita.move4 = iron_tail
Chikorita.move_set = [energy_ball, ancient_power, tackle, iron_tail]

Pikachu = Pikachu(30, 1, 15, 30, 15, 33, Electric, "Pikachu")
Pikachu.move_list = [brick_break, iron_tail, thunderbolt, signal_beam, surf]
Pikachu.move1 = thunderbolt
Pikachu.move2 = signal_beam
Pikachu.move3 = surf
Pikachu.move4 = iron_tail
Pikachu.move_set = [thunderbolt, signal_beam, surf, iron_tail]

Bulbasaur = Bulbasaur(40, 10, 25, 10, 25, 14, Grass, "Bulbasaur", Poison)
Bulbasaur.move_list = [tackle, iron_tail, energy_ball, sludge_bomb]
Bulbasaur.move1 = energy_ball
Bulbasaur.move2 = sludge_bomb
Bulbasaur.move3 = tackle
Bulbasaur.move4 = iron_tail
Bulbasaur.move_set = [energy_ball, sludge_bomb, tackle, iron_tail]

Jynx = Jynx(23, 1, 10, 30, 30, 30, Ice, "Jynx", Psychic)
Jynx.move_list = [ice_beam, ice_punch, psychic, signal_beam, brick_break, energy_ball, shadow_ball]
Jynx.move1 = ice_beam
Jynx.move2 = psychic
Jynx.move3 = signal_beam
Jynx.move4 = energy_ball
Jynx.move_set = [ice_beam, psychic, signal_beam, energy_ball]
