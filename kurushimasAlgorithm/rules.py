def rule1(x,n,upright):
    return ((x+((-1)**upright)*n)%n**2)


def rule2(x,n,upleft):
    return((x + ((-1)**upleft))%n**2)


def rule3(x,n,upleft):
    return((x + ((-1)**upleft*(-n+1)))%n**2)

