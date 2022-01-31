arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf') # 파이썬에서 가장큰값을 저장(가~~~장 큰값: 거의 무한대값)
# arrMin = arr[0]  # 이땐 for문의 range값을 (1, len(arr))로 해야겠지?
for i in arr:
    if arrMin < i:
        arrMin = i
print(arrMin)
