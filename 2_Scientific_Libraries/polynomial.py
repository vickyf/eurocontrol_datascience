def calc_poly(params, data):
    x = np.c_[[data**i for i in range(len(params))]]
    return np.dot(params, x)