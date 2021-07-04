class Individual(object):
    def __init__(self, rate: float):
        self._rate = rate

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, rate: float):
        self._rate = rate
