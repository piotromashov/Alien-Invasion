import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	#initialize game and create a screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(ai_settings.screen_size)
	pygame.display.set_caption("Alien Invasion")

	# Make a ship, a group of bullets, and a group of aliens.
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()

	# Create the fleet of aliens.
	gf.create_fleet(ai_settings, screen, ship, aliens)

	#start the main loop for the game
	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		bullets.update()

		# Get rid of bullets that have disappeared.
		for bullet in bullets.copy():
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)

		ship.update()
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()