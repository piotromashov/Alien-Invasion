import sys

import pygame

from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, ship, bullets):
	"""Respond to keypresses and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	#debugger
	print str(event.key)
	if event.key == pygame.K_RIGHT:
		#Move ship to the right.
		ship.moving_right = True
	if event.key == pygame.K_LEFT:
		#Move ship to the right.
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, screen, ship, bullets)
	elif event.key == pygame.K_q:
		sys.exit()

def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		#Stop moving ship to the right
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		#Stop moving ship to the right
		ship.moving_left = False

def update_screen(ai_settings, screen, ship, aliens, bullets):
	# Redraw the screen during each pass through the loop
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	aliens.draw(screen)

	# Redraw all bullets behind ship and aliens.
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	#make the most recently drawn screen visible
	pygame.display.flip()

def fire_bullet(ai_settings, screen, ship, bullets):
	# Create a new bullet and add it to the bullets group.
	new_bullet = Bullet(ai_settings, screen, ship)
	bullets.add(new_bullet)

def create_fleet(ai_settings, screen, ship, aliens):
	"""Create a full fleet of aliens."""
	# Create an alien and find the number of aliens in a row.
	# Spacing between each alien is equal to one alien width.
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

	# Create the first row of aliens
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number, row_number)

def get_number_rows(ai_settings, ship_height, alien_height):	
	"""Determine the number of rows of aliens that fit on the screen."""
	available_space_y = (ai_settings.screen_size[1] - (3 * alien_height) - ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows

def get_number_aliens_x(ai_settings, alien_width):
	"""Determine the number of aliens that fit in a row."""
	available_space_x = ai_settings.screen_size[0] - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	"""Create an alien and place it in the row."""
	alien = Alien(ai_settings, screen)
	alien.x = alien.rect.width+2*alien.rect.width*alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)