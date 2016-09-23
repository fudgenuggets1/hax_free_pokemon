from __future__ import division
import pygame, Functions, math, time
from yo_buttons import Button
from pokemon import *
from vision import *
from pokemon_types import *


class Game():

	home_screen = Home_Screen()
	team_builder_screen = Team_Builder_Screen()
	play_screen = Play_Screen()

	screens = []
	screens.append(home_screen)
	screens.append(team_builder_screen)
	screens.append(play_screen)
	current_screen_number = 0

	Pokemon_List = []

	Pokemon_List.append(squirtle)
	Pokemon_List.append(chikorita)
	Pokemon_List.append(charmander)
	Pokemon_List.append(pikachu)
	Pokemon_List.append(jynx)
	current_pokemon_number = 0

	Opponent_Pokemon_List = []
	Opponent_Pokemon_List.append(opponent_squirtle)
	Opponent_Pokemon_List.append(snorlax)
	Opponent_Pokemon_List.append(bulbasaur)
	Opponent_Pokemon_List.append(sandslash)
	Opponent_Pokemon_List.append(primeape)
	current_opponent_number = 0
	opponent = Opponent(Opponent_Pokemon_List, current_opponent_number)

	current_turn_text = []

	pause = False
	playing = True
	previous_screen = None
	square_info = ["","","",""]
	show_party = False
	Pokemon_Party = [1, 2, 3, 4]
	Opponent_Party = [1, 2, 3, 4]
	Pokemon_Fainted = False

	@staticmethod
	def update(screen):
		Game.current_screen = Game.screens[Game.current_screen_number]
		Game.current_screen.Block_List.draw(screen)
		Button.update(screen, Game.current_screen.Button_List)
		Game.current_pokemon = Game.Pokemon_List[Game.current_pokemon_number]
		Game.opponent.pokemon = Game.Opponent_Pokemon_List[Game.current_opponent_number]
		if Game.current_screen_number == 2:
			Game.update_info(screen)
		elif Game.current_screen_number == 1:
			Game.show_stats(screen)

	@staticmethod
	def update_info(screen):
		text = [
		["%s" % Game.square_info[0], 115, 397],
		["%s" % Game.square_info[1], 340, 397],
		["%s" % Game.square_info[2], 115, 447],
		["%s" % Game.square_info[3], 340, 447],
		["%s" % Game.current_pokemon.name, 525, 250],
		["%s" % Game.opponent.pokemon.name, 100, 25],
		["HP: %s/%s" % (int(round(Game.current_pokemon.current_health)), Game.current_pokemon.health), 525, 335],
		["HP: %s" % Game.get_percent(Game.opponent.pokemon.current_health, Game.opponent.pokemon.health), 105, 115],
		["Type: %s" % Game.opponent.pokemon.type.name, 100, 50],
		["Type: %s" % Game.current_pokemon.type.name, 525, 275],
		]
		if Game.current_pokemon.type2 != None:
			type2 = ["%s" % Game.current_pokemon.type2.name, 550, 305]
			text.append(type2)
		if Game.opponent.pokemon.type2 != None:
			type2 = ["%s" % Game.opponent.pokemon.type2.name, 125, 80]
			text.append(type2)
		for item in text:
			Functions.text_to_screen(screen, item[0], item[1], item[2])
		# Check if all pokemon in party are fainted or not
		x, y = 0, 0
		Lose, Win = True, True
		for pokemon in Game.Pokemon_List:
			if pokemon != Game.current_pokemon:
				Game.Pokemon_Party[x] = pokemon
				x+=1
			if pokemon.current_health > 0:
				Lose = False
		x, y = 0, 0
		for pokemon in Game.Opponent_Pokemon_List:
			if pokemon != Game.opponent.pokemon:
				Game.Opponent_Party[x] = pokemon
				x+=1
			if pokemon.current_health > 0:
				Win = False
		# Win or Lose
		if Win:
			Game.game_over(screen, Game.current_pokemon)
		if Lose:
			Game.game_over(screen, Game.opponent.pokemon)
		# Show the current turn info and pause the Game
		if Game.pause:
			for item in Game.current_turn_text:
				Functions.text_to_screen(screen, item[0], item[1], item[2], item[3], item[4])
		elif not Game.pause:
			Game.current_turn_text[:] = []
		# Check if a pokemon on the battlefield has fainted
		if Game.current_pokemon.current_health <= 0 or Game.opponent.pokemon.current_health <= 0:
			Game.Pokemon_Fainted = True
			Game.pause = True
			if Game.current_pokemon.current_health <= 0:
				Game.current_pokemon.fainted = True
			if Game.opponent.pokemon.current_health <= 0:
				Game.opponent.pokemon.fainted = True
		# Tell player a Pokemon has fainted
		if Game.Pokemon_Fainted:
			Game.pause = True
			Game.show_party = True
			if Game.current_pokemon.fainted:
				text = ("%s died!" % Game.current_pokemon.name)
				color = RED
				Functions.text_to_screen(screen, text, 200, 250, 25, color)
			elif Game.opponent.pokemon.fainted:
				dead_text = ("%s died!" % Game.opponent.pokemon.name)
				Functions.text_to_screen(screen, dead_text, 200, 250, 25, BLUE)
				switch = Game.best_switch()
				Game.send_in_opponent(switch)

		# Show moves or team in the squares
		if not Game.show_party:
			Game.square_info = [Game.current_pokemon.move1.name, Game.current_pokemon.move2.name,
			Game.current_pokemon.move3.name, Game.current_pokemon.move4.name,]
		elif Game.show_party:
			Game.square_info = [Game.Pokemon_Party[0].name, Game.Pokemon_Party[1].name, Game.Pokemon_Party[2].name, Game.Pokemon_Party[3].name]


	@staticmethod
	def show_stats(screen):
		text = [
		["%s" % Game.current_pokemon.health, 515, 150],
		["%s" % Game.current_pokemon.attack, 515, 210],
		["%s" % Game.current_pokemon.defense, 515, 270],
		["%s" % Game.current_pokemon.special_attack, 515, 330],
		["%s" % Game.current_pokemon.special_defense, 515, 390],
		["%s" % Game.current_pokemon.speed, 515, 450],
		]

		for item in text:
			Functions.text_to_screen(screen, item[0], item[1], item[2])

		buttons = [
		["Name: %s" % Game.current_pokemon.name, 75, 15, 250, 30, BLUE, BLUE, None],
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
		["Sp.Attack", 340, 315, 115, 30, BLUE, BLUE, None],
		["Sp.Defense", 335, 375, 140, 30, BLUE, BLUE, None],
		["Speed", 340, 435, 100, 30, BLUE, BLUE, None],
		]
		if Game.current_pokemon.type2 != None:
			type2 = ["%s" % Game.current_pokemon.type2.name, 375, 35, 200, 30, BLUE, BLUE, None]
			buttons.append(type2)
		button_list = []
		for item in buttons:
			button = Button(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
			button_list.append(button)

		Button.update(screen, button_list)
		Game.update_points(Game.current_pokemon)

		Game.current_pokemon.move1 = Game.current_pokemon.move_list[Game.current_pokemon.move1_number]
		Game.current_pokemon.move2 = Game.current_pokemon.move_list[Game.current_pokemon.move2_number]
		Game.current_pokemon.move3 = Game.current_pokemon.move_list[Game.current_pokemon.move3_number]
		Game.current_pokemon.move4 = Game.current_pokemon.move_list[Game.current_pokemon.move4_number]

		Game.current_pokemon.move_set[0] = Game.current_pokemon.move1
		Game.current_pokemon.move_set[1] = Game.current_pokemon.move2
		Game.current_pokemon.move_set[2] = Game.current_pokemon.move3
		Game.current_pokemon.move_set[3] = Game.current_pokemon.move4


	@staticmethod
	def reset():

		Game.pause = False
		Game.playing = True
		Game.current_pokemon_number = 0
		Game.current_opponent_number = 0
		for pokemon in Game.Pokemon_List:
			pokemon.current_health = pokemon.health
			pokemon.fainted = False
		for pokemon in Game.Opponent_Pokemon_List:
			pokemon.current_health = pokemon.health
			pokemon.fainted = False
		Game.current_turn_text[:] = []
		Game.show_party = False
		Game.Pokemon_Fainted = False

	@staticmethod
	def attack(attacker, defender, move, y):
		type_advantage = Game.type_advantage(defender, move)
		power = Game.damage_calc(attacker, defender, move, type_advantage)
		x = y
		if defender.current_health - power > 0:
			defender.current_health -= power
			damage = power
		elif defender.current_health - power <= 0:
			damage = defender.current_health
			defender.current_health = 0
		if type_advantage == 2 or type_advantage == 4:
			type_advantage_text = ["It's super effective!", 425, y+35]
			x+=35
		elif type_advantage == 0.5 or type_advantage == 0.25:
			type_advantage_text = ["It's not very effective...", 425, y+35]
			x+=35
		elif type_advantage == 0:
			type_advantage_text = ["It didn't do anything...", 425, y+35]
			x+=35
		else:
			type_advantage_text = ""
		if attacker.name == Game.current_pokemon.name:
			last_text = "%s lost %s HP!" % (defender.name, Game.get_percent(damage, defender.health))
			color = BLUE
		elif attacker.name == Game.opponent.pokemon.name:
			last_text = "%s lost %s HP!" % (defender.name, int(round(damage)))
			color = DARK_RED
		text = [
		["%s used %s!" % (attacker.name, move.name), 425, y],
		["%s" % last_text, 425, x+35]
		]
		if type_advantage != 1:
			text.append(type_advantage_text)
		for item in text:
			Game.current_turn_text.append((item[0], item[1], item[2], 25, color))
		return defender.current_health

	@staticmethod
	def do_moves(move):
		Game.pause = True
		opponent_move = Game.opponent_move()
		y=25
		if not isinstance(move, int) and not isinstance(opponent_move, int):
			if Game.current_pokemon.speed > Game.opponent.pokemon.speed:
				Game.attack(Game.current_pokemon, Game.opponent.pokemon, move, 25)
				if Game.opponent.pokemon.current_health > 0:
					Game.attack(Game.opponent.pokemon, Game.current_pokemon, opponent_move, 135)

			elif Game.opponent.pokemon.speed >= Game.current_pokemon.speed:
				Game.attack(Game.opponent.pokemon, Game.current_pokemon, opponent_move, 25)
				if Game.current_pokemon.current_health > 0:
					Game.attack(Game.current_pokemon, Game.opponent.pokemon, move, 135)
		else:
			if isinstance(move, int):
				y = 135
				defender = Game.switch_pokemon(Game.current_pokemon, move, opponent_move, 25)
				if not isinstance(opponent_move, int):
					Game.attack(Game.opponent.pokemon, defender, opponent_move, 135)
				else:
					Game.switch_pokemon(Game.opponent.pokemon, opponent_move, move, y)
			elif not isinstance(move, int):
				defender = Game.switch_pokemon(Game.opponent.pokemon, opponent_move, move, y)
				Game.attack(Game.current_pokemon, defender, move, 135)

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
		damage = (0.11 * (attack / defense) * power) * (type_advantage * STAB)
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
			for immune in defender.type.immune_list:
				if move.type.name == immune:
					type_advantage = 0
					break

		return type_advantage

	@staticmethod
	def update_points(pokemon):
		pokemon.points = 124 + 20
		pokemon.points -= pokemon.health
		pokemon.points -= pokemon.attack
		pokemon.points -= pokemon.defense
		pokemon.points -= pokemon.special_attack
		pokemon.points -= pokemon.special_defense
		pokemon.points -= pokemon.speed

	@staticmethod
	def get_percent(numerator, denominator):
		number = int(round((numerator/denominator)*100))
		percent = ("%s%%" % number)
		return percent

	@staticmethod
	def switch_pokemon(pokemon, pokemon_number, move, y):
		if pokemon == Game.current_pokemon:
			old = Game.current_pokemon
			new = Game.Pokemon_Party[pokemon_number]
			new_number = Game.Pokemon_List.index(new)
			Game.current_pokemon_number = new_number
			Game.show_party = False
			poke = Game.opponent.pokemon
			color = GREEN
		else:
			old = Game.opponent.pokemon
			new = Game.Opponent_Party[pokemon_number]
			new_number = Game.Opponent_Pokemon_List.index(new)
			Game.current_opponent_number = new_number
			poke = Game.current_pokemon
			color = YELLOW
		text = [
		["%s come back!" % old.name, 425, y],
		["Go %s!" % new.name, 425, y+35]
		]
		for item in text:
			Game.current_turn_text.append((item[0], item[1], item[2], 25, color))
		return new

	@staticmethod
	def send_in_pokemon(pokemon_number):
		if Game.Pokemon_Party[pokemon_number].current_health > 0:
			Game.pause = True
			old = Game.current_pokemon
			new = Game.Pokemon_Party[pokemon_number]
			new_number = Game.Pokemon_List.index(new)
			Game.current_pokemon_number = new_number
			text = ("Go %s" % new.name, 200, 285, 25, GREEN)
			Game.current_turn_text.append(text)
			Game.Pokemon_Fainted = False
			Game.show_party = False

	@staticmethod
	def game_over(screen, winner):
		Game.pause = True
		Game.show_party = False
		if winner == Game.current_pokemon:
			win_text = "You win!"
			Functions.text_to_screen(screen, win_text, 200, 310)
		elif winner == Game.opponent.pokemon:
			lose_text = "You are out of Pokemon!"
			Functions.text_to_screen(screen, lose_text, 200, 310)

	@staticmethod
	def send_in_opponent(pokemon_number):
		if isinstance(pokemon_number, int):
			if Game.Opponent_Party[pokemon_number].current_health > 0:
				old = Game.opponent.pokemon
				new = Game.Opponent_Party[pokemon_number]
				new_number = Game.Opponent_Pokemon_List.index(new)
				Game.current_opponent_number = new_number
				dead_text = ("%s died!" % Game.opponent.pokemon.name, 200, 250, 25, BLUE)
				Game.current_turn_text.append(dead_text)
				text = ("Go %s" % new.name, 200, 285, 25, YELLOW)
				Game.current_turn_text.append(text)
				Game.Pokemon_Fainted = False
				Game.show_party = False

	@staticmethod
	def best_switch():
		switch = 0
		pokemon = Game.current_pokemon
	 	opponent = Game.opponent.pokemon
		TA1 = Game.type_advantage(Game.Opponent_Party[0], pokemon)
		TA2 = Game.type_advantage(Game.Opponent_Party[1], pokemon)
		TA3 = Game.type_advantage(Game.Opponent_Party[2], pokemon)
		TA4 = Game.type_advantage(Game.Opponent_Party[3], pokemon)
		choice1 = Game.Opponent_Party[0]
		choice2 = Game.Opponent_Party[1]
		choice3 = Game.Opponent_Party[2]
		choice4 = Game.Opponent_Party[3]
		potential_switches = []
		best_switches = [TA1, TA2, TA3, TA4]
		for switch in Game.Opponent_Party:
			if not isinstance(switch, int):
				if switch.current_health > 0:
					potential_switches.append(switch)
		super_effective_list = set(pokemon.type.super_effective_list)
		not_effective_list = set(pokemon.type.not_effective_list)
		no_effect_list = set(pokemon.type.no_effect_list)
		#switches = set(potential_switches)

		#TA1 = Game.type_advantage(Game.Opponent_Party[0], pokemon)
		"""if len(potential_switches):
			for switch in potential_switches:
				for weakness in switch.type.weakness_list:
					if switch.type2 != None:
						for weakness2 in switch.type2.weakness_list:
							if pokemon.type.name == weakness or pokemon.type.name == weakness2:
								potential_switches.remove(switch)
							if pokemon.type2 != None:
								if pokemon.type2.name == weakness or pokemon.type2.name == weakness2:
									potential_switches.remove(switch)
					else:
						if pokemon.type.name == weakness:
							potential_switches.remove(switch)
						if pokemon.type2 != None:
							if pokemon.type2.name == weakness:
								potential_switches.remove(switch)
				TA = Game.type_advantage(switch, pokemon) * Game.type_advantage(pokemon, switch)
				if TA > 1:
					pass
					#potential_switches.remove(switch)"""
		switches = set(potential_switches)
		while len(best_switches) > 1:

			if best_switches[0] < best_switches[1]:
				best_switches.remove(best_switches[1])
			elif best_switches[0] > best_switches[1]:
				best_switches.remove(best_switches[0])
			else:
				best_switches.remove(best_switches[1])
			#if TA > 1:
				#best_switches.remove(best_switches[0])
		print "potential_switches:", potential_switches
		print "best_switches:", best_switches
		if best_switches[0] == TA1:
			choice = choice1
		elif best_switches[0] == TA2:
			choice = choice2
		elif best_switches[0] == TA3:
			choice = choice3
		elif best_switches[0] == TA4:
			choice = choice4
		return Game.Opponent_Party.index(choice)

	@staticmethod
	def opponent_move():
		opponent = Game.opponent.pokemon
		pokemon = Game.current_pokemon
		TA1 = Game.type_advantage(Game.current_pokemon, Game.opponent.pokemon.move1)
		TA2 = Game.type_advantage(Game.current_pokemon, Game.opponent.pokemon.move2)
		TA3 = Game.type_advantage(Game.current_pokemon, Game.opponent.pokemon.move3)
		TA4 = Game.type_advantage(Game.current_pokemon, Game.opponent.pokemon.move4)
		move1 = Game.damage_calc(opponent, Game.current_pokemon, opponent.move1, TA1)
		move2 = Game.damage_calc(opponent, Game.current_pokemon, opponent.move2, TA2)
		move3 = Game.damage_calc(opponent, Game.current_pokemon, opponent.move3, TA3)
		move4 = Game.damage_calc(opponent, Game.current_pokemon, opponent.move4, TA4)
		type_advantages = [TA1, TA2, TA3, TA4]
		best_moves = [move1, move2, move3, move4]
		while len(best_moves) > 1:
			if best_moves[0] > best_moves[1]:
				best_moves.remove(best_moves[1])
			elif best_moves[0] < best_moves[1]:
				best_moves.remove(best_moves[0])
			else:
				if best_moves[-1] > best_moves[-2]:
					best_moves.remove(best_moves[-2])
				elif best_moves[-1] < best_moves[-2]:
					best_moves.remove(best_moves[1])
				else:
					if best_moves[0] > best_moves[-1]:
						best_moves.remove(best_moves[-1])
					elif best_moves[0] < best_moves[-1]:
						best_moves.remove(best_moves[0])
					else:
						best_moves.remove(best_moves[-1])
		# While loop to get the best move choice
		checking = True
		while checking:
			for number in type_advantages:
				if len(type_advantages) > 0:
					if number >= 1:
						checking = False
					elif number < 1:
						type_advantages.remove(number)
				else:
					checking = False
			checking = False
		switch = False

		if Game.best_switch() != None:
			for weakness in opponent.type.weakness_list:
				if pokemon.type.name == weakness:
					#if pokemon.speed > opponent.speed:
					switch = True
				if pokemon.type2 != None:
					if pokemon.type2.name == weakness:
						switch = True
		minimum = Game.current_pokemon.health / 4
		if best_moves[0] >= minimum and not switch:
			if best_moves[0] == move1:
				opponent_move = Game.opponent.pokemon.move1
			elif best_moves[0] == move2:
				opponent_move = Game.opponent.pokemon.move2
			elif best_moves[0] == move3:
				opponent_move = Game.opponent.pokemon.move3
			elif best_moves[0] == move4:
				opponent_move = Game.opponent.pokemon.move4
		else:
			opponent_move = Game.best_switch()
		print type_advantages
		return opponent_move
