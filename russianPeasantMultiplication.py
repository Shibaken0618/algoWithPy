import math
from multiprocessing.connection import answer_challenge
import pandas as pd

def russianPeasantMultiplication(n1,n2):
    halving = [n1]
    doubling = [n2]
    while(min(halving) > 1):
        halving.append(math.floor(min(halving)/2))
    while(len(doubling)<len(halving)):
        doubling.append(max(doubling)*2)
    half_double = pd.DataFrame(zip(halving,doubling))
    half_double = half_double.loc[half_double[0]%2 == 1,:]
    answer = sum(half_double.loc[:,1])
    return answer

print(russianPeasantMultiplication(89,18))
print(russianPeasantMultiplication(76,32))