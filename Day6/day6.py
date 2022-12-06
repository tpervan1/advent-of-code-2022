f=open('input.txt', 'r')
for line in f:
    for i in range(0, len(line)-3):
        if len(set(line[i:i+4]))==4:
            break
#Solution for the first star
print(i+4)

f.seek(0)
for line in f:
    for i in range(0, len(line)-13):
        if len(set(line[i:i+14]))==14:
            break
#Solution for the second star
print(i+14)
