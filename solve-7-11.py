input_file = open('input.txt', 'r')
output_file = open('output.txt', 'w')

def Merge(A, B):
    a = 0
    b = 0
    a_size = len(A)
    b_size = len(B)
    ans = []
    while(a < a_size and b < b_size):
        if A[a] < B[b]:
            ans.append(A[a])
            a += 1
        else:
            ans.append(B[b])
            b += 1
    if a < a_size:
        while a < a_size:
            ans.append(A[a])
            a += 1
    if b < b_size:
        while b < b_size:
            ans.append(B[b])
            b += 1
    return ans

A = list(map(int, input_file.readline().split()))
B = list(map(int, input_file.readline().split()))

for i in Merge(A, B):
    output_file.write(str(i) + ' ')

input_file.close()
output_file.close()