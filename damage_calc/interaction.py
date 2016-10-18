import pygame, sys
from buttons import Button

def interaction(screen):

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
					break
			else:
				button.mouse_off()