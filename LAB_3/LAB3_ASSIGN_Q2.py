import random
def has_duplicate(l1):
    for i in range(len(l1)-1):
        for j in range(i+1,len(l1)):
            if l1[i] == l1[j]:
                return True
    return False

count=0
for i in range(1000): 
    birthdays=[]
    for x in range(23):
        birthdays.append(str(random.randint(1,30))+'/'+str(random.randint(1,12))+'/'+str(random.randint(1990,1996)))
    if has_duplicate(birthdays):
        count+=1

print("If if take 1000 samples of 23 student attendance.Then the Prbability of getting the duplicate birthdays in sample is")
print('Probability::',count/1000)
