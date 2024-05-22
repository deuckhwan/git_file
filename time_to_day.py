import datetime
import pandas as pd

bus_num = int(input("순번을 입력하세요:")) # 순번 입력(input리스트 형을 int형으로 변환)
month_end = int(input("출력 일짜 입력:")) # 총 출력 할 일수 입력  30 * N = N
order = 0 # 순서 번호
today = datetime.date.today() # 날짜 출력
days = ['월', '화', '수', '목', '금', '토', '일'] # 요일 출력
r = datetime.datetime.today().weekday() # 날짜 변환
data =[] # 순번 리스트 저장

print(f'[ {today} ] [ {days[r]} ] ({bus_num})   오전[ ] / 휴무[ ] / 오후[ ]')
print(f'[ {today} ] [ {days[r]} ] ({bus_num})   오전[ ] / 휴무[ ] / 오후[ ]')
today += datetime.timedelta(+1)
r += 1

while True:
    bus_num += 7 # 7칸씩 증가
    if bus_num > 0 and bus_num <= 8 or bus_num > 18 and bus_num <= 30: # 1번에서 8번사이 출력 19번에서 30번 사이 출력
        order += 1
        print(f'[ {today} ] [ {days[r]} ] ({bus_num})   오전[ ] / 휴무[ ] / 오후[ ]')
        today += datetime.timedelta(+1)
        r += 1
        for i in range(month_end):
            if r >= 7:
                r -= 7
        data.append([today, days[r], bus_num, "오전[ ] / 휴무[ ] / 오후[ ]"])
    elif bus_num > 8  and bus_num < 19: # 9번에서 18번 사이 진입시 10칸 더함
        order += 1
        bus_num += 10
        print(f'[ {today} ] [ {days[r]} ] ({bus_num})   오전[ ] / 휴무[ ] / 오후[ ]')
        today += datetime.timedelta(+1)
        r += 1
        for i in range(month_end):
            if r >= 7:
                r -= 7
        data.append([today, days[r], bus_num, "오전[ ] / 휴무[ ] / 오후[ ]"])
    elif bus_num > 30 : # 30번 이상 일때 -30 빼줌
        bus_num -= 30
        order += 1
        print(f'[ {today} ] [ {days[r]} ] ({bus_num})    오전[ ] / 휴무[ ] / 오후[ ]')
        today += datetime.timedelta(+1)
        r += 1
        for i in range(month_end):
            if r >= 7:
                r -= 7
        data.append([today, days[r], bus_num, "오전[ ] / 휴무[ ] / 오후[ ]"])
    if order > month_end:
        break
    df = pd.DataFrame(data, columns=['날짜', '요일', '순번', '오전[ ] / 휴무[ ] / 오후[ ]']) # 2차원 리스트 정렬
    df.to_excel("115-1_1894.xlsx", index= False) # xcel 저장 openpyxl 패키지 설치
    # elif num >= 41: 10칸씩 이동식 40번 이상 일때 빼줌
    #     num -= 1

    #     continue 
    # 추가된 부분임


