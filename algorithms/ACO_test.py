from ACO import ant_colony

test_nodes = {0: (0, 7), 1: (3, 9), 2: (12, 4), 3: (14, 11), 4: (8, 11), 5: (15, 6), 6: (6, 15), 7: (15, 9), 8: (12, 10), 9: (10, 7)}


def distance(start, end):
	x_distance = abs(start[0] - end[0])
	y_distance = abs(start[1] - end[1])
	
	import math
	return math.sqrt(pow(x_distance, 2) + pow(y_distance, 2))

colony = ant_colony(test_nodes, distance)

answer = colony.mainloop()