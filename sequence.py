# https://github.com/Fridrik93/T-111-PROG-Sequence
n = int(input("Enter the length of the sequence: ")) # Do not change this line
n1 = 1
n2 = 2
n3 = 3

for i in range(1, n+1):
    if 1 <= i <= 3:
        print(i)
    else:
        total = n1 + n2 + n3
        n1 = n2
        n2 = n3
        n3 = total
        print(total)