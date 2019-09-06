# # print("hh")
# # # print("hahaha")
# # #
# # #
# # # name="代双"
# # # age=20
# # # tizhong=60.5
# # # print("姓名是:%s,年龄是:%d,体重是:%r"%(name,age,tizhong))
# # #
# # # counter = 100  # 整型变量
# # # miles = 1000.0  # 浮点型变量
# # # name = "runoob"  # 字符串
# # # print(counter)
# # # print(miles)
# # # print(name)
# # #
# # # #多个变量一起赋值（同类型）
# # # a = b = c = 1
# # # print(a)
# # # print(b)
# # # print(c)
# # #
# # # #多个变量一起赋值（不同类型）
# # # a, b, c = 1, 2, "aa"
# # # print(a)
# # # print(b)
# # # print(c)
# # #
# # # '''
# # # int（有符号整型）
# # # long（长整型[也可以代表八进制和十六进制]）
# # # float（浮点型）
# # # complex（复数）
# # # string(字符串)
# # # '''
# # # str = 'Hello 小阿代!'
# # # print(str)
# # # print(str[0])
# # # print(str[2:5])
# # # print(str*2)
# # # print(str+"hahaha")
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # # #数字  字符串  列表  元组  字典  集合 （三）
# # # #数字
# # # a=23
# # # b=12.7#复数  a+bj
# # # c=5+6j
# # # print(c)
# # # d=-9
# # # print(type(a))
# # # print(type(b))
# # # print(type(c))
# # # print(type(d))
# # # #字符串
# # # s='ab'
# # # s1="abcdfertyuio"
# # # #切片 截取
# # # print(s1[2])
# # # print(s1[-1])
# # # print(s1[4])
# # # print(s1[1:4])
# # # print(s1[1:])
# # # print(s1[:3])
# # # print(s1[1::2])
# # # print(s1[::-1])#字符串的反转
# # # s1="Wqert Eutry      Eew5rtd Ghj"
# # # print(s1.isdigit())#判断字符串是否是纯数字
# # # print(s1.isdecimal())#
# # # print(s1.isalnum())#数字和字母  纯数字   纯字母
# # # print(s1.isalpha())#判断是否是纯字母
# # # print(s1.islower())#判断字母是小写
# # # print(s1.isupper())#判断字母是大写
# # # print(s1.isspace())#判断是否是空格
# # # print(s1.istitle())#每个单词首字母大写 就是标题
# # # s2="wearTaiua"
# # # print(len(s1))#取字符串的长度
# # # print(s2.capitalize())
# # # print(s2.find("a"))
# # # print(s2.find("a",6))
# # # print(s2.find("a",3,6))
# # # print(s2.find("m"))#字符串中没有该字母 返回-1
# # # print("######################")
# # # print(s2.rfind("a"))
# # # print(s2.rfind("a",6))
# # # print(s2.rfind("a",2,6))
# # #
# # # print(s2.index("a"))
# # # print(s2.index("a",6))
# # # print(s2.index("a",3,6))
# # # print(s2.rindex("a"))
# # # print(s2.rindex("a",6))
# # # print(s2.rindex("a",3,6))
# # # #print(s2.index("m"))#字符串中没有该字母 报错
# # #
# # # s="hauya weawak"
# # # print(s.startswith("h"))
# # # print(s.startswith("hu"))
# # # print(s.startswith("h",3))
# # # print(s.startswith("h",3,7))
# # # print("########################")
# # # print(s.endswith("k"))
# # # print(s.endswith("k",3))
# # # print(s.endswith("a",3,7))
# # # #分隔
# # # s="hRuyERTYUIea Yak"
# # # print(s.split("a"))#返回列表
# # # print(s.split())#默认以空格分隔
# # # print(s.split("a",2))#2代表最多分隔2个a
# # # #print(s.splitlines())
# # # print(s.rsplit("a"))
# # # print(s.rsplit("a",2))
# # # #连接 join
# # # print("#".join(s))
# # # #统计 该字符串有多少个字母
# # # print(s.count("a"))
# # # print(s.count("a",3))
# # # print(s.count("a",3,8))
# # # #大小写转换
# # # print(s.swapcase())
# # # #替换
# s=" hello word "
# print(s.replace("o","hh"))
#  print(s.replace("a","W",2))
 # # #去空格
# # # s=" ha u yE "
# # # print(len(s))
# # # print(s.strip())
# # # print(len(s.strip()))
# # # print(s.rstrip())
# # # print(len(s.rstrip()))
# # # print(s.lstrip())
# # # print(len(s.lstrip()))
# # # print(s.replace(" ",""))
# # #
# # #
# # #
# # #
# # #
# x = "abc1z"
# print(x="abc2z")

# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # # #s="fgjktyu"
# # # str1 = 'ab c\n\nde fg\rkl\r\n'
# # # print(str1.splitlines())
# # # str2 = 'ab c\n\nde fg\rkl\r\n'
# # # print(str2.splitlines(True))
# # # s="d:\new\table\aa.txt"
# # # print(s)
# # # s="d:\\new\\table\\aa.txt"
# # # print(s)
# # # s=r"d:\new\table\aa.txt"#raw
# # # print(s)
# # # s=R"d:\new\table\aa.txt"#raw
# # # print(s)
# # # s="fgjktyu"
# # # print(s.ljust(20,'a'))
# # # print(s.rjust(20))#默认空格填充
# # # print(s.center(20,'a'))
# # # print(s.zfill(20))
# # # s1="fgjktyu"
# # # print(s+s1)
# # # print(s1*3)
# # # print("f" in s1)#成员运算符
# # # print("f" not in s1)#成员运算符
# # # for x in s1:#迭代输出
# # #     print(x)
# # # #列表 list   str
# # # list1=[]#定义空列表
# list1=[1,2,3,4,5]
# # # #访问列表的元素切片
# # # print(list1[0])
# # # print(list1[3])
# # # print(list1[2:4])
# # # print(list1[2:])
# # # print(list1[::2])
# print(list1[::-1])
# # # #新增元素
# # # list1.append("asd")#追加的元素在最后面  且每次只能追加一个
# # # print(list1)
# # # list1.insert(2,"ss")
# # # print(list1)
# # # #修改
# # # list1[2]=12
# # # print(list1)
# # # #删除
# # # del  list1[2]
# # # print(list1)
# # # list1.remove("aa")#删除匹配到的第一个元素
# # # print(list1)
# # # # del  list1#删除列表的定义
# # # # print(list1)
# # # a=list1.pop()#默认删除最后一个元素并返回
# # # print(a)
# # # print(list1)
# # # a=list1.pop(3)#
# # # print(a)
# # # print(list1)
# # # list2=[12,34,True,"aa",5.78,'we',34,'ty']
# # # list2[2:4]="23"
# # # print(list2)
# # #
# # #
# # # import copy
# # # k1=['qw',12,89,'qw']
# # # k2=['rt',67]
# # # k1.extend(k2)
# # # print(k1)
# # # print(k2)
# # # k2.clear()
# # # print(k2)
# # # print(k1.index('qw'))
# # # print(k1.index('qw',2))
# # # print(k1.index('qw',2,4))
# # # k1=[12,89,7]
# # # k1.sort()
# # # print(k1)
# # # k1.sort(reverse=True)
# # # print(k1)
# # # k1=['as','tyW','Tr','tyw']
# # # k1.sort()
# # # print(k1)
# # # k1.sort(reverse=True)
# # # print(k1)
# # #
# # # k1=[12,56,8,66,2]
# # # k3=sorted(k1)
# # # print(k1)
# # # print(k3)
# # # print(max(k1))
# # # print(min(k1))
# # #
# # # f=["qw",78,'ty',90,[78,"yu",88],'op']
# # # print(f[4][2])
# # # h2=[23,56,'a']
# # # h=[23,56,[12,34,'tt'],'a']
# # # m1=h
# # # print(m1,h)
# # # m2=h[::]
# # # print(m2,h)
# # # m3=h.copy()
# # # print(m3,h)
# # # m4=copy.deepcopy(h)
# # # print(m4,h)
# # # print("###########")
# # # h[2][1]=88
# # # print(m1,h)
# # # print(m2,h)
# # # print(m3,h)
# # # print(m4,h)
# # # k1=['as','tyw','Tr','tyw']
# # # k2=['23',56]
# # #
# # # print(k1.count("tyw"))
# # # print("_".join(k1))
# # # print(len(k1))
# # # print(k1+k2)
# # # print(k2*3)
# # # print('as' in k1)
# # # print('as' not in k1)
# # # for x in k1:
# # #     print(x)
#
#
# t=(12,45,'we',45,90)#元组
# #切片 截取
# print(t[2])
# print(t[2:4])
# print(t[::-1])
# t1=(23,9)
# print(t+t1)
# print(t1*3)
# print("we" in t)
# print("we" not in t)
# del t
# for x  in t1:
#     print(x,end=" ")
# print(type(t1))
# #字典 dict
# d={}#空字典
# d1={'name':'zs','age':21,'price':28}
# #访问
# print(d1["name"])
# #新增
# d1["num"]=18
# print(d1)
# #修改
# d1["num"]=19
# print(d1)
# #删除
# del d1["num"]#删除某一个键
# print(d1)
# # d1.clear()#清空字典的内容
# # print(d1)
# # del  d1#删除字典的定义
# # print(d1)
# print(d1.pop("price"))#删除键值对并返回
# print(d1)
# d1={'name':'zs','age':21,'price':28}
# print(d1.keys())#获取所有的键
# print(d1.values())#获取所有的值
# print(d1.items())#获取所有的键值对
# for k,v  in d1.items():
#     print(k,v)
# # d1.fromkeys()两个参数，一个是seq默认值为None，一个是赋值，替换值
# # d1.update(d2)把dict2里面的键值对添加到d1字典中
# # d1.setdefault()setdefault() 方法和 get()方法 类似, 如果键不已经存在于字典中，将会添加键并将值设为默认值。
# # #集合
# h=input("请输入名字")
# print('名字是%s'%h)
#
#
#
#
# a='3456GJ'
# print(type(a))
# print(isinstance(a,dict))
# c=123
# d=str(c)#把变量c转成str类型
# print(d)
# print(type(d))
# c='abc'
# d=list(c)#把变量str转成list类型
# print(d)
# print(type(d))
# d=tuple(c)#把变量str转成tuple类型
# print(d)
# print(type(d))
# # d=int(input("请输入数字"))
# # f=input("请输入数字")
# # print(d+int(f))
# #运算符表达式
# #算数运算符
# print(3+9)
# print(9-7)
# print(4*5)
# print(9/4)#整除
# print(9//2)#取商的整数部分
# print(9%2)
# print("#############")
# print(3**4)
# #比较运算符
# print(8>2)
# print(8<2)
# print(8>=2)
# print(8<=2)
# print(8!=2)
# print(5==6)
# #赋值运算符
# a=8
# a+=4
# a*=2
# a/=6
# a%=3
# a**=5
# #逻辑运算符  and (&&) or(||)  not(!)
# print(1<5 and 7>6)
# print(1<5 or 7<6)
# print(not 1<5 )
# #成员运算符
# #in   not  in
# #身份运算符 123  '123'
# print(id(123))
# print(id('123'))
# print(123 is '123')
# print(123 is not '123')
# import random
# b=random.randint(1,3)
# print(b)
# d=int(input("请输入数字"))
# if d<b:
#     print('你猜小了')
# elif d>b:
#     print('你猜大了')
# elif d==b:
#     print('你猜对了')

# d=int(input("请输入年份"))
# if d%4 and d//4:
#     print("这是闰年")
# else:
#     print("这是平年")
# i=1
# while i<51:
#     i+=1
#     if i%2==0:
#         print(i)


# a=1
# b=0
# while a<51:
#     a+=1
#     if a%2==1:
#         print(a)
# #         b+=a
# # print(b)

# i=1
# a=0
# while i<51:
#     a += i
#     i+=2
# print(a)



# score=100
# if  score>90:
#     print("1")
# elif score>80:
#     print("2")
# elif score>70:
#     print("3")
# elif score>60:
#     print('4')
# else:
#     print('5')
# stime=8
# sex="男"
# if stime<10:
#     print("恭喜进入决赛")
#     if sex=="男":
#         print("进入男子组")
#     else:
#         print("进入女子组")
# else:
#     print("被淘汰")
# #猜大小  自己写一个数字  系统随机生成一个 1-20的数字
# print(isinstance("sss",list))
# i=1
# while i<11:
#     print(i)
#     i+=1#i=i+1
# else:#当表达式为假时执行
#     print(i)
# # k=(12,34,'454',56)
# # for x in k:
# #     print(x)
# print("##############")
# for x in range(1,11):
#     if x%2==0:
#         print(x)
#     #print(x)
# print(list(range(1,11,2)))
# for x in range(11):
#     print(x)
# print("############")
# for x in range(11):
#     if x%2==0:
#         #continue
#         break
#     print(x)


# for i in range(100,1000):
#     s=str(i)
#     if int(s[0])**3+int(s[1])**3+int(s[2])**3==i:
#         print(i)
#
# i=1
# l=1
# while i<=5:
#     l*=i
#     i+=1
#     print(l)

