class TimeUnit:
    def __init__(self, seconds: int):
        self.seconds = seconds

    def __truediv__(self, other):
        if isinstance(other, TimeUnit):
            return self.seconds / other.seconds
        if isinstance(other, float) or isinstance(other, int):
            return TimeUnit(self.seconds / other)
        raise TypeError(
            "unsupported operand type(s) for /: "
            + f"{type(self)} and {type(other)}"
        )

    def __mul__(self, other):
        return TimeUnit(self.seconds * other)

    def __eq__(self, other):
        if isinstance(other, TimeUnit):
            return self.seconds == other.seconds
        return False


TimeUnit.SECOND = TimeUnit(1)
TimeUnit.MINUTE = TimeUnit.SECOND * 60
TimeUnit.HOUR = TimeUnit.MINUTE * 60
TimeUnit.DAY = TimeUnit.HOUR * 24
TimeUnit.WEEK = TimeUnit.DAY * 7
TimeUnit.FORTNIGHT = TimeUnit.WEEK * 7

TimeUnit.AVG_YEAR = TimeUnit.DAY * 365.25
TimeUnit.AVG_QTR = TimeUnit.AVG_YEAR / 4
TimeUnit.AVG_MONTH = TimeUnit.AVG_YEAR / 12


class SECONDS_IN:  # noqa
    MINUTE = TimeUnit.MINUTE / TimeUnit.SECOND
    HOUR = TimeUnit.HOUR / TimeUnit.SECOND
    DAY = TimeUnit.DAY / TimeUnit.SECOND
    WEEK = TimeUnit.WEEK / TimeUnit.SECOND
    FORTNIGHT = TimeUnit.FORTNIGHT / TimeUnit.SECOND

    AVG_MONTH = TimeUnit.AVG_MONTH / TimeUnit.SECOND
    AVG_QTR = TimeUnit.AVG_QTR / TimeUnit.SECOND
    AVG_YEAR = TimeUnit.AVG_YEAR / TimeUnit.SECOND


TimeUnit.SECONDS_IN = SECONDS_IN


class DAYS_IN:  # noqa
    AVG_MONTH = TimeUnit.AVG_MONTH / TimeUnit.DAY
    AVG_QTR = TimeUnit.AVG_QTR / TimeUnit.DAY
    AVG_YEAR = TimeUnit.AVG_YEAR / TimeUnit.DAY


TimeUnit.DAYS_IN = DAYS_IN
