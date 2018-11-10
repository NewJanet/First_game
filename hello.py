# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 17:27:12 2018

@author: WangYuran
"""
#定义函数  普通函数 递归函数
def hello():
    print('goodbye,world')

def square_of_sum(L):
    i=len(L)
    print (i)
L1=[1,2,3,4]
square_of_sum(L1)
    

def return3():
    return 3

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
def power(x,n=2):
    s=1
    while n>1 
    n=n-1
    s=s*x
    return x

#函数可变参数
    def average(*n)

def move(n,a,b,c):
    if n==1:
        print  (a,'->',c)
    else:
        move(n-1,a,c,b)
        print(a,'->',c)
        move(n-1,b,a,c)

move(6,'A','B','C')

hello()
#变量定义 整型/浮点/布尔/字符
a=1
11/4
11%4
10/4+2.5
b="so easy"
c="adjust yourself"
print (a) 
f=True
print('hello,',a or 'world')

x1=1
d=3

#字符串
d='bob said \"I\'m OK\".'
print (d)
print('中文')

#列表 list
empty_list=[]
MyList =['会好的','你说呢','这是个字符list哦']
MyList
print(MyList[0])
print(MyList[-1])
MyList.insert(1,'love you')
print (MyList)
MyList.pop(4)
print (MyList)
MyList[2]='希望'
print (MyList)
MyList.append(11)

###切片
MyList[1:3]
MyList[-2:]
MyList[-2:1]
'ABCDR'[:3]

range(1,11)

#tuple元组-不能像list[]一样修改
t=(1,2,3,4)
print(t)
t=('s','b',['a','b'])
print(t)
L=t[2]
L[0]='Change!'
print(t)

#if 语句   缩进规则
age=20
if age >= 18:
    print('your age is', age)
elif age>=10:
    print('Teenager')
else:
    print('小屁孩')

#循环
 L=[4,1,2,3,4,5]
for i in L:
    print (i)
## 取出索引
for index,i in enumerate(L):
    print (index,'-',i)
        
        
for i in L:
    if i>=4:
        continue
    print(i)
 L2=[1,2,3,4]
for x in L:
    for y in L2:
        print (x+y)

x=1
summ=0
while x<=100:
    x=x+2
    summ=summ+x
print (summ)


while True:
     x=x+2
     summ=summ+x
     if x>=100:
         break
print(summ)
     
# 花括号 dict  {}
d={
   '今天':10,
   '明天':20
   }
print (d['今天'])
print(d)
d['今天']=30
for i in d:
    print (i,d[i])


# 集合set  无重复值
    s=set([1,2,3,4,1,2,3])
    print (s)
for i in s:
    print(i)
    
s.remove(3)
s.add(3)

5 in s
3 in s
x=1
if x in s:
    print('是咱set的人')



#函数
    
























