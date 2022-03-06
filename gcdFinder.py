def gcd(x,y):
    larger = max(x,y)
    smaller = min(x,y)
    remainder = larger%smaller

    if (larger == smaller):
        return larger
    if(remainder == 0):
        return smaller
    if (remainder != 0):
        return (gcd(smaller,remainder))

print(gcd(105,33))
print(gcd(44,88))
print(gcd(987,987))
print(gcd(1,777))