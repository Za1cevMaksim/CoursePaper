import time
import random
import SegmentTreeP

size=10

data = [random.randint(1, size) for _ in range(size)]
print(data)
seg_tree = SegmentTreeP.SegmentTree(data)



L, R = 1, 5
start_time_sum_seg = time.perf_counter()
sum_result = seg_tree.range_sum(L, R, 0, 0, seg_tree.n - 1)
end_time_sum_seg = time.perf_counter()
print(sum_result)


min_result = seg_tree.range_min(L, R, 0, 0, seg_tree.n - 1)
print(min_result)

max_result = seg_tree.range_max(L, R, 0, 0, seg_tree.n - 1)
print(max_result)

count_result = seg_tree.range_count(L, R, 5, 0, 0, seg_tree.n - 1)
print(count_result)


index_to_update = 3
new_value = 0
seg_tree.update(index_to_update, new_value, 0, 0, seg_tree.n - 1)


sum_result = seg_tree.range_sum(L, R, 0, 0, seg_tree.n - 1)
print(sum_result)

min_result = seg_tree.range_min(L, R, 0, 0, seg_tree.n - 1)
print(min_result)

max_result = seg_tree.range_max(L, R, 0, 0, seg_tree.n - 1)
print(max_result)

count_result = seg_tree.range_count(L, R, 0, 0, 0, seg_tree.n - 1)
print(count_result)