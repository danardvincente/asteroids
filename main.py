import pygame
from constants import *
from player import *


def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	clock = pygame.time.Clock()
	dt = 0

	print("Starting Asteroids!")

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()

	Player.containers = (updatable, drawable)  # Player.containers dynamically create containers as static variable

	the_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	


	while True:

		# This will check if the user has closed the window and exit the game loop if they do. It will make the window's close button work.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		# the_player.update(dt) # moves player left/right etc. based on key input [wasd]
		updatable.update(dt) # using pygame groups to manage game object

		screen.fill("black")

		
		# re-render the player on the screen each frame
		# the_player.draw(screen)
		for f in drawable:
			# using pygame groups to manage game object
			f.draw(screen)

		pygame.display.flip() # refreshes the screen

		amt_time_loop = clock.tick(60) # returns he amount of time that has passed since the last time it was called: the delta time
		dt = amt_time_loop / 1000 # converts milliseconds from amt_time_loop to seconds (delta time in seconds)



if __name__ == "__main__":
	main()
