def productFib(prod):
    return fibprod(0,1,prod)
def fibprod(c,n,prod):
    while c*n<prod:
        c,n = n,n+c
    return [c, n, True] if c*n == prod else [c, n, False]
