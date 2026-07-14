import re

from dateutil import parser


class Parse:
    PRECISION_FLOAT = 4
    PRECISION_PERCENT = 4

    @staticmethod
    def _clean_(x: str) -> str:
        return x.strip().lower().replace(",", "").replace("*", "")

    @staticmethod
    def int(x) -> int:
        if x == "-":
            return 0
        if x == "*":
            return 0
        try:
            return int(Parse._clean_(x))
        except ValueError:
            return None

    @staticmethod
    def float(x) -> float:
        if x == "-":
            return 0
        try:
            return round(float(Parse._clean_(x)), Parse.PRECISION_FLOAT)
        except ValueError:
            return None

    @staticmethod
    def percent(x) -> float:
        x = str(x)
        if x == "-":
            return 0
        x = x.replace("%", "")
        try:
            return round(
                float(Parse._clean_(x)) / 100.0, Parse.PRECISION_PERCENT
            )
        except ValueError:
            return None

    TIME_FORMAT = "%Y-%m-%d %H:%M"

    @staticmethod
    def time_str(x) -> str:
        dt = parser.parse(x)
        return dt.strftime(Parse.TIME_FORMAT)

    @staticmethod
    def boolean(x) -> bool:
        x = str(x).strip().lower()
        if x in ["yes", "true", "1", "x", "\u00d7"]:
            return True
        return False

    @staticmethod
    def str(x) -> str:
        x = str(x).strip()
        x = re.sub(r"\s+", " ", x)
        return x
