class Settings():
	"""A class to store all settings for alien invasion."""

	def __init__(self):
		"""Initialize the game's settings."""
		#screen settings
		self.screen_size = (1280, 800)
		self.bg_color = (230, 230, 230)

		#ship settings
		self.ship_speed_factor = 1.5
		self.ship_charge_factor = 1
		self.ship_charge_time = 250
		self.ship_limit = 3

		#Alien settings
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		self.fleet_direction = 1

		# Bullet settings
		self.bullet_speed_factor = 2
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 250, 0, 0

		# Beam settings
		self.beam_speed_factor = 20
		self.beam_width = 3
		self.beam_height = 200
		self.beam_color = 250, 0, 0