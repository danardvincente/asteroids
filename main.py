import pygame, sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *



def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	clock = pygame.time.Clock()
	dt = 0

	print("Starting Asteroids!")

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()


	Player.containers = (updatable, drawable)  # Player.containers dynamically create containers as static variable
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)


	the_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	the_asteroids = AsteroidField()


	while True:

		# This will check if the user has closed the window and exit the game loop if they do. It will make the window's close button work.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		# the_player.update(dt) # moves player left/right etc. based on key input [wasd]
		updatable.update(dt) # using pygame groups to manage game object

		# when player collides with an asteroid
		for asterd in asteroids:
			if asterd.collisons(the_player):
				print("Game Over!")
				sys.exit()

		# when bullet collides with asteroid
		for ast in asteroids:
			for shot in shots:
				if shot.collisons(ast):
					ast.split()
					shot.kill()


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
