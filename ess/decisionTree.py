import pandas as pd
import numpy as np

ess = pd.read_csv('ess.csv')

def get_splitpoint(allvalues, predictedvalues):
    lowest_error = float('inf')
    best_split = None
    best_lowermean = np.mean(predictedvalues)
    best_highermean = np.mean(predictedvalues)
    for pctl in range(0,100): # pctl is percentile
        split_candidate = np.percentile(allvalues, pctl)
        loweroutcomes = [outcome for value, outcome in zip(allvalues, predictedvalues) if \
            value <= split_candidate]
        higheroutcomes = [outcome for value, outcome in zip(allvalues, predictedvalues) if \
            value >= split_candidate]

        if np.min([len(loweroutcomes), len(higheroutcomes)]) > 0:
            meanlower = np.mean(loweroutcomes)
            meanhigher = np.mean(higheroutcomes)
            lowererrors = [abs(outcome - meanlower) for outcome in loweroutcomes]
            highererrors = [abs(outcome - meanhigher) for outcome in higheroutcomes]
            total_error = sum(lowererrors) + sum(highererrors)

            if total_error < lowest_error:
                best_split = split_candidate
                lowest_error = total_error
                best_lowermean = meanlower
                best_highermean = meanhigher
    return(best_split, lowest_error, best_lowermean, best_highermean)

maxdepth = 3

def getsplit(depth, data, variables, outcome_variable):
    best_var = ''
    lowest_error = float('inf')
    best_split = None
    predictedvalues = list(data.loc[:,outcome_variable])
    best_lowermean = -1
    best_highermean = -1
    for var in variables:
        allvalues = list(data.loc[:,var])
        splitted = get_splitpoint(allvalues, predictedvalues)
        if(splitted[1] < lowest_error):
            best_split = splitted[0]
            lowest_error = splitted[1]
            best_var = var
            best_lowermean = splitted[2]
            best_highermean = splitted[3]

    generated_tree = [[best_var, float('-inf'), best_split, []], [best_var, best_split, \
        float('inf'), []]]

    if depth < maxdepth:
        splitdata1 = data.loc[data[best_var] <= best_split,:]
        splitdata2 = data.loc[data[best_var] > best_split,:]
        if len(splitdata1.index) > 10 and len(splitdata2.index) > 10:
            generated_tree[0][3] = getsplit(depth+1, splitdata1, variables, outcome_variable)
            generated_tree[1][3] = getsplit(depth+1, splitdata2, variables, outcome_variable)
        else:
            depth = maxdepth + 1
            generated_tree[0][3] = best_lowermean
            generated_tree[1][3] = best_highermean

    else:
        generated_tree[0][3] = best_lowermean
        generated_tree[1][3] = best_highermean

    return generated_tree


variables = ['rlgdgr', 'hhmmb', 'netusoft', 'agea', 'eduyrs']
outcome_variable = 'happy'
print(getsplit(0, ess, variables, outcome_variable))


