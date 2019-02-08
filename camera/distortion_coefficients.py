import numpy as np

class DistortionCoefficients:

    def __init__(self):
        self._k1 = 0.0
        self._k2 = 0.0
        self._p1 = 0.0
        self._p2 = 0.0
        self._k3 = 0.0

    def matrix(self):
        result = np.array([self._k1, self._k2, self._p1, self._p2, self._k3], np.float)
        return result

    @property
    def k1(self):
        return self._k1

    @k1.setter
    def k1(self, value):
        self._k1 = value

    @property
    def k2(self):
        return self._k2

    @k2.setter
    def k2(self, value):
        self._k2 = value

    @property
    def k3(self):
        return self._k3

    @k3.setter
    def k3(self, value):
        self._k3 = value

    @property
    def p1(self):
        return self._p1

    @p1.setter
    def p1(self, value):
        self._p1 = value

    @property
    def p2(self):
        return self._p2

    @p2.setter
    def p2(self, value):
        self._p2 = value
