def split_string(line):
    half_size = int(len(line)/2)
    return line[:half_size], line[half_size:]


def priority_value(first_half, second_half):
    for letter in first_half:
        if second_half.find(letter) != -1:
            same_letter = letter
            break

    return ord(same_letter)-ord('a')+1 if same_letter.islower() else ord(same_letter)-ord('A')+27


def priority_value_lines(line1, line2, line3):
    for letter in line1:
        if line2.find(letter) != -1 and line3.find(letter) != -1:
            same_letter = letter
            break

    return ord(same_letter)-ord('a')+1 if same_letter.islower() else ord(same_letter)-ord('A')+27


f = open('input.txt', 'r')
sum = 0
for line in f:
    first_half, second_half = split_string(line.strip())
    sum += priority_value(first_half, second_half)

print(sum)

# ---------SECOND PART--------------

f.seek(0)
sum = 0
for line in f:
    line1 = line.strip()
    line2 = f.readline().strip()
    line3 = f.readline().strip()
    sum += priority_value_lines(line1, line2, line3)

print(sum)
