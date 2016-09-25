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

    def __init__(self, health, attack, defense, special_attack, special_defense, speed,
    ptype1, name, front_image, back_image, ptype2=None):

        self.health = health + 20
        self.current_health = self.health
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
        self.points = (124 - health) + 20
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
        self.front_image = pygame.image.load(front_image)
        self.back_image = pygame.image.load(back_image)


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
    front_image = 'images/squirtle_front.png'
    back_image = 'images/squirtle_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=22, attack=15, defense=30, special_attack=19, special_defense=29, speed=9,
        ptype1=Water, name="Squirtle", front_image=Squirtle.front_image, back_image=Squirtle.back_image)
        self.move1 = Squirtle.move1
        self.move2 = Squirtle.move2
        self.move3 = Squirtle.move3
        self.move4 = Squirtle.move4
        self.move_list = Squirtle.move_list
        self.move_set = Squirtle.move_set


class Snorlax(Pokemon):

    move1 = earthquake
    move2 = surf
    move3 = thrash
    move4 = ice_punch
    move_list = [iron_tail, surf, waterfall, ice_punch, ice_beam, water_gun, brick_break, tackle, crunch]
    move_set = [move1, move2, move3, move4]
    front_image = 'images/snorlax_front.png'
    back_image = 'images/snorlax_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=50, attack=32, defense=20, special_attack=1, special_defense=20, speed=1,
        ptype1=Normal, name="Snorlax", front_image=Snorlax.front_image, back_image=Snorlax.back_image)
        self.move1 = Snorlax.move1
        self.move2 = Snorlax.move2
        self.move3 = Snorlax.move3
        self.move4 = Snorlax.move4
        self.move_list = Snorlax.move_list
        self.move_set = Snorlax.move_set


class Charmander(Pokemon):
    move_set = [ancient_power, flamethrower, crunch, thunder_punch]
    move1 = ancient_power
    move2 = flamethrower
    move3 = crunch
    move4 = thunder_punch
    move_list = [scratch, flamethrower, crunch, thunder_punch, aerial_ace, ancient_power, brick_break, dragon_claw]
    front_image = 'images/charmander_front.png'
    back_image = 'images/charmander_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=15, attack=19, defense=19, special_attack=28, special_defense=19, speed=24,
        ptype1=Fire, name="Charmander", front_image=Charmander.front_image, back_image=Charmander.back_image)
        self.move1 = Charmander.move1
        self.move2 = Charmander.move2
        self.move3 = Charmander.move3
        self.move4 = Charmander.move4
        self.move_list = Charmander.move_list
        self.move_set = Charmander.move_set


class Chikorita(Pokemon):
    move_list = [energy_ball, ancient_power, tackle, iron_tail]
    move1 = energy_ball
    move2 = ancient_power
    move3 = tackle
    move4 = iron_tail
    move_set = [energy_ball, ancient_power, tackle, iron_tail]
    front_image = 'images/chikorita_front.png'
    back_image = 'images/chikorita_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=19, attack=19, defense=24, special_attack=19, special_defense=24, speed=19,
        ptype1=Grass, name="Chikorita", front_image=Chikorita.front_image, back_image=Chikorita.back_image)
        self.move1 = Chikorita.move1
        self.move2 = Chikorita.move2
        self.move3 = Chikorita.move3
        self.move4 = Chikorita.move4
        self.move_list = Chikorita.move_list
        self.move_set = Chikorita.move_set


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
        Pokemon.__init__(self, health=15, attack=16, defense=10, special_attack=40, special_defense=10, speed=33,
        ptype1=Electric, name="Pikachu", front_image=Pikachu.front_image, back_image=Pikachu.back_image)
        self.move1 = Pikachu.move1
        self.move2 = Pikachu.move2
        self.move3 = Pikachu.move3
        self.move4 = Pikachu.move4
        self.move_set = Pikachu.move_set
        self.move_list = Pikachu.move_list


class Bulbasaur(Pokemon):
    move_list = [tackle, iron_tail, energy_ball, sludge_bomb, ancient_power]
    move1 = energy_ball
    move2 = sludge_bomb
    move3 = ancient_power
    move4 = iron_tail
    move_set = [energy_ball, sludge_bomb, ancient_power, iron_tail]
    front_image = 'images/bulbasaur_front.png'
    back_image = 'images/bulbasaur_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=24, attack=10, defense=20, special_attack=30, special_defense=30, speed=10,
        ptype1=Grass, name="Bulbasaur", front_image=Bulbasaur.front_image, back_image=Bulbasaur.back_image, ptype2=Poison)
        self.move1 = Bulbasaur.move1
        self.move2 = Bulbasaur.move2
        self.move3 = Bulbasaur.move3
        self.move4 = Bulbasaur.move4
        self.move_list = Bulbasaur.move_list
        self.move_set = Bulbasaur.move_set


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
        Pokemon.__init__(self, health=13, attack=11, defense=10, special_attack=30, special_defense=30, speed=30,
        ptype1=Ice, name="Jynx", front_image=Jynx.front_image, back_image=Jynx.back_image, ptype2=Psychic)
        self.move1 = Jynx.move1
        self.move2 = Jynx.move2
        self.move3 = Jynx.move3
        self.move4 = Jynx.move4
        self.move_set = Jynx.move_set
        self.move_list = Jynx.move_list


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
        Pokemon.__init__(self, health=25, attack=30, defense=35, special_attack=1, special_defense=20, speed=13,
        ptype1=Ground, name="Sandslash", front_image=Sandslash.front_image, back_image=Sandslash.back_image)
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
    front_image = 'images/primeape_front.png'
    back_image = 'images/primeape_back.png'
    def __init__(self):
        Pokemon.__init__(self, health=15, attack=40, defense=15, special_attack=11, special_defense=15, speed=28,
        ptype1=Fight, name="Primeape", front_image=Primeape.front_image, back_image=Primeape.back_image)
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
charmander = Charmander()
chikorita = Chikorita()
pikachu = Pikachu()
bulbasaur = Bulbasaur()
jynx = Jynx()
