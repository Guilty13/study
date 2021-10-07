input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

itxt = input_file.read().split()

max = int(itxt[0]) - 1
index = -1

for i in range(len(itxt)):
    a = int(itxt[i])
    if a >= max:
        max = a
        index = i

output_file.write(str(max) + ' ' + str(index))

input_file.close()
output_file.close()
