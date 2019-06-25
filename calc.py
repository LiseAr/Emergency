from random import expovariate, normalvariate, triangular, uniform, betavariate, \
    weibullvariate, gammavariate, lognormvariate, paretovariate
from random import randrange, random

def get_dist_num(args):
    dist = args[0]
    
    for i in range(len(args[1:])):
        args[i+1] = float(args[1:][i])

    if dist == 'EXP':
        return expovariate(args[1])
    elif dist == 'NOR':
        return normalvariate(args[1], args[2]) 
    elif dist == 'TRI':
        return triangular(args[1], args[2], args[3])
    elif dist == 'UNI':
        return uniform(args[1], args[2])
    elif dist == 'BET':
        return betavariate(args[1], args[2])
    elif dist == 'WEI':
        return weibullvariate(args[1], args[2])
    elif dist == 'CAU': # CAU: Cauchy
        return 0
    elif dist == 'CHI':
        return 0
    elif dist == 'ERL': # ERL: Erlang
        return 0
    elif dist == 'GAM':
        return gammavariate(args[1], args[2])
    elif dist == 'LOG':
        return lognormvariate(args[1], args[2])
    elif dist == 'PAR':
        return paretovariate(args[1])
    elif dist == 'STU':
        return 0

def get_priority(args):
    list = []
    for i in range(len(args)):
        if i != 0:
            list.append(int(args[i]) + list[-1])
        else:
            list.append(int(args[i]))
            
    p = randrange(0,100)+1
    for i in range(len(list)):
        if p <= list[i]:
            return 5-i

def get_exam_medicine(probability) -> bool:
    if random() <= float(probability[0]):
        return True
    else:
        return False