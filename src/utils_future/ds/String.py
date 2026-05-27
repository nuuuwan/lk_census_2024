import re


class String:
    def __init__(self, s: str):
        self.s = s

    def __str__(self):
        return self.s

    def __repr__(self):
        return self.s

    @property
    def float(self, default=None):
        float_str = self.s
        float_str = float_str.replace(',', '')
        float_str = float_str.replace('-', '0')
        try:
            return (float)(float_str)
        except ValueError:
            return default

    @property
    def int(self, default=None):
        int_str = self.s
        int_str = int_str.replace(',', '')
        int_str = int_str.replace('-', '0')
        try:
            return (int)((float)(int_str))
        except ValueError:
            return default

    @property
    def kebab(self):
        s = self.s
        s = re.sub(r'[^a-zA-Z0-9]+', ' ', s)
        s = re.sub(r'\s+', ' ', s)
        s = s.replace(' ', '-')
        return s.lower()

    @property
    def snake(self):
        s = self.s
        return re.sub(r'(\s|-)+', '_', s).lower()

    @property
    def camel(self):
        s = self.snake
        return s.replace('_', ' ').title().replace(' ', '')
