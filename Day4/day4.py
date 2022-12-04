def split_into_numbers(string):
    return int(string.split('-')[0]), int(string.split('-')[1])

f = open('input.txt', 'r')
sum1=0
sum2=0
number_of_lines=0

for line in f:
    number_of_lines+=1
    line=line.strip()
    first_pair, second_pair=line.split(',')
    a,b=split_into_numbers(first_pair)
    x,y=split_into_numbers(second_pair)
    #first star
    #check if one assignment(pair) fully contains the other one
    if abs(a-b)>=abs(x-y):
        sum1+=(x>=a and y<=b)
    else:
        sum1+=(a>=x and b<=y)
    
    #second star
    #check if assignments(pairs) don't overlap
    if b<x or y<a:
        sum2+=1

print(sum1)
#pairs that overlap = all pairs - pairs that don't overlap
print(number_of_lines-sum2)
