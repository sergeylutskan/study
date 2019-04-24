# find the best pupils in classes and tell "ДА"(YES) if in each class there is a best pupil. Else print "НЕТ" (NO)
# Best pupil is a pupil, who have a grade of 5

KL = int(input())
OTL = []
OTLKL = []
for i in range(KL):
    UCH = int(input())
    OTL = []
    for j in range(UCH):
        student = input().split()
        if student[1] == '5':
            OTL.append(1)
        else:
            OTL.append(0)
    if any(OTL):
        OTLKL.append(1)
if all(OTLKL) and len(OTLKL) != 0:
    print('ДА')
else:
    print('НЕТ')
    
