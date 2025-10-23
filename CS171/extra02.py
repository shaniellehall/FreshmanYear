def coulombs_law(charge1, charge2, distance):
    k = 8.9875517923 * (10**9)
    top = charge1 * charge2
    bottom = distance ** 2
    
    fraction = top/bottom
    newtons = k * fraction
 
    return newtons

result = coulombs_law(1e-6,1e-6,0.1)
print(result)