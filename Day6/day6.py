def start_of_marker(input, number_of_characters):
    for i in range(0, len(input)-number_of_characters+1):
        if len(set(input[i:i+number_of_characters]))==number_of_characters:
            break
    return i+number_of_characters

f=open('input.txt', 'r')
line=f.readline()
#solution for the first star
print(start_of_marker(line,4))
#solution for the second star
print(start_of_marker(line,14))
