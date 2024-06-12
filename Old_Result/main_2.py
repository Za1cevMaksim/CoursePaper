import pandas
import time
import tracemalloc
import random
import SegmentTreeP
import FenwickTree
import Treap





all_store=[]

for size in range(10,2001):
    init__time = []
    init__memory = []
    update = []
    sum_ = []
    min_ = []
    max_ = []
    count_ = []

    print("size", size)
    data = [random.randint(1, int(size * 100)) for _ in range(size)]


    tracemalloc.start()
    start_time_init_seg = time.perf_counter()
    seg_tree = SegmentTreeP.SegmentTree(data)
    end_time_init_seg = time.perf_counter()
    mem_init_seg, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    # print(f"Инициализация: {end_time_init_seg - start_time_init_seg:.9f} секунд, память: {mem_init_seg / 1024:.2f} КБ")
    init__time.append((end_time_init_seg - start_time_init_seg)*1000)
    init__memory.append(mem_init_seg / 1024)

    # Обновление элемента
    index_to_update = random.randint(0, size - 1)
    new_value = random.randint(1, int(size * 100))
    start_time_upd_seg = time.perf_counter()
    seg_tree.update(index_to_update, new_value, 0, 0, seg_tree.n - 1)
    end_time_upd_seg = time.perf_counter()
    update.append((end_time_upd_seg - start_time_upd_seg)*1000)
    # print(f"Обновление элемента: {index_to_update,new_value} {end_time_upd_seg - start_time_upd_seg:.9f} секунд")

    # Запрос суммы на отрезке
    L, R = sorted([random.randint(0, size - 1) for _ in range(2)])
    start_time_sum_seg = time.perf_counter()
    sum_result = seg_tree.range_sum(L, R, 0, 0, seg_tree.n - 1)
    end_time_sum_seg = time.perf_counter()
    sum_.append((end_time_sum_seg - start_time_sum_seg)*1000)
    # print(f"Сумма на отрезке [{L}, {R}]:{sum_result} {end_time_sum_seg - start_time_sum_seg:.9f} секунд")

    # Запрос минимума на отрезке
    start_time_min_seg = time.perf_counter()
    min_result = seg_tree.range_min(L, R, 0, 0, seg_tree.n - 1)
    end_time_min_seg = time.perf_counter()
    min_.append((end_time_min_seg - start_time_min_seg)*1000)
    # print(f"Минимум на отрезке [{L}, {R}: {min_result}]: {end_time_min_seg - start_time_min_seg:.9f} секунд")

    # Запрос максимума на отрезке
    start_time_max_seg = time.perf_counter()
    max_result = seg_tree.range_max(L, R, 0, 0, seg_tree.n - 1)
    end_time_max_seg = time.perf_counter()
    max_.append((end_time_max_seg - start_time_max_seg)*1000)
    # print(f"Максимум на отрезке [{L}, {R}: {max_result}]: {end_time_max_seg - start_time_max_seg:.9f} секунд")

    # Количество вхождений значения на отрезке
    value_to_count = random.randint(1, int(size / 10))
    start_time_cnt_seg = time.perf_counter()
    count_result = seg_tree.range_count(L, R, value_to_count, 0, 0, seg_tree.n - 1)
    end_time_cnt_seg = time.perf_counter()
    # print(f"Количество вхождений значения {value_to_count} на отрезке [{L}, {R}]: {count_result} {end_time_cnt_seg - start_time_cnt_seg:.9f} секунд")
    count_.append((end_time_cnt_seg - start_time_cnt_seg)*1000)


    # Инициализация дерева Фенвика
    tracemalloc.start()
    start_time_init_fen = time.perf_counter()
    fenwick_tree = FenwickTree.FenwickTree(data)
    end_time_init_fen = time.perf_counter()
    mem_init_fen, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    # print(f"Инициализация: {end_time_init_fen - start_time_init_fen:.9f} секунд, память: {mem_init_fen / 1024:.2f} КБ")
    init__time.append((end_time_init_fen - start_time_init_fen)*1000)
    init__memory.append(mem_init_fen / 1024)

    # Обновление элемента
    start_time_upd_fen = time.perf_counter()
    fenwick_tree.update(index_to_update, new_value - fenwick_tree.range_sum(index_to_update, index_to_update))
    end_time_upd_fen = time.perf_counter()
    update.append((end_time_upd_fen - start_time_upd_fen)*1000)
    # print(f"Обновление элемента: {end_time_upd_fen - start_time_upd_fen:.9f} секунд")

    # Запрос суммы на отрезке
    start_time_sum_fen = time.perf_counter()
    sum_result = fenwick_tree.range_sum(L, R)
    end_time_sum_fen = time.perf_counter()
    sum_.append((end_time_sum_fen - start_time_sum_fen)*1000)
    # print(f"Сумма на отрезке [{L}, {R}]: {sum_result}, {end_time_sum_fen - start_time_sum_fen:.9f} секунд")

    min_.append(None)
    max_.append(None)
    count_.append(None)
    data2 = [(i, data[i]) for i in range(size)]

    # Инициализация Дек. дерева
    tracemalloc.start()
    start_time_init_trp = time.perf_counter()
    treap = Treap.Treap()
    for key, value in data2:
        treap.insert(key, value)
    end_time_init_trp = time.perf_counter()
    mem_init_trp, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    # print(f"Инициализация: {end_time_init_trp - start_time_init_trp:.9f} секунд, память: {mem_init_trp / 1024:.2f} КБ")
    init__time.append((end_time_init_trp - start_time_init_trp)*1000)
    init__memory.append(mem_init_trp / 1024)

    # Обновление элемента
    start_time_upd_trp = time.perf_counter()
    treap.erase(index_to_update)
    treap.insert(index_to_update, new_value)
    end_time_upd_trp = time.perf_counter()
    update.append((end_time_upd_trp - start_time_upd_trp)*1000)
    # print(f"Обновление элемента {index_to_update,new_value}: {end_time_upd_trp - start_time_upd_trp:.9f} секунд")

    # Запрос суммы на отрезке
    start_time_sum_trp = time.perf_counter()
    sum_result = treap.range_sum(L, R)
    end_time_sum_trp = time.perf_counter()
    sum_.append((end_time_sum_trp - start_time_sum_trp)*1000)
    # print(f"Сумма на отрезке [{L}, {R}]: {end_time_sum_trp - start_time_sum_trp:.9f} секунд, результат: {sum_result}")

    # Запрос минимального значения на отрезке
    start_time_min_trp = time.perf_counter()
    min_result = treap.range_min(L, R)
    end_time_min_trp = time.perf_counter()
    min_.append((end_time_min_trp - start_time_min_trp)*1000)
    # print(f"Минимум на отрезке [{L}, {R}]:{end_time_min_trp - start_time_min_trp:.9f} секунд, результат: {min_result}")

    # Запрос максимального значения на отрезке
    start_time_max_trp = time.perf_counter()
    max_result = treap.range_max(L, R)
    end_time_max_trp = time.perf_counter()
    max_.append((end_time_max_trp - start_time_max_trp)*1000)
    # print(f"Максимум на отрезке [{L}, {R}]:{end_time_max_trp - start_time_max_trp:.9f} секунд, результат: {max_result}")

    # Запрос количества элементов на отрезке
    start_time_cnt_trp = time.perf_counter()
    count_result = treap.range_count(L, R, value_to_count)
    end_time_cnt_trp = time.perf_counter()
    count_.append((end_time_cnt_trp - start_time_cnt_trp)*1000)
    # print(f"Количество {value_to _count} на отрезке [{L}, {R}]: {end_time_cnt_trp - start_time_cnt_trp:.9f} секунд, результат: {count_result}")


    all_store.append(init__time)
    all_store.append(init__memory)
    all_store.append(update)
    all_store.append(sum_)
    all_store.append(min_)
    all_store.append(max_)
    all_store.append(count_)

dp=pandas.DataFrame(all_store, columns= ["Segment","Fenwick","Treap"])

print(dp)



with pandas.ExcelWriter('Result_2000.xlsx') as writer:
    dp.to_excel(writer, sheet_name='2000')

