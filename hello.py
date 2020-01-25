# print ('hello world!')
#
# a=3
# b=a
# a=a+1
#
# num1=a*b
# num2=99
#
#
# a_list = []
# a_list.append(1)
# b_list = [1,2,3]
#
# a_list.append(b_list)
# print(a_list[0])
# print(a_list[1])
# print(a_list[1][2])

# a_dict = {}
# a_dict = {'name':'bob','age':21}
# a_dict['height']=178
# a_dict['country']='korea'
#
# a_dict['gender']='male'
# print(a_dict['gender'])


# people = [{'name':'jingyo','gender':'male','height':185},{'name':'youri','gender':'female','height':165}]
#
# newPerson = {'name':'yeunbok','gender':'male','height':181}
# people.append(newPerson)
#
# print(people[2]['height'])


# def f(x):
#     return 2*x+3
#
# y=f(20)
# print(y)

# def sum_all(a,b,c):
#     return a+b+c
#
# def mul(a,b):
#     return a*b
#
# result=sum_all(1,2,3)+mul(10,10)
# print(result)
#
# def minus(a,b):
#     return a-b
#
# result2 = minus(mul(10,10),sum_all(1,2,3))
# print(result2)

# def oddeven(num):
#     if num%2==0:
#         return True
#     else:
#         return False
#
# def checkbob(name):
#     if name=='bob':
#         return True
#     else:
#         return False
#
# print(checkbob(bob))

#
# def allsum(mylist):
#     sum=0
#     for i in mylist:
#         sum = sum+i
#     return sum
#
# sth_list = [0,1,2,3,4,5,6,7,8,9]
# print(allsum(sth_list))
#
#
# sth_list_2=range(10) # [0,1,2,3,4,5,6,7,8,9]
# print(allsum(sth_list_2))
#
# print(sth_list_2[9])
#
# people = [{'name':'bob','age':20},{'name':'carry','age':38},{'name':'john','age':7}]
#
# # for person in people:
# #     print(person['name'],person['age'])
#
# def get_age(myname):
#     for person in people:
#         if person['name'] == myname:
#             return person['age']
#     return '해당하는 이름이 없습니다'
#
# print(get_age('bob'))
# print(get_age('jingyo'))

#메일주소가 맞는지 판단하기

a='spartacodingclub@gmail.com'

# #채워야하는 함수
# def check_mail(s):
#     return s.find('@')>-1s
#     #find 함수를 통해 찾고자 하는 특정 문자열을 입력하면 반환 값으로 그 문자열의 시작위치가 나온다.
#     #찾는 문자열이 없으면 -1값을 반환
# print(check_mail(a))
# print(a.find('@'))
#
# def get_mails(s):
#     return s.split('@')[1].split('.')[0]
# print(get_mails(a))

# #입력값
# a=['사과','감','감','배','포도','포도','딸기','포도','감','수박','딸기']
#
# def count_list(a_list): #'count_list'라는 함수 선언 (변수:a_list)
#     result={} #변수 result는 딕셔너리 형태임
#     for element in a_list: #
#         if element in result:
#             result[element]+=1
#         else:
#             result[element]=1
#     return result
#
# print(count_list(a))

# import random
#
# def get_lotto():
#     lotto_range = range(1,47)
#     lotto_nums = random.sample(lotto_range,6)
#     return lotto_nums
#
# print(get_lotto())
#

# import requests  # requests 라이브러리 설치 필요
#
# r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
# rjson = r.json()
# print(rjson['RealtimeCityAir']['row'][0]['NO2'])

# import requests # requests 라이브러리 설치 필요
#
# r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
# rjson = r.json()
#
# gus = rjson['RealtimeCityAir']['row']
#
# for gu in gus:
#     print (gu['MSRSTE_NM'], gu['IDEX_MVL'])

import requests # requests 라이브러리 설치 필요

r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
rjson = r.json()

gus = rjson['RealtimeCityAir']['row']

for gu in gus:
    if gu['IDEX_MVL']<100:
        print (gu['MSRSTE_NM'], gu['IDEX_MVL'])