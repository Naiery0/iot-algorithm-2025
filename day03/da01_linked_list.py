# da01_linked_list.py
# 단순 연결리스트

memory = []  # 컴퓨터 메모리처럼 보이게 만든 변수
head, prev, curr = None, None, None # 항상 첫 번째 노드, curr 바로 앞의 노드, 현재 선택한 노드
dataArray = ['다현', '정연', '쯔위', '사나', '지효'] # 연결 리스트를 만들 데이터

class Node:
    def __init__(self, data):
        self.__data = data
        self.__link = None
    
    def setLink(self, link):
        self.__link = link
    def getData(self):
        return self.__data
    def getLink(self):
        return self.__link
    def __str__(self):
        return self.__data
    
def printNodes(start):
    global memory, head, prev, curr
    curr = start
    if curr == None: return

    print(curr.getData(), end='->')

    while curr.getLink() != None: # 현재 링크의 다음 링크가 있는 동안 
        curr = curr.getLink() # 다음 노드
        print(curr.getData(), end='->')
    print() # 그냥 한 줄 내려줌

def insertNode(findData, insertData):
    global memory, head, prev, curr # 전역 변수를 가져와 이 함수 안에서 쓰겠다

    # 맨 처음에 데이터 삽입
    if head.getData() == findData:
        node = Node(insertData)
        node.setLink(head) # 현재 head가 가리키는 node를 새 노드의 링크로 연결
        head = node # head는 새 node로 설정 
        return # 더이상 밑으로 실행 안 되도록 함수 탈출

    # 중간에 데이터 삽입
    curr = head
    while curr.getLink() != None:
        prev = curr
        curr = curr.getLink()
        if curr.getData() == findData:
            node = Node(insertNode)
            node.setLink(curr)
            prev.setLink(node)
            return # 더이상 밑으로 실행 안 되도록 함수 탈출 
    
    
    # 마지막에 데이터 삽입 
    node = Node(insertData)
    curr.setLink(node)

def deleteNode(deleteData):
    global memory, head, prev, curr

    if head.getData() == deleteData: # 첫 번째 노드 삭제
        curr = head
        head = head.getLink() 
        del(curr)
        return
    
    curr = head # 중간 노드 삭제
    while curr.getLink != None:
        prev = curr
        curr = curr.getLink()
        if curr is None: return # 예외처리
        if curr.getData() == deleteData:
            prev.setLink(curr.getLink()) # 지울 노드의 링크를 prev에서 가리키도록
            del(curr)
            return

def findNode(findData):
    global memory, head, prev, curr
    
    curr = head
    if curr.getData() == findData:
        return curr
    
    while curr.getLink() != None:
        curr = curr.getLink()
        if curr.getData() == findData:
            return curr
    
    return None # 찾는 데이터 없음
    

# 연결리스트 생성 구현
if __name__ == '__main__':
    node = Node(dataArray[0])
    head = node
    memory.append(node)

    for name in dataArray[1:]: # '정연'부터 사용
        prev = node # '다현'이 들어있는 노드를 prev 할당
        node = Node(name) # 0/정현, 1/쯔위, ...
        prev.setLink(node) # 이전 노드에 현재 노드 연결
        memory.append(node)


printNodes(head)
# 5개 데이터를 가지는 연결리스트 생성 긑

# 데이터 삽입 구현
insertNode('다현', '화사')
printNodes(head)

insertNode('사나', '솔라')
printNodes(head)

insertNode('', '문별')
printNodes(head)

# 데이터 검색
fNode = findNode('화사')
print(fNode)

fNode = findNode('유고')
print(fNode)

# 데이터 삭제
deleteNode('화사')
printNodes(head)

deleteNode('쯔위')
printNodes(head)

deleteNode('유고')
printNodes(head)
