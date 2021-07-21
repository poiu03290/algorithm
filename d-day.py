from datetime import datetime
import math

today = datetime.today().strftime("%Y%m%d")
input = input()
today_Y = int(today[0:4])
input_Y = int(input[0:4])
today_M = int(today[4:6])
input_M = int(input[4:6])
today_D = int(today[6:8])
input_D = int(input[6:8])
difference_large = (input_Y - today_Y) - 1
difference_small = (today_Y - input_Y) - 1
leapYear = math.floor(abs((input_Y - 2020)) / 4)
date = 0

if today_Y == input_Y:   # 연도가 같을때
    if today_M < input_M:
        for i in range(today_M, input_M):
            if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i ==  10 or i == 12:
                date += 31
            elif i == 4 or i == 6 or i == 9 or i == 11:
                date += 30
            elif i == 2:
                date += 28
        date = date + input_D - today_D
        print("D-{0}".format(date))


    elif today_M > input_M:
        for i in range(input_M, today_M):
            if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i ==  10 or i == 12:
                date += 31
            elif i == 4 or i == 6 or i == 9 or i == 11:
                date += 30
            elif i == 2:
                date += 28
        date = date + today_D - input_D
        print("D+{0}".format(date))

    elif today_M == input_M and today_D < input_D:
        date = date + input_D - today_D
        print("D-{0}".format(date))
    
    elif today_M == input_M and today_D > input_D:
        date = date + today_D - input_D
        print("D+{0}".format(date))

    elif today_M == input_M and today_D == input_D:
        print("D-Day!!")


elif today_Y < input_Y and difference_large == 0:  # 입력연도가 클때(2022년)
    for i in range(today_M, 13):
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i ==  10 or i == 12:
            date += 31
        elif i == 4 or i == 6 or i == 9 or i == 11:
            date += 30
        elif i == 2:
            date += 28
    for i in range(1, input_M):
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i ==  10 or i == 12:
            date += 31
        elif i == 4 or i == 6 or i == 9 or i == 11:
            date += 30
        elif i == 2:
            date += 28  
    date = date + input_D - today_D
    print("D-{0}".format(date))

 # 입력연도가 크고, 2년이상 차이날때(2023~)
elif input_Y > today_Y and difference_large >= 1:
    for i in range(today_M, 13):
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i ==  10 or i == 12:
            date += 31
        elif i == 4 or i == 6 or i == 9 or i == 11:
            date += 30
        elif i == 2:
            date += 28
    for i in range(1, input_M):
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i ==  10 or i == 12:
            date += 31
        elif i == 4 or i == 6 or i == 9 or i == 11:
            date += 30
        elif i == 2:
            date += 28  
    for i in range(leapYear):
        if (True):
            date += 1
    date = (date + input_D - today_D) + (365 * difference_large)
    print("D-{0}".format(date))

# 입력연도가 작을때(2020년)
elif input_Y < today_Y and difference_small == 0: 
    for i in range(input_M, 13):
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i ==  10 or i == 12:
            date += 31
        elif i == 4 or i == 6 or i == 9 or i == 11:
            date += 30
        elif i == 2:
            date += 28
    for i in range(1, today_M):
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i ==  10 or i == 12:
            date += 31
        elif i == 4 or i == 6 or i == 9 or i == 11:
            date += 30
        elif i == 2:
            date += 28  
    date = date + today_D - input_D
    print("D+{0}".format(date))

# 입력연도가 작고, 2년이상 차이날때(2019~)
elif input_Y < today_Y and difference_small >= 1:
    for i in range(input_M, 13):
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i ==  10 or i == 12:
            date += 31
        elif i == 4 or i == 6 or i == 9 or i == 11:
            date += 30
        elif i == 2:
            date += 28
    for i in range(1, today_M):
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i ==  10 or i == 12:
            date += 31
        elif i == 4 or i == 6 or i == 9 or i == 11:
            date += 30
        elif i == 2:
            date += 28 
    for i in range(leapYear):
        if (True):
            date += 1
    date = (date + today_D - input_D) + (365 * difference_small) + 1
    print("D+{0}".format(date))
    