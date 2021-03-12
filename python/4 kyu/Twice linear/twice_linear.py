def dbl_linear(n):
    u=[1]
    i=0
    while len(u) <n*10:
        u.append(2*u[i]+1)
        u.append(3*u[i]+1)
        i+=1
    return sorted(set(u))[n]
