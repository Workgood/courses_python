import math

from geometry.point import distance

class Triangle:
    '''
    Checks, if triangle could be constructed from specified points.

    Args:
      p1 (Point): first point
      p2 (Point): second point
      p3 (Point): third point
    '''
    @staticmethod
    def __isTriangle(p1, p2, p3):
        edges = [distance(p1, p2), distance(p2, p3), distance(p1, p3)]
        max_edge = max(edges)
        edges.remove(max_edge)
        if (max_edge < edges[0] + edges[1]):
            return True
        return False

    '''
    Constructs triangle from specified points.

    Args:
      p1 (Point): first point
      p2 (Point): second point
      p3 (Point): third point

    Throws:
      AssertionError if specified point are not
                     suitable to create a triangle.
    '''
    def __init__(self, p1, p2, p3):
        if (not self.__isTriangle(p1, p2, p3)):
            raise AssertionError("Unable to satisfy triangle inequality")
        self.a = p1
        self.b = p2
        self.c = p3

class OrthogonalTriangle(Triangle):
    '''
    Checks, if triangle could be constructed from specified points.

    Args:
      p1 (Point): first point
      p2 (Point): second point
      p3 (Point): third point
    '''
    @staticmethod
    def __isOrthogonalTriangle(p1, p2, p3):
        edges = [distance(p1, p2), distance(p2, p3), distance(p1, p3)]
        max_edge = max(edges)
        edges.remove(max_edge)
        if (math.isclose(max_edge**2, edges[0]**2 + edges[1]**2)):
            return True
        return False

    '''
    Constructs triangle from specified points.

    Args:
      p1 (Point): first point
      p2 (Point): second point
      p3 (Point): third point

    Throws:
      AssertionError if specified point are not
                     suitable to create a orthogonal triangle.
    '''
    def __init__(self, p1, p2, p3):
        super().__init__(p1, p2, p3)
        if (not self.__isOrthogonalTriangle(p1, p2, p3)):
            raise AssertionError("Unable to satisfy the Pythagorean theorem")
