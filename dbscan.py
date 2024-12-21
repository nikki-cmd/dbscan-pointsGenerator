import pygame
import numpy as np
import random
from mydbscan import calc

from sklearn.cluster import DBSCAN

import matplotlib.pyplot as plt

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def dist(self, point):
		return np.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)


pygame.init()
screen = pygame.display.set_mode((600, 400))
screen.fill("#FFFFFF")
pygame.display.update()
radius = 5

points = []

new_points = []

flag=False
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.MOUSEBUTTONUP:
		
			flag=False
		if event.type == pygame.MOUSEBUTTONDOWN:
			flag=True
		if flag == True:
			pos = event.pos
			

			n_point = Point(*pos)
			

			if len(points) == 0 or n_point.dist(points[-1]) > 30:
				points.append(Point(pos[0], pos[1]))

				pygame.draw.circle(screen, "black", pos, radius)
				n = random.randint(1, 3)
				for i in range(0, n):
					new_pos = (pos[0] + random.randint(-10, 10), pos[1] + random.randint(-10, 10))
					pygame.draw.circle(screen, "black", new_pos, radius)
					points.append(Point(new_pos[0], new_pos[1]))
				pygame.display.update()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				dbscan = DBSCAN(eps=30, min_samples=10)
				arr_p = [[p.x, p.y] for p in points ]
				dbscan.fit(arr_p)
				res = calc(arr_p, 100, 5)
				#labels = dbscan.labels_
				labels = []
				for i in range(0, len(res)):
					labels.append(res[i][2])
				print(f'labels{labels}')
				plt.figure(figsize=(10, 6))
				x = [point.x for point in points]
				y = [point.y for point in points]
				plt.scatter(
				    x,
				    y,
				    c=labels,
				    cmap='viridis',
				    s=10
				)
				plt.show()
