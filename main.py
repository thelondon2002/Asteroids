import pygame
from constants import *
from player import Player

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

	Player.containers = (updatable, drawable)

	player = Player(x, y)

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

		pygame.display.flip()


if __name__ ==  "__main__":
	main()
