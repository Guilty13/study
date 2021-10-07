input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

itxt = list(map(int, input_file.read().split()))

size = itxt[0]
values = itxt[1:]

values.sort()
counter = 0
last = size - 3

for i in values:
    if last + 3 <= i:
        last = i
        counter += 1

output_file.write(str(counter))

input_file.close()
output_file.close()