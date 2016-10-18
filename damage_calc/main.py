from __future__ import division
import pygame, sys, math

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

screen = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()
FPS = 20
total_frames = 0

def text_to_screen(screen, text, x, y, size = 25,
    color = (255,255,255), font_type = 'Arial'):

    text = str(text)

    font = pygame.font.SysFont(font_type, size)
    size = font.size(text)
    text = font.render(text, True, color)

    screen.blit(text, (x-(size[0]/2), y-(size[1]/2)))

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


class Button():

	List = []
	attack = 0
	special_attack = 0
	defense = 0
	special_defense = 0
	move_power = 0
	damage = 0
	STAB = "No"
	type_advantage = 1

	def __init__(self, msg, x, y, w, h, color, highlight, action, action_effect=None):

		self.msg = msg
		self.x, self.y = x, y
		self.w, self.h = w, h
		self.regular_color, self.highlight_color = color, highlight
		self.action = action
		self.action_effect = action_effect
		self.color = self.regular_color
		self.mouse_on = False
		Button.List.append(self)

	@staticmethod
	def update(screen, list):

		for button in list:
			pygame.draw.rect(screen, button.color, (button.x, button.y, button.w, button.h))
			x = button.w / 2
			y = button.h / 2
			text_to_screen(screen, button.msg, button.x+x, button.y+y)

	def mouse_over(self):
		self.color = self.highlight_color
		self.mouse_on = True
	def mouse_off(self):
		self.color = self.regular_color
		self.mouse_on = False
	def do_action(self):
		if self.action == "clear_attack":
			Button.attack = 0
		elif self.action == "clear_defense":
			Button.defense = 0
		elif self.action == "clear_move":
			Button.move_power = 0
		elif self.action == "STAB":
			if Button.STAB == "No":
				Button.STAB = "Yes"
			elif Button.STAB == "Yes":
				Button.STAB = "No"
		elif self.action == "calculate":
			if Button.attack > 0 and Button.defense > 0 and Button.move_power > 0:
				#Button.damage = 0
				Button.damage = damage_calc(Button.attack, Button.defense,
					Button.move_power, Button.STAB, Button.type_advantage)
		if self.action_effect == "attack":
			if Button.attack == 0:
				Button.attack = self.action
			elif len(str(Button.attack)) < 3:
				Button.attack *= 10
				Button.attack += self.action
		elif self.action_effect == "defense":
			if Button.defense == 0:
				Button.defense = self.action
			elif len(str(Button.defense)) < 3:
				Button.defense *= 10
				Button.defense += self.action
		elif self.action_effect == "move_power":
			if Button.move_power == 0:
				Button.move_power = self.action
			elif len(str(Button.move_power)) < 3:
				Button.move_power *= 10
				Button.move_power += self.action
		elif self.action_effect == "effectiveness":
			Button.type_advantage = self.action

buttons = [
	["1", 100, 175, 20, 20, BLUE, BRIGHT_BLUE, 1, "attack"],
	["2", 125, 175, 20, 20, BLUE, BRIGHT_BLUE, 2, "attack"],
	["3", 150, 175, 20, 20, BLUE, BRIGHT_BLUE, 3, "attack"],
	["4", 175, 175, 20, 20, BLUE, BRIGHT_BLUE, 4, "attack"],
	["5", 200, 175, 20, 20, BLUE, BRIGHT_BLUE, 5, "attack"],
	["6", 100, 200, 20, 20, BLUE, BRIGHT_BLUE, 6, "attack"],
	["7", 125, 200, 20, 20, BLUE, BRIGHT_BLUE, 7, "attack"],
	["8", 150, 200, 20, 20, BLUE, BRIGHT_BLUE, 8, "attack"],
	["9", 175, 200, 20, 20, BLUE, BRIGHT_BLUE, 9, "attack"],
	["0", 200, 200, 20, 20, BLUE, BRIGHT_BLUE, 0, "attack"],
	["clear", 225, 140, 70, 25, GREEN, BRIGHT_GREEN, "clear_attack", None],
	["1", 400, 175, 20, 20, BLUE, BRIGHT_BLUE, 1, "defense"],
	["2", 425, 175, 20, 20, BLUE, BRIGHT_BLUE, 2, "defense"],
	["3", 450, 175, 20, 20, BLUE, BRIGHT_BLUE, 3, "defense"],
	["4", 475, 175, 20, 20, BLUE, BRIGHT_BLUE, 4, "defense"],
	["5", 500, 175, 20, 20, BLUE, BRIGHT_BLUE, 5, "defense"],
	["6", 400, 200, 20, 20, BLUE, BRIGHT_BLUE, 6, "defense"],
	["7", 425, 200, 20, 20, BLUE, BRIGHT_BLUE, 7, "defense"],
	["8", 450, 200, 20, 20, BLUE, BRIGHT_BLUE, 8, "defense"],
	["9", 475, 200, 20, 20, BLUE, BRIGHT_BLUE, 9, "defense"],
	["0", 500, 200, 20, 20, BLUE, BRIGHT_BLUE, 0, "defense"],
	["clear", 530, 140, 70, 25, GREEN, BRIGHT_GREEN, "clear_defense", None],
	["1", 300, 325, 20, 20, BLUE, BRIGHT_BLUE, 1, "move_power"],
	["2", 325, 325, 20, 20, BLUE, BRIGHT_BLUE, 2, "move_power"],
	["3", 350, 325, 20, 20, BLUE, BRIGHT_BLUE, 3, "move_power"],
	["4", 375, 325, 20, 20, BLUE, BRIGHT_BLUE, 4, "move_power"],
	["5", 400, 325, 20, 20, BLUE, BRIGHT_BLUE, 5, "move_power"],
	["6", 300, 350, 20, 20, BLUE, BRIGHT_BLUE, 6, "move_power"],
	["7", 325, 350, 20, 20, BLUE, BRIGHT_BLUE, 7, "move_power"],
	["8", 350, 350, 20, 20, BLUE, BRIGHT_BLUE, 8, "move_power"],
	["9", 375, 350, 20, 20, BLUE, BRIGHT_BLUE, 9, "move_power"],
	["0", 400, 350, 20, 20, BLUE, BRIGHT_BLUE, 0, "move_power"],
	["clear", 425, 290, 70, 25, GREEN, BRIGHT_GREEN, "clear_move", None],
	["Calculate", 75, 390, 115, 30, GREEN, BRIGHT_GREEN, "calculate", None],
	["STAB:", 75, 350, 70, 30, GREEN, BRIGHT_GREEN, "STAB", None],
	["0.25x", 285, 425, 60, 30, BLUE, BRIGHT_BLUE, 0.25, "effectiveness"],
	["0.5x", 350, 425, 60, 30, BLUE, BRIGHT_BLUE, 0.5, "effectiveness"],
	["1x", 415, 425, 60, 30, BLUE, BRIGHT_BLUE, 1, "effectiveness"],
	["2x", 480, 425, 60, 30, BLUE, BRIGHT_BLUE, 2, "effectiveness"],
	["4x", 545, 425, 60, 30, BLUE, BRIGHT_BLUE, 4, "effectiveness"],
	]
for item in buttons:
	button = Button(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8])

while True:
	screen.fill((120,120,120))
	Button.update(screen, Button.List)
	mouse_pos = pygame.mouse.get_pos()
	mouse_x = mouse_pos[0]
	mouse_y = mouse_pos[1]
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		for button in Button.List:
			if button.x+button.w > mouse_x > button.x and button.y+button.h > mouse_y > button.y:
				button.mouse_over()
				if event.type == pygame.MOUSEBUTTONDOWN:
					button.do_action()
			else:
				button.mouse_off()
		

	text = [
	["Attacker", 150, 50],
	["Attack:", 140, 150],
	["%s" % Button.attack, 200, 150],
	#["Special Attack:", 100, 300],
	#["%s" % special_attack, 200, 300],
	["Defender", 450, 50],
	["Defense:", 440, 150],
	["%s" % Button.defense, 510, 150],
	#["Special Defense:", 400, 300],
	["Move Power:", 300, 300],
	["%s" % Button.move_power, 400, 300],
	["%s" % Button.STAB, 170, 365],
	["Damage:", 130, 445],
	["%s" % Button.damage, 225, 445],
	["Type Effectiveness:", 385, 400],
	["%sx" % Button.type_advantage, 525, 400]
	]
	
	for item in text:
		text_to_screen(screen, item[0], item[1], item[2])

	pygame.display.set_caption("Damage Calculator")
	pygame.display.flip()
	clock.tick(FPS)
	total_frames += 1
