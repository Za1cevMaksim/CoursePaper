class FenwickTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (self.n + 1)
        self.build(data)

    def build(self, data):
        for i, value in enumerate(data):
            self.update(i, value)

    def update(self, idx, delta):
        idx += 1
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & -idx

    def prefix_sum(self, idx):
        sum = 0
        idx += 1
        while idx > 0:
            sum += self.tree[idx]
            idx -= idx & -idx
        return sum

    def range_sum(self, left, right):
        return self.prefix_sum(right) - self.prefix_sum(left - 1)





