from utils_base.ds.Iter import Iter


class List(Iter):
    def __init__(self, x=[]):
        assert isinstance(x, list)
        self.x = x

    @property
    def raw(self):
        return self.x

    def __iter__(self):
        return self.x.__iter__()

    def __len__(self):
        return len(self.x)

    def __getitem__(self, idx):
        return self.x[idx]

    def __setitem__(self, idx, value):
        self.x[idx] = value

    def __eq__(self, other):
        if isinstance(other, List):
            return self.x == other.x
        if isinstance(other, list):
            return self.x == other
        return False

    def __str__(self):
        return str(self.x)

    def __repr__(self):
        return repr(self.x)

    def __add__(self, other):
        assert isinstance(other, List)
        return List(self.x + other.x)

    def flatten(self):
        lst2 = []
        for lst_inner in self.x:
            if not isinstance(lst_inner, list):
                raise TypeError("List.flatten: list contains non-lists")
            lst2 += lst_inner
        return List(lst2)

    def unique(self):
        return List(list(set(self.x)))

    def map(self, func) -> "List":
        return List(list(map(func, self.x)))

    def filter(self, func) -> "List":
        return List(list(filter(func, self.x)))
