import pygame


class Item():
	all_items = []
	def __init__(self, name, effect):
		self.name = name
		self.effect = effect
		Item.all_items.append(self)

# After turn
Leftovers = Item("Leftovers", "after_turn")

# Choice Items
Choice_band = Item("Choice Band", "choice")
Choice_specs = Item("Choice Specs", "choice")
Choice_band = Item("Choice Scarf", "choice")

# Berries
Lum_berry = Item("Lum Berry", "berry")