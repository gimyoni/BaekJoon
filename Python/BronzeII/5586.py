str = input()
JOI = 0
IOI = 0

for i in range(len(str)-2):
    answer = str[i] + str[i+1] + str[i+2]
    
    if answer == 'JOI':
        JOI += 1
    if answer == 'IOI':
        IOI += 1
        
print(JOI)
print(IOI)
