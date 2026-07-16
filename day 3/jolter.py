joltage=0
with open ('banks') as file:
    banks= file.read().splitlines()
    for batteries in banks:
        biggest1=-1
        biggest2=-1
        biggest1position=-1 
        for position, battery in enumerate(batteries):
            if int(battery) > biggest1 and position != len(batteries)-1:
                biggest1 = int(battery)
                biggest1position=position       
        for position, battery in enumerate(batteries):
            if int(battery)>biggest2 and position> biggest1position:
                biggest2=int(battery)
        joltage+=(biggest1*10) + biggest2
print(joltage)
    