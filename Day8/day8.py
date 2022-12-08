def surrounding_rows_and_columns(list,i,j):
    left=list[i][0:j]
    right=list[i][j+1:]
    top=[row[j] for k,row in enumerate(list) if k<i]
    bottom=[row[j] for k,row in enumerate(list) if k>i]
    return left,right,top,bottom

def check_visibility(i,j,list):
    left,right,top,bottom=surrounding_rows_and_columns(list,i,j)
    return list[i][j]>max(left) or list[i][j]>max(right) or list[i][j]>max(top) or list[i][j]>max(bottom) 

def scenic_score(i,j,list):
    left,right,top,bottom=surrounding_rows_and_columns(list,i,j)
    left.reverse()
    top.reverse()
    product=1
    for k in [left,right,top, bottom]:
        sum=0
        for l in k:
            sum+=1
            if list[i][j]<=l:
                break
        product*=sum
    return product
        

f=open('input.txt', 'r')
x,y=[],[]
 
for line in f:
    x.append([int(number) for number in line.strip()])

sum=2*len(x)+2*len(x[0])-4
for i in range(1,len(x)-1):
    for j in range(1, len(x[0])-1):
        sum+=int(check_visibility(i,j,x))
        y.append(scenic_score(i,j,x))

#solution for the first star
print(sum)
#solution for the second star
print(max(y))
