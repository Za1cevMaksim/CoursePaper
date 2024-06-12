import random
import FenwickTree


size=10

data = [random.randint(1, size) for _ in range(size)]
print(data)

fenwick_tree = FenwickTree.FenwickTree(data)
L,R=1,5

sum_result = fenwick_tree.range_sum(L, R)
print(sum_result)

fenwick_tree.update(3, 5 - fenwick_tree.range_sum(3, 3))

sum_result = fenwick_tree.range_sum(L, R)
print(sum_result)