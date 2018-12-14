L=int(input("墙长="))
D=int(input("墙宽="))
l=int(input("砖长="))
d=int(input("砖宽="))
t=int(L*D/l/d)

import sys
if (L*D)%(l*d)!=0:
	print("墙不能被铺满")
	sys.exit()
if max(L,D)<max(l,d):
	print("砖长大于墙长")
	sys.exit()

def Wall(x,y,l,d):  #制作墙的网格
    list=[]
    for i in range(x,x+l):
        for j in range(y,y+d):
            list.append((i,j))
    return list

def Brick(x,y,l,d):   #制作砖的网格
    list=[(x,y),(x+l-1,y),(x,y+d-1),(x+l-1,y+d-1)]
    if l>d:
        for i in range(0,l,d):
            list.append((x+i,y))
            list.append((x+i,y+d-1))
    if d>l:
        for i in range(0,d,l):
            list.append((x,y+i))
            list.append((x+l-1,y+i))
    return list

def remove(i,j,l,d,plot):    #将砖从墙上扣除
    for point in Wall(i,j,l,d):
        plot.remove(point)
    return plot

def number(brick):    #将砖的左下角顶点转为序号
    return brick[0][0]+brick[0][1]*L  

def point(number):  
    return (number%L,number//L)

choices=[]
Plot=Wall(0,0,L,D)

def tile(ans,k=t,plot=Plot):    #定义递归函数
    if k==0:
        choices.append(ans.copy())
    else:
        for num in range(number(ans[t-k-1]),L*D):
            i,j=point(num)[0],point(num)[1]
            plot_1=plot.copy()
            plot_2=plot.copy()
            if set(Brick(i,j,l,d)).issubset(plot):
                ans[t-k]=Wall(i,j,l,d)
                tile(ans,k-1,remove(i,j,l,d,plot_1))
            if l!=d and set(Brick(i,j,d,l)).issubset(plot):
                ans[t-k]=Wall(i,j,d,l)
                tile(ans,k-1,remove(i,j,d,l,plot_2))
                break

import time    #计时
c=time.time()
tile([None]*(t-1)+[[(0,0)]])
d=time.time()
print("runtime:",d-c,"seconds")
if len(choices)==0:
	print("no choices!")
	sys.exit()
print("The number of the choices:",len(choices)) 
e=int(input("print how many:"))
for (i,ans) in enumerate(choices[:e]):
        print(i,":",ans)
        print("")
answer=choices[int(input("which choice"))]

import turtle   #画图
t=turtle.Turtle()
t.speed(0)
t.shape("blank")
def draw(tuple1,tuple2):
    a,b=20*(tuple1[0]-0.5-L/2),20*(tuple1[1]-0.5-D/2)
    c,d=20*(tuple2[0]+0.5-L/2),20*(tuple2[1]+0.5-D/2)
    t.penup()
    t.goto(a,b)
    t.pendown()#到达砖砖左下角的点开始绘图
    t.goto(c,b)
    t.goto(c,d)
    t.goto(a,d)
    t.goto(a,b)
for brick in answer:
    draw(brick[0],brick[-1])

