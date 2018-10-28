import pygame 


from snake import * 
from apple import NewApple

FIELD_SIZE = (20,20)
START_POS = (2,2)
WIDTH = 300
HEIGHT = 300


def drawApple(disp, apple):
	pygame.draw.rect(
		disp, 
		(255,0,0),
		[
			apple[0]*(WIDTH/(FIELD_SIZE[1]+1)),
			apple[1]*(HEIGHT/(FIELD_SIZE[1]+1)),
			(WIDTH/(FIELD_SIZE[1]+1)),
			(HEIGHT/(FIELD_SIZE[1]+1))
		]
	)

def drawSnake(disp, snake):
	for pos in snake:
		pygame.draw.rect(
			disp, 
			(255,255,255),
			[
				pos[0]*(WIDTH/(FIELD_SIZE[1]+1)),
				pos[1]*(HEIGHT/(FIELD_SIZE[1]+1)),
				(WIDTH/(FIELD_SIZE[1]+1)),
				(HEIGHT/(FIELD_SIZE[1]+1))
			]
		)
	pygame.draw.rect(
		disp, 
		(0,0,255),
		[
			snake[-1][0]*(WIDTH/(FIELD_SIZE[1]+1)),
			snake[-1][1]*(HEIGHT/(FIELD_SIZE[1]+1)),
			(WIDTH/(FIELD_SIZE[1]+1)),
			(HEIGHT/(FIELD_SIZE[1]+1))
		]
	)

def MoveDir(snake, field_size, direction):
	import pygame
	cur_pos = snake[-1]

	if direction == pygame.K_DOWN \
	and cur_pos[1]+1 <= field_size[1]\
	and (cur_pos[0], cur_pos[1]+1) not in snake:
		return Move(snake, (cur_pos[0], cur_pos[1]+1))
	
	elif direction == pygame.K_UP \
	and cur_pos[1]-1 >= 0 \
	and (cur_pos[0], cur_pos[1]-1) not in snake:
		return Move(snake, (cur_pos[0], cur_pos[1]-1))
	
	elif direction == pygame.K_RIGHT \
	and cur_pos[0]+1 <= field_size[0] \
	and (cur_pos[0]+1, cur_pos[1]) not in snake:
		return Move(snake, (cur_pos[0]+1, cur_pos[1]))
	
	elif direction == pygame.K_LEFT \
	and cur_pos[0]-1 >= 0 \
	and (cur_pos[0]-1, cur_pos[1]) not in snake:
		return Move(snake, (cur_pos[0]-1, cur_pos[1]))
	
	else:
		return snake

def main(disp, snake, apple):
	clock = pygame.time.Clock()
	
	ai = False
	cur_plan = []
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return 0

			if event.type == pygame.KEYDOWN:
				snake = MoveDir(snake, FIELD_SIZE, event.key)
				
				if event.key == pygame.K_a:	
					ai = not ai
					if not ai:
						cur_plan = []

		if ai:
			if not cur_plan:
				print("Calulating path!")
				cur_plan = PathsToApple(FIELD_SIZE, snake, apple)
			if not cur_plan:
				print("No valid")
			else:
				snake = Move(snake, cur_plan[0])
				del cur_plan[0]

		if snake[-1] == apple:
			snake = EatApple(snake, apple)
			apple = NewApple(FIELD_SIZE, snake)
			if not apple:
				print("Game Over, Won!")
				return 0

		valid_moves = validMoves(FIELD_SIZE, snake, snake[-1])
		if not valid_moves:
			print("Game Over, Lost!")
			return 0



		disp.fill((0,0,0))
		drawApple(disp, apple)
		drawSnake(disp, snake)

		pygame.display.update()
		clock.tick(10)

if __name__ == "__main__":
	snake = NewSnake(pos=START_POS)
	apple = NewApple(FIELD_SIZE, snake)

	disp = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Snake")

	main(disp, snake, apple)
	input("Press any key to exit")

