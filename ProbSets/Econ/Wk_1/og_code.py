# solver for the steady-state and TPI of 3-person OG model
import pdb
import numpy as np
import scipy.optimize as opt #included for root finder
import matplotlib.pyplot as plt
import os

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

# TPI parameters
T = 20 
xi = 0.2
bvec_scal = np.array([0.8,1.1]) #scalars on SS betas for TPI start
epsilon = 1e-9

def get_r(K, nvec, args):
    A, alpha, delta = args
    L = sum(nvec)
    r = alpha * A * ((L / K) ** (1 - alpha)) - delta
    return r

def get_w(K, nvec, args):
    A, alpha = args
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
    r = get_r(sum(bvec), nvec, args=(r_params))
    w = get_w(sum(bvec), nvec, args=(w_params))

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

def get_Kpath_guess(K_init, K_SS, T):
    result = np.zeros((T, 1)) 
    K_step = (K_init - K_SS) / (T - 1)
    K_t = K_init
    for i in range(0, T):
        result[i] = K_t
        K_t -= K_step
    return result.flatten()

def get_rwpath(K_path, args):
    A, alpha, delta, T = args
    rpath = np.zeros((T, 1)) 
    wpath = np.zeros((T, 1))
    for i in range(0, T):
        r = get_r(K_path[i], nvec, args=(A, alpha, delta))
        rpath[i] = r
        w = get_w(K_path[i], nvec, args=(A, alpha))
        wpath[i] = w
    return rpath.flatten(), wpath.flatten()

# eq. 5.31
def get_EulErr_1(b32, *args):
    b21, w1, w2, r1, r2,  beta, sigma = args
    c2 = get_ct(b21, b32, r1, w1)
    c3 = get_ct(b32, 0.0, r2, (0.2*w2))

    MU_c2 = get_MU(c2, sigma)
    MU_c3 = get_MU(c3, sigma)

    return MU_c2 - beta * (1 + r2) * MU_c3

def get_EulErr_2(bvec, *args):
    w1, w2, w3, r2, r3, beta, sigma = args
    b2, b3 = bvec
    c1 = get_ct(0.0, b2, 0.0, w1)
    c2 = get_ct(b2, b3, r2, w2)
    c3 = get_ct(b3, 0.0, r3, 0.2*w3)
    MU_c1 = get_MU(c1, sigma)
    MU_c2 = get_MU(c2, sigma)
    MU_c3 = get_MU(c3, sigma)

    err1 = MU_c1 - beta * (1 + r2) * MU_c2
    err2 = MU_c2 - beta * (1 + r3) * MU_c3
    errs = np.array([err1, err2])
    return errs

def get_b_path(K_path, b_init,  args):
    A, alpha, delta, T = args
    result = np.zeros((T, 2))
    r_path, w_path = get_rwpath(K_path, args=(args))
    b_32 = opt.newton(get_EulErr_1, b_init[1], args=(b_init[0], w_path[0],
        w_path[1], r_path[0], r_path[1], beta, sigma))
    result[0] = b_init
    result[1,1] = b_32
    for i in range(1, T - 1):
        b_args = (w_path[i-1], w_path[i], w_path[i+1], r_path[i],
            r_path[i+1], beta, sigma)
        b_guess = b_init 
        b_nn = opt.root(get_EulErr_2, b_guess, args=(b_args))
        result[i,0] = b_nn.x[0]
        result[i+1,1] = b_nn.x[1]
    return result

def TPI_graph(K_path_conj):
    fig, ax = plt.subplots()
    ax.plot(K_path_conj)
    plt.show()

def print_SS(bvec, args):
    A, alpha, delta, nvec = args
    K_SS = sum(bvec)
    L_SS = sum(nvec)
    r = get_r(K_SS, nvec, args=(A, alpha, delta))
    w = get_w(K_SS, nvec, args=(A, alpha))

    c1 = get_ct(0.0, bvec[0], 0.0, nvec[0]*w)
    c2 = get_ct(bvec[1], bvec[1], r, nvec[1]*w)
    c3 = get_ct(bvec[1], 0.0, r, nvec[2]*w)
    cvec = np.array([c1, c2, c3])

    print('Steady state savings:', bvec,
            '\nSteady state consumption:', cvec,
            '\nSteady state r:', r,
            '\nSteady state w:', w)


# SS thingz
def get_SS(args):
    A, alpha, delta, beta, sigma, nvec = args
    b2_init = 0.10
    b3_init = 0.10
    b_init = np.array([b2_init, b3_init])
    b_args = (A, alpha, delta, beta, sigma)
    b_results = opt.root(get_EulErrs, b_init, args=(b_args))
    #print_SS(b_results.x, args=(A, alpha, delta, nvec))
    return b_results.x

# TPI things: First sets up variables, then proceeds through:
#   (1) assume transition paths for K, r, w
#   (2) solve b_{3,2} for initial s=2 aged individual
def get_TPI(args):

    A, alpha, delta, T, nvec = args
    ss_args = A, alpha, delta, beta, sigma, nvec
    b_SS = get_SS(ss_args) #steady-state savings
    b_init = (0.8*b_SS[0], 1.1*b_SS[1]) #initial savings
    K_init = sum(b_init) #initial levels of capital
    K_SS = sum(b_SS) #SS levels of capital
    K_path_conj = get_Kpath_guess(K_init, K_SS, T) #linear transition path
    while True:
        b_path = get_b_path(K_path_conj, b_init, args=(A, alpha, delta, T))
        K_path_imp = b_path.sum(axis=1) # K path implied by capital stock
        K_dist = np.linalg.norm(K_path_imp - K_path_conj)
        if K_dist < epsilon:
            TPI_graph(K_path_conj[:15])
            print(K_path_conj[:15])
            print(K_SS)
            break

        else: 
            K_path_conj = xi*K_path_imp + (1-xi)*K_path_conj

#get_SS(args=(A, alpha, delta, beta, sigma, nvec))
get_TPI(args=(A, alpha, delta, T, nvec))

