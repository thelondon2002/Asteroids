import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

black = (0, 0, 0)


def main():

	pygame.init()
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	dt = 0

	print("Starting asteroids!")

	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2


	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable
	Shot.containers = (shots, updatable, drawable)

	player = Player(x, y)
	asteroid_field = AsteroidField()

	while True:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return


		for i in updatable:
			i.update(dt)

		screen.fill(black)

		for i in drawable:
			i.draw(screen)


		dt = clock.tick(60) / 1000


		for asteroid in asteroids:
			if player.collisions(asteroid):
				print("Game over!")
				pygame.quit()
				sys.exit()

			for shot in shots:
                        	if asteroid.collisions(shot):
                                	asteroid.split()
                                	shot.kill()

		pygame.display.flip()


if __name__ ==  "__main__":
	main()
