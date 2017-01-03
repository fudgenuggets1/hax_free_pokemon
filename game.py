from __future__ import division
import pygame, Functions, math, time, computer_move
from yo_buttons import Button
from pokemon import *
from vision import *
from pokemon_types import *


class Game():

	home_screen = Home_Screen()
	team_builder_screen = Team_Builder_Screen()
	play_screen = Play_Screen()
	options_screen = Options_Screen()
	gym_leaders_screen = Gym_Leaders_Screen()

	screens = [
    home_screen,
    team_builder_screen,
    play_screen,
    options_screen,
    gym_leaders_screen
    ]
	current_screen_number = 0

	Pokemon_Team = test_team
	Pokemon_List = Pokemon_Team.list
	opponent = test_opponent
	Opponent_Pokemon_List = opponent.list

	current_pokemon_number = 0
	current_opponent_number = 0

	current_turn_text = set([])
	turn_text = set([])
	battle_text = []
	current_turn = 0
	turn_index = -1
	dead_text = ""

	current_turn_sprites = [Pokemon_List[0], Opponent_Pokemon_List[0]]
	turn_sprites = set([])
	battle_sprites = []
	current_sprites = [Pokemon_List[0], Opponent_Pokemon_List[0]]
	battle_sprites.append(current_sprites)

	text_y = 0
	pause = False
	previous_screen = None
	square_info = ["","","",""]
	show_party = False
	Pokemon_Party = [1, 2, 3, 4]
	Opponent_Party = [1, 2, 3, 4]
	Pokemon_Fainted = False
	switched_in = False
	switching = False
	opponent_switching = False
	second_move_info = None
	first_move_done = False
	second_move_done = False
	going_to_switch = False
	can_switch = True
	opponent_can_switch = True
	image_filename_list = [
	    'images/next_move.png',
	    'images/next_pokemon.png',
	    'images/exit_text.png',
	    'images/continue.png',
	    'images/game_over.png',
	]
	text_bubbles = [pygame.image.load(file_name) for file_name in image_filename_list]
	help_text_number = 0
	turn_logged = False
	playing = True
	stop_that = False

	player_field = {
		"stealth rock": False,
		"spikes": 0,
		"toxic spikes": 0,
	}
	opponent_field = {
		"stealth rock": False,
		"spikes": 0,
		"toxic spikes": 0,
	}
	stealth_rock_sprite = pygame.image.load("images/stealth_rock.png")
	spike_sprite = pygame.image.load('images/triangle.png')
	damage_list = []
	new_y = 90

	@staticmethod
	def update(screen):
		Game.current_screen = Game.screens[Game.current_screen_number]
		Game.current_screen.Block_List.draw(screen)
		Button.update(screen, Game.current_screen.Button_List)
		Game.current_pokemon = Game.Pokemon_List[Game.current_pokemon_number]
		Game.opponent.pokemon = Game.Opponent_Pokemon_List[Game.current_opponent_number]
		Game.Opponent_Pokemon_List = Game.opponent.list
		Game.help_text = Game.text_bubbles[Game.help_text_number]

		Game.screen = screen

		if Game.current_screen_number == 2:
			Game.update_info(screen)
		elif Game.current_screen_number == 1:
			Game.show_stats(screen)
		elif Game.current_screen_number == 3:
			Game.options(screen)
		elif Game.current_screen_number == 4:
			Game.Gym_Leaders(screen)

	@staticmethod
	def update_info(screen):

		# sprites
		if Game.turn_index+1 == Game.current_turn:	
			pokemon, opponent = Game.current_pokemon, Game.opponent.pokemon
			pokemon_health, opponent_health = Game.current_pokemon.current_health, Game.opponent.pokemon.current_health

		else:
			pokemon, opponent = Game.current_sprites[0], Game.current_sprites[1]
			if Game.turn_index == 0:
				pokemon_health, opponent_health = pokemon.max_health, opponent.max_health
			else:
				pokemon_health, opponent_health = Game.current_sprites[2], Game.current_sprites[3]
		sprites = [
		        [pokemon.back_image, (225, 250)],
		        [opponent.front_image, (475, 50)],
		        [pokemon.type.image, (495, 265)],
		        [opponent.type.image, (75, 40)],
		    ]
		if opponent.type2 != None:
		    type2 = (opponent.type2.image, (107, 40))
		    sprites.append(type2)
		if pokemon.type2 != None:
		    type2 = (pokemon.type2.image, (527, 265))
		    sprites.append(type2)

		help_text = [Game.help_text, (5, 300)]
		sprites.append(help_text)
		
		# text
		text = [
		["%s" % Game.square_info[0], 125, 385],
		["%s" % Game.square_info[1], 375, 385],
		["%s" % Game.square_info[2], 125, 442],
		["%s" % Game.square_info[3], 375, 442],
		["%s" % pokemon.name, 525, 250],
		["%s" % opponent.name, 100, 25],
		["%s/%s" % (int(math.floor(pokemon_health)), pokemon.max_health), 525, 315],
		["%s" % Game.get_percent(opponent_health, opponent.max_health), 105, 90],
		["hp:", 30, 70],
		["hp:", 450, 295],
		]
		for item in text:
			Functions.text_to_screen(screen, item[0], item[1], item[2], 20)
		pokemon_hp = math.floor((pokemon_health / pokemon.max_health) * 110)
		opponent_hp = math.floor((opponent_health / opponent.max_health) * 110)

		# Show moves or team in the squares
		if not Game.show_party:
			Game.square_info = [Game.current_pokemon.move1.name, Game.current_pokemon.move2.name, Game.current_pokemon.move3.name, Game.current_pokemon.move4.name,]
			secondary_info = [
				["power:", 185, 405],
				["%s" % Game.current_pokemon.move1.power, 230, 405],
				["power:", 435, 405],
				["%s" % Game.current_pokemon.move2.power, 480, 405],
				["power:", 185, 462],
				["%s" % Game.current_pokemon.move3.power, 230, 462],
				["power:", 435, 462],
				["%s" % Game.current_pokemon.move4.power, 480, 462],
			]
			info_sprites = [
				[Game.current_pokemon.move1.type.image, (50, 400)],
				[Game.current_pokemon.move1.contact_image, (100, 400)],
				[Game.current_pokemon.move2.type.image, (300, 400)],
				[Game.current_pokemon.move2.contact_image, (350, 400)],
				[Game.current_pokemon.move3.type.image, (50, 457)],
				[Game.current_pokemon.move3.contact_image, (100, 457)],
				[Game.current_pokemon.move4.type.image, (300, 457)],
				[Game.current_pokemon.move4.contact_image, (350, 457)],
			]

		elif Game.show_party:
			Game.square_info = [Game.Pokemon_Party[0].name, Game.Pokemon_Party[1].name, Game.Pokemon_Party[2].name, Game.Pokemon_Party[3].name]
			secondary_info = [
				["hp:", 160, 408],
				["%s/%s" % (int(Game.Pokemon_Party[0].current_health), Game.Pokemon_Party[0].max_health), 210, 408],
				["hp:", 410, 408],
				["%s/%s" % (int(Game.Pokemon_Party[1].current_health), Game.Pokemon_Party[1].max_health), 460, 408],
				["hp:", 160, 465],
				["%s/%s" % (int(Game.Pokemon_Party[2].current_health), Game.Pokemon_Party[2].max_health), 210, 465],
				["hp:", 410, 465],
				["%s/%s" % (int(Game.Pokemon_Party[3].current_health), Game.Pokemon_Party[3].max_health), 460, 465],	
			]
			info_sprites = [
				[Game.Pokemon_Party[0].type.image, (50, 400)],
				[Game.Pokemon_Party[1].type.image, (300, 400)],
				[Game.Pokemon_Party[2].type.image, (50, 457)],
				[Game.Pokemon_Party[3].type.image, (300, 457)],
			]
			if Game.Pokemon_Party[0].type2 != None:
				sprite = (Game.Pokemon_Party[0].type2.image, (82, 400))
				sprites.append(sprite)
			if Game.Pokemon_Party[1].type2 != None:
				sprite = (Game.Pokemon_Party[1].type2.image, (332, 400))
				sprites.append(sprite)
			if Game.Pokemon_Party[2].type2 != None:
				sprite = (Game.Pokemon_Party[2].type2.image, (82, 457))
				sprites.append(sprite)
			if Game.Pokemon_Party[3].type2 != None:
				sprite = (Game.Pokemon_Party[3].type2.image, (332, 457))
				sprites.append(sprite)

		sprite_list, Win, Lose = Game.check_pokemon()
		for item in sprite_list:
			sprites.append(item)

		# Entry Hazards
		if Game.opponent_field["stealth rock"]:
			rock_icon = (Game.stealth_rock_sprite, (425, 100))
			sprites.append(rock_icon)
		if Game.player_field["stealth rock"]:
			rock_icon = (Game.stealth_rock_sprite, (350, 300))
			sprites.append(rock_icon)
		if Game.opponent_field["spikes"] > 0:
			x = 450
			for spike in range(Game.opponent_field["spikes"]):	
				spikes_icon = (Game.spike_sprite, (x, 150))
				sprites.append(spikes_icon)
				x+=25
		if Game.player_field["spikes"] > 0:
			x = 300
			for spike in range(Game.player_field["spikes"]):	
				spikes_icon = (Game.spike_sprite, (x, 340))
				sprites.append(spikes_icon)
				x+=25

		def blitting_the_sprites():
		    for item in info_sprites:
		        screen.blit(item[0], item[1])
		    for item in secondary_info:
		        Functions.text_to_screen(screen, item[0], item[1], item[2], 18)
		    for item in sprites:
		        screen.blit(item[0], item[1])
		blitting_the_sprites()

		#### Health Bars ###
		block_list = pygame.sprite.Group()
		health_bars = [
			[50, 65, 110, 12, RED],
			[470, 290, 110, 12, RED],
		]
		for block in health_bars:
			new_block = Block(block[0], block[1], block[2], block[3], block[4])
			block_list.add(new_block)
		block_list.draw(screen)

		block_list = pygame.sprite.Group()

		# Health Bar Colors
		if 28 < pokemon_hp <= 55:
			pokemon_color = YELLOW
		elif 0 < pokemon_hp <= 28:
			pokemon_color = DARK_RED
		else:
			pokemon_color = BLUE
		if 28 < opponent_hp <= 55:
			opponent_color = YELLOW
		elif 0 < opponent_hp <= 28:
			opponent_color = DARK_RED
		else:
			opponent_color = BLUE
		health_bar_color = (25,25,25)
		blocks = [
			[470, 290, pokemon_hp, 12, pokemon_color],
			[50, 65, opponent_hp, 12, opponent_color],
			[160, 63, 6, 16, health_bar_color],
			[580, 288, 6, 16, health_bar_color],
			[48, 63, 2, 16, health_bar_color],
			[468, 288, 2, 16, health_bar_color],
			[48, 77, 112, 2, health_bar_color],
			[468, 302, 112, 2, health_bar_color],
			[48, 63, 112, 2, health_bar_color],
			[468, 288, 112, 2, health_bar_color],
		]
		for block in blocks:
			try:	
				new_block = Block(block[0], block[1], block[2], block[3], block[4])
				block_list.add(new_block)
			except:
				print block
		block_list.draw(screen)

		# Show the current turn info and pause the Game
		if Game.pause:
			if Game.playing:
				Game.help_text_number = 3
			
		if not Game.pause:
			Game.log_turn(False)
			Game.current_turn_text = set([])
			Game.first_move_done = False
			Game.second_move_done = False
			Game.help_text_number = 0
			Game.turn_logged = False
			Game.stop_that = False
			Game.damage_list[:] = []
			Game.new_y = 90
		# Check if a pokemon on the battlefield has fainted
		if math.floor(Game.current_pokemon.current_health) <= 0 or math.floor(Game.opponent.pokemon.current_health) <= 0:
			Game.Pokemon_Fainted = True
			Game.pause = True
			if Game.current_pokemon.current_health <= 0:
				Game.show_party = True
				Game.current_pokemon.fainted = True
				Game.current_pokemon.current_health = 0
				Game.help_text_number = 1
			if Game.opponent.pokemon.current_health <= 0:
				Game.opponent.pokemon.fainted = True
				Game.opponent.pokemon.current_health = 0
				
		# Tell player a Pokemon has fainted
		if Game.Pokemon_Fainted and not Game.stop_that:
			Game.pause = True
			if Game.current_pokemon.fainted and not Game.opponent.pokemon.fainted:	
				dead_text = ("%s died!" % Game.current_pokemon.name,1,1, Game.new_y, RED)
				
				Functions.text_to_list(dead_text)
				Game.stop_that = True
				
			elif Game.opponent.pokemon.fainted and not Game.current_pokemon.fainted:
				dead_text = ("%s died!" % Game.opponent.pokemon.name,1,1, Game.new_y, BLUE)
				
				Functions.text_to_list(dead_text)
				if not Game.switching:
					Game.switch_opponent(True)
				else:
					
					Game.going_to_switch = True
				Game.stop_that = True

			elif Game.current_pokemon.fainted and Game.opponent.pokemon.fainted:
				dead_text = ("%s died!" % Game.current_pokemon.name, 150, Game.new_y+35, 25, RED)
				Functions.text_to_list(dead_text)
				dead_text = ("%s died!" % Game.opponent.pokemon.name, 150, Game.new_y, BLUE)
				Functions.text_to_list(dead_text)
				Game.stop_that = True

		# Win or Lose
		if Win and Game.playing:
			Game.game_over(screen, Game.current_pokemon)
			Game.playing = False
		if Lose:
			Game.game_over(screen, Game.opponent.pokemon)

		# Show specific turn info on the side
		if Game.current_turn > 0:
	
			for item in Game.battle_text[Game.turn_index]:

				try:
					Functions.text_to_screen(screen, item[0], 800, item[1], 20, item[2])
				
				except:

					pass
					print(item)

			Game.current_sprites = Game.battle_sprites[Game.turn_index+1]
				
		### U-turn/Volt-Switch ###
		if Game.switching:
			Game.show_party = True
			Game.help_text_number = 1
		# Opponent U-turn/Volt-switch
		if Game.opponent_switching:
			switch = computer_move.best_switch(Game.current_pokemon, Game.Opponent_Party)
			Game.switch_move(Game.opponent.pokemon, switch)
		
		# Switch after dying from U-turn/Volt-switch
		if not Game.switching and Game.going_to_switch:
			Game.switch_opponent()

		# Game Over help text
		if not Game.playing:
			Game.help_text_number = 4

		# After Turn
		"""if Game.second_move_done:
			if Game.current_pokemon.speed > Game.opponent.pokemon.speed:	
				Game.after_turn_item(Game.current_pokemon)
				Game.after_turn_item(Game.opponent.pokemon)
			else:
				Game.after_turn_item(Game.opponent.pokemon)
				Game.after_turn_item(Game.current_pokemon)
			Game.second_move_done = False"""

		#show damage
		for damage in Game.damage_list:
			#Functions.text_to_screen(screen, damage[0], damage[1], damage[2], damage[3], damage[5])
			pass

	@staticmethod
	def show_stats(screen):
		text = [
		["%s" % Game.current_pokemon.max_health, 515, 150],
		["%s" % Game.current_pokemon.attack, 515, 210],
		["%s" % Game.current_pokemon.defense, 515, 270],
		["%s" % Game.current_pokemon.special_attack, 515, 330],
		["%s" % Game.current_pokemon.special_defense, 515, 390],
		["%s" % Game.current_pokemon.speed, 515, 450],
		]

		for item in text:
			Functions.text_to_screen(screen, item[0], item[1], item[2])

		buttons = [
		["%s" % Game.current_pokemon.name, 75, 25, 250, 30, BLUE, BLUE, None],
		["Type: %s" % Game.current_pokemon.type.name, 375, 5, 200, 30, BLUE, BLUE, None],
		#move1 & stats
		["Move 1: %s" % Game.current_pokemon.move1.name, 25, 75, 275, 30, BLUE, BLUE, None],
		["Type: %s" % Game.current_pokemon.move1.type.name, 25, 107, 250, 30, DODGER_BLUE, BLUE, None],
		["Power:%s" % Game.current_pokemon.move1.power, 5, 142, 125, 30, DODGER_BLUE, BLUE, None],
		["Contact: %s" % Game.current_pokemon.move1.contact, 135, 142, 200, 30, DODGER_BLUE, BLUE, None],
		# move 2 & stats
		["Move 2: %s" % Game.current_pokemon.move2.name, 25, 175, 275, 30, BLUE, BLUE, None],
		["Type: %s" % Game.current_pokemon.move2.type.name, 25, 207, 250, 30, DODGER_BLUE, BLUE, None],
		["Power:%s" % Game.current_pokemon.move2.power, 5, 242, 125, 30, DODGER_BLUE, BLUE, None],
		["Contact: %s" % Game.current_pokemon.move2.contact, 135, 242, 200, 30, DODGER_BLUE, BLUE, None],
		# move 3 & stats
		["Move 3: %s" % Game.current_pokemon.move3.name, 25, 275, 275, 30, BLUE, BLUE, None],
		["Type: %s" % Game.current_pokemon.move3.type.name, 25, 307, 250, 30, DODGER_BLUE, BLUE, None],
		["Power:%s" % Game.current_pokemon.move3.power, 5, 342, 125, 30, DODGER_BLUE, BLUE, None],
		["Contact: %s" % Game.current_pokemon.move3.contact, 135, 342, 200, 30, DODGER_BLUE, BLUE, None],
		# move 4 & stats
		["Move 4: %s" % Game.current_pokemon.move4.name, 25, 375, 275, 30, BLUE, BLUE, None],
		["Type: %s" % Game.current_pokemon.move4.type.name, 25, 407, 250, 30, DODGER_BLUE, BLUE, None],
		["Power:%s" % Game.current_pokemon.move4.power, 5, 442, 125, 30, DODGER_BLUE, BLUE, None],
		["Contact: %s" % Game.current_pokemon.move4.contact, 135, 442, 200, 30, DODGER_BLUE, BLUE, None],
		# points
		["Points: %s" % Game.current_pokemon.points, 400, 75, 150, 30, BRIGHT_BLUE, BRIGHT_BLUE, None],
		["Health", 340, 135, 100, 30, BLUE, BLUE, None],
		["Attack", 340, 195, 100, 30, BLUE, BLUE, None],
		["Defense", 340, 255, 100, 30, BLUE, BLUE, None],
		["Sp.Atk", 340, 315, 100, 30, BLUE, BLUE, None],
		["Sp.Def", 340, 375, 100, 30, BLUE, BLUE, None],
		["Speed", 340, 435, 100, 30, BLUE, BLUE, None],
		]
		if Game.current_pokemon.type2 != None:
			type2 = ["%s" % Game.current_pokemon.type2.name, 375, 35, 200, 30, BLUE, BLUE, None]
			buttons.append(type2)
		button_list = []
		for item in buttons:
			button = Button(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
			button_list.append(button)

		base_stats = [
		["%s" % Game.current_pokemon.base_health, 460, 150],
		["%s" % Game.current_pokemon.base_attack, 460, 210],
		["%s" % Game.current_pokemon.base_defense, 460, 270],
		["%s" % Game.current_pokemon.base_special_attack, 460, 330],
		["%s" % Game.current_pokemon.base_special_defense, 460, 390],
		["%s" % Game.current_pokemon.base_speed, 460, 450],
		]

		for item in base_stats:
			Functions.text_to_screen(screen, item[0], item[1], item[2], 20)

		Button.update(screen, button_list)
		Pokemon.update()

		Game.current_pokemon.move1 = Game.current_pokemon.move_list[Game.current_pokemon.move1_number]
		Game.current_pokemon.move2 = Game.current_pokemon.move_list[Game.current_pokemon.move2_number]
		Game.current_pokemon.move3 = Game.current_pokemon.move_list[Game.current_pokemon.move3_number]
		Game.current_pokemon.move4 = Game.current_pokemon.move_list[Game.current_pokemon.move4_number]

		Game.current_pokemon.move_set[0] = Game.current_pokemon.move1
		Game.current_pokemon.move_set[1] = Game.current_pokemon.move2
		Game.current_pokemon.move_set[2] = Game.current_pokemon.move3
		Game.current_pokemon.move_set[3] = Game.current_pokemon.move4

	@staticmethod
	def options(screen):
		button_list = []
		y = 100
		for pokemon in Game.opponent.list:
			button = Button("%s" % pokemon.name, 335, y, 300, 30, RED, RED, None)
			button_list.append(button)
			y += 50
		y = 100
		for pokemon in Game.Pokemon_List:
			button = Button("%s" % pokemon.name, 5, y, 300, 30, BLUE, BLUE, None)
			button_list.append(button)
			y += 50

		text = [
		["Your Team", 155, 50],
		["Opponent Team", 485, 50],
		["%s Pokemon" % len(Pokemon.All_Pokemon), 300, 25],
		["%s" % len(Opponent.All_Pokemon), 500, 25],
		]

		for item in text:
			Functions.text_to_screen(screen, item[0], item[1], item[2])
		Button.update(screen, button_list)

	@staticmethod
	def Gym_Leaders(screen):
		text = [
			["Gym Leaders Room", 325, 25],
			["Click to Challenge!", 325, 50]
		]
		for item in text:
			Functions.text_to_screen(screen, item[0], item[1], item[2])

	@staticmethod
	def reset():

		Game.pause = False
		Game.current_pokemon_number = 0
		Game.current_opponent_number = 0
		for pokemon in Game.Pokemon_List:
			pokemon.current_health = pokemon.max_health
			pokemon.fainted = False
			pokemon.first_turn = True
		for pokemon in Game.Opponent_Pokemon_List:
			pokemon.current_health = pokemon.max_health
			pokemon.fainted = False
			pokemon.first_turn = True
		Game.current_turn_text = set([])
		Game.show_party = False
		Game.Pokemon_Fainted = False
		Game.battle_text[:] = []
		Game.turn_index = -1
		Game.current_turn = 0
		Game.switching = False
		Game.opponent_switching = False
		Game.first_move_done = False
		Game.second_move_done = False
		Game.going_to_switch = False
		Game.help_text_number = 0
		Game.turn_logged = False
		Game.playing = True
		Game.stop_that = False
		Game.battle_sprites[:] = []
		Game.current_sprites = [Game.Pokemon_List[0], Game.Opponent_Pokemon_List[0]]
		Game.battle_sprites.append(Game.current_sprites)
		Game.player_field["stealth rock"] = False
		Game.opponent_field["stealth rock"] = False
		Game.player_field["spikes"] = 0
		Game.opponent_field["spikes"] = 0

	@staticmethod
	def attack(attacker, defender, move, y):
		type_advantage = Game.type_advantage(defender, move)
		power = Game.damage_calc(attacker, defender, move, type_advantage)
		x = y
		damage = None
		if defender.current_health - power > 0 and type_advantage > 0:
			defender.current_health -= power
			damage = power
		elif defender.current_health - power <= 0:
			damage = defender.current_health
			defender.current_health = 0
		x+=35
		
		if type_advantage == 2 or type_advantage == 4:
			type_advantage_text = ["It's super effective!", 375, y+35]
		elif type_advantage == 0.5 or type_advantage == 0.25:
			type_advantage_text = ["It's not very effective...", 375, y+35]
		elif type_advantage == 0:
			type_advantage_text = ["It didn't do anything...", 375, y+35]
		else:
			type_advantage_text = ""
			x -= 35
		last_text = ""
		if attacker == Game.current_pokemon:
			if type_advantage > 0:
				last_text = "%s lost %s HP!" % (defender.name, Game.get_percent(damage, defender.max_health))
			color = BLUE
		elif attacker == Game.opponent.pokemon:
			if type_advantage > 0:
				last_text = "%s lost %s HP!" % (defender.name, int(math.floor(damage)))
			color = DARK_RED
		text = [
		["%s used %s!" % (attacker.name, move.name), 375, y],
		["%s" % last_text, 375, x+35]
		]
		if type_advantage != 1:
			text.append(type_advantage_text)
		for item in text:
			Functions.text_to_list(item, color)
		attacker.first_turn = False

		Game.damage_sprites(defender, damage)
		return damage

	@staticmethod
	def do_moves(move):
		Game.pause = True
		opponent_move = Game.opponent_move()		
		if not isinstance(move, int) and not isinstance(opponent_move, int):	
			if move.priority == opponent_move.priority:	
				if Game.current_pokemon.speed > Game.opponent.pokemon.speed:
					first = Game.current_pokemon
					second = Game.opponent.pokemon

				elif Game.opponent.pokemon.speed >= Game.current_pokemon.speed:
					first = Game.opponent.pokemon
					second = Game.current_pokemon
			
			elif move.priority > opponent_move.priority:
				first = Game.current_pokemon
				second = Game.opponent.pokemon
	
			elif move.priority < opponent_move.priority:
				first = Game.opponent.pokemon
				second = Game.current_pokemon
			
			if first == Game.current_pokemon:
				move1 = move
				move2 = opponent_move
			elif first == Game.opponent.pokemon:
				move1 = opponent_move
				move2 = move

			can_move = True
			if move1.effect != None:
				can_move = Game.move_with_effect(first, second, move1, move2, Game.text_y)
			else:
				Game.attack(first, second, move1, Game.text_y)
			
			Game.first_move_done = True
			if (second.current_health > 0 and can_move):
				if not Game.switching and not Game.opponent_switching:
					if move2.effect != None:
						Game.move_with_effect(second, first, move2, 1, Game.text_y)
					else:
						Game.attack(second, first, move2, Game.text_y)
					Game.second_move_done = True
				elif Game.switching or Game.opponent_switching: 
					Game.second_move_info = (second, first, move2, Game.text_y)
		
		elif isinstance(move, int) and isinstance(opponent_move, int):
			if Game.current_pokemon.speed > Game.opponent.pokemon.speed:
				Game.switch_pokemon(Game.current_pokemon, move, Game.text_y)
				Game.switch_pokemon(Game.opponent.pokemon, opponent_move, Game.text_y)
			elif Game.current_pokemon.speed <= Game.opponent.pokemon.speed:
				Game.switch_pokemon(Game.opponent.pokemon, opponent_move, Game.text_y)
				Game.switch_pokemon(Game.current_pokemon, move, Game.text_y)
			Game.second_move_done = True

		else:
			if isinstance(move, int):
				defender = Game.switch_pokemon(Game.current_pokemon, move, Game.text_y)
				Game.first_move_done = True
				if opponent_move.effect == None:	
					Game.attack(Game.opponent.pokemon, defender, opponent_move, Game.text_y)
				elif opponent_move.effect != None:
					Game.move_with_effect(Game.opponent.pokemon, defender, opponent_move, move, Game.text_y)
				Game.second_move_done = True
			elif not isinstance(move, int):
				defender = Game.switch_pokemon(Game.opponent.pokemon, opponent_move, Game.text_y)
				Game.first_move_done = True
				if move.effect == None:	
					Game.attack(Game.current_pokemon, defender, move, Game.text_y)
				elif move.effect != None:
					Game.move_with_effect(Game.current_pokemon, defender, move, opponent_move, Game.text_y)
				Game.second_move_done = True
		
		if not Game.turn_logged:	
			Game.log_turn()
			

	@staticmethod
	def damage_calc(attacker, defender, move, type_advantage):
		# Damage = (0.44*(attack/defense)*move power)*modifier
		# Modifier = STAB * Type effectiveness * other(items, abilities)
		if move.contact == "physical":
			attack = attacker.attack
			defense = defender.defense
		elif move.contact == "special":
			attack = attacker.special_attack
			defense = defender.special_defense
		power = move.power

		#STAB
		STAB = 1
		if attacker.type.name == move.type.name:
			STAB = 1.5
		if attacker.type2 != None and STAB == 1:
			if attacker.type2.name == move.type.name:
				STAB = 1.5
		# Damage calculation
		damage = math.floor((0.2 * (attack / defense) * power + 2) * (type_advantage * STAB))
		return damage

	@staticmethod
	def type_advantage(defender, move):
		type_advantage = 1

		for weakness in defender.type.weakness_list:
			if move.type.name == weakness:
				type_advantage = 2
				break
		for resist in defender.type.resist_list:
			if move.type.name == resist:
				type_advantage = 0.5
				break
		for immune in defender.type.immune_list:
			if move.type.name == immune:
				type_advantage = 0
				break

		if defender.type2 != None and type_advantage > 0:
			for weakness in defender.type2.weakness_list:
				if move.type.name == weakness:
					if type_advantage == 1:
						type_advantage = 2
					elif type_advantage == 2:
						type_advantage = 4
					elif type_advantage == 0.5:
						type_advantage = 1
					break
			for resist in defender.type2.resist_list:
				if move.type.name == resist:
					if type_advantage == 1:
						type_advantage = 0.5
					elif type_advantage == 2:
						type_advantage = 1
					elif type_advantage == 0.5:
						type_advantage = 0.25
					break
			for immune in defender.type2.immune_list:
				if move.type.name == immune:
					type_advantage = 0
					break

		return type_advantage

	@staticmethod
	def get_percent(numerator, denominator):
		number = int(round((numerator/denominator)*100))
		percent = ("%s%%" % number)
		return percent

	@staticmethod
	def switch_pokemon(pokemon, pokemon_number, y):
		if pokemon == Game.current_pokemon:
			old = Game.current_pokemon
			new = Game.Pokemon_Party[pokemon_number]
			new_number = Game.Pokemon_List.index(new)
			Game.current_pokemon_number = new_number
			Game.show_party = False
			poke = Game.opponent.pokemon
			color = GREEN
			field = Game.player_field
		else:
			old = Game.opponent.pokemon
			new = Game.Opponent_Party[pokemon_number]
			new_number = Game.Opponent_Pokemon_List.index(new)
			Game.current_opponent_number = new_number
			poke = Game.current_pokemon
			color = YELLOW
			Game.switched_in = True
			field = Game.opponent_field
		text = [
		["%s come back!" % old.name, 375, y],
		["Go %s!" % new.name, 375, y+35]
		]
		for item in text:
			Functions.text_to_list(item, color)
		new.first_turn = True
		Game.switching = False
		
		Game.entry_hazard_damage(new, field)
		
		return new

	@staticmethod
	def send_in_pokemon(pokemon_number):
		if Game.Pokemon_Party[pokemon_number].current_health > 0:
			
			Game.pause = True
			old = Game.current_pokemon
			new = Game.Pokemon_Party[pokemon_number]
			new_number = Game.Pokemon_List.index(new)
			Game.current_pokemon_number = new_number
			text = ("Go %s" % new.name, Game.new_y, GREEN)
			Functions.text_to_list(text)
			Game.entry_hazard_damage(new, Game.player_field)
			Game.Pokemon_Fainted = False
			Game.show_party = False
			new.first_turn = True
			

	@staticmethod
	def switch_opponent(dead=False):
		next_switch = computer_move.best_switch(Game.current_pokemon, Game.Opponent_Party, dead)
		Game.send_in_opponent(next_switch)
	
	@staticmethod
	def game_over(screen, winner):
		Game.pause = True
		Game.show_party = False
		Game.help_text_number = 4
		if Game.playing:
			if winner == Game.current_pokemon:
				text = ("You win!", Game.new_y, WHITE)
			elif winner == Game.opponent.pokemon:
				text = ("You are out of Pokemon!", Game.new_y, WHITE)
			Functions.text_to_list(text)
			Game.playing = False

	@staticmethod
	def send_in_opponent(pokemon_number):
		if isinstance(pokemon_number, int):
			if Game.Opponent_Party[pokemon_number].current_health > 0:
				old = Game.opponent.pokemon
				new = Game.Opponent_Party[pokemon_number]
				new_number = Game.Opponent_Pokemon_List.index(new)
				Game.current_opponent_number = new_number
				
				text = ("Go %s" % new.name, Game.new_y, YELLOW)
				Functions.text_to_list(text)
				Game.entry_hazard_damage(new, Game.opponent_field)
				Game.Pokemon_Fainted = False
				Game.show_party = False
				Game.switched_in = True
				new.first_turn = True
				Game.going_to_switch = False

	@staticmethod
	def log_turn(next_turn=True):
		if next_turn:
			Game.turn_index = Game.current_turn	
			Game.current_turn += 1
			turn_number = ("Turn %s" % Game.current_turn, 40, (255,255,255))
			Game.turn_text.add(turn_number)
			Game.battle_text.append(Game.turn_text)
			Game.turn_logged = True
			Game.log_sprites(Game.current_pokemon, Game.opponent.pokemon)
		else:
			for text in Game.turn_text:
				Functions.text_to_list(text)
		for text in Game.current_turn_text:
			Game.turn_text.add(text)
		Game.turn_text = set([])

	@staticmethod
	def log_sprites(pokemon, opponent):
		Game.current_turn_sprites = (pokemon, opponent, pokemon.current_health, opponent.current_health)
		Game.battle_sprites.append(Game.current_turn_sprites)

	@staticmethod
	def move_with_effect(attacker, defender, move, defender_move, y):
		can_move = True
		if attacker == Game.current_pokemon:
			attacker_color = BLUE
		elif attacker == Game.opponent.pokemon:
			attacker_color = DARK_RED
		if move.power > 0:	
			
			if move.effect == "flinch": 
				if attacker.first_turn:
					Game.attack(attacker, defender, move, y)
					if defender.current_health > 0 and not isinstance(defender_move, int):
						flinch_text = ("%s flinched!" % defender.name, 375, y+110, 25, DARK_RED)
						
						Functions.text_to_list(flinch_text)
						can_move = False
				else:
					flinch_text = ("%s used %s..." % (attacker.name, move.name), 375, y, 25, attacker_color)
					flinch_text2 = ("But it failed!", 375, y+35, 25, attacker_color)
				
					Functions.text_to_list(flinch_text)
					Functions.text_to_list(flinch_text2)
			elif move.effect == "sucker_punch":
				if isinstance(defender_move, int):
					sucker_text = ("%s used %s..." % (attacker.name, move.name), 375, y, 25, attacker_color)
					sucker_text2 = ("But it failed!", 375, y+35, 25, attacker_color)
					
					Functions.text_to_list(sucker_text)
					Functions.text_to_list(sucker_text2)
				else:
					Game.attack(attacker, defender, move, y)

			elif move.effect == "recoil":
				damage = Game.attack(attacker, defender, move, y)
				if damage != None:	
					recoil_damage = math.floor(damage/3)
					attacker.current_health -= recoil_damage
					recoil_text = ("%s was hurt by recoil!" % attacker.name, 375, y+105, 25, attacker_color)
				
					Functions.text_to_list(recoil_text)
					
				if attacker.current_health <= 0:
					attacker.current_health = 0
			elif move.effect == "drain":
				damage = Game.attack(attacker, defender, move, y)
		
				if damage != None:
					drain_damage = math.floor(damage/2)
					attacker.current_health += drain_damage
					drain_text = ("%s drained some health!" % attacker.name, 375, y+105, 25, GREEN)
					
					Functions.text_to_list(drain_text)
				if attacker.current_health > attacker.max_health:
					attacker.current_health = attacker.max_health
			elif move.effect == "switch":
				damage = Game.attack(attacker, defender, move, y)
				if damage:
					if Game.can_switch and attacker == Game.current_pokemon:
						Game.switching = True
						if defender.current_health <= 0:
							Game.going_to_switch = True
					elif Game.opponent_can_switch and attacker == Game.opponent.pokemon:
						Game.opponent_switching = True
				if Game.first_move_done:
					Game.second_move_done = True
				else:
					Game.first_move_done = True
				if isinstance(defender_move, int):
					Game.second_move_done = True
					Game.second_move_info = None
		else:
			can_move = Game.non_damaging_move(attacker, defender, move, defender_move, y, attacker_color)
		return can_move

	@staticmethod
	def non_damaging_move(pokemon, opponent, move, opponent_move, y, color):
		can_move = True
		if pokemon == Game.current_pokemon:
			field = Game.opponent_field
		elif pokemon == Game.opponent.pokemon:
			field = Game.player_field
		text = ("%s used %s!" % (pokemon.name, move.name), 375, y, 25, color)
		Functions.text_to_list(text, color)
		
		if move.effect == "stealth rock":
			if field["stealth rock"]:
				failed_text = ("But it failed!", 375, y+35, 25, YELLOW)
				Functions.text_to_list(failed_text)
				
			field["stealth rock"] = True
		elif move.effect == "spikes":
			if field["spikes"] < 3:
				field["spikes"] += 1
			else:
				failed_text = ("But it failed!", 375, y+35, 25, YELLOW)
				Functions.text_to_list(failed_text)

		return can_move

	@staticmethod
	def switch_move(pokemon, switch_number):
		if Game.second_move_info != None:
			y = 175
		else:
			y = 360
		
		new = Game.switch_pokemon(pokemon, switch_number, Game.text_y)
		
		if (Game.second_move_info != None and not Game.second_move_done):
			if Game.second_move_info[2].effect == None:
				Game.attack(Game.second_move_info[0], new, Game.second_move_info[2], Game.text_y)
			elif Game.second_move_info[2].effect != None:
				Game.move_with_effect(Game.second_move_info[0], new, Game.second_move_info[2], 1, Game.text_y)
			Game.second_move_info = None
				
		Game.switching = False
		Game.opponent_switching = False
			
		Game.log_turn(False)

	@staticmethod
	def entry_hazard_damage(switch, field):
		percent = math.floor(switch.max_health * 0.125)
		if field["stealth rock"]:
			
			TA = Game.type_advantage(switch, stealth_rock_damage)
			damage = math.floor(percent * TA)
			switch.current_health -= damage
			text = ("%s was hurt by Stealth Rock!" % switch.name, 150, Game.text_y, 20, YELLOW)
			Functions.text_to_list(text)
			
		if field["spikes"] > 0 and (switch.type != Flying and switch.type2 != Flying):
			
			if field["spikes"] == 2:
				percent = math.floor(switch.max_health * 0.1667)
			elif field["spikes"] == 3:
				percent = math.floor(switch.max_health * 0.25)
			switch.current_health -= percent
			text = ("%s was hurt by Spikes!" % switch.name, 150, Game.text_y, 20, YELLOW)
			Functions.text_to_list(text)
		
		sprites, win, lose = Game.check_pokemon()

	@staticmethod
	def after_turn_item(pokemon):
		pokemon = pokemon
		if pokemon == Game.current_pokemon:
			color = GREEN
		else:
			color = YELLOW
		if pokemon.item != None and pokemon.current_health > 0:	
			if pokemon.item.name == "Leftovers" and pokemon.current_health < pokemon.max_health:
				gained = math.floor(pokemon.max_health * 0.0625)	
				pokemon.current_health += gained
				if pokemon.current_health > pokemon.max_health:
					pokemon.current_health = pokemon.max_health
				gained_text = ("%s ate some Leftovers" % pokemon.name, 375, Game.text_y, 25, color)
				Functions.text_to_list(gained_text)
				
		Game.log_turn(False)

	@staticmethod
	def damage_sprites(pokemon, damage):
		pass
		"""color = WHITE
		if pokemon == Game.current_pokemon:
			x, y = 200, 250
			damage_str = ("-%s" % int(damage), x, y, 25, color)
		elif pokemon == Game.opponent.pokemon and pokemon != Game.current_pokemon:
			x, y = 250, 100
			damage_str = ("-%s" % int(damage), x, y, 25, color)
		Game.damage_list.append(damage_str)"""

	@staticmethod
	def check_pokemon():
		# Check if all pokemon in party are fainted or not
		# Also display Pokeballs for each pokemon
		sprites = []
		x = 0
		x_axis = 470
		Lose, Win = True, True
		Game.can_switch = False
		for pokemon in Game.Pokemon_List:
			pokeball = [Pokemon.Pokeball, (x_axis, 334)]
			sprites.append(pokeball)
			if pokemon != Game.current_pokemon:
				Game.Pokemon_Party[x] = pokemon
				x+=1
				if pokemon.current_health > 0:
					Game.can_switch = True
			if pokemon.current_health > 0:
				Lose = False
			else:
				icon = [Pokemon.icon_x, (x_axis, 334)]
				sprites.append(icon)
			x_axis += 24
		x = 0
		x_axis = 50
		Game.opponent_can_switch = False
		for pokemon in Game.Opponent_Pokemon_List:
			pokeball = [Pokemon.Pokeball, (x_axis, 109)]
			sprites.append(pokeball)
			if pokemon != Game.opponent.pokemon:
				Game.Opponent_Party[x] = pokemon
				x+=1
				if pokemon.current_health > 0:
					Game.opponent_can_switch = True
			if pokemon.current_health > 0:
				Win = False
			else:
				icon = [Pokemon.icon_x, (x_axis, 109)]
				sprites.append(icon)
			x_axis += 24
		return sprites, Win, Lose

	@staticmethod
	def opponent_move():
		opponent = Game.opponent.pokemon
		pokemon = Game.current_pokemon
		strongest_move = computer_move.opponent_move(pokemon, opponent)
		type_advantage = computer_move.move_type_advantage(pokemon, strongest_move)
		damage = Game.damage_calc(opponent, pokemon, strongest_move, type_advantage)
		switch = False
		kill = False
		best_switch = Game.Opponent_Party[computer_move.best_switch(pokemon, Game.Opponent_Party)]
		test = computer_move.who_wins(pokemon, opponent)
		if computer_move.best_switch(pokemon, Game.Opponent_Party):	
			if test == "loses":
				switch = True
		if pokemon.current_health - damage <= 0 and pokemon.speed < opponent.speed:
			switch = False
			kill = True
		minimum = Game.current_pokemon.max_health / 4
		if (damage >= minimum and not switch) or Game.switched_in:
			opponent_move = strongest_move
			Game.switched_in = False
		else:
			opponent_move = computer_move.best_switch(pokemon, Game.Opponent_Party)
		test_move = computer_move.stay_alive(pokemon, opponent, Game.Opponent_Party)
		if test_move and not kill:
			opponent_move = test_move
		#return spikes
		return opponent_move






