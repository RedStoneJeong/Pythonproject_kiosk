## 5/28
#카페 메뉴 5개 주문 받기(여러개 가능) > 주문이 끝나면 while 끝 > 주문 목록이 list에 저장
#계산 > 1잔 기본가격 2잔 10%할인, 3잔 이상 20% 할인

myorder_list = []

menu_list ={'1.아메리카노':4500, '2.카페라떼':5000, '3.아이스티':3000, '4.카라멜마끼아또':6000, '5.바닐라라떼':7000}
menu_list_name = list(menu_list.keys())
print('카페 오신걸 환영합니다 주문해주세요 ?')
print(menu_list_name)

#주문
while True:
    order = int(input("주문 번호: "))
    if order == 9:
        break
    elif 0 < order < 6 :
        myorder_list.append(menu_list_name[order-1])

#계산
if len(myorder_list) == 1:
    price = menu_list[myorder_list[0]]
    print('총 계산 금액: ', price)

elif len(myorder_list) == 2:
    price = 0
    price += menu_list[myorder_list[0]]
    price += menu_list[myorder_list[1]]
    print('총 계산 금액: ', price * 0.9)

elif len(myorder_list) >= 3:
    price = 0
    for i in range(len(myorder_list)):
        price += menu_list[myorder_list[i]]
    print('총 계산 금액: ', price * 0.8)




