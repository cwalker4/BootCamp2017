# solution for question 6.14

def newton_minimize(x, epsilon, df, ddf):
    '''
    ------------------------------------------------
    Finds the minimizer of a function f by iterating
    over Newton's Method. Accepts an initial guess
    of minimizer, x, a stopping tolerance, epsilon,
    and callabe functions for finding the first and
    second derivatives evaluated at x, df and ddf,
    respectively. 
    -----------------------------------------------
    '''
    
    max_iters = 10000
    iters = 0
    while iters < max_iters:
        x_temp = x
        x -= (df(x) / ddf(x))
        if abs(x - x_temp) < (x * epsilon):
            break
        iters += 1
    return x
        
