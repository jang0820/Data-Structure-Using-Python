F = [0]*16
F[0] = 1
F[1] = 1
for i in range(2, 16):
    F[i] = F[i-1] + F[i-2]
for i in range(0, 16):
    print(F[i])
