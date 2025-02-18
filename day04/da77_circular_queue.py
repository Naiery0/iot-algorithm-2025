# da77_circular_queue.py
# 원형 큐

# da01_queue.py
# 큐 자료구조 구현

# 함수 선언
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear+1) % SIZE == front:
        return 1
    else: return 0

def isQueueEmpty():
    global SIZE, queue, front, rear
    if front == rear: return True
    else: return False

def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        print('Queue is Full')
        return
    else: 
        rear = rear + 1 % SIZE
        queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queus is empty')
        return None
    else:
        front = (front + 1) % SIZE
        data = queue[front]
        queue[front] = None
        return data
    
def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queus is empty')
        return None
    else: return queue[(front+1) % SIZE]
    
# 전역 변수
SIZE = int(input("큐 크기를 입력하세요 ==>"))
queue = [None for _ in range(SIZE)]
front = rear = 0


if __name__ == '__main__':
    print('메인시작')
    while 1: 
        select = input('삽입 (I) / 추출 (E) / 확인 (V) / 종료 (Q)-> ').upper()
            
        if select == 'Q':
            break
        elif select == 'I':
            data = input('데이터 입력 >')
            enQueue(data)
            print(f'큐 상태 : {queue}')
        elif select == 'E': 
            data = deQueue()
            print(f'추출 데이터 : {data}')
            print(f'큐 상태 : {queue}')
        elif select == 'V': 
            data = peek()
            print(f'확인 데이터 : {data}')
            print(f'큐 상태 : {queue}')
        
        
        
        else: print('!!!입력오류!!!')
