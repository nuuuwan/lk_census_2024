class Iter:
    def count(self, func_key=None):
        key_to_n = {}
        for item in self:
            key = func_key(item) if func_key else item
            if key not in key_to_n:
                key_to_n[key] = 0
            key_to_n[key] += 1
        return key_to_n
