f = open("input.txt", "r")
# rows represent opponent and columns represent player
# there are 3 rows and columns for rock, paper ans scissors, so values in matrix are points player gets for every possible combination
outcome_points1 = [[3, 6, 0], [0, 3, 6], [6, 0, 3]]

#rows represent rock, paper and scissors, while columns represent loss, draw and win
#each value represents shape - 1,2 and 3 for rock, paper and scissors
shape_points2 = [[3, 1, 2], [1, 2, 3], [2, 3, 1]]

shape_points1 = [1, 2, 3]
outcome_points2 = [0, 3, 6]

sum,sum1=0,0

for line in f:
    #for character A-C and X-Z get indexes for matrix
    index1, index2 = (lambda char1, char2: [ord(
        char1)-ord('A'), ord(char2)-ord('X')])(line[0], line[2])
    sum += outcome_points1[index1][index2] + shape_points1[index2]
    sum1 += shape_points2[index1][index2] + outcome_points2[index2]

#solution for the first star
print(sum)
#solution for the second star
print(sum1)
