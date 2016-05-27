class Settings():
	"""A class to store all settings for alien invasion."""

	def __init__(self):
		"""Initialize the game's settings."""
		#screen settings
		self.screen_size = (1280, 800)
		self.bg_color = (230, 230, 230)

		#ship settings
		self.ship_speed_factor = 1.5

		#Alien settings
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		self.fleet_direction = 1

		# Bullet settings
		self.bullet_speed_factor = 2
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 250, 0, 0