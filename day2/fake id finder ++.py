fakeids=0
with open ('ranges') as file:
    ranges=file.read().split(',')
for rang in ranges:
    start, end = rang.split('-')
    start=int(start)
    end=int(end)
    for ids in range (start,end+1):
        id_string=(str(ids))
        lenght=(len(str(ids)))
        for patternlenght in range (1,lenght//2+1 ):
            if lenght % patternlenght != 0:
                continue
            patternamount = lenght // patternlenght
            patterns=[]
            for i in range (patternamount):
                start= i*patternlenght
                end= start+patternlenght
                pattern= id_string[start:end]
                patterns.append(pattern)
            if all(item == patterns[0] for item in patterns):
                    fakeids+=ids
                    break
print(fakeids)

                

                


