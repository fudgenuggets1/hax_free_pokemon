import pygame, sys
from yo_buttons import Button
from game import Game

def interaction(screen):

    mouse_pos = pygame.mouse.get_pos()
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()
    	    sys.exit()

        for button in Game.current_screen.Button_List:
            if button.x+button.w > mouse_x > button.x and button.y+button.h > mouse_y > button.y:
                button.mouse_over()
            else:
                button.mouse_off()
        if Game.previous_screen != None:
            for button in Game.previous_screen.Button_List:
                button.mouse_off()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in Game.current_screen.Button_List:
                if button.mouse_on:
                    button.do_action()

    if pygame.mouse.get_pressed()[0] and Game.current_screen == Game.screens[1]:
        for button in Game.current_screen.Button_List:
            if button.mouse_on:
                button.do_action()
