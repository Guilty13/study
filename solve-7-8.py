input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

itxt = list(map(int, input_file.read().split()))

size = int(itxt[0])
values = itxt[2:]

values.sort()

sum = 0

end = True

for i in range(len(values)):
    a = int(values[i])
    if sum + a < size:
        sum += a
    else:
        output_file.write(str(i))
        end = False
        break

if end:
    output_file.write(str(len(values)))

input_file.close()
output_file.close()