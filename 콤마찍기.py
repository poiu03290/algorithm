def comma(s):
    if len(s) < 3:
        return s
    else:
        return comma(s[:len(s)-3]) + ',' + s[len(s)-3:]

print(comma('100000000'))