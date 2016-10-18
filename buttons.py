import pygame, Functions
pygame.font.init()

class Button():

    List = []

    def __init__(self, msg, x, y, w, h, color, highlight, action, action_effect=None, msg_size=25):

        self.msg = msg
        self.msg_size = msg_size
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.regular_color, self.highlight_color = color, highlight
        self.action = action
        self.color = self.regular_color
        self.action_effect = action_effect
        Button.List.append(self)

    @staticmethod
    def update(screen, list):

        for button in list:
            pygame.draw.rect(screen, button.color, (button.x, button.y, button.w, button.h))
            x = button.w / 2
            y = button.h / 2
            Functions.text_to_screen(screen, button.msg, button.x+x, button.y+y, button.msg_size)

    def mouse_over(self):
        self.color = self.highlight_color
    def mouse_off(self):
        self.color = self.regular_color
    def do_action(self):
        #from damage_calc import buttons
        from damage_calc import pokemon1
        from damage_calc import pokemon2
        from damage_calc import Calc
        max_points = 7
        
        if self.action_effect == "health":
            if self.action == "down" and pokemon1.health_points > 0:
                pokemon1.health_points -= 1
            elif self.action == "up" and pokemon1.health_points < max_points and pokemon1.points > 0:
                pokemon1.health_points += 1
            elif self.action in range(0, 10):
                if pokemon1.base_health == 0:
                    pokemon1.base_health = self.action
                elif pokemon1.base_health > 0 and len(str(pokemon1.base_health)) < 2: 
                    pokemon1.base_health *= 10
                    pokemon1.base_health += self.action
            elif self.action == "clear":
                pokemon1.base_health = 0
        
        elif self.action_effect == "attack":
            if self.action == "down" and pokemon1.attack_points > 0:
                pokemon1.attack_points -= 1
            elif self.action == "up" and pokemon1.attack_points < max_points and pokemon1.points > 0:
                pokemon1.attack_points += 1
            elif self.action in range(0, 10):
                if pokemon1.base_attack == 0:
                    pokemon1.base_attack = self.action
                elif pokemon1.base_attack > 0 and len(str(pokemon1.base_attack)) < 2:
                    pokemon1.base_attack *= 10
                    pokemon1.base_attack += self.action
            elif self.action == "clear":
                pokemon1.base_attack = 0
        
        elif self.action_effect == "defense":
            if self.action == "down" and pokemon1.defense_points > 0:
                pokemon1.defense_points -= 1
            elif self.action == "up" and pokemon1.defense_points < max_points and pokemon1.points > 0:
                pokemon1.defense_points += 1
            elif self.action in range(0, 10):
                if pokemon1.base_defense == 0:
                    pokemon1.base_defense = self.action
                elif pokemon1.base_defense > 0 and len(str(pokemon1.base_defense)) < 2:
                    pokemon1.base_defense *= 10
                    pokemon1.base_defense += self.action
            elif self.action == "clear":
                pokemon1.base_defense = 0
        
        elif self.action_effect == "special_attack":
            if self.action == "down" and pokemon1.special_attack_points > 0:
                pokemon1.special_attack_points -= 1
            elif self.action == "up" and pokemon1.special_attack_points < max_points and pokemon1.points > 0:
                pokemon1.special_attack_points += 1
            elif self.action in range(0, 10):
                if pokemon1.base_special_attack == 0:
                    pokemon1.base_special_attack = self.action
                elif pokemon1.base_special_attack > 0 and len(str(pokemon1.base_special_attack)) < 2:
                    pokemon1.base_special_attack *= 10
                    pokemon1.base_special_attack += self.action
            elif self.action == "clear":
                pokemon1.base_special_attack = 0
        
        elif self.action_effect == "special_defense":
            if self.action == "down" and pokemon1.special_defense_points > 0:
                pokemon1.special_defense_points -= 1
            elif self.action == "up" and pokemon1.special_defense_points < max_points and pokemon1.points > 0:
                pokemon1.special_defense_points += 1
            elif self.action in range(0, 10):
                if pokemon1.base_special_defense == 0:
                    pokemon1.base_special_defense = self.action
                elif pokemon1.base_special_defense > 0 and len(str(pokemon1.base_special_defense)) < 2:
                    pokemon1.base_special_defense *= 10
                    pokemon1.base_special_defense += self.action
            elif self.action == "clear":
                pokemon1.base_special_defense = 0
        
        elif self.action_effect == "speed":
            if self.action == "down" and pokemon1.speed_points > 0:
                pokemon1.speed_points -= 1
            elif self.action == "up" and pokemon1.speed_points < max_points and pokemon1.points > 0:
                pokemon1.speed_points += 1
            elif self.action in range(0, 10):
                if pokemon1.base_speed == 0:
                    pokemon1.base_speed = self.action
                elif pokemon1.base_speed > 0 and len(str(pokemon1.base_speed)) < 2:
                    pokemon1.base_speed *= 10
                    pokemon1.base_speed += self.action
            elif self.action == "clear":
                pokemon1.base_speed = 0

        pokemon2
        if self.action_effect == "health2":
            if self.action == "down" and pokemon2.health_points > 0:
                pokemon2.health_points -= 1
            elif self.action == "up" and pokemon2.health_points < max_points and pokemon2.points > 0:
                pokemon2.health_points += 1
            elif self.action in range(0, 10):
                if pokemon2.base_health == 0:
                    pokemon2.base_health = self.action
                elif pokemon2.base_health > 0 and len(str(pokemon2.base_health)) < 2: 
                    pokemon2.base_health *= 10
                    pokemon2.base_health += self.action
            elif self.action == "clear":
                pokemon2.base_health = 0
        
        elif self.action_effect == "attack2":
            if self.action == "down" and pokemon2.attack_points > 0:
                pokemon2.attack_points -= 1
            elif self.action == "up" and pokemon2.attack_points < max_points and pokemon2.points > 0:
                pokemon2.attack_points += 1
            elif self.action in range(0, 10):
                if pokemon2.base_attack == 0:
                    pokemon2.base_attack = self.action
                elif pokemon2.base_attack > 0 and len(str(pokemon2.base_attack)) < 2:
                    pokemon2.base_attack *= 10
                    pokemon2.base_attack += self.action
            elif self.action == "clear":
                pokemon2.base_attack = 0
        
        elif self.action_effect == "defense2":
            if self.action == "down" and pokemon2.defense_points > 0:
                pokemon2.defense_points -= 1
            elif self.action == "up" and pokemon2.defense_points < max_points and pokemon2.points > 0:
                pokemon2.defense_points += 1
            elif self.action in range(0, 10):
                if pokemon2.base_defense == 0:
                    pokemon2.base_defense = self.action
                elif pokemon2.base_defense > 0 and len(str(pokemon2.base_defense)) < 2:
                    pokemon2.base_defense *= 10
                    pokemon2.base_defense += self.action
            elif self.action == "clear":
                pokemon2.base_defense = 0
        
        elif self.action_effect == "special_attack2":
            if self.action == "down" and pokemon2.special_attack_points > 0:
                pokemon2.special_attack_points -= 1
            elif self.action == "up" and pokemon2.special_attack_points < max_points and pokemon2.points > 0:
                pokemon2.special_attack_points += 1
            elif self.action in range(0, 10):
                if pokemon2.base_special_attack == 0:
                    pokemon2.base_special_attack = self.action
                elif pokemon2.base_special_attack > 0 and len(str(pokemon2.base_special_attack)) < 2:
                    pokemon2.base_special_attack *= 10
                    pokemon2.base_special_attack += self.action
            elif self.action == "clear":
                pokemon2.base_special_attack = 0
        
        elif self.action_effect == "special_defense2":
            if self.action == "down" and pokemon2.special_defense_points > 0:
                pokemon2.special_defense_points -= 1
            elif self.action == "up" and pokemon2.special_defense_points < max_points and pokemon2.points > 0:
                pokemon2.special_defense_points += 1
            elif self.action in range(0, 10):
                if pokemon2.base_special_defense == 0:
                    pokemon2.base_special_defense = self.action
                elif pokemon2.base_special_defense > 0 and len(str(pokemon2.base_special_defense)) < 2:
                    pokemon2.base_special_defense *= 10
                    pokemon2.base_special_defense += self.action
            elif self.action == "clear":
                pokemon2.base_special_defense = 0
        
        elif self.action_effect == "speed2":
            if self.action == "down" and pokemon2.speed_points > 0:
                pokemon2.speed_points -= 1
            elif self.action == "up" and pokemon2.speed_points < max_points and pokemon2.points > 0:
                pokemon2.speed_points += 1
            elif self.action in range(0, 10):
                if pokemon2.base_speed == 0:
                    pokemon2.base_speed = self.action
                elif pokemon2.base_speed > 0 and len(str(pokemon2.base_speed)) < 2:
                    pokemon2.base_speed *= 10
                    pokemon2.base_speed += self.action
            elif self.action == "clear":
                pokemon2.base_speed = 0
        
        elif self.action_effect == "move_power":
            if self.action in range(0, 10):
                if pokemon1.move_power == 0:
                    pokemon1.move_power = self.action
                elif pokemon1.move_power > 0 and len(str(pokemon1.move_power)) < 3:
                    pokemon1.move_power *= 10
                    pokemon1.move_power += self.action
            elif self.action == "clear":
                pokemon1.move_power = 0

        elif self.action_effect == "effectiveness":
            Calc.type_effectiveness = self.action
        elif self.action_effect == "STAB":
            if Calc.STAB == "Yes":
                Calc.STAB = "No"
            elif Calc.STAB == "No":
                Calc.STAB = "Yes"

        elif self.action_effect == "calculate":
            Calc.damage = Calc.damage_calc(pokemon1.attack, pokemon2.defense,
                pokemon1.move_power, Calc.STAB, Calc.type_effectiveness)









