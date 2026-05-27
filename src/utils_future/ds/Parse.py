from dateutil import parser


class Parse:
    @staticmethod
    def _clean_(x: str) -> str:
        return x.strip().lower().replace(",", "")

    @staticmethod
    def int(x) -> int:
        try:
            return int(Parse._clean_(x))
        except ValueError:
            return None

    @staticmethod
    def float(x) -> float:
        try:
            return float(Parse._clean_(x))
        except ValueError:
            return None

    TIME_FORMAT = "%Y-%m-%d %H:%M"

    @staticmethod
    def time_str(x) -> str:
        dt = parser.parse(x)
        return dt.strftime(Parse.TIME_FORMAT)
