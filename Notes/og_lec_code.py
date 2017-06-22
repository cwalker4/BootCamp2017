# solve for the steady-state in 3-per OG model

import numpy as np
import scipy.optimize as opt # included for root finder

# Household parameters
yrs_live = 60
S = 3 # num periods per lifetime
beta_annual = 0.96
beta = beta_anual**(yrs_live / S)
sigma = 2.5 # coefficient of relative risk aversion in utility functions

nvec = np.array([1.0, 1.0, 0.2]) # labour supply

# Firm parameters
alpha = 0.3
A = 1.0 # total factor productivity
delta_annual = 0.5
delta = 1 - (1 - delta_annual)**(yrs_live / S) # depreciation


def get_r(K, L, params):
    A, alpha, delta = params
    r = alpha * A * ((L / K) ** (1 - alpha))
    
    return r


def stuff(b2b3vals, args):
    beta, sigma, nvec, alpha, A, delta = args
    MUc1 = somefunc(b2b3vals)
    MUc2 = someotherfunc(b2b3vals)
    MUc3 = somelastfunc(b2b3vals)
    r = get_r(b2b3vals, nvec, alpha, A, delta) # change the args of this to fit get_r
    error1 = MUc1 - beta * (1 + r) * MUc2
    error2 = MUc2 - beta * (1 + r) * MUc3
    errors = np.array([error1, error2])
    
    return errors # vector of errors

b2bar, b3bar = opt.root(stuff...) # check out tutorial section for info on root finder (tries to make errors = 0)
