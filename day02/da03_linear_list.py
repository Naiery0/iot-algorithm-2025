# da03_linear_list.py
# 선형리스트 일반 구현
# 실제 파이썬이 이렇게 동작하는 게 아님
# 배열(선형리스트)이 어떻게 동작하는지 로직을 파악할 것
katok = [] # 빈 배열

# 데이터 추가
def add_data(friend):
    katok.append(None)
    lenKatok = len(katok)
    katok[lenKatok - 1] = friend

# 데이터 삭제
def delete_data(pos):
    if pos < 0 or pos > len(katok):
        print('삭제 범위 오버')
        return
    lenKatok = len(katok)
    katok[pos] = None # 지정된 위치에 값을 삭제

    for i in range(pos + 1, lenKatok):
        katok[i - 1] = katok[i]
        katok[i] = None

    del(katok[lenKatok - 1]) # 배열 마지막 삭제

# 중간 데이터 삽입
def insert_data(pos, friend):
    katok.append(None)

    lenKatok = len(katok)
    for i in range(lenKatok - 1, pos, -1):
        katok[i]=katok[i - 1]
        katok[i - 1] = None

    katok[pos] = friend


add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
print(katok)

insert_data(2, '솔라')
print(katok)
print(katok)
