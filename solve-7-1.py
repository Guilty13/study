input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

itxt = input_file.read().split()

N = int(itxt[0])
array = []

for i in range(1, N + 1):
    x = int(itxt[i])
    array.append(x)

array.sort()

for i in range(N):
    output_file.write(str(array[i]) + " ")

input_file.close()
output_file.close()
