import pygame

def text_to_screen(screen, text, x, y, size = 25,
    color = (255,255,255), font_type = 'Arial'):

    text = str(text)

    font = pygame.font.SysFont(font_type, size)
    size = font.size(text)
    text = font.render(text, True, color)

    screen.blit(text, (x-(size[0]/2), y-(size[1]/2)))

def text_to_list(text_list, color=(255,255,255)):
	from game import Game

	text = text_list[0]

	try:
		Game.current_turn_text.add((text, Game.new_y, text_list[4]))
	except:
		Game.current_turn_text.add((text, Game.new_y, color))
	Game.new_y += 35
	
		
