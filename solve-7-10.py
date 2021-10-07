input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

itxt = input_file.read().split()

size = int(itxt[0])
values = list(map(int, itxt[2::2]))
names = {}

for i in range(size):
    names[values[i]] = itxt[2*i + 1]

values.sort(reverse=True)

for i in values:
    output_file.write(names[i] + '\n')

input_file.close()
output_file.close()