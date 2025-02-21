# ts01_ compare_sort.py

import random
import time

def sortSelection(ary):
    n = len(ary)
    for i in range(0, n-1):
        minIdx = i
        for j in range(i+1, n):
            if ary[minIdx] > ary[j]:
                minIdx = j

        tmp = ary[i]
        ary[i] = ary[minIdx]
        ary[minIdx] = tmp

    return ary

def sortQuickN(ary, start, end):
    if end <= start: return # 재귀호출 종료

    low = start; high = end 

    pivot = ary[(low + high) // 2] # 리스트 중간값을 기준값으로
    while low <= high:
        while ary[low] < pivot:
            low += 1
        while ary[high] > pivot:
            high -= 1
        if low <= high:
            ary[low], ary[high] = ary[high], ary[low]
            low, high = low + 1, high - 1

    # mid = low # 모든 정렬을 한 바퀴 돌면 low는 리스트의 중간쯤 가있음

    sortQuickN(ary, start, low - 1) # 왼쪽 그룹 다시 정렬
    sortQuickN(ary, low, end) # 오른쪽 그룹 다시 정렬

def sortQuick(ary):
    sortQuickN(ary, 0, len(ary)-1)

## 메인코드
countAry = [1000, 10000, 12000, 15000, 40000]

for count in countAry:
    tempAry = [random.randint(10000, 99999) for _ in range(count)]
    selectAry = tempAry[:]
    quickAry = tempAry[:]

    print(f'## 데이터 수 : {count} 개')
    start = time.time()
    sortSelection(selectAry)
    end = time.time()
    print(f'## 선택 정렬 --> {end-start}초')
    start = time.time()
    sortQuick(quickAry)
    end = time.time()
    print(f'## 퀵 정렬 --> {end-start}초')
    print()

    count *= 5