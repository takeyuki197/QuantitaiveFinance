import numpy as np

def get_path(seed, grid_num, path_num, T, S0, H, eta, xi, rho):
    np.random.seed(seed)
    dt = T/grid_num
    t = np.array([np.ones(path_num)*dt*i for i in range(grid_num + 1)])
    dW1 = np.random.randn(grid_num, path_num)*np.sqrt(dt)
    dW2 = np.random.randn(grid_num, path_num)*np.sqrt(dt)
    dB = rho * dW1 + np.sqrt(1 - rho**2) * dW2
    
    Y = np.zeros((grid_num + 1, path_num))
    for n in range(1, grid_num + 1):
        tn = dt*n
        for i in range(n):
            ti = dt*i
            Y[n] += ((tn - ti)**(H-0.5))*dW1[i]
    Y *= np.sqrt(2.0*H)
    
    V = xi * np.exp(eta * Y - 0.5 * eta**2 * t**(2.0*H))
    
    increments = np.sqrt(V)[:-1]*dB - 0.5*V[:-1]*dt
    integral = np.cumsum(increments, axis = 0)

    S = np.ones((grid_num + 1, path_num))*S0
    S[1:] = S0 * np.exp(integral)
    
    return S, V