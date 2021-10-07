input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

itxt = input_file.read().split()

max_1 = max(int(itxt[0]), int(itxt[1]), int(itxt[2]))
max_3 = min(int(itxt[0]), int(itxt[1]), int(itxt[2]))
max_2 = int(itxt[0]) + int(itxt[1]) + int(itxt[2]) - max_1 - max_3
min_1 = min(int(itxt[0]), int(itxt[1]), int(itxt[2]))
min_2 = max_2

for i in range(3, len(itxt)):
    if int(itxt[i]) > max_1:
        max_3 = max_2
        max_2 = max_1
        max_1 = int(itxt[i])
    elif int(itxt[i]) > max_2:
        max_3 = max_2
        max_2 = int(itxt[i])
    elif int(itxt[i]) > max_2:
        max_3 = int(itxt[i])
    if int(itxt[i]) < min_1:
        min_2 = min_1
        min_1 = int(itxt[i])
    elif int(itxt[i]) < min_2:
        min_2 = int(itxt[i])

if max_1 * max_2 * max_3 > min_1 * min_2 * max_1:
    output_file.write(str(max_2) + ' ' + str(max_1) + ' ' + str(max_3))
else:
    output_file.write(str(min_1) + ' ' + str(min_2) + ' ' + str(max_1))

input_file.close()
output_file.close()
