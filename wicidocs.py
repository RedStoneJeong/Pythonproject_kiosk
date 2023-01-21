"""
#11
samsung = 50000
stock = 10
value = samsung * stock
print(value)

#13~20
s = "hello"
t = "python"
print(s+'!', t)

#type function
a = 128
print(type(a))

num_str = "720"
print(type(num_str))
num_int = int(num_str)
print(type(num_int), num_int+1)

num = 100
tostr = str(num)
print(tostr, type(tostr))

num2 = "15.79"
num_flo = float(num2)
print(num_flo, type(num_flo))

year = "2022"
year2 = int(year)
print(year2, type(year2))

month_cost = 48584
total = month_cost * 36
print(total)
"""

"""
##21~30
letters = 'python' #21
print(letters[0], letters[2])

license_plate = "24가 2210" #22
print(license_plate[-4:])

string = "홀짝홀짝홀짝" #23
print(string[::2])

string = "PYTHON" #24
print(string[::-1])

phone_number = "010-1111-2222" #25
phone_number1 = phone_number.replace("-", " ")
print(phone_number1)

phone_number2 = phone_number.replace("-", "") #26
print(phone_number2)

url = "http://sharebook.kr" #27
url_split = url.split(".")
print(url_split[-1])

lang = 'python' #28 문자열은 수정 불가
lang[0]

string = 'abcdfe2a354a32a' #29 변수에 할당
string = string.replace('a', 'A')
print(string)

string = 'abcd' #30
string.replace('b', 'B') #문자열은 변경할 수 없으니까 변수에 할당 필요
print(string)
"""
"""
##31~40
a = "3"  #31
b = "4"
print(a + b)

print("hi" * 3) #32

print("실행 예: \n","-"*80) #33

t1 = "python"
t2 = "java"
print((t1+" "+t2+" ")*4) #34

name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1)) #35
print("이름: %s 나이: %d" % (name2, age2)) # %s = 문자열 %d = 정수형

print("이름: {} 나이: {}".format(name1, age1)) #36
print("이름: {} 나이: {}".format(name2, age2)) #format() 매서드 사용

print(f"이름: {name1} 나이: {age1}") #37
print(f"이름: {name2} 나이: {age2}") #f-string 이용

상장주식수 = "5,969,782,550" #38
컴마제거 = 상장주식수.replace(",", "")
타입변환 = int(컴마제거)
print(타입변환, type(타입변환))

분기 = "2020/03(E) (IFRS연결)" #39
print(분기[:7])

data = "        삼성전자      "
data1 = data.strip()    #40 strip 메서드
print(data1)
"""
"""
##41~50
ticker = "btc_krw" #41
ticker2= ticker.upper()
print(ticker, ticker2)

ticker = "BTC_KRW"  #42
ticker1 = ticker.lower()
print(ticker, ticker1)

a = 'hello' #43
a1 = a.capitalize()
print(a, a1)

file_name = '보고서.xlsx' #44 끝이 xlsx로 끝나는지 확인
file_name2 = file_name.endswith("xlsx")
print(file_name2)

file_name = "보고서.xlsx" #45
file_name1 = file_name.endswith(("xlsx", "xls"))
print(file_name1)

file_name = "2020_보고서.xlsx" #46
file_name3 = file_name.startswith("2020")
print(file_name3)

a = "hello world" #47
a1 = a.split()
print(a1)

ticker = "btc_krw" #48
ticker1 = ticker.split('_')
print(ticker1)

date = "2020-05-01" #49
date1 = date.split('-')
print(date1)

data = "0392830            " #50
data = data.rstrip()
print(data)
"""
"""
##51~60
movie_rank = ["닥터스트레인지", "스플릿", "럭키"] #51
print(movie_rank)

movie_rank.append("배트맨")
print(movie_rank)#52

movie_rank = ["닥터스트레인지", "슈퍼맨", "스플릿", "럭키", "배트맨"] #54
del movie_rank[3]
print(movie_rank)

del movie_rank[2] #55
del movie_rank[2]
print(movie_rank)

lang1 = ["C", "C++", "JAVA"] #56
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

nums = [1, 2, 3, 4, 5, 6, 7] #57
nums1 = max(nums)
nums2 = min(nums)
print(nums1, nums2)

nums = [1, 2, 3, 4, 5] #58
nums_sum = sum(nums)
print(nums_sum)

cook = ["피자", "김밥", "만두", " 양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook)) #59

nums = [1, 2, 3, 4, 5] #60
average = sum(nums) / len(nums)
print(average)
"""

##61~70
price = ['20190720', 100, 130, 140, 150, 160, 170] #61
print(price[1:])

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #62
print(nums[::2])

print(nums[1::2]) #63

nums = [1, 2, 3, 4, 5] #64
print(nums[::-1])

interest = ['삼성전자', 'LG전자', 'Naver'] #65
print(interest[0], interest[2])

interest.append('SK하이닉스')
interest.append('미래에셋대우')

print(" ".join(interest)) #66

print("/".join(interest)) #67

print("\n".join(interest)) #68

string = '삼성전자/LG전자/Naver' #69
interest = string.split("/")
print(interest)

data = [2, 4, 3, 1, 5, 10, 9] #70
data.sort()
print(data)



