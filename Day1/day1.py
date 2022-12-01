f = open("input.txt", "r")
list_of_elves=[]
sum_of_calories=0
for line in f:
    if bool(line.strip()):
        sum_of_calories+=int(line.strip())
    else:
        list_of_elves.append(sum_of_calories)
        sum_of_calories=0

#solution for the first star     
print(max(list_of_elves))

list_of_elves.sort()
#solution for the second star 
print(list_of_elves[-1]+list_of_elves[-2]+list_of_elves[-3])
