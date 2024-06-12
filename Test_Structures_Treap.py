import time
import random
import Treap

size=10

data = [random.randint(1, size) for _ in range(size)]


data2 = [(i, data[i]) for i in range(size)]
print(data)

treap = Treap.Treap()
for key, value in data2:
    treap.insert(key, value)

L,R=1,5
sum_result = treap.range_sum(L, R)
print(sum_result)

min_result = treap.range_min(L, R)
print(min_result)

max_result = treap.range_max(L, R)
print(max_result)

count_result = treap.range_count(L, R, 5)
print(count_result)

treap.erase(3)
treap.insert(3, 5)


sum_result = treap.range_sum(L, R)
print(sum_result)

min_result = treap.range_min(L, R)
print(min_result)

max_result = treap.range_max(L, R)
print(max_result)

count_result = treap.range_count(L, R, 5)
print(count_result)
