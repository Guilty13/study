input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

itxt = input_file.read().split()

x = int(itxt[-1])
answer = int(itxt[1])

for i in range(1, int(itxt[0]) + 1):
    if abs(x - answer) > abs(x - int(itxt[i])):
        answer = int(itxt[i])


output_file.write(str(answer))

input_file.close()
output_file.close()
