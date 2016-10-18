from __future__ import division
import pygame, math

def best_move(pokemon, opponent, opponent_party):
	strongest_move = opponent_move(pokemon, opponent)
	pokemon_strongest_move = opponent_move(opponent, pokemon)
	safest_switch_number = best_switch(pokemon, opponent_party)
	safest_switch = opponent_party[safest_switch_number]
	safest_switch_best_move = opponent_move(pokemon, safest_switch)
	type_advantage = move_type_advantage(pokemon, safest_switch_best_move)
	safest_switch_damage = damage_calc(safest_switch, pokemon, safest_switch_best_move, type_advantage)

	# If player's pokemon is faster and will kill the opponent
	# but the opponent has a pokemon that can take two hits and
	# kill the player's pokemon. 
	move = False
	if pokemon.base_speed > opponent.base_speed:

		type_advantage = move_type_advantage(opponent, pokemon_strongest_move)
		damage = damage_calc(pokemon, opponent, pokemon_strongest_move, type_advantage)
		
		if opponent.current_health - damage <= 0:
	
			type_advantage = move_type_advantage(safest_switch, pokemon_strongest_move)
			damage = damage_calc(pokemon, safest_switch, pokemon_strongest_move, type_advantage)
			
			pokemon_strongest_move = opponent_move(safest_switch, pokemon)
			type_advantage = move_type_advantage(safest_switch, pokemon_strongest_move)
			pokemon_damage = damage_calc(pokemon, safest_switch, pokemon_strongest_move, type_advantage)
	
			test_pokemon_health = pokemon.current_health
			test_safest_switch_health = safest_switch.current_health - damage
			if pokemon.base_speed > safest_switch.base_speed:
				
				while test_pokemon_health > 0 and test_safest_switch_health > 0:
					test_safest_switch_health -= pokemon_damage
					if test_safest_switch_health > 0:
						test_pokemon_health -= safest_switch_damage
			
			if pokemon.base_speed <= safest_switch.base_speed:

				while test_pokemon_health > 0 and test_safest_switch_health > 0:
					test_pokemon_health -= safest_switch_damage
					if test_pokemon_health > 0:
						test_safest_switch_health -= pokemon_damage
			
			if test_pokemon_health <= 0:
				return safest_switch_number
			# In case a pokemon is faster and can take a hit and kill.
			# I had Tangela vs the opponent's Slowpoke and the opponent
			# had a Munchlax and a Ghastly. Munchlax takes hits better
			# and is the safest_switch. Ghastly is the actual safest
			# switch (and best switch) but was not tested before this code. 
			elif test_pokemon_health > 0:
				safest_switch_number = best_switch(pokemon, opponent_party, True)
				safest_switch = opponent_party[safest_switch_number]
				safest_switch_best_move = opponent_move(pokemon, safest_switch)
				
				type_advantage = move_type_advantage(pokemon, safest_switch_best_move)
				safest_switch_damage = damage_calc(safest_switch, pokemon, safest_switch_best_move, type_advantage)
				type_advantage = move_type_advantage(safest_switch, pokemon_strongest_move)
				damage = damage_calc(pokemon, safest_switch, pokemon_strongest_move, type_advantage)
				
				pokemon_strongest_move = opponent_move(safest_switch, pokemon)
				type_advantage = move_type_advantage(safest_switch, pokemon_strongest_move)
				pokemon_damage = damage_calc(pokemon, safest_switch, pokemon_strongest_move, type_advantage)
		
				test_pokemon_health = pokemon.current_health
				test_safest_switch_health = safest_switch.current_health - damage
				if pokemon.base_speed > safest_switch.base_speed:
				
					while test_pokemon_health > 0 and test_safest_switch_health > 0:
						test_safest_switch_health -= pokemon_damage
						if test_safest_switch_health > 0:
							test_pokemon_health -= safest_switch_damage
				
				if pokemon.base_speed <= safest_switch.base_speed:

					while test_pokemon_health > 0 and test_safest_switch_health > 0:
						test_pokemon_health -= safest_switch_damage
						if test_pokemon_health > 0:
							test_safest_switch_health -= pokemon_damage
			if test_pokemon_health <= 0:
				return safest_switch_number
	return move


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
		damage = math.floor(0.2 * (attack / defense) * power + 2) * (type_advantage * STAB)
		return damage

def move_type_advantage(pokemon, move):
	# Test how effective a move is vs a pokemon
	type_advantage = 1
	for immune in pokemon.type.immune_list:
		if move.type.name == immune:
			type_advantage = 0
			break
	for weakness in pokemon.type.weakness_list:
		if move.type.name == weakness:
			type_advantage = 2
			break
	for resist in pokemon.type.resist_list:
		if move.type.name == resist:
			type_advantage = 0.5
			break
	if pokemon.type2 != None:
		for immune in pokemon.type2.immune_list:
			if move.type.name == immune:
				type_advantage = 0
				break
		for weakness in pokemon.type2.weakness_list:
			if move.type.name == weakness:
				if type_advantage == 0.5:
					type_advantage = 1
				elif type_advantage == 1:
					type_advantage = 2
				elif type_advantage == 2:
					type_advantage = 4
				break
		for resist in pokemon.type2.resist_list:
			if move.type.name == resist:
				if type_advantage == 0.5:
					type_advantage = 0.25
				elif type_advantage == 1:
					type_advantage = 0.5
				elif type_advantage == 2:
					type_advantage = 1
				break

	return type_advantage


def type_vs_type(type1, type2):
	type_advantage = 1
	for resist in type1.resist_list:
		if type2.name == resist:
			type_advantage = 1


def pokemon_type_advantage(pokemon1, pokemon2):
	# Test the type advantage of two pokemon
	type_advantage = 1
	offense_advantage = 1
	defense_advantage = 1
	# The first type of each pokemon
	if pokemon1.type == pokemon2.type:
		for resist in pokemon1.type.resist_list:
			if pokemon2.type.name == resist:
				offense_advantage = 0.5
				defense_advantage = 0.5
				break
		for weakness in pokemon1.type.weakness_list:
			if pokemon2.type.name == weakness:
				pass
	else:
		# Defense
		for resist in pokemon2.type.resist_list:
			if pokemon1.type.name == resist:
				defense_advantage *= 2
				break
		for weakness in pokemon2.type.weakness_list:
			if pokemon1.type.name == weakness:
				defense_advantage /= 2
				break
		for immune in pokemon2.type.immune_list:
			if pokemon1.type.name == immune:
				defense_advantage = 4
				break
		# Offense
		for resist in pokemon1.type.resist_list:
			if pokemon2.type.name == resist:
				offense_advantage /= 2
				break
		for weakness in pokemon1.type.weakness_list:
			if pokemon2.type.name == weakness:
				offense_advantage *= 2
				break
		for immune in pokemon1.type.immune_list:
			if pokemon2.type.name == immune:
				offense_advantage = 0
				break
	# If only one pokemon is a multi-type
	if pokemon1.type2 != None or pokemon2.type2 != None:
		if pokemon1.type2 != None and pokemon2.type2 == None:
			# Offense
			for immune in pokemon1.type2.immune_list:
				if pokemon2.type.name == immune:
					offense_advantage = 0
					break
			for resist in pokemon1.type2.resist_list:
				if pokemon2.type.name == resist:
					if 0 < offense_advantage < 4:	
						offense_advantage /= 2
					break
			for weakness in pokemon1.type2.weakness_list:
				if pokemon2.type.name == weakness:
					if 0 < offense_advantage < 4:	
						offense_advantage *= 2
					break
			# Defense
			for immune in pokemon2.type.immune_list:
				if pokemon1.type2.name == immune:
					defense_advantage = 4
					break
			for resist in pokemon2.type.resist_list:
				if pokemon1.type2.name == resist:
					if 0 < defense_advantage < 4:	
						defense_advantage *= 2
					break
			for weakness in pokemon2.type.weakness_list:
				if pokemon1.type2.name == weakness:
					if 0 < defense_advantage < 4:	
						defense_advantage /= 2
					break
		elif pokemon1.type2 == None and pokemon2.type2 != None:
			# Defense
			for immune in pokemon2.type2.immune_list:
				if pokemon1.type.name == immune:
					defense_advantage = 4
					break
			for resist in pokemon2.type2.resist_list:
				if pokemon1.type.name == resist:
					if 0 < defense_advantage < 4:
						defense_advantage *= 2
					break
			for weakness in pokemon2.type2.weakness_list:
				if pokemon1.type.name == weakness:
					if 0 < defense_advantage < 4:	
						defense_advantage /= 2
					break
			# Offense
			for immune in pokemon1.type.immune_list:
				if pokemon2.type2.name == immune:
					offense_advantage = 0
					break
			for resist in pokemon1.type.resist_list:
				if pokemon2.type2.name == resist:
					offense_advantage /= 2
					break
			for weakness in pokemon1.type.weakness_list:
				if pokemon2.type2.name == weakness:
					offense_advantage *= 2
					break
		# if both pokemon are multi-types
		elif pokemon1.type2 != None and pokemon2.type2 != None:
			# Defense
			for immune in pokemon2.type2.immune_list:
				if pokemon1.type.name == immune or pokemon1.type2.name == immune:
					defense_advantage = 4
					break
			for resist in pokemon2.type2.resist_list:
				if pokemon1.type.name == resist or pokemon1.type2.name == resist:
					if 0 < defense_advantage < 4:	
						defense_advantage *= 2
					break
			for weakness in pokemon2.type2.weakness_list:
				if pokemon1.type.name == weakness or pokemon1.type2.name == weakness:
					if 0 < defense_advantage < 4:	
						defense_advantage /= 2
					break
			# Offense
			for immune in pokemon1.type2.immune_list:
				if pokemon2.type.name == immune or pokemon2.type2.name == immune:
					offense_advantage = 4
					break
			for resist in pokemon1.type2.resist_list:
				if pokemon2.type.name == resist or pokemon2.type2.name == resist:
					if 0 < offense_advantage < 4:	
						offense_advantage /= 2
					break
			for weakness in pokemon1.type2.weakness_list:
				if pokemon2.type.name == weakness or pokemon2.type2.name == weakness:
					if 0 < offense_advantage < 4:	
						offense_advantage *= 2
					break
	#if 0 < defense_advantage < 4 and 0 < offense_advantage < 4:
	type_advantage = defense_advantage + offense_advantage
	type_advantage /= 2
	if offense_advantage == 0:
		type_advantage = 0
	if defense_advantage == 4:
		type_advantage = 4
	return type_advantage

def best_switch(pokemon, opponent_party, dead=False):
	choice1 = opponent_party[0]
	choice2 = opponent_party[1]
	choice3 = opponent_party[2]
	choice4 = opponent_party[3]
	TA1 = pokemon_type_advantage(choice1, pokemon)
	TA2 = pokemon_type_advantage(choice2, pokemon)
	TA3 = pokemon_type_advantage(choice3, pokemon)
	TA4 = pokemon_type_advantage(choice4, pokemon)
	damages = []
	faster_switches = []
	damage1, damage2, damage3, damage4 = 999, 999, 999, 999
	if choice1.current_health > 0:
		move1 = opponent_move(choice1, pokemon)
		TA1 = move_type_advantage(choice1, move1)
		damage = damage_calc(pokemon, choice1, move1, TA1)
		damage1 = damage / choice1.max_health
		damages.append(damage1)
		if choice1.base_speed >= pokemon.base_speed:
			move = opponent_move(pokemon, choice1)
			type_advantage = move_type_advantage(pokemon, move)
			damage = damage_calc(choice1, pokemon, move, type_advantage)
			if pokemon.current_health - damage <= 0:
				faster_switches.append(choice1)
	if choice2.current_health > 0:
		move2 = opponent_move(choice2, pokemon)
		TA2 = move_type_advantage(choice2, move2)
		damage = damage_calc(pokemon, choice2, move2, TA2)
		damage2 = damage / choice2.max_health
		damages.append(damage2)
		if choice2.base_speed >= pokemon.base_speed:
			move = opponent_move(pokemon, choice2)
			type_advantage = move_type_advantage(pokemon, move)
			damage = damage_calc(choice2, pokemon, move, type_advantage)
			if pokemon.current_health - damage <= 0:
				faster_switches.append(choice2)
	if choice3.current_health > 0:
		move3 = opponent_move(choice3, pokemon)
		TA3 = move_type_advantage(choice3, move3)
		damage = damage_calc(pokemon, choice3, move3, TA3)
		damage3 = damage / choice3.max_health
		damages.append(damage3)
		if choice3.base_speed >= pokemon.base_speed:
			move = opponent_move(pokemon, choice3)
			type_advantage = move_type_advantage(pokemon, move)
			damage = damage_calc(choice3, pokemon, move, type_advantage)
			if pokemon.current_health - damage <= 0:
				faster_switches.append(choice3)
	if choice4.current_health > 0:	
		move4 = opponent_move(choice4, pokemon)
		TA4 = move_type_advantage(choice4, move4)
		damage = damage_calc(pokemon, choice4, move4, TA4)
		damage4 = damage / choice4.max_health
		damages.append(damage4)
		if choice4.base_speed >= pokemon.base_speed:
			move = opponent_move(pokemon, choice4)
			type_advantage = move_type_advantage(pokemon, move)
			damage = damage_calc(choice4, pokemon, move, type_advantage)
			if pokemon.current_health - damage <= 0:
				faster_switches.append(choice4)
	damages = [damage1, damage2, damage3, damage4]
	while len(damages) > 1:
		if damages[0] < damages[1]:
			damages.remove(damages[1])
		else:
			damages.remove(damages[0])
	if damages[0] == damage1:
		best_switch = choice1
	elif damages[0] == damage2:
		best_switch = choice2	
	elif damages[0] == damage3:
		best_switch = choice3
	elif damages[0] == damage4:
		best_switch = choice4
	best_switch_number = opponent_party.index(best_switch)
	if len(faster_switches) >= 1 and dead:
		best_switch_number = opponent_party.index(faster_switches[0])
	return best_switch_number

def opponent_move(pokemon, opponent):
	TA1 = move_type_advantage(pokemon, opponent.move1)
	TA2 = move_type_advantage(pokemon, opponent.move2)
	TA3 = move_type_advantage(pokemon, opponent.move3)
	TA4 = move_type_advantage(pokemon, opponent.move4)	
	move1 = damage_calc(opponent, pokemon, opponent.move1, TA1)
	move2 = damage_calc(opponent, pokemon, opponent.move2, TA2)
	move3 = damage_calc(opponent, pokemon, opponent.move3, TA3)
	move4 = damage_calc(opponent, pokemon, opponent.move4, TA4)
	moves = [move1, move2, move3, move4]
	while len(moves) > 1:
		if moves[0] > moves[1]:
			moves.remove(moves[1])
		elif moves[0] < moves[1]:
			moves.remove(moves[0])
		else:
			moves.remove(moves[1])
	if moves[0] == move1:
		move = opponent.move1
	elif moves[0] == move2:
		move = opponent.move2
	elif moves[0] == move3:
		move = opponent.move3
	elif moves[0] == move4:
		move = opponent.move4
	return move


 



		