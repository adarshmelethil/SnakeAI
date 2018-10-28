from random import randint

def NewApple(field_size, snake):
	if len(snake) >= field_size[0]*field_size[1]:
		return None
	
	while True:
		apple = (randint(0, field_size[0]), randint(0,field_size[1]))
		if apple not in snake:
			break
	
	return apple

