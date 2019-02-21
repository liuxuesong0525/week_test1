
# 1、var1 = 'Hello World'
# var2 = "Runoob"
# print ('var1[0]:',var1[0])
# print ('var2[1:5]:',var2[1:5])

# print (7//2)  #整除--取整数
# print (7%2)   #取余

#2、查看类型
# a=100
# print (type(a))
# b=101.1
# print(type(b))
# c=1.1+2.2j
# print(type(c))

#3、
# str='asdfghjkl'
# str1=str+str.upper()
# print(str1)

# import random
# print(random.choice(range(10)))

# import random
#
# str0 = 'abcdefghijklmnopqrstuvwxyz'
# str1 = str0 + str0.upper()
#
#
# rand_str = ''
# for i in range(1,101):
#     rand_str += random.choice( str1 )
#     print(i,rand_str)

#输入自己的姓名、性别、年龄，并且原样输出
# print('请输入姓名，性别，年龄')
# a=input()
# b=input()
# c=input()
# print(a+','+b+','+c)
#输入一个数字，求其平方根
# import math
# print('请输入一个数字')
# a=input()
# print(math.sqrt(int(a)))
#猜大小游戏：输入一个整数，随机生成一个数字，比较这两个数字的大小，并输出比较结果
# import random
# print('请输入一个整数')
# a=int(input())
# b=random.choice(range(10))
# print('a>b',a>b)


# i=0
# sum=0
# while i<=100:
#     sum += i
#     i += 1
# print(sum)

#4、在字符串里随机字符
# import random
# str=random.choice('Runoob')
# print(str)

# import random
# print(random.random())

# a = "Hello"
# b = "Python"
# print("a + b 输出结果：", a + b)
# print("a * 2 输出结果：", a * 2)
# print("a[1] 输出结果：", a[1])
# print("a[1:4] 输出结果：", a[1:4])
#
# if( "H" in a) :
#     print("H 在变量 a 中")
# else :
#     print("H 不在变量 a 中")
# if( "M" not in a) :
#     print("M 不在变量 a 中")
# else :
#     print("M 在变量 a 中")


# 5、检测字符串中是否包含索引的对象，在第几位。
# a='hello world I am Anna'
# print(a.find('I',0,len(a)))


# 6、检测字符在字符串中出现的次数
# a='hello world I am Anna'
# print(a.count('Anna',0,len(a)))

# 7、替换掉字符串里的字符
# a='hello world I am Anna'
# print(a.replace('l','b',2))

# 8、字符串切割 ,根据指定条件切割
# a='hello world I am Anna'
# print(a.split(' ',2))

# 9、把字符串的第一个字符变成大写，其他全部改成小写
# a='hello world I am Anna'
# print(a.capitalize())

# 10、检测是否是以规定的目标条件开头
# a='hello world I am Anna'
# print(a.startswith('hello'))


# 11、检测是否以规定的目标条件结尾
# a='hello world I am Anna'
# print(a.endswith('Anna'))

#12、将字符串中的所有大写字符改为小写
# a='Hello World I Am Anna'
# print(a.lower())

#13、将字符串中的小写字母变为大写
# a='hello world i am anna'
# print(a.upper())

#1.	编写Python程序判断字符串是否重复
# a='hello world I am Anna am am am'
# b=a.count('am')
# if b>1:
#     print('有重复',b)
# else:
#     print('不重复')

#2判断字符串是否重复
# s='euebkdkjdsdd'
# l1=list(s)
# if len(l1)!=len(set(l1)):
#     print('字符串重复')
# else:
#     print('字符串没有重复')


# 3、判断字符串是否重复
# s='abcdcacqwcaea'
# l1=list(s)
# if len(l1)!=len(set(l1)):
#     print('字符串重复')
# else:
#     print('字符串没有重复')
#
# 4查找字符串中重复的
# str='euebkdkjdsdd'
# i=0
# cf=''   #记录重复的数据
# bcf=''   #记录不重复的数据
# while i<len(str):
#     if str.count(str[i])>1:
#         if str[i] in cf:
#             i+=1
#             continue
#         cf += str[i]
#     else:
#         bcf+=str[i]
#     i+=1
# print('重复的元素有：%s'%cf)
# print('不重复的元素有：%s'%(bcf))
#
#
# 5、输入某年某月某日，判断这一天是这一年的第几天？
# import time
# D=input("请输入年份，格式如XXXX-XX-XX：")
# d=time.strptime( D,'%Y-%m-%d').tm_yday
# print("这是这一年的第 {} 天!" .format(d))

# import time
# D=input('请输入年份，格式如xxxx-xx-xx:')
# d=time.strptime(D,'%Y-%m-%d').tm_yday
# print('这是这一年的第{}天'.format(d))


#/6、输入两个人的出生月份，来计算两个人的缘分（30分）
# 要求：余数为1   非常有缘
#       余数为2   比较有缘
#       余数为3   缘份一般
#       余数为4   有仇

# a = int(input("请输入第一个人的月份："))
# b = int(input("请输入第二个人的月份："))
# c = a%b
# if c==1:
#     print("非常有缘")
# elif c==2:
#     print("比较有缘")
# elif c==3:
#     print("缘分一般")
# elif c==4:
#     print("有仇")
# else:
#     print("无缘")

#------------------------------------------

#7、随机生成一个序列，再次生成一个整数，查看这个整数有没有在序列中
# import random
# list1 = []
# for i in range(1,20):
#     list1.append(random.randint(1,100))
# print(list1)
#
# num1 = random.randint(1,100)
#
# if num1 in list1:
#     print("这个整数在序列中")
# else:
#     print("不在此序列中")

# import random
# list=[]
# for i in range(1,20):
#     list.append(random.randint(1,100))
# print(list)
# num=random.randint(1,100)
# if num in list:
#     print("在序列中")
# else:
#     print('不在')


# import random
# list=[]
# for i in range(1,20):
#     list.append(random.randrange(1,100))
# print(list)
# num=random.randint(1,100)
# if num in list:
#     print('在')
# else:
#     print('不在')
# #------------------------------------------

# 8、随机生成一个序列，10个元素，并对序列进行升序排序
# list2 = []
# for i in range(10):
#     list2.append(random.randrange(1,100))
#
# for i in range(0,len(list2)):  #从首位开始索引下标
#     for j in range(i+1,len(list2)):  #从上一个数字的下一个数字开始比较
#
#         if list2[i]>list2[j]:
#            temp = list2[i]
#            list2[i] = list2[j]
#            list2[j] = temp
#
# list2.sort()
# print(list2)
# import random
# list=[]
# for i in range(10):
#     list.append(random.randrange(1,100))
#
# for i in range(0,len(list)):
#     for j in range(i+1,len(list)):
#         if list[i]>list[j]:
#             temp = list[i]
#             list[i] = list[j]
#             list[j] = temp
# print(list)

# import random
# list=[]
# for i in range(10):
#     list.append(random.randrange(1,100))
#
# for i in range(0,len(list)):
#     for j in range(i+1,len(list)):
#         if list[i]>list[j]:
#             temp = list[i]
#             list[i] = list[j]
#             list[j] = temp
# print(list)

#/9、计算1-100的总和：
# i=0
# sum=0
# while i<=100:
#     sum+=i
#     i+=1
# print(sum)

#10打印
# *
# * *
# * * *
# * * * *
# * * * * *
# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         print('*',end=' ')
#         j+=1
#     print('')
#     i+=1


#11、 for循环可以遍历任何序列的项目，如一个列表或者一个字符串
# list=['a','b','c','d','e']
# for i in list:
#     print(i)

#12、for循环中使用break
# name=['hello','world','I','am','Anna']
# for i in name:
#     if i=='I':
#         break
#     print(i)
# print('循环结束')

#range()函数
# a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
# for i in range(len(a)):
#    print(i, a[i])

# a = 2.0
# b = 1.0
# s = 0
# for n in range(1,21):
#     s += a / b
#     t = a
#     a = a + b
#     b = t
# print (s)


#1.	请手动输入一个三位数字判断该数字是否为水仙花数？
# print('请输入一个三位数：')
# num = int(input())
# g = num % 10
# s = num // 10 % 10
# b = num // 100 % 10
# sum = g ** 3 + s ** 3 + b ** 3
# if num == sum:
#     print('是水仙花数')
# else:
#     print('不是水仙花数')

#2.	生成一个随机的整数，判断该整数是否为偶数
# import random
# num2=random.randint(1,100)
# print(num2)
# if num2 % 2 == 0:
#     print('num2是偶数')
# else:
#     print('num2不是偶数')

#3、四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# count=0
# for i in range(1,5):
#     for j in range (1,5):
#         for k in range (1,5):
#             if(i!=j) and (i!=k) and (j!=k):
#                 count+=1
#                 print(i,j,k)
# print('共有%d个三位数'%count)

#4、 请根据字符串’Today is Sunday. It is very warm.
#  Many children are playing the slide ,climbing the stones in the playground.
#  The children are preparing to take their autumn holiday.
#  But we are studying in the classroom. I like python. I like python. I like python.’
#计算出每个单词的数量为多少
#思路：可以使用字符串分割进行处理  计数可以使用字典

# d={}
# a = 'Today is Sunday. It is very warm. Many children are playing the slide ,' \
#         'climbing the stones in the playground. The children are preparing to take ' \
#         'their autumn holiday. But we are studying in the classroom. I like python. ' \
#         'I like python. I like python.'
# s1 = a.replace(",", "").replace(".", "")
# li = s1.split(" ")
# for i in li:
#     d[i] = li.count(i)
# print(d)

# d={}
# a='Today is Sunday. It is very warm. Many children are playing the slide ,' \
#         'climbing the stones in the playground. The children are preparing to take ' \
#          'their autumn holiday. But we are studying in the classroom. I like python. ' \
#          'I like python. I like python.'
# list1=a.replace(',','').replace('.','')
# list2=list1.split(' ')
# for i in list2:
#     d[i] = list2.count(i)
# print(d)
#实现100-200里面所有的质数字,打印这些质数并且求出个数
# a=[]
# for i in range(100,201):
#     b=0
#     for x in range(2,i-1):
#         if i%x==0:
#             b+=1
#     if b==0:
#         a.append(i)
# print(a)
# print(len(a))

# a=[]
# for i in range(100,201):
#     b=0
#     for j in range(2,i-1):
#         if i % j==0:
#             b+=1
#     if b==0:
#         a.append(i)
# print('100-200的质数有',a)
# print('质数共有',len(a))

#关于异常的讲解，老师代码
#try:
#    print("请输入一个数字：")
#    user=input()
#    print(int(user)+1)
#except ValueError:
#    print("只能输入数字！")
#except (IOError,Valueerror):
#    print("文件夹错误")
#except Exception:
#    print("WRONG!")
#except ValueError:
#    print("111")
#print("hello world")
#IOError
#KeyError
#ValueError
#Exception(所有异常的基类)
# try:
#     print("a")
#     print("b")
#     raise(ValueError)
#     print("c")
# except:
#     print("我想在这里先停下来")
# else:#没有发生异常时执行的代码
#     print("这里没有发生异常哦")
# finally:#无论是否发生异常都一定要执行的语句！
#     print("你们要好好学习！")
# print("hallo world")

#电脑随机生成1~100随机数，用户输入一个数字，
# 电脑提示用户大或者小，猜错，继续提示；猜对，则程序终止。
# import random
# num0=random.randint(1,101)
# print(num0)
# print('请输入一个数字')
# num=int(input())
# while True:
#     if num>num0:
#         print('数字大')
#     if num<num0:
#         print("数字小")
#     if num ==num0:
#         print('猜对了')
#         break
#     num=int(input())

#输入一个数a，求1+2!+3!+...+a!的和




