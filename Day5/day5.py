f=open('input.txt', 'r')
#example
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2

#get the number of stacks
for line in f:
    if len(line)>1 and line[1].isnumeric():
        number_of_stacks=int(line.strip()[-1])
        break

stacks=[[] for i in range(number_of_stacks)]
moves=[]
f.seek(0)
for line in f:
    if len(line)>1 and not line[1].isnumeric():
        if line[0] !='m':
            for i in range(number_of_stacks):
                stacks[i].append(line[4*i+1])
        else:
            moves.append([int(i) for i in line.split() if i.isnumeric()])

for i in range(len(stacks)):
    stacks[i]=list(filter(lambda x: x.strip(), stacks[i]))

stacks_copy=[stack.copy() for stack in stacks]

#solution for the first star
for i in range(len(moves)):
    for j in range(moves[i][0]):
        stacks[moves[i][2]-1].insert(0, stacks[moves[i][1]-1].pop(0))

answer1=""
for stack in stacks:
    answer1+=stack[0]
print(answer1)

#solution for the second star
for i in range(len(moves)):
    for j in range(moves[i][0]):
        stacks_copy[moves[i][2]-1].insert(0, stacks_copy[moves[i][1]-1].pop(moves[i][0]-j-1))

answer2=""
for stack in stacks_copy:
    answer2+=stack[0]
print(answer2)
