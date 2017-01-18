
class CircleIntersect(object):
    def __init__(self, radius1, radius2, x1, x2, y1, y2):
        self._radius1 = radius1
        self._radius2 = radius2
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

    def if_intersect(self):
        radius_minus = pow(self._radius1 - self._radius2, 2)
        radius_add = pow(self._radius1 + self._radius2, 2)
        co_ordinates = pow(self._x1 - self._x2, 2) + pow(self._y1 - self._y2, 2)
        if radius_minus <= co_ordinates <= radius_add:
            return True
        else:
            return False
