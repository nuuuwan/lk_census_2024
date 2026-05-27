class TimeDelta:
    def __init__(self, dut: int = 0):
        self.dut = dut

    def __eq__(self, other) -> bool:
        return self.dut == other.dut

    def humanize(self):
        dut = self.dut

        for dut_limit, label in [
            (60, 'second'),
            (60, 'minute'),
            (24, 'hour'),
            (7, 'day'),
            (None, 'week'),
        ]:
            if not dut_limit or dut < dut_limit:
                suffix = ''
                if dut != 1:
                    suffix = 's'
                return f'{dut:.0f} {label}{suffix}'
            else:
                dut /= dut_limit
