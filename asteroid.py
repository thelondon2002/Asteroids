from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
		self.x = x
		self.y = y
		self.radius = radius

	def draw(self, screeen):
		pygame.draw.circle(screen, "white", (self.x, self.y), self.radius, 2)

	def update(self, dt):
		self.x += (self.velocity * dt)
		self.y += (self.velocity * dt)
