import tracemalloc # python 3.4이상부터 지원된다 // 메모리 얼로케이션. 메모리 할당을 추적하고자 할때

tracemalloc.start()

# 메모리 할당이 진행되는 작업 아무거나 작성된 것
data = [b'%d' % num for num in range (1, 10000)]
joined_data = b' '.join(data)

current, peak = tracemalloc.get_traced_memory()
print(f'현재 메모리 사용량: {current / 10 ** 6} MB')
print(f'최대 메모리 사용량: {peak / 10 ** 6} MB')

tracemalloc.stop()
traced = tracemalloc.get_tracemalloc_memory()
print(traced / 10 ** 6)