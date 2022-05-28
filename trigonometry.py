from math import pi, cos, gamma

def cosine(t:float|int) -> float:
    reduced_t = t % (2*pi)
    s=1 + sum((( reduced_t ** i) / gamma(i+1)) * (-1)**(i//2) for i in range(2,40,2))
    return s
def sine(t:float|int) -> float:
    return (1-(cosine(t))**2)**.5