import streamlit as st
import re
from decimal import Decimal
import sympy
from sympy import *
def jie2(a,b,c):
 try:
  s = float(a)
  d = float(b)
  f = float(c)
  der = d**2-4*s*f
  if der > 0:
      u = hua(der)
      p = int(2 * s)
      c = -d
      st.write("原方程的解是：x1 = ", "(", int(c), '+', u,')/',  int(p), ',', "x2 = ", "(", int(c), '-', u, ')/', int(p))
  elif der == 0:
      st.write('原方程的解是：x1=x2=',trans(-d,int(2*s)))
  else:
      '方程无实数根'
      u = hua(-der)
      p = int(2*s)
      c = -d

      st.write("原方程的解是：x1 = ", "(", int(c),'+',u ,'i)/' , int(p) ,',', "x2 = ", "(", int(c),'-',u ,'i)/' , int(p) )
 except ValueError:

  st.write('输入不合法')
oi =''
pp = 0
def shan(oi):
    oi =re.sub(r'[0-9]',"", oi)
    return oi
def trans(a,b):


    global pp
    if b == 0:
        '方程无解'
    elif b%a == 0:

        pp = str(int(b/a))

    elif a > 0 and b > 0:
        ll = int(min(a,b))
        for i in range(1,ll):
            if a%i == 0 and b%i == 0:
                a /= i
                b /= i
                pp = str(int(a)) + '/' + str(int(b))
    elif a < 0 or b < 0:
        c = abs(a)
        d = abs(b)
        ll = int(min(c, d))
        for i in range(1, ll):
            if c % i == 0 and d % i == 0:
                c /= i
                d /= i
                if a < 0 and b < 0:
                 pp = str(int(c)) + '/' + str(int(d))
                else:
                 pp = '-' + str(int(c)) + '/' + str(int(d))

    return pp
list_2 = []
u = 0
def hua(a):
    global list_2, u
    n = 1000
    while n != 0:
        b = a / n / n
        list_1 = []
        list_1.append(b)
        for i in list_1:
            list_2 = ('{:g}'.format(i))
        if list_2 == 0:
            u = 0

        if (Decimal(list_2) == Decimal(list_2).to_integral()) == True:
            if int(list_2) == 1:
                u = n
                del list_1[0]
                n = 0
            else:
                u = str(n) + "√("+ str(list_2) + ")"
                n = 0
        else:
            n = n - 1
            del list_1[0]
    return u

st.title('计算器')
o = st.selectbox('请选择你的计算类型',
                 (' ','四则运算','二元一次方程组','一元二次方程'))
if o == '四则运算':
    try:
     k = st.text_input('请输入算式（如1+2,3*4-5,666/555）')
     st.write('计算结果为：',eval(k))
    except SyntaxError:
     st.write("输入不合法")
if o == '二元一次方程组':
    try:
     '方程默认等于0'
     k = st.text_input('请输入1式：（形如a*x+b*y-c）')
     i = st.text_input('请输入2式：（形如m*x+n*y-c）')
     x,y = sympy.symbols('x y')
     k = eval(k)
     i = eval(i)
     try:
      k = sympy.linsolve([k,i],(x,y))
      k = list(k)
      ooc = list(k[0])
      st.write('运算结果为：x=',str(ooc[0]),'y=',str(ooc[1]))
     except IndexError:
      '输入不合法'
    except SyntaxError or ValueError :
        '输入不合法'
if o == '一元二次方程':
    '方程默认等于0'
    a = st.text_input('请输入二次项系数')
    b = st.text_input('请输入一次项系数')
    c = st.text_input('请输入常数项')
    jie2(a,b,c)
if o == ' ':
    '看，空气！'











