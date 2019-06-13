from scipy.stats import expon
from random import randrange

def get_dist_num(args):
    dist = args[0]

    if dist == 'EXP':
        return expon.rvs(loc=float(args[1]), scale=float(args[2]), size=1)[0]
#    elif dist == 'NOR':
# NOR: Normal
# TRI: Triangular
# UNI: Uniforme
# BET: Beta
# WEI: Weibull
# CAU: Cauchy
# CHI: Chi-Quadrado
# ERL: Erlang
# GAM: Gama
# LOG: Log-Normal
# PAR: Pareto
# STU: t-Student

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
    em = randrange(0,100)+1
    if em <= float(probability[0]):
        return True
    else:
        return False