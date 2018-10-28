
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

def validMoves(field_size, visted, cur_pos):
	valid_moves = list()
	# right
	if cur_pos[0]+1 <= field_size[0]\
	and (cur_pos[0]+1, cur_pos[1]) not in visted:
		valid_moves.append((cur_pos[0]+1, cur_pos[1]))
	# left
	if cur_pos[0]-1 >= 0\
	and (cur_pos[0]-1, cur_pos[1]) not in visted:
		valid_moves.append((cur_pos[0]-1, cur_pos[1]))
	# up
	if cur_pos[1]+1 <= field_size[1]\
	and (cur_pos[0], cur_pos[1]+1) not in visted:
		valid_moves.append((cur_pos[0], cur_pos[1]+1))
	# down
	if cur_pos[1]-1 >= 0\
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

from queue import Queue
def PathsToApple(field_size, snake, apple):	
	if snake[-1] == apple:
		print("already at apple")
		return []

	search_queue = Queue()
	visted = list(snake)
	next_moves = validMoves(field_size, visted, snake[-1])
	if not next_moves:
		return []

	reverse_map = {}
	for nm in next_moves:
		search_queue.put(nm)
		reverse_map[nm] = snake[-1]

	visted.extend(next_moves)
	while not search_queue.empty():
		cur_pos = search_queue.get()

		if cur_pos == apple:
			break

		# Didn't find apple, get next possible moves
		next_moves = validMoves(field_size, visted, cur_pos)
		# no possible next moves, move back one
		if not next_moves:
			continue

		for nm in next_moves:
			search_queue.put(nm)
			reverse_map[nm] = cur_pos
		visted.extend(next_moves)
	
	full_path = [cur_pos]
	while True:
		cur_pos = reverse_map[cur_pos] 
		if cur_pos == snake[-1]:
			break
		full_path.append(cur_pos)

	full_path.reverse()
	return full_path

