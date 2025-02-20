# da03_fractal02.py
# 시에르핀스키 삼각형

from tkinter import *


## 함수선언
def drawTraiangel(x, y, size):
    if size >= 10:
        drawTraiangel(x, y, size/2) # 왼쪽 아래
        drawTraiangel(x+size/2, y, size/2) # 오른족 아래
        drawTraiangel(x+size/4, int(y-size*(3**0.5)/4), size/2) # 중심 위쪽
    else:
        canvas.create_polygon(x, y, x+size, y, x+size/2, y-size*(3**0.5)/2,
                              fill='red', outline='red')

## 전역변수
wSize = 1000
radius = 400

## 메인코드
root = Tk()
root.title('시에르핀스키 삼각형')
canvas = Canvas(root, width=wSize, height=wSize, bg='white')
canvas.pack()

drawTraiangel(wSize/5, wSize/5*4, wSize*2/3)

root.mainloop()
