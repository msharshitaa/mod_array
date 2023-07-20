def mod_array(A, B):
    num = 0
    for digit in A:
        num = num * 10 + digit
    result = num % B
    return result
A = list(map(int,input().split()))
B = int(input())
output = mod_array(A,B)
print(output)
