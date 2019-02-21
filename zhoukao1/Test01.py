#用python语句判断所输入的手机号，是否正确
#要对手机号的号段进行判断，号段任意给出6个作为模拟号段即可.
# 判断手机号码是否是由数字组成的
print("请输入手机号：")
phone=input()
num=['132','133','134','135','136','151']#模拟号段
b = 0
try:
    num2 = int(phone)
except ValueError:
    b+=1
    print("请输入数字形式的手机号！")

if b == 0:
    if phone[:3] in num and len(phone)==11:    #判断与模拟号段是否相等
        print("输入正确")

    else:
        print("请输入正确的手机号")


