class SpaceAge(object):
    
    periods = dict(earth=1.0,mercury=0.2408467,mars=1.8808158,jupiter=11.862615,
                    saturn=29.447498,uranus=84.016846,neptune=164.79132,venus=0.61519726)

    def __init__(self, seconds):
        self.seconds = seconds

    def __getattr__(self, name):
        planet = name[3:]
        period = self.periods[planet]
        print(period)
        return lambda: self._years(period)

    def _years(self, period):
        return round(self.seconds / (31557600 * period), 2)