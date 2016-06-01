import pygame, pygame.mixer

class Ship():

	def __init__(self, ai_settings, screen):
		"""Initialize the ship and set its starting position."""
		self.screen = screen
		self.ai_settings = ai_settings
		#Load the ship image and gets its rect.
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#Start each new ship at the bottom center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#Store a decimal value for the ship's center.
		self.center = float(self.rect.centerx)

		#Movement flag
		self.moving_right = False
		self.moving_left = False

		#Sounds loads
		self.laser_shot = pygame.mixer.Sound('sounds/shot.wav')
		self.laser_charge = pygame.mixer.Sound('sounds/charge.wav')
		self.laser_beam = pygame.mixer.Sound('sounds/beam.wav')

	def update(self):
		"""Update thes ship's position based on the movement flag."""
		if self.moving_right:
			self.center += self.ai_settings.ship_speed_factor
			if self.center >= self.screen_rect.right:
				self.center = self.screen_rect.right

		if self.moving_left:
			self.center -= self.ai_settings.ship_speed_factor
			if self.center <= self.screen_rect.left:
				self.center = self.screen_rect.left

		#Update rect object from self.center
		self.rect.centerx = self.center

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)

	def fire(self):
		self.laser_shot.play()

	def charge(self):
		self.laser_charge.play()

	def beam(self):
		self.laser_beam.play()