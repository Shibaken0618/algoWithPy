import pandas as pd
import numpy as np

ess = pd.read_csv('ess.csv')
# variables = pd.read_csv('variables.csv')
# print(ess.shape)
# print(ess.loc[:,'happy'].head())
# print(ess.loc[:,'sclmeet'].head())

# ess = ess.loc[ess['sclmeet'] <= 10,:].copy()
# ess = ess.loc[ess['rlgdgr'] <= 10,:].copy()
# ess = ess.loc[ess['hhmmb'] <= 50,:].copy()
# ess = ess.loc[ess['netusoft'] <= 5,:].copy()
# ess = ess.loc[ess['agea'] <= 200,:].copy()
# ess = ess.loc[ess['health'] <= 5,:].copy()
# ess = ess.loc[ess['happy'] <= 10,:].copy()
# ess = ess.loc[ess['eduyrs'] <= 100,:].copy().reset_index(drop=True)


# social = list(ess.loc[:,'sclmeet'])
# happy = list(ess.loc[:,'happy'])
# low_social_happiness = [hap for soc, hap in zip(social,happy) if soc <= 5]
# high_social_happiness = [hap for soc, hap in zip(social, happy) if soc > 5]

# meanlower = np.mean(low_social_happiness)
# meanhigher = np.mean(high_social_happiness)

# lowererrors = [abs(lowhappy - meanlower) for lowhappy in low_social_happiness]
# highererrors = [abs(highhappy - meanhigher) for highhappy in high_social_happiness]

# total_error = sum(lowererrors) + sum(highererrors)


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


# allvalues = list(ess.loc[:,'hhmmb'])
# predictedvalues = list(ess.loc[:,'happy'])
# print(get_splitpoint(allvalues, predictedvalues))

def getsplit(data, variables, outcome_variable):
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

    generated_tree = [[best_var, float('-inf'), best_split, best_lowermean], [best_var, best_split, \
        float('inf'), best_highermean]]

    return(generated_tree)

variables = ['rlgdgr', 'hhmmb', 'netusoft', 'agea', 'eduyrs']
outcome_variable = 'happy'
print(getsplit(ess, variables, outcome_variable))


