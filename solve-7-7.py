input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

itxt = input_file.read().split()

keys = []
size = int(itxt[0])

for i in range(size):
    keys.append(int(itxt[i + 1]))

for i in range(int(itxt[size + 1])):
    a = int(itxt[i + size + 2])
    keys[a - 1] -= 1

for i in keys:
    if i < 0:
        output_file.write('YES' + '\n')
    else:
        output_file.write('NO' + '\n')

input_file.close()
output_file.close()