from utils_base.ds.Iter import Iter


class Dict(Iter):
    def __init__(self, x={}):
        assert isinstance(x, dict)
        self.x = x

    def todict(self):
        return self.x

    def keys(self):
        return self.x.keys()

    def values(self):
        return self.x.values()

    def items(self):
        return self.x.items()

    def items_sorted_by_key(self):
        return sorted(
            self.x.items(),
            key=lambda item: item[0],
        )

    def items_sorted_by_value(self):
        return sorted(
            self.x.items(),
            key=lambda item: item[1],
        )

    def len(self):
        return len(self.x)

    def __eq__(self, other):
        if isinstance(other, Dict):
            return self.x == other.x
        if isinstance(other, dict):
            return self.x == other
        return False

    def __getitem__(self, key):
        return self.x[key]

    def __setitem__(self, key, value):
        self.x[key] = value

    def __delitem__(self, key):
        del self.x[key]

    def __iter__(self):
        return self.x.__iter__()

    def extract_keys(self, keys):
        return Dict(
            dict(
                list(
                    filter(
                        lambda item: item[0] in keys,
                        self.x.items(),
                    )
                )
            )
        )

    def __str__(self):
        return self.x.__str__()

    def __repr__(self):
        return self.x.__repr__()
