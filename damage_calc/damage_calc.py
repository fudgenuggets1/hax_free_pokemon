from __future__ import division
import pygame, math, sys, Functions
from interaction import interaction
from buttons import Button

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 200)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
PURPLE = (255, 0, 255)
ORANGE = (255, 155, 0)
BRIGHT_GREEN = (0, 255, 0)
BRIGHT_BLUE = (0, 0, 255)
BRIGHT_RED = (255, 0, 0)

pygame.init()

screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()
FPS = 20
total_frames = 0


class Calc:
	damage = 0
	type_effectiveness = 1
	STAB = "No"
	@staticmethod
	def damage_calc(attack, defense, power, stab, advantage):
		# Damage = (0.44*(attack/defense)*move power)*modifier
		# Modifier = STAB * Type effectiveness * other(items, abilities)

		#STAB
		STAB = 1
		if stab == "Yes":
			STAB = 1.5
		type_advantage = advantage

		# Damage calculation
		damage = math.floor((0.2 * (attack / defense) * power + 2) * (type_advantage * STAB))
		#damage *= 0.9
		return int(damage)

def get_percent(numerator, denominator):
		number = int(round((numerator/denominator)*100))
		percent = ("%s%%" % number)
		return percent

def stat_calc(base_stat, points):
	stat = (2 * base_stat + points) + 18
	return stat
def hp_calc(base_stat, points):
	hp = (2 * base_stat + points) + 34
	return hp

class Pokemon():

	def __init__(self):
		self.points = 15
		self.base_stat_total = 0
		self.base_health, self.health, self.health_points = 0, 0, 0
		self.base_attack, self.attack, self.attack_points = 0, 0, 0
		self.base_defense, self.defense, self.defense_points = 0, 0, 0
		self.base_special_attack, self.special_attack, self.special_attack_points = 0, 0, 0
		self.base_special_defense, self.special_defense, self.special_defense_points = 0, 0, 0
		self.base_speed, self.speed, self.speed_points = 0, 0, 0
		self.health_percent = 0
		self.move_power = 0

	def update(self):
		self.points = 15
		self.points -= self.health_points
		self.points -= self.attack_points
		self.points -= self.defense_points
		self.points -= self.special_attack_points
		self.points -= self.special_defense_points
		self.points -= self.speed_points
		self.health = hp_calc(self.base_health, self.health_points)
		self.attack = stat_calc(self.base_attack, self.attack_points)
		self.defense = stat_calc(self.base_defense, self.defense_points)
		self.special_attack = stat_calc(self.base_special_attack, self.special_attack_points)
		self.special_defense = stat_calc(self.base_special_defense, self.special_defense_points)
		self.speed = stat_calc(self.base_speed, self.speed_points)
		self.health_percent = get_percent(Calc.damage, self.health)



pokemon1 = Pokemon()
pokemon2 = Pokemon()

buttons = [
	["clear", 160, 142, 60, 25, GREEN, BRIGHT_GREEN, "clear", "health"],
	["clear", 160, 217, 60, 25, GREEN, BRIGHT_GREEN, "clear", "attack"],
	["clear", 160, 292, 60, 25, GREEN, BRIGHT_GREEN, "clear", "defense"],
	["clear", 160, 367, 60, 25, GREEN, BRIGHT_GREEN, "clear", "special_attack"],
	["clear", 160, 442, 60, 25, GREEN, BRIGHT_GREEN, "clear", "special_defense"],
	["clear", 160, 517, 60, 25, GREEN, BRIGHT_GREEN, "clear", "speed"],
	
	["<", 235, 140, 20, 20, GREEN, BRIGHT_GREEN, "down", "health"],
	["<", 235, 215, 20, 20, GREEN, BRIGHT_GREEN, "down", "attack"],
	["<", 235, 290, 20, 20, GREEN, BRIGHT_GREEN, "down", "defense"],
	["<", 235, 365, 20, 20, GREEN, BRIGHT_GREEN, "down", "special_attack"],
	["<", 235, 440, 20, 20, GREEN, BRIGHT_GREEN, "down", "special_defense"],
	["<", 235, 515, 20, 20, GREEN, BRIGHT_GREEN, "down", "speed"],
	[">", 300, 140, 20, 20, GREEN, BRIGHT_GREEN, "up", "health"],
	[">", 300, 215, 20, 20, GREEN, BRIGHT_GREEN, "up", "attack"],
	[">", 300, 290, 20, 20, GREEN, BRIGHT_GREEN, "up", "defense"],
	[">", 300, 365, 20, 20, GREEN, BRIGHT_GREEN, "up", "special_attack"],
	[">", 300, 440, 20, 20, GREEN, BRIGHT_GREEN, "up", "special_defense"],
	[">", 300, 515, 20, 20, GREEN, BRIGHT_GREEN, "up", "speed"],
	
	["<", 660, 140, 20, 20, GREEN, BRIGHT_GREEN, "down", "health2"],
	["<", 660, 215, 20, 20, GREEN, BRIGHT_GREEN, "down", "attack2"],
	["<", 660, 290, 20, 20, GREEN, BRIGHT_GREEN, "down", "defense2"],
	["<", 660, 365, 20, 20, GREEN, BRIGHT_GREEN, "down", "special_attack2"],
	["<", 660, 440, 20, 20, GREEN, BRIGHT_GREEN, "down", "special_defense2"],
	["<", 660, 515, 20, 20, GREEN, BRIGHT_GREEN, "down", "speed2"],
	[">", 725, 140, 20, 20, GREEN, BRIGHT_GREEN, "up", "health2"],
	[">", 725, 215, 20, 20, GREEN, BRIGHT_GREEN, "up", "attack2"],
	[">", 725, 290, 20, 20, GREEN, BRIGHT_GREEN, "up", "defense2"],
	[">", 725, 365, 20, 20, GREEN, BRIGHT_GREEN, "up", "special_attack2"],
	[">", 725, 440, 20, 20, GREEN, BRIGHT_GREEN, "up", "special_defense2"],
	[">", 725, 515, 20, 20, GREEN, BRIGHT_GREEN, "up", "speed2"],
	
	["clear", 585, 142, 60, 25, GREEN, BRIGHT_GREEN, "clear", "health2"],
	["clear", 585, 217, 60, 25, GREEN, BRIGHT_GREEN, "clear", "attack2"],
	["clear", 585, 292, 60, 25, GREEN, BRIGHT_GREEN, "clear", "defense2"],
	["clear", 585, 367, 60, 25, GREEN, BRIGHT_GREEN, "clear", "special_attack2"],
	["clear", 585, 442, 60, 25, GREEN, BRIGHT_GREEN, "clear", "special_defense2"],
	["clear", 585, 517, 60, 25, GREEN, BRIGHT_GREEN, "clear", "speed2"],

	["clear", 200, 13, 60, 25, GREEN, BRIGHT_GREEN, "clear", "move_power"],
	["STAB:", 600, 8, 70, 30, GREEN, BRIGHT_GREEN, "STAB", "STAB"],
	["Calculate", 350, 85, 100, 40, RED, BRIGHT_RED, "calculate", "calculate"]
	]
x = 1
for i in range(100, 201, 25): 
	b = ["%s" % x, i, 170, 20, 20, BLUE, BRIGHT_BLUE, x, "health"]
	buttons.append(b)
	b = ["%s" % x, i, 245, 20, 20, BLUE, BRIGHT_BLUE, x, "attack"]
	buttons.append(b)
	b = ["%s" % x, i, 320, 20, 20, BLUE, BRIGHT_BLUE, x, "defense"]
	buttons.append(b)
	b = ["%s" % x, i, 395, 20, 20, BLUE, BRIGHT_BLUE, x, "special_attack"]
	buttons.append(b)
	b = ["%s" % x, i, 470, 20, 20, BLUE, BRIGHT_BLUE, x, "special_defense"]
	buttons.append(b)
	b = ["%s" % x, i, 545, 20, 20, BLUE, BRIGHT_BLUE, x, "speed"]
	buttons.append(b)
	x+=1
x = 6
for i in range(100, 201, 25):
	if x == 10:
		x = 0
	b = ["%s" % (x), i, 195, 20, 20, BLUE, BRIGHT_BLUE, x, "health"]
	buttons.append(b)
	b = ["%s" % (x), i, 270, 20, 20, BLUE, BRIGHT_BLUE, x, "attack"]
	buttons.append(b)
	b = ["%s" % (x), i, 345, 20, 20, BLUE, BRIGHT_BLUE, x, "defense"]
	buttons.append(b)
	b = ["%s" % (x), i, 420, 20, 20, BLUE, BRIGHT_BLUE, x, "special_attack"]
	buttons.append(b)
	b = ["%s" % (x), i, 495, 20, 20, BLUE, BRIGHT_BLUE, x, "special_defense"]
	buttons.append(b)
	b = ["%s" % (x), i, 570, 20, 20, BLUE, BRIGHT_BLUE, x, "speed"]
	buttons.append(b)
	x += 1
x = 1
for i in range(525, 626, 25):
	b = ["%s" % x, i, 170, 20, 20, BLUE, BRIGHT_BLUE, x, "health2"]
	buttons.append(b)
	b = ["%s" % x, i, 245, 20, 20, BLUE, BRIGHT_BLUE, x, "attack2"]
	buttons.append(b)
	b = ["%s" % x, i, 320, 20, 20, BLUE, BRIGHT_BLUE, x, "defense2"]
	buttons.append(b)
	b = ["%s" % x, i, 395, 20, 20, BLUE, BRIGHT_BLUE, x, "special_attack2"]
	buttons.append(b)
	b = ["%s" % x, i, 470, 20, 20, BLUE, BRIGHT_BLUE, x, "special_defense2"]
	buttons.append(b)
	b = ["%s" % x, i, 545, 20, 20, BLUE, BRIGHT_BLUE, x, "speed2"]
	buttons.append(b)
	x+=1
x = 6
for i in range(525, 626, 25):
	if x == 10:
		x = 0
	b = ["%s" % (x), i, 195, 20, 20, BLUE, BRIGHT_BLUE, x, "health2"]
	buttons.append(b)
	b = ["%s" % (x), i, 270, 20, 20, BLUE, BRIGHT_BLUE, x, "attack2"]
	buttons.append(b)
	b = ["%s" % (x), i, 345, 20, 20, BLUE, BRIGHT_BLUE, x, "defense2"]
	buttons.append(b)
	b = ["%s" % (x), i, 420, 20, 20, BLUE, BRIGHT_BLUE, x, "special_attack2"]
	buttons.append(b)
	b = ["%s" % (x), i, 495, 20, 20, BLUE, BRIGHT_BLUE, x, "special_defense2"]
	buttons.append(b)
	b = ["%s" % (x), i, 570, 20, 20, BLUE, BRIGHT_BLUE, x, "speed2"]
	buttons.append(b)
	x += 1
x = 1
for i in range(100, 201, 25):
	b = ["%s" % x, i, 40, 20, 20, BLUE, BRIGHT_BLUE, x, "move_power"]
	buttons.append(b)
	x += 1
x = 6
for i in range(100, 201, 25):
	if x == 10:
		x = 0
	b = ["%s" % x, i, 65, 20, 20, BLUE, BRIGHT_BLUE, x, "move_power"]
	buttons.append(b)
	x+=1
effect = 0.25
for i in range(275, 526, 55):
	if effect >= 1:
		effect = int(effect)
	b = ["%sx" % effect, i, 50, 50, 25, BLUE, BRIGHT_BLUE, effect, "effectiveness"]
	buttons.append(b)
	effect *= 2
for item in buttons:
	button = Button(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], 20)

while True:

	screen.fill((120,120,120))

	# Regular Text
	text = [
	["Pokemon 1", 150, 100],
	["%s" % pokemon1.points, 275, 100],
	["Health:", 75, 150],
	["%s" % pokemon1.base_health, 135, 150],
	["%s" % pokemon1.health_points, 275, 150],
	["%s" % pokemon1.health, 375, 150],
	["Attack:", 75, 225],
	["%s" % pokemon1.base_attack, 135, 225],
	["%s" % pokemon1.attack_points, 275, 225],
	["%s" % pokemon1.attack, 375, 225],
	["Defense:", 65, 300],
	["%s" % pokemon1.base_defense, 135, 300],
	["%s" % pokemon1.defense_points, 275, 300],
	["%s" % pokemon1.defense, 375, 300],
	["Sp.Atk:", 75, 375],
	["%s" % pokemon1.base_special_attack, 135, 375],
	["%s" % pokemon1.special_attack_points, 275, 375],
	["%s" % pokemon1.special_attack, 375, 375],
	["Sp.Def:", 75, 450],
	["%s" % pokemon1.base_special_defense, 135, 450],
	["%s" % pokemon1.special_defense_points, 275, 450],
	["%s" % pokemon1.special_defense, 375, 450],
	["Speed:", 75, 525],
	["%s" % pokemon1.base_speed, 135, 525],
	["%s" % pokemon1.speed_points, 275, 525],
	["%s" % pokemon1.speed, 375, 525],
	["Pokemon 2", 575, 100],
	["%s" % pokemon2.points, 700, 100],
	["Health:", 500, 150],
	["%s" % pokemon2.base_health, 560, 150],
	["%s" % pokemon2.health_points, 700, 150],
	["%s" % pokemon2.health, 775, 150],
	["Attack:", 500, 225],
	["%s" % pokemon2.base_attack, 560, 225],
	["%s" % pokemon2.attack_points, 700, 225],
	["%s" % pokemon2.attack, 775, 225],
	["Defense:", 490, 300],
	["%s" % pokemon2.base_defense, 560, 300],
	["%s" % pokemon2.defense_points, 700, 300],
	["%s" % pokemon2.defense, 775, 300],
	["Sp.Atk:", 500, 375],
	["%s" % pokemon2.base_special_attack, 560, 375],
	["%s" % pokemon2.special_attack_points, 700, 375],
	["%s" % pokemon2.special_attack, 775, 375],
	["Sp.Def:", 500, 450],
	["%s" % pokemon2.base_special_defense, 560, 450],
	["%s" % pokemon2.special_defense_points, 700, 450],
	["%s" % pokemon2.special_defense, 775, 450],
	["Speed:", 500, 525],
	["%s" % pokemon2.base_speed, 560, 525],
	["%s" % pokemon2.speed_points, 700, 525],
	["%s" % pokemon2.speed, 775, 525],
	["Move Power:", 75, 25],
	["%s" % pokemon1.move_power, 175, 25],
	["Type Effectiveness:", 375, 25],
	["%sx" % Calc.type_effectiveness, 525, 25],
	#["STAB:", 640, 20],
	["%s" % Calc.STAB, 700, 20],
	["Damage:", 625, 60],
	["%s" % Calc.damage, 700, 60],
	["%s" % pokemon2.health_percent, 750, 60],
	]
	
	for item in text:
		Functions.text_to_screen(screen, item[0], item[1], item[2])

	# Small Text
	text = [
	["Base Stat", 125, 125, 15],
	["Base Stat", 550, 125, 15],
	["Points", 275, 125, 15],
	["Points", 700, 125, 15],
	]

	for item in text:
		Functions.text_to_screen(screen, item[0], item[1], item[2], item[3], color=(200, 200, 200))

	Button.update(screen, Button.List)
	pokemon1.update()
	pokemon2.update()
	interaction(screen)
	pygame.display.update()
	pygame.display.set_caption("Damage Calculator 2.0")
	pygame.display.flip()
	clock.tick(FPS)
	total_frames += 1