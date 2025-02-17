# da77_linked_list_example.py

# 사용자가 이름과 이메일을 입력하면 이메일 순서대로 단순 연결 리스트를 생성하는 프로그램.
# 이름에서 Enter를 누르면 입력 종료.

# while 1:
# if 입력=="": break
# 1. 이름, 이메일을 입력받기
# 2. 노드 만들기
# 3. 만들어진 노드에 이름, 이메일 정보 삽입
# 

# 전역변수
head = None
curt = None

# 노드 선언
class Node:
    def __init__(self, data):
        self.__data = data
        self.__link = None

    def setLink(self, link):
        self.__link = link
    def getLink(self):
        return self.__link
    def getData(self):
        return self.__data

def insertNode(inData):
    global head, curt

    if head == None:  # 첫 노드 생성 시 헤드 지정
        node = Node(inData)
        head = node
        curt = head
        return
    
    node = Node(inData)
    curt.setLink(node)

def printNodes(start):
    global head, curt
    curt = start
    if curt == None: return

    print(curt.getData(), end='->')

    while curt.getLink() != None: # 현재 링크의 다음 링크가 있는 동안 
        curt = curt.getLink() # 다음 노드
        print(curt.getData(), end='->')
    print() # 그냥 한 줄 내려줌


# 정보 입력 받기
while 1:
    name = str(input('이름을 입력하세요.'))
    if name == '': break # 엔터 입력 시 종료

    mail = str(input('메일을 입력하세요'))
    data = f'[이름: {name} / 이메일: {mail}]'

    insertNode(data)
    printNodes(head)
    