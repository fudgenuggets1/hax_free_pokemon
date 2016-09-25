import pygame, Functions
pygame.font.init()

class Button():

    List = []

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
    def pause(self, time=2):
        for i in range(time):
            self.mouse_off
            self.mouse_on = False
    def do_action(self):
        from game import Game
        if self.action != None:
            if self.action in range(0, 4):
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
            elif self.action == "ok" and Game.pause:
                Game.pause = False

            if not Game.pause and Game.show_party and not Game.Pokemon_Fainted:
                if self.action == "move1":
                    pokemon_number = 0
                elif self.action == "move2":
                    pokemon_number = 1
                elif self.action == "move3":
                    pokemon_number = 2
                elif self.action == "move4":
                    pokemon_number = 3
                if Game.Pokemon_Party[pokemon_number].current_health > 0:    
                    Game.do_moves(pokemon_number)
            if Game.Pokemon_Fainted and Game.show_party:
                if self.action == "move1":
                    Game.send_in_pokemon(0)
                elif self.action == "move2":
                    Game.send_in_pokemon(1)
                elif self.action == "move3":
                    Game.send_in_pokemon(2)
                elif self.action == "move4":
                    Game.send_in_pokemon(3)

            #badly coded to increase and decrease points
            if Game.current_pokemon.points < 124:
                if self.action == "-health":
                    if Game.current_pokemon.health > 20:
                        Game.current_pokemon.health -= 1
                elif self.action == "-attack":
                    if Game.current_pokemon.attack > 1:
                        Game.current_pokemon.attack -= 1
                elif self.action == "-defense":
                    if 1 < Game.current_pokemon.defense:
                        Game.current_pokemon.defense -= 1
                elif self.action == "-special_attack":
                    if 1 < Game.current_pokemon.special_attack:
                        Game.current_pokemon.special_attack -= 1
                elif self.action == "-special_defense":
                    if 1 < Game.current_pokemon.special_defense:
                        Game.current_pokemon.special_defense -= 1
                elif self.action == "-speed":
                    if 1 < Game.current_pokemon.speed:
                        Game.current_pokemon.speed -= 1
            max_stat = 60
            if Game.current_pokemon.points > 0:
                if self.action == "+health":
                    if Game.current_pokemon.health < max_stat+20:
                        Game.current_pokemon.health += 1
                elif self.action == "+attack":
                    if Game.current_pokemon.attack < max_stat:
                        Game.current_pokemon.attack += 1
                elif self.action == "+defense":
                    if Game.current_pokemon.defense < max_stat:
                        Game.current_pokemon.defense += 1
                elif self.action == "+special_attack":
                    if Game.current_pokemon.special_attack < max_stat:
                        Game.current_pokemon.special_attack += 1
                elif self.action == "+special_defense":
                    if Game.current_pokemon.special_defense < max_stat:
                        Game.current_pokemon.special_defense += 1
                elif self.action == "+speed":
                    if Game.current_pokemon.speed < max_stat:
                        Game.current_pokemon.speed += 1


            if self.action == "<move1":
                if Game.current_pokemon.move1_number > 0:
                    Game.current_pokemon.move1_number -= 1
                    self.pause()
            elif self.action == ">move1":
                if Game.current_pokemon.move1_number in range(len(Game.current_pokemon.move_list)-1):
                    Game.current_pokemon.move1_number += 1
                    self.pause()
            elif self.action == "<move2":
                if Game.current_pokemon.move2_number > 0:
                    Game.current_pokemon.move2_number -= 1
                    self.pause()
            elif self.action == ">move2":
                if Game.current_pokemon.move2_number in range(len(Game.current_pokemon.move_list)-1):
                    Game.current_pokemon.move2_number += 1
                    self.pause()
            elif self.action == "<move3":
                if Game.current_pokemon.move3_number > 0:
                    Game.current_pokemon.move3_number -= 1
                    self.pause()
            elif self.action == ">move3":
                if Game.current_pokemon.move3_number in range(len(Game.current_pokemon.move_list)-1):
                    Game.current_pokemon.move3_number += 1
                    self.pause()
            elif self.action == "<move4":
                if Game.current_pokemon.move4_number > 0:
                    Game.current_pokemon.move4_number -= 1
                    self.pause()
            elif self.action == ">move4":
                if Game.current_pokemon.move4_number in range(len(Game.current_pokemon.move_list)-1):
                    Game.current_pokemon.move4_number += 1
                    self.pause()

            if self.action == "next":
                if Game.current_pokemon_number in range(len(Game.Pokemon_List)-1):
                    Game.current_pokemon_number += 1
                    self.pause()
            elif self.action == "previous":
                if Game.current_pokemon_number > 0:
                    Game.current_pokemon_number -= 1
                    self.pause()
            elif self.action == "party":
                if Game.show_party:
                    Game.show_party = False
                elif not Game.show_party:
                    Game.show_party = True

        elif self.action == None:
            pass
