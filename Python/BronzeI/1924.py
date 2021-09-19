week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
sum=0

m,d = map(int,input().split())

for i in range(1,m): # 1월인 경우
    if i in [1,3,5,7,8,10,12] : sum+=31 #31일인 달
    elif i in [4,6,9,11] : sum+=30 #30일인 달
    elif i==2 : sum+=28   #2월은 28일

sum+=d
print(week[sum%7])
