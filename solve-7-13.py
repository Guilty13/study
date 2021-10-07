input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

average = {9: 0, 10: 0, 11: 0}
number = {9: 0, 10: 0, 11: 0}

while True:
    itxt = input_file.readline().split()
    if itxt == []:
        break
    klass = int(itxt[2])
    result = float(itxt[3])
    average[klass] = ((average[klass] * number[klass] + result) /
                      (number[klass] + 1))
    number[klass] += 1

for i in average:
    output_file.write(str(average[i]) + ' ')

input_file.close()
output_file.close()