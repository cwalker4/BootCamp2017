# solver for the steady-state and TPI of 3-person OG model

import numpy as np
import scipy.optimize as opt #included for root finder

#Three markets for which we define parameters:
#   (1): Households (i.e. goods market)
#   (2): Labour market
#   (3): Firms

#Household parameters
yrs_live = 60
S = 3 # num periods per lifetime
beta_annual = 0.96 # annual discount rate
beta = beta_annual ** (yrs_live / S) # per-period discount rate
sigma = 3.0 # coefficient of relative risk aversion

#Labour market parameters
nvec = np.array([1.0, 1.0, 0.2]) # exogenous labour supply

#Firm parameters
alpha = 0.35 # capital share of income
A = 1.0 # total factor productivity
delta_annual = 0.05 # annual depreciation
delta = 1 - (1 - delta_annual)**(yrs_live / S) #per=period depreciation

def get_r(bvec, nvec, args):
    A, alpha, delta = args
    K = sum(bvec)
    L = sum(nvec)
    r = alpha * A * ((L / K) ** (1 - alpha)) - delta
    return r

def get_w(bvec, nvec, args):
    A, alpha = args
    K = sum(bvec)
    L = sum(nvec)
    w = (1 - alpha) * A * ((K / L) ** (alpha))
    return w

def get_ct(bt, btp1, rt, wt):
    ct = wt + (1 + rt)*bt - btp1
    return ct

def get_MU(ct, sigma):
    return ct **(-sigma)

def get_EulErrs(bvec, *args):
    b2, b3 = bvec
    A, alpha, delta, beta, sigma = args

    r_params = (A, alpha, delta)
    w_params = (A, alpha)
    r = get_r(bvec, nvec, args=(r_params))
    w = get_w(bvec, nvec, args=(w_params))

    c1 = get_ct(0.0, b2, 0.0, nvec[0]*w) 
    c2 = get_ct(b2, b3, r, nvec[1]*w)
    c3 = get_ct(b3, 0.0, r, nvec[2]*w)

    MU_c1 = get_MU(c1, sigma)
    MU_c2 = get_MU(c2, sigma)
    MU_c3 = get_MU(c3, sigma)

    err1 = MU_c1 - beta * (1 + r) * MU_c2
    err2 = MU_c2 - beta * (1 + r) * MU_c3
    errs = np.array([err1, err2])
    return errs

b2_init = 0.10
b3_init = 0.10
b_init = np.array([b2_init, b3_init])
b_args = (A, alpha, delta, beta, sigma)
b_results = opt.root(get_EulErrs, b_init, args=(b_args))
print(b_results)
print('Roots: ', b_results.x)


