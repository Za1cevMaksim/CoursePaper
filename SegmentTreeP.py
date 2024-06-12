from collections import defaultdict

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.min_tree = [float('inf')] * (4 * self.n)
        self.max_tree = [-float('inf')] * (4 * self.n)
        self.count_tree = [defaultdict(int) for _ in range(4 * self.n)]
        self.build(data, 0, 0, self.n - 1)

    def build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
            self.min_tree[node] = data[start]
            self.max_tree[node] = data[start]
            self.count_tree[node][data[start]] = 1
        else:
            mid = (start + end) // 2
            self.build(data, 2 * node + 1, start, mid)
            self.build(data, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
            self.min_tree[node] = min(self.min_tree[2 * node + 1], self.min_tree[2 * node + 2])
            self.max_tree[node] = max(self.max_tree[2 * node + 1], self.max_tree[2 * node + 2])
            self.count_tree[node] = defaultdict(int, self.count_tree[2 * node + 1])
            for k, v in self.count_tree[2 * node + 2].items():
                self.count_tree[node][k] += v

    def update_node(self, node, start, end, value):
        self.tree[node] = (end - start + 1) * value
        self.min_tree[node] = value
        self.max_tree[node] = value
        self.count_tree[node] = defaultdict(int)
        self.count_tree[node][value] = end - start + 1

    def update_range(self, L, R, value, node, start, end):
        if start > end or start > R or end < L:
            return
        if L <= start and end <= R:
            self.update_node(node, start, end, value)
            return
        mid = (start + end) // 2
        self.update_range(L, R, value, 2 * node + 1, start, mid)
        self.update_range(L, R, value, 2 * node + 2, mid + 1, end)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
        self.min_tree[node] = min(self.min_tree[2 * node + 1], self.min_tree[2 * node + 2])
        self.max_tree[node] = max(self.max_tree[2 * node + 1], self.max_tree[2 * node + 2])
        self.count_tree[node] = defaultdict(int, self.count_tree[2 * node + 1])
        for k, v in self.count_tree[2 * node + 2].items():
            self.count_tree[node][k] += v

    def update(self, idx, value, node, start, end):
        if start == end:
            self.tree[node] = value
            self.min_tree[node] = value
            self.max_tree[node] = value
            self.count_tree[node] = defaultdict(int)
            self.count_tree[node][value] = 1
        else:
            mid = (start + end) // 2
            if start <= idx <= mid:
                self.update(idx, value, 2 * node + 1, start, mid)
            else:
                self.update(idx, value, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
            self.min_tree[node] = min(self.min_tree[2 * node + 1], self.min_tree[2 * node + 2])
            self.max_tree[node] = max(self.max_tree[2 * node + 1], self.max_tree[2 * node + 2])
            self.count_tree[node] = defaultdict(int, self.count_tree[2 * node + 1])
            for k, v in self.count_tree[2 * node + 2].items():
                self.count_tree[node][k] += v

    def range_sum(self, L, R, node, start, end):
        if R < start or end < L:
            return 0
        if L <= start and end <= R:
            return self.tree[node]
        mid = (start + end) // 2
        left_sum = self.range_sum(L, R, 2 * node + 1, start, mid)
        right_sum = self.range_sum(L, R, 2 * node + 2, mid + 1, end)
        return left_sum + right_sum

    def range_min(self, L, R, node, start, end):
        if R < start or end < L:
            return float('inf')
        if L <= start and end <= R:
            return self.min_tree[node]
        mid = (start + end) // 2
        left_min = self.range_min(L, R, 2 * node + 1, start, mid)
        right_min = self.range_min(L, R, 2 * node + 2, mid + 1, end)
        return min(left_min, right_min)

    def range_max(self, L, R, node, start, end):
        if R < start or end < L:
            return -float('inf')
        if L <= start and end <= R:
            return self.max_tree[node]
        mid = (start + end) // 2
        left_max = self.range_max(L, R, 2 * node + 1, start, mid)
        right_max = self.range_max(L, R, 2 * node + 2, mid + 1, end)
        return max(left_max, right_max)

    def range_count(self, L, R, value, node, start, end):
        if R < start or end < L:
            return 0
        if L <= start and end <= R:
            return self.count_tree[node].get(value, 0)
        mid = (start + end) // 2
        left_count = self.range_count(L, R, value, 2 * node + 1, start, mid)
        right_count = self.range_count(L, R, value, 2 * node + 2, mid + 1, end)
        return left_count + right_count



