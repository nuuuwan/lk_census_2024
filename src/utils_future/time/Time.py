import time

from utils_base.time.TimeDelta import TimeDelta


class Time:
    def __init__(self, ut: int = None):
        if ut is None:
            ut = time.time()
        self.ut = ut

    def __eq__(self, other) -> bool:
        return self.ut == other.ut

    def __sub__(self, other) -> TimeDelta:
        if isinstance(other, TimeDelta):
            return Time(self.ut - other.dut)
        if isinstance(other, Time):
            return TimeDelta(self.ut - other.ut)
        raise TypeError(
            "unsupported operand type(s) for -: 'Time' and '%s'" % type(other)
        )

    def __add__(self, other):
        if isinstance(other, TimeDelta):
            return Time(self.ut + other.dut)
        raise TypeError(
            "unsupported operand type(s) for -: 'Time' and '%s'" % type(other)
        )

    @staticmethod
    def now():
        return Time()
