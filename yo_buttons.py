import pygame, Functions, pokemon, random, time
pygame.font.init()

class Button():

    List = []
    time = time.time()

    def __init__(self, msg, x, y, w, h, color, highlight, action):

        self.msg = msg
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.regular_color, self.highlight_color = color, highlight
        self.action = action
        self.color = self.regular_color
        self.mouse_on = False
        Button.List.append(self)

    @staticmethod
    def update(screen, list):

        for button in list:
            pygame.draw.rect(screen, button.color, (button.x, button.y, button.w, button.h))
            x = button.w / 2
            y = button.h / 2
            Functions.text_to_screen(screen, button.msg, button.x+x, button.y+y)

    def mouse_over(self):
        self.color = self.highlight_color
        self.mouse_on = True
    def mouse_off(self):
        self.color = self.regular_color
        self.mouse_on = False
    def do_action(self):
        from game import Game
        if self.action != None:
            if self.action in range(0, 5):
                Game.previous_screen = Game.current_screen
                Game.current_screen_number = self.action
                if self.action == 0:
                    Game.reset()
            if not Game.pause and not Game.show_party:
                if self.action == "move1":
                    Game.do_moves(Game.current_pokemon.move1)
                elif self.action == "move2":
                    Game.do_moves(Game.current_pokemon.move2)
                elif self.action == "move3":
                    Game.do_moves(Game.current_pokemon.move3)
                elif self.action == "move4":
                    Game.do_moves(Game.current_pokemon.move4)
            elif self.action == "ok" and Game.pause and not Game.Pokemon_Fainted:
                Game.pause = False

            if not Game.pause and Game.show_party and not Game.Pokemon_Fainted:
                pokemon_number = None
                if self.action == "move1":
                    if Game.Pokemon_Party[0].current_health > 0:
                        Game.do_moves(0)
                elif self.action == "move2":
                    pokemon_number = 1
                elif self.action == "move3":
                    pokemon_number = 2
                elif self.action == "move4":
                    pokemon_number = 3
                if pokemon_number:
                    if Game.Pokemon_Party[pokemon_number].current_health > 0:
                        Game.do_moves(pokemon_number)
            if Game.Pokemon_Fainted and Game.show_party and not Game.switching:
                if self.action == "move1":
                    Game.send_in_pokemon(0)
                elif self.action == "move2":
                    Game.send_in_pokemon(1)
                elif self.action == "move3":
                    Game.send_in_pokemon(2)
                elif self.action == "move4":
                    Game.send_in_pokemon(3)
            if Game.switching and Game.show_party:
                pokemon_number = False
                if self.action == "move1":
                    Game.switch_move(Game.current_pokemon, pokemon_number)
                elif self.action == "move2":
                    pokemon_number = 1
                elif self.action == "move3":
                    pokemon_number = 2
                elif self.action == "move4":
                    pokemon_number = 3
                if pokemon_number:
                    Game.switch_move(Game.current_pokemon, pokemon_number)
            #badly coded to increase and decrease points
            if Game.current_pokemon.points < 15:
                if self.action == "-health":
                    if Game.current_pokemon.max_health > pokemon.hp_calc(Game.current_pokemon.base_health):
                        Game.current_pokemon.health_points -= 1
                elif self.action == "-attack":
                    if Game.current_pokemon.attack > pokemon.stat_calc(Game.current_pokemon.base_attack):
                        Game.current_pokemon.attack_points -= 1
                elif self.action == "-defense":
                    if Game.current_pokemon.defense > pokemon.stat_calc(Game.current_pokemon.base_defense):
                        Game.current_pokemon.defense_points -= 1
                elif self.action == "-special_attack":
                    if Game.current_pokemon.special_attack > pokemon.stat_calc(Game.current_pokemon.base_special_attack):
                        Game.current_pokemon.special_attack_points -= 1
                elif self.action == "-special_defense":
                    if Game.current_pokemon.special_defense > pokemon.stat_calc(Game.current_pokemon.base_special_defense):
                        Game.current_pokemon.special_defense_points -= 1
                elif self.action == "-speed":
                    if Game.current_pokemon.speed > pokemon.stat_calc(Game.current_pokemon.base_speed):
                        Game.current_pokemon.speed_points -= 1
            if Game.current_pokemon.points > 0:
                if self.action == "+health":
                    if Game.current_pokemon.max_health < pokemon.hp_calc(Game.current_pokemon.base_health, 7):
                        Game.current_pokemon.health_points += 1
                elif self.action == "+attack":
                    if Game.current_pokemon.attack < pokemon.stat_calc(Game.current_pokemon.base_attack, 7):
                        Game.current_pokemon.attack_points += 1
                elif self.action == "+defense":
                    if Game.current_pokemon.defense < pokemon.stat_calc(Game.current_pokemon.base_defense, 7):
                        Game.current_pokemon.defense_points += 1
                elif self.action == "+special_attack":
                    if Game.current_pokemon.special_attack < pokemon.stat_calc(Game.current_pokemon.base_special_attack, 7):
                        Game.current_pokemon.special_attack_points += 1
                elif self.action == "+special_defense":
                    if Game.current_pokemon.special_defense < pokemon.stat_calc(Game.current_pokemon.base_special_defense, 7):
                        Game.current_pokemon.special_defense_points += 1
                elif self.action == "+speed":
                    if Game.current_pokemon.speed < pokemon.stat_calc(Game.current_pokemon.base_speed, 7):
                        Game.current_pokemon.speed_points += 1


            if self.action == "<move1":
                if Game.current_pokemon.move1_number > 0:
                    Game.current_pokemon.move1_number -= 1
            elif self.action == ">move1":
                if Game.current_pokemon.move1_number in range(len(Game.current_pokemon.move_list)-1):
                    Game.current_pokemon.move1_number += 1
            elif self.action == "<move2":
                if Game.current_pokemon.move2_number > 0:
                    Game.current_pokemon.move2_number -= 1
            elif self.action == ">move2":
                if Game.current_pokemon.move2_number in range(len(Game.current_pokemon.move_list)-1):
                    Game.current_pokemon.move2_number += 1
            elif self.action == "<move3":
                if Game.current_pokemon.move3_number > 0:
                    Game.current_pokemon.move3_number -= 1
            elif self.action == ">move3":
                if Game.current_pokemon.move3_number in range(len(Game.current_pokemon.move_list)-1):
                    Game.current_pokemon.move3_number += 1
            elif self.action == "<move4":
                if Game.current_pokemon.move4_number > 0:
                    Game.current_pokemon.move4_number -= 1
            elif self.action == ">move4":
                if Game.current_pokemon.move4_number in range(len(Game.current_pokemon.move_list)-1):
                    Game.current_pokemon.move4_number += 1

            if self.action == "next":
                if Game.current_pokemon_number in range(len(Game.Pokemon_List)-1):
                    Game.current_pokemon_number += 1
            elif self.action == "previous":
                if Game.current_pokemon_number > 0:
                    Game.current_pokemon_number -= 1
            elif self.action == "party":
                if Game.show_party:
                    Game.show_party = False
                elif not Game.show_party:
                    Game.show_party = True

            pokemon_set = set(Game.Pokemon_List)
            if self.action == "down":
                next_pokemon_number = pokemon.Pokemon.All_Pokemon.index(Game.current_pokemon)
                while next_pokemon_number in range(len(pokemon.Pokemon.All_Pokemon)) and pokemon.Pokemon.All_Pokemon[next_pokemon_number] in pokemon_set:
                    next_pokemon_number += 1
                if next_pokemon_number in range(len(pokemon.Pokemon.All_Pokemon)):
                    next_pokemon = pokemon.Pokemon.All_Pokemon[next_pokemon_number]
                    current_pokemon_number = Game.Pokemon_List.index(Game.current_pokemon)
                    Game.Pokemon_List[current_pokemon_number] = next_pokemon
                else:
                    next_pokemon_number = 0
                    while pokemon.Pokemon.All_Pokemon[next_pokemon_number] in pokemon_set:
                        next_pokemon_number += 1
                    next_pokemon = pokemon.Pokemon.All_Pokemon[next_pokemon_number]
                    current_pokemon_number = Game.Pokemon_List.index(Game.current_pokemon)
                    Game.Pokemon_List[current_pokemon_number] = next_pokemon
            elif self.action == "up":
                next_pokemon_number = pokemon.Pokemon.All_Pokemon.index(Game.current_pokemon)
                while next_pokemon_number >= 0 and pokemon.Pokemon.All_Pokemon[next_pokemon_number] in pokemon_set:
                    next_pokemon_number -= 1
                while pokemon.Pokemon.All_Pokemon[next_pokemon_number] in pokemon_set:
                    next_pokemon_number -= 1
                next_pokemon = pokemon.Pokemon.All_Pokemon[next_pokemon_number]
                current_pokemon_number = Game.Pokemon_List.index(Game.current_pokemon)
                Game.Pokemon_List[current_pokemon_number] = next_pokemon
            
            if self.action == "new_opponent":
                Game.opponent = random.choice(pokemon.Opponent.opponents)
                Game.Opponent_Pokemon_List = Game.opponent.list
            elif self.action == "random_opponent":
                pokemon1 = random.choice(pokemon.Opponent.All_Pokemon)
                pokemon2 = random.choice(pokemon.Opponent.All_Pokemon)
                while pokemon2 == pokemon1:
                    pokemon2 = random.choice(pokemon.Opponent.All_Pokemon)
                pokemon3 = random.choice(pokemon.Opponent.All_Pokemon)
                while pokemon3 == pokemon2 or pokemon3 == pokemon1:
                    pokemon3 = random.choice(pokemon.Opponent.All_Pokemon)
                pokemon4 = random.choice(pokemon.Opponent.All_Pokemon)
                while pokemon4 == pokemon3 or pokemon4 == pokemon2 or pokemon4 == pokemon1:
                    pokemon4 = random.choice(pokemon.Opponent.All_Pokemon)
                pokemon5 = random.choice(pokemon.Opponent.All_Pokemon)
                while pokemon5 == pokemon4 or pokemon5 == pokemon3 or pokemon5 == pokemon2 or pokemon5 == pokemon1:
                    pokemon5 = random.choice(pokemon.Opponent.All_Pokemon)
                new_opponent = pokemon.Opponent([pokemon1, pokemon2, pokemon3, pokemon4, pokemon5])
                Game.opponent = new_opponent
                Game.Opponent_Pokemon_List = Game.opponent.list
            elif self.action == "new_team":
                team = random.choice(pokemon.Team.teams)
                Game.Pokemon_List = team.list
            elif self.action == "random_team":
                pokemon1 = random.choice(pokemon.Pokemon.All_Pokemon)
                pokemon2 = random.choice(pokemon.Pokemon.All_Pokemon)
                while pokemon2 == pokemon1:
                    pokemon2 = random.choice(pokemon.Pokemon.All_Pokemon)
                pokemon3 = random.choice(pokemon.Pokemon.All_Pokemon)
                while pokemon3 == pokemon2 or pokemon3 == pokemon1:
                    pokemon3 = random.choice(pokemon.Pokemon.All_Pokemon)
                pokemon4 = random.choice(pokemon.Pokemon.All_Pokemon)
                while pokemon4 == pokemon3 or pokemon4 == pokemon2 or pokemon4 == pokemon1:
                    pokemon4 = random.choice(pokemon.Pokemon.All_Pokemon)
                pokemon5 = random.choice(pokemon.Pokemon.All_Pokemon)
                while pokemon5 == pokemon4 or pokemon5 == pokemon3 or pokemon5 == pokemon2 or pokemon5 == pokemon1:
                    pokemon5 = random.choice(pokemon.Pokemon.All_Pokemon)
                new_team = pokemon.Team([pokemon1, pokemon2, pokemon3, pokemon4, pokemon5])
                Game.Pokemon_List = new_team.list
            if Game.current_screen_number == 4:
                if self.action == "normal":
                    Game.opponent = pokemon.normal_gym
                elif self.action == "fight":
                    Game.opponent = pokemon.fight_gym
                elif self.action == "ice":
                    Game.opponent = pokemon.ice_gym
                elif self.action == "poison":
                    Game.opponent = pokemon.poison_gym
                elif self.action == "ground":
                    Game.opponent = pokemon.ground_gym
                elif self.action == "fire":
                    Game.opponent = pokemon.fire_gym
                elif self.action == "psychic":
                    Game.opponent = pokemon.psychic_gym
                elif self.action == "grass":
                    Game.opponent = pokemon.grass_gym
                elif self.action == "electric":
                    Game.opponent = pokemon.electric_gym
                if isinstance(self.action, str):    
                    Game.Opponent_Pokemon_List = Game.opponent.list
                    Game.current_screen_number = 2
            if self.action == "previous_turn" and Game.turn_index > 0:
                Game.turn_index -= 1

            if self.action == "next_turn" and Game.turn_index < Game.current_turn - 1:
                Game.turn_index += 1

        elif self.action == None:
            pass
        Button.time = time.time()
        self.mouse_off()



