import random
arrayA = [10, 20, 30, 40, 50, 60, 70, 80, 90] #ukol cislo 1

serazene_pole = sorted(arrayA)
prostredni_hodnota = serazene_pole[len(serazene_pole) // 2]
max = max(arrayA)
min = min(arrayA)
print(min,",",prostredni_hodnota,",",max) #ukol cislo 2

arrayA[6] = 34 # ukol cislo 3

print(arrayA[8]) #ukol cislo 4

print (len(arrayA)) #ukol cislo 5

print(min, ",", max) #ukol cislo 6

arrayB = [7, 17, 6, 55, 25, 65] #ukol cislo 7

print (sum(arrayB)) #ukol cislo 8

print(arrayB[0] + arrayB[5])#ukol cislo 9

random.shuffle (arrayB)
print(arrayB)#bonus