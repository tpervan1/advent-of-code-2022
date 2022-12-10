def update(cycle, row, position,X, crt,sum):
    if(cycle==20 or cycle==60 or cycle==100 or cycle==140 or cycle==180 or cycle==220):
        sum+=cycle*X
    if cycle==41 or cycle==81 or cycle==121 or cycle==161 or cycle==201:
        row+=1
    if position in [row*40+X-1, row*40+X, row*40+X+1]:
        crt[position]='#'
    position+=1

    return row,position,sum
    
f=open('input.txt','r')
X=1
cycle=sum=row=position=0
crt=['.']*240

for line in f:
    if line.strip().split(' ')[0]=='noop':
        cycle+=1
        row, position,sum=update(cycle, row, position, X, crt,sum)

    else:
        cycle+=1
        row, position,sum=update(cycle, row, position, X, crt,sum)
        cycle+=1
        row, position,sum=update(cycle, row, position, X, crt,sum)
        X+=int(line.strip().split(' ')[1])

#solution for the first star
print(sum)
#solution for the second star
print(''.join(crt[0:40]))
print(''.join(crt[40:80]))
print(''.join(crt[80:120]))
print(''.join(crt[120:160]))
print(''.join(crt[160:200]))
print(''.join(crt[200:240]))
