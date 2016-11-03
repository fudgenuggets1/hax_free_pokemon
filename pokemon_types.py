import pygame

class Type():

    List = [
    "normal",
    "fight",
    "flying",
    "poison",
    "ground",
    "rock",
    "bug",
    "ghost",
    "steel",
    "fire",
    "water",
    "grass",
    "electric",
    "psychic",
    "ice",
    "dragon",
    "dark",
    "fairy"
    ]
    type_list = []

    def __init__(self, name):
        self.name = name
        self.resist_list = []
        self.weakness_list = []
        self.immune_list = []
        self.not_effective_list = []
        self.super_effective_list = []
        self.no_effect_list = []
        self.image = pygame.image.load('images/' + self.name + '.png')
        Type.type_list.append(self)


Normal = Type("normal")
Normal.weakness_list.append("fight")
Normal.immune_list.append("ghost")
Normal.not_effective_list = ["rock", "steel"]
Normal.no_effect_list.append("ghost")

Fight = Type("fight")
Fight.resist_list = ["bug", "rock", "dark"]
Fight.weakness_list = ["flying", "psychic", "fairy"]
Fight.not_effective_list = ["bug", "fairy", "flying", "poison", "psychic"]
Fight.super_effective_list = ["dark", "normal", "rock", "steel"]
Fight.no_effect_list.append("ghost")

Flying = Type("flying")
Flying.resist_list = ["bug", "fight", "grass"]
Flying.weakness_list = ["electric", "ice", "rock"]
Flying.immune_list.append("ground")
Flying.not_effective_list = ["electric", "rock", "Steel"]
Flying.super_effective_list = ["bug", "fight", "grass"]

Poison = Type("poison")
Poison.resist_list = ["fight", "poison", "bug", "grass", "fairy"]
Poison.weakness_list = ["ground", "psychic"]
Poison.not_effective_list = ["poison", "ground", "rock", "ghost"]
Poison.super_effective_list = ["fairy", "grass"]
Poison.no_effect_list.append("steel")

Water = Type("water")
Water.resist_list = ["fire", "ice", "steel", "water"]
Water.weakness_list = ["grass", "electric"]
Water.not_effective_list = ["dragon", "grass", "water"]
Water.super_effective_list = ["fire", "ground", "rock"]

Fire = Type("fire")
Fire.resist_list = ["bug", "fairy", "fire", "grass", "ice", "steel"]
Fire.weakness_list = ["ground", "rock", "water"]
Fire.not_effective_list = ["dragon", "fire", "rock", "water"]
Fire.super_effective_list = ["bug", "grass", "ice", "steel"]

Grass = Type("grass")
Grass.resist_list = ["grass", "water", "electric", "ground"]
Grass.weakness_list = ["fire", "bug", "flying", "ice", "poison"]
Grass.not_effective_list = ["bug", "dragon", "grass", "fire", "steel", "poison", "flying"]
Grass.super_effective_list = ["water", "ground", "rock"]

Ground = Type("ground")
Ground.resist_list = ["poison", "rock"]
Ground.weakness_list = ["grass", "ice", "water"]
Ground.immune_list.append("electric")
Ground.not_effective_list = ["bug", "grass"]
Ground.super_effective_list = ["electric", "fire", "poison", "rock", "steel"]
Ground.no_effect_list.append("flying")

Rock = Type("rock")
Rock.resist_list = ["fire", "flying", "normal", "poison"]
Rock.weakness_list = ["fight", "grass", "ground", "water", "steel"]
Rock.not_effective_list = ["fight", "ground", "steel"]
Rock.super_effective_list = ["bug", "fire", "flying", "ice"]

Bug = Type("bug")
Bug.resist_list = ["fight", "grass", "ground"]
Bug.weakness_list = ["fire", "flying", "rock"]
Bug.not_effective_list = ["fairy", "fight", "fire", "flying", "ghost", "poison", "steel"]
Bug.super_effective_list = ["dark", "grass", "psychic"]

Ghost = Type("ghost")
Ghost.resist_list = ["bug", "poison"]
Ghost.weakness_list = ["dark", "ghost"]
Ghost.immune_list = ["normal", "fight"]
Ghost.not_effective_list.append("dark")
Ghost.super_effective_list = ["ghost", "psychic"]
Ghost.no_effect_list.append("normal")

Steel = Type("steel")
Steel.resist_list = ["bug", "dragon", "fairy", "flying", "grass", "ice", "normal", "psychic", "rock", "steel"]
Steel.weakness_list = ["fight", "fire", "ground"]
Steel.immune_list.append("poison")
Steel.not_effective_list = ["electric", "fire", "steel", "water"]
Steel.super_effective_list = ["fairy", "ice", "rock"]

Electric = Type("electric")
Electric.resist_list = ["electric", "flying", "steel"]
Electric.weakness_list.append("ground")
Electric.not_effective_list = ["dragon", "electric", "grass"]
Electric.super_effective_list = ["flying", "water"]
Electric.no_effect_list.append("ground")

Psychic = Type("psychic")
Psychic.resist_list = ["fight", "psychic"]
Psychic.weakness_list = ["bug", "dark", "ghost"]
Psychic.not_effective_list = ["psychic", "steel"]
Psychic.super_effective_list = ["fight", "poison"]
Psychic.no_effect_list.append("dark")

Ice = Type("ice")
Ice.resist_list.append("ice")
Ice.weakness_list = ["fight", "fire", "rock", "steel"]
Ice.not_effective_list = ["fire", "ice", "steel", "water"]
Ice.super_effective_list = ["dragon", "flying", "grass", "ground"]

Dragon = Type("dragon")
Dragon.resist_list = ["electric", "fire", "grass", "water"]
Dragon.weakness_list = ["dragon", "fairy", "ice"]
Dragon.not_effective_list.append("steel")
Dragon.super_effective_list.append("dragon")
Dragon.no_effect_list.append("fairy")

Dark = Type("dark")
Dark.resist_list = ["dark", "ghost"]
Dark.weakness_list = ["bug", "fairy", "fight"]
Dark.immune_list.append("psychic")
Dark.not_effective_list = ["dark", "fairy", "fight"]
Dark.super_effective_list = ["ghost", "psychic"]

Fairy = Type("fairy")
Fairy.resist_list = ["bug", "dark", "fight"]
Fairy.weakness_list = ["poison", "steel"]
Fairy.immune_list.append("dragon")
Fairy.not_effective_list = ["fire", "poison", "steel"]
Fairy.super_effective_list = ["dark", "dragon", "fight"]
