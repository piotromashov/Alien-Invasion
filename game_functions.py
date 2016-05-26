import sys

import pygame

from bullet import Bullet

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

def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		#Stop moving ship to the right
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		#Stop moving ship to the right
		ship.moving_left = False

def update_screen(ai_settings, screen, ship, bullets):
	# Redraw the screen during each pass through the loop
	screen.fill(ai_settings.bg_color)
	ship.blitme()

	# Redraw all bullets behind ship and aliens.
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	#make the most recently drawn screen visible
	pygame.display.flip()

def fire_bullet(ai_settings, screen, ship, bullets):
	# Create a new bullet and add it to the bullets group.
	new_bullet = Bullet(ai_settings, screen, ship)
	bullets.add(new_bullet)