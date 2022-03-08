import matplotlib.pyplot as plt
from linearCongruentialGenerator import *

def over_lapping_sums(the_list, sum_length):
    length_of_list = len(the_list)
    the_list.extend(the_list)
    output = []
    for n in range(0,length_of_list):
        output.append(sum(the_list[n:(n+sum_length)]))
    return output

overlap = over_lapping_sums(listRandom(211111,111112,300007),12)
plt.hist(overlap,20,facecolor='blue',alpha=0.5)
plt.title('Results of the Overlapping Sums Test')
plt.xlabel('Sum of Elements of Overlapping Consecutive Sections of List')
plt.ylabel('Frequency of Sum')
plt.show()