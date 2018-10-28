
def NewSnake(pos=(0,0)):
	return [pos]

def EatApple(snake, apple):
	cur_pos = snake[-1]
	if cur_pos == apple:
		return snake[0:1] + snake
	else:
		return snake

def Move(snake, new_pos):
	new_snake = list(snake)
	new_snake.append(new_pos)
	del new_snake[0]

	return new_snake

def validMoves(field_size, visted, snake, cur_pos):
	valid_moves = list()
	# right
	if cur_pos[0]+1 <= field_size[0]\
	and (cur_pos[0]+1, cur_pos[1]) not in snake\
	and (cur_pos[0]+1, cur_pos[1]) not in visted:
		valid_moves.append((cur_pos[0]+1, cur_pos[1]))
	# left
	if cur_pos[0]-1 >= 0\
	and (cur_pos[0]-1, cur_pos[1]) not in snake\
	and (cur_pos[0]-1, cur_pos[1]) not in visted:
		valid_moves.append((cur_pos[0]-1, cur_pos[1]))
	# up
	if cur_pos[1]+1 <= field_size[1]\
	and (cur_pos[0], cur_pos[1]+1) not in snake\
	and (cur_pos[0], cur_pos[1]+1) not in visted:
		valid_moves.append((cur_pos[0], cur_pos[1]+1))
	# down
	if cur_pos[1]-1 >= 0\
	and (cur_pos[0], cur_pos[1]-1) not in snake\
	and (cur_pos[0], cur_pos[1]-1) not in visted:
		valid_moves.append((cur_pos[0], cur_pos[1]-1))

	return valid_moves

def DirToString(old_pos, pos):
	move_dir = (pos[0]-old_pos[0], pos[1]-old_pos[1])
	if move_dir[0] == -1:
		return "LEFT"
	if move_dir[0] == 1:
		return "RIGHT"
	if move_dir[1] == -1:
		return "UP"
	if move_dir[1] == 1:
		return "DOWN"

def moveToPos(snake, reverse_map, new_pos):
	new_snake = list(snake)

	path_to_pos = list()
	cur_pos = new_pos
	while True:
		pre_pos = reverse_map[cur_pos]
		if pre_pos == snake[-1]:
			break
		path_to_pos.append(pre_pos)
		cur_pos = pre_pos
	path_to_pos.reverse()
	for pos in path_to_pos:
		new_snake = Move(new_snake, pos)
	return new_snake

from queue import Queue
def PathsToApple(field_size, snake, apple):	
	if snake[-1] == apple:
		print("already at apple")
		return []

	search_queue = Queue()
	visted = list()
	snake_pos = list(snake)
	next_moves = validMoves(field_size, visted, snake_pos, snake[-1])
	if not next_moves:
		return []

	reverse_map = {}
	for nm in next_moves:
		search_queue.put(nm)
		reverse_map[nm] = snake[-1]

	counter = 0
	while not search_queue.empty():
		cur_pos = search_queue.get()

		if cur_pos == apple:
			break

		visted.append(cur_pos)
		# Didn't find apple, get next possible moves
		# next_moves = validMoves(field_size, visted, cur_pos)
		new_snake = moveToPos(snake, reverse_map, cur_pos)
		counter += 1
		print(counter, snake, new_snake)
		next_moves = validMoves(field_size, visted, new_snake, cur_pos)

		# no possible next moves, move back one
		if not next_moves:
			continue

		for nm in next_moves:
			search_queue.put(nm)
			reverse_map[nm] = cur_pos
	
	full_path = [cur_pos]
	while True:
		cur_pos = reverse_map[cur_pos] 
		if cur_pos == snake[-1]:
			break
		full_path.append(cur_pos)

	full_path.reverse()
	return full_path

