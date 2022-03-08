def next_random(previous,n1,n2,n3):
    the_next = (previous * n1 + n2) % n3
    return the_next

print(next_random(21,33,54,92))


def listRandom(n1,n2,n3):
    output = [1]
    while len(output) <= n3:
        output.append(next_random(output[len(output) - 1],n1,n2,n3))
    return output

print(listRandom(29,32,23))