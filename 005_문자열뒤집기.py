# def 문자열뒤집기(문자열):
#     if 문자열 == '':
#         return None
#     else:
#         문자열뒤집기(문자열[1:])
#         print(문자열[0])

# print(문자열뒤집기('kwonhyuk'))


result = ''
for i in 'kwonhyuk':
    result = i + result

print(result)

x = 0
for i in '2231':
    x += int(i)

print(x)
    

def sum(s):
    if s == '':
        return 0
    else:
        return int(s[0]) + int(sum(s[1:]))

print(sum('2231'))
