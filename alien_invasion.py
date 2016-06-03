import pygame, pygame.mixer
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
import game_functions as gf

def run_game():
	#initialize game and create a screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(ai_settings.screen_size)
	pygame.display.set_caption("Alien Invasion")

	#start game sound
	# pygame.mixer.music.load('sounds/sandstorm.mp3')
	# pygame.mixer.music.play()

	# Make the Play button.
	play_button = Button(ai_settings, screen, "Play")

	# Create an instance to store game statistics.
	stats = GameStats(ai_settings)

	# Make a ship, a group of bullets, a group of beams, and a group of aliens.
	ship = Ship(ai_settings, screen)
	bullets = Group()
	beams = Group()
	aliens = Group()

	# Create the fleet of aliens.
	gf.create_fleet(ai_settings, screen, ship, aliens)

	#start the main loop for the game
	while True:
		gf.check_events(ai_settings, stats, screen, ship, bullets, beams, play_button)
		gf.update_screen(ai_settings, stats, screen, ship, aliens, bullets, beams, play_button)

		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
			gf.update_beams(ai_settings, screen, ship, aliens, beams)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens)

run_game()