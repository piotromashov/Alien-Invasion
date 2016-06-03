import pygame
from pygame.sprite import Sprite

class Beam(Sprite):
	"""A class to manage beams fired from the ship"""

	def __init__(self, ai_settings, screen, ship):
		"""Create a beam object at the ship's current position."""
		super(Beam, self).__init__()
		self.screen = screen

		# Create a beam rect at (0, 0) and then set correct position.
		self.rect = pygame.Rect(0, 0, ai_settings.beam_width, ai_settings.beam_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		# Store the beam's position as a decimal value.
		self.y = float(self.rect.y)

		self.color = ai_settings.beam_color
		self.speed_factor = ai_settings.beam_speed_factor

		self.laser_beam = pygame.mixer.Sound('sounds/beam.wav')
		self.laser_beam.play()

	def update(self):
		"""Move the beam up the screen."""

		# Update the decimal position of the beam.
		self.y -= self.speed_factor

		# Update the rect position.
		self.rect.y = self.y

	def draw(self):
		"""Draw the beam to the screen."""
		pygame.draw.rect(self.screen, self.color, self.rect)