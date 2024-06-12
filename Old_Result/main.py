import pandas
import time
import tracemalloc
import random
import SegmentTreeP
import FenwickTree
import Treap


sizes=[100, 500, 1000, 5000, 10000]


all_store=[]

for size in sizes:
    antidp = []
    init_Segment_time = []
    init_Segment_memory = []
    update_Segment = []
    sum_Segment = []
    min_Segment = []
    max_Segment = []
    count_segment = []

    init_Fen_time = []
    init_Fen_memory = []
    update_Fen = []
    sum_Fen = []


    init_Treap_time = []
    init_Treap_memory = []
    update_Treap = []
    sum_Treap = []
    min_Treap = []
    max_Treap = []
    long_update_Treap = []
    count_Treap = []

    for iterations in range(0,500):
        print("Segment", size)
        data = [random.randint(1, int(size/10)) for _ in range(size)]
        tracemalloc.start()
        start_time_init_seg = time.perf_counter()
        seg_tree = SegmentTreeP.SegmentTree(data)
        end_time_init_seg = time.perf_counter()
        mem_init_seg, _ = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        #print(f"Инициализация: {end_time_init_seg - start_time_init_seg:.9f} секунд, память: {mem_init_seg / 1024:.2f} КБ")
        init_Segment_time.append(end_time_init_seg - start_time_init_seg)
        init_Segment_memory.append(mem_init_seg / 1024)

        # Обновление элемента
        index_to_update = random.randint(0, size-1)
        new_value = random.randint(1, int(size/10))
        start_time_upd_seg = time.perf_counter()
        seg_tree.update(index_to_update, new_value, 0, 0, seg_tree.n - 1)
        end_time_upd_seg = time.perf_counter()
        update_Segment.append(end_time_upd_seg - start_time_upd_seg)
        #print(f"Обновление элемента: {index_to_update,new_value} {end_time_upd_seg - start_time_upd_seg:.9f} секунд")

        # Запрос суммы на отрезке
        L, R = sorted([random.randint(0, size-1) for _ in range(2)])
        start_time_sum_seg = time.perf_counter()
        sum_result = seg_tree.range_sum(L, R, 0, 0, seg_tree.n - 1)
        end_time_sum_seg = time.perf_counter()
        sum_Segment.append(end_time_sum_seg - start_time_sum_seg)
        #print(f"Сумма на отрезке [{L}, {R}]:{sum_result} {end_time_sum_seg - start_time_sum_seg:.9f} секунд")

        # Запрос минимума на отрезке
        start_time_min_seg = time.perf_counter()
        min_result = seg_tree.range_min(L, R, 0, 0, seg_tree.n - 1)
        end_time_min_seg = time.perf_counter()
        min_Segment.append(end_time_min_seg - start_time_min_seg)
        #print(f"Минимум на отрезке [{L}, {R}: {min_result}]: {end_time_min_seg - start_time_min_seg:.9f} секунд")

        # Запрос максимума на отрезке
        start_time_max_seg = time.perf_counter()
        max_result = seg_tree.range_max(L, R, 0, 0, seg_tree.n - 1)
        end_time_max_seg = time.perf_counter()
        max_Segment.append(end_time_max_seg - start_time_max_seg)
        #print(f"Максимум на отрезке [{L}, {R}: {max_result}]: {end_time_max_seg - start_time_max_seg:.9f} секунд")


        # Количество вхождений значения на отрезке
        value_to_count = random.randint(1, int(size/10))
        start_time_cnt_seg = time.perf_counter()
        count_result = seg_tree.range_count(L, R, value_to_count, 0, 0, seg_tree.n - 1)
        end_time_cnt_seg = time.perf_counter()
        #print(f"Количество вхождений значения {value_to_count} на отрезке [{L}, {R}]: {count_result} {end_time_cnt_seg - start_time_cnt_seg:.9f} секунд")
        count_segment.append(end_time_cnt_seg - start_time_cnt_seg)

        print("Fen",size)
        # Инициализация дерева
        tracemalloc.start()
        start_time_init_fen = time.perf_counter()
        fenwick_tree = FenwickTree.FenwickTree(data)
        end_time_init_fen = time.perf_counter()
        mem_init_fen, _ = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        #print(f"Инициализация: {end_time_init_fen - start_time_init_fen:.9f} секунд, память: {mem_init_fen / 1024:.2f} КБ")
        init_Fen_time.append(end_time_init_fen- start_time_init_fen)
        init_Fen_memory.append(mem_init_fen / 1024)


        # Обновление элемента
        start_time_upd_fen = time.perf_counter()
        fenwick_tree.update(index_to_update, new_value - fenwick_tree.range_sum(index_to_update, index_to_update))
        end_time_upd_fen = time.perf_counter()
        update_Fen.append(end_time_upd_fen - start_time_upd_fen)
        #print(f"Обновление элемента: {end_time_upd_fen - start_time_upd_fen:.9f} секунд")

        # Запрос суммы на отрезке
        start_time_sum_fen = time.perf_counter()
        sum_result = fenwick_tree.range_sum(L, R)
        end_time_sum_fen = time.perf_counter()
        sum_Fen.append(end_time_sum_fen - start_time_sum_fen)
        #print(f"Сумма на отрезке [{L}, {R}]: {sum_result}, {end_time_sum_fen - start_time_sum_fen:.9f} секунд")




        ###
        ###
        print("Treap",size)


        data2 = [(i, data[i]) for i in range(size)]

        # Инициализация дерева
        tracemalloc.start()
        start_time_init_trp = time.perf_counter()
        treap = Treap.Treap()
        for key, value in data2:
            treap.insert(key, value)
        end_time_init_trp = time.perf_counter()
        mem_init_trp, _ = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        #print(f"Инициализация: {end_time_init_trp - start_time_init_trp:.9f} секунд, память: {mem_init_trp / 1024:.2f} КБ")
        init_Treap_time.append(end_time_init_trp - start_time_init_trp)
        init_Treap_memory.append(mem_init_trp / 1024)


        # Обновление элемента
        start_time_upd_trp = time.perf_counter()
        treap.erase(index_to_update)
        treap.insert(index_to_update, new_value)
        end_time_upd_trp = time.perf_counter()
        update_Treap.append(end_time_upd_trp - start_time_upd_trp)
        #print(f"Обновление элемента {index_to_update,new_value}: {end_time_upd_trp - start_time_upd_trp:.9f} секунд")


        # Запрос суммы на отрезке
        start_time_sum_trp = time.perf_counter()
        sum_result = treap.range_sum(L, R)
        end_time_sum_trp = time.perf_counter()
        sum_Treap.append(end_time_sum_trp - start_time_sum_trp)
        #print(f"Сумма на отрезке [{L}, {R}]: {end_time_sum_trp - start_time_sum_trp:.9f} секунд, результат: {sum_result}")

        # Запрос минимального значения на отрезке
        start_time_min_trp = time.perf_counter()
        min_result = treap.range_min(L, R)
        end_time_min_trp = time.perf_counter()
        min_Treap.append(end_time_min_trp - start_time_min_trp)
        #print(f"Минимум на отрезке [{L}, {R}]:{end_time_min_trp - start_time_min_trp:.9f} секунд, результат: {min_result}")

        # Запрос максимального значения на отрезке
        start_time_max_trp = time.perf_counter()
        max_result = treap.range_max(L, R)
        end_time_max_trp = time.perf_counter()
        max_Treap.append(end_time_max_trp - start_time_max_trp)
        #print(f"Максимум на отрезке [{L}, {R}]:{end_time_max_trp - start_time_max_trp:.9f} секунд, результат: {max_result}")

        # Запрос количества элементов на отрезке
        start_time_cnt_trp = time.perf_counter()
        count_result = treap.range_count(L, R, value_to_count)
        end_time_cnt_trp = time.perf_counter()
        count_Treap.append(end_time_cnt_trp - start_time_cnt_trp)
        #print(f"Количество {value_to_count} на отрезке [{L}, {R}]: {end_time_cnt_trp - start_time_cnt_trp:.9f} секунд, результат: {count_result}")

    antidp.append((sum(init_Segment_time)/len(init_Segment_time),sum(init_Fen_time)/len(init_Fen_time),sum(init_Treap_time)/len(init_Treap_time)))
    antidp.append((sum(init_Segment_memory) / len(init_Segment_memory), sum(init_Fen_memory) / len(init_Fen_memory),
               sum(init_Treap_memory) / len(init_Treap_memory)))
    antidp.append((sum(update_Segment) / len(update_Segment), sum(update_Fen) / len(update_Fen),
               sum(update_Treap) / len(update_Treap)))
    antidp.append((sum(sum_Segment) / len(sum_Segment), sum(sum_Fen) / len(sum_Fen),
               sum(sum_Treap) / len(sum_Treap)))
    antidp.append((sum(min_Segment) / len(min_Segment), None,
               sum(min_Treap) / len(min_Treap)))
    antidp.append((sum(max_Segment) / len(max_Segment), None,
               sum(max_Treap) / len(max_Treap)))
    antidp.append((sum(count_segment) / len(count_segment), None,
               sum(count_Treap) / len(count_Treap)))

    dp=pandas.DataFrame(antidp, index=["Init","Init Memory","Update","Sum","Min","Max","Count"], columns= ["Segment","Fenwick","Treap"])
    all_store.append(dp)





with pandas.ExcelWriter('Result.xlsx') as writer:
    all_store[0].to_excel(writer, sheet_name='100')
    all_store[1].to_excel(writer, sheet_name='500')
    all_store[2].to_excel(writer, sheet_name='1000')
    all_store[3].to_excel(writer, sheet_name='5000')
    all_store[4].to_excel(writer, sheet_name='10000')
