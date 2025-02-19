# da02_dfs.py
# 그래프 깊이 우선 탐색

# deque 데크
# collections.deque = double ended queue

stack = [] # 스택
visitedAry = [] # 방문기록

class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

## 메인코드
SIZE = 4
G1 = Graph(4)
# 0:A, 1:B, 2:C, 3:D
G1.graph[0][2] = 1
G1.graph[0][3] = 1
G1.graph[1][2] = 1
G1.graph[2][0] = 1
G1.graph[2][1] = 1
G1.graph[2][3] = 1
G1.graph[3][0] = 1
G1.graph[3][2] = 1

print('## G1 무방향 그래프')

for row in range(G1.SIZE):
    for col in range(G1.SIZE):
        print(G1.graph[row][col], end=' ')
    print()

print('## DFS 시작')

current = 0   # A
stack.append(current) # Stack push A
visitedAry.append(current) # 방문기록 A

while len(stack) != 0:
    next = None
    for vertex in range(SIZE):
        if G1.graph[current][vertex] == 1: # 간산이 있다
            if vertex in visitedAry: # 도착점이 이미 방문했으면
                pass
            else:
                next = vertex # 다음 번 방문할 정점
                break
    if next != None:
        current = next
        stack.append(current)
        visitedAry.append(current)
    else:
        current = stack.pop()

print('방문순서', end = '->')
for i in visitedAry:
    print(chr(ord('A') + i), end=' ')

# print()
# print(ord('a')) # ASCII 코드값 출력
        
            