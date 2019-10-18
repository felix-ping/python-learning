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
s1 = input()
s2 =input()
weight = float(s2)
height = float(s1)
print(height*height)
ibm = weight/(height*height)
if ibm <18.5:
    print('qing')
elif ibm >=18.5 and ibm <25:
    print('zhengchang')
elif ibm >=25 and ibm <28:
    print('zhong')
elif ibm >=28 and ibm <32:
    print('guozhong')
else:
    print('fei')
