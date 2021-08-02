sentence = str(input())         # 입력 받는 문자열
char = sentence[0]          # 입력 받은 문자열의 첫번째 글자를 의미, 
                            # for문에서 반복될때 첫번째 글자부터 포커스하기위해, 
                            # 추후에 다른 문자로 포커스 될수 있도록 변수로 지정
cnt = 0                        # 출력하기 위한 숫자

for i in range(len(sentence)):    # 입력받은 문자열의 개수만큼 for문을 반복, 글자 하나하나 포커스가 맞춰짐
    if char == sentence[i]:         # 입력받은 문자열의 첫번째 글자와 for문에서 반복될때 포커스되는 문자가 같을때
                                    # 즉, 문자열이 aaaa처럼 첫번째 글자가 마지막까지 연속될때를 의미
        if i != len(sentence)-1:        # i가 0부터 반복되기 때문에 len(sentence)에 -1을 적용,
                                        # 즉, i != len(sentence)-1은 "문장의 마지막이 아닐때"를 의미 
            cnt += 1                # 문장의 마지막이 아니기 때문에 카운트를 세줌(출력x)
        else:                       # 문장의 마지막일 때
            cnt += 1                    
            print(char, end="")         # 첫번째 글자를 그대로 출력해줌
                                        # 이때 숫자와 연속되게 출력될수 있도록 end=''를 붙여줌
            if cnt >= 2:             # 카운트가 2 이상일때만 출력해줌(1일땐 글자만 출력)
                print(cnt, end="")      # 숫자 출력
    elif char != sentence[i]:       # 첫번째 글자와 포커스된 문자가 서로 다를때, 
                                    # 즉, 문자열이 aaac처럼 포커스가 a에서 c로 변하기 전
        if i != len(sentence)-1:        # 문장의 마지막이 아닐때
            print(char, end="")         # 포커스가 a에서 c로 다른 문자로 변하기때문에 변하기 전까지의 글자와
            if cnt >= 2 :
                print(cnt, end="")      # 숫자를 출력 
            char = sentence[i]      # 다른 문자로 새로 변수를 지정 
            cnt = 1                 # 카운트된 숫자도 1로 초기화
        elif i == len(sentence)-1:      # 문장의 마지막일때
            print(char, end="")         
            if cnt >= 2:
                print(cnt, end="")
            char = sentence[i]          # 다른문자로 변하기 전까지의 문자를 출력했기 때문에 
                                        # 출력 다음의 문자를 새로 변수를 지정
            cnt = 1                     # 카운트도 같이 초기화
            print(char, end="")         # 지정된 문자와
            if cnt >= 2:
                print(cnt, end="")      # 숫자를 출력