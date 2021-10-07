input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

max = {9: 0, 10: 0, 11: 0}
number = {9: 0, 10: 0, 11: 0}

while True:
    itxt = input_file.readline().split()
    if itxt == []:
        break
    if max[int(itxt[2])] < int(itxt[3]):
        max[int(itxt[2])] = int(itxt[3])
        number[int(itxt[2])] = 1
    elif max[int(itxt[2])] == int(itxt[3]):
        number[int(itxt[2])] += 1

for i in max:
    output_file.write(str(number[i]) + ' ')

input_file.close()
output_file.close()
