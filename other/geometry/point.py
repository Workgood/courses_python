import math

'''
Provides the distance between two points.

Args:
  p1 (Point): first point
  p2 (Point): second point
'''
def distance(p1, p2):
    return math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
