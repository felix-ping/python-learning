# name = input('please enter your name:')
# print('hello',name)


# a=input()
# b=input()
# print(1024*768,a+b)


# n=int(input())
# if n < 5:
#     print('xiao')
# elif n >= 5 or n<10:
#     print('zhong')
# else :
#     print('da')

# s1 = 72
# s2 = 85
# r =s2-s1
# print('' % r)
# s1 = input()
# s2 =input()
# weight = float(s2)
# height = float(s1)
# # print(height*height)
# ibm = weight/(height*height)
# if ibm <18.5:
#     print('qing')
# elif ibm >=18.5 and ibm <25:
#     print('zhengchang')
# elif ibm >=25 and ibm <28:
#     print('zhong')
# elif ibm >=28 and ibm <32:
#     print('guozhong')
# else:
#     print('fei')


# sum = 0
# for x in range(101):
#     sum = sum + x
# print(sum)

# L = ['Bart', 'Lisa', 'Adam']
# for key in L:
#     print(key)

# n = 0 
# while n < 10:
#     n = n + 1
#     if n%2==1:
#         continue
#     print(n)
# print('end')


# a = (1, 2, 3)
# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# b = (1, [2, 3])

# n1 = 255
# n2 = 1000
# print(hex(n1))
# print(max(n1,n2))

import math

def quadratic(a, b, c):
    dart=b*b-4*a*c
    sqr= math.sqrt(dart)
    x1= (-b+sqr)/(2*a)
    x2= (-b-sqr)/(2*a)
    return x1,x2
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')