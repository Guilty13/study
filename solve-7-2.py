input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

itxt = input_file.read().split()

now = int(itxt[0]) - 1
check = True

for i in itxt:
    if now < int(i):
        now = int(i)
    else:
        check = False
        break

if check:
    output_file.write('YES')
else:
    output_file.write('NO')

input_file.close()
output_file.close()
