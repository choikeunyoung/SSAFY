money = [500, 100, 50, 10]
TOTAL = 780
cnt = 0

for i in money:
    cnt += (TOTAL//i)
    TOTAL -= (TOTAL//i * i)
print(cnt) # 