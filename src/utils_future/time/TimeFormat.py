import time

from utils_base.time.Time import Time
from utils_base.time.TimeZoneOffset import TimeZoneOffset


class TimeFormat:
    def __init__(self, format_str: str, timezone_offset=TimeZoneOffset.LK):
        self.format_str = format_str
        self.timezone_offset = timezone_offset

    @property
    def dut_timezone(self):
        return time.timezone - self.timezone_offset

    def parse(self, time_str: str) -> Time:
        ut_base = time.mktime(time.strptime(time_str, self.format_str))
        ut = ut_base - self.dut_timezone
        return Time(ut)

    def stringify(self, t: Time) -> str:
        return time.strftime(
            self.format_str, time.localtime(t.ut + self.dut_timezone)
        )

    def format(self, t: Time) -> str:
        return self.stringify(t)

    @property
    def formatNow(self) -> str:
        return self.format(Time.now())


TimeFormat.DATE = TimeFormat('%Y-%m-%d')  # noqa
TimeFormat.TIME = TimeFormat('%Y-%m-%d %H:%M:%S')  # noqa

TimeFormat.DATE_ID = TimeFormat('%Y%m%d')  # noqa
TimeFormat.TIME_ID = TimeFormat('%Y%m%d.%H%M%S')  # noqa
