def latdef(L,a,dt):
        
    dy = L*((0.5*a*dt)**(1/2))
    return dy                    #dt determined by 5% above record high in summer
                                 #and 5% below record low in winter
print(latdef(60,0.00009,32))

def tempchange(maxT, minT):
    
    newMax = 0.05 * maxT + maxT
    newMin = minT - 0.05 * minT
    
    dt = newMax - newMin
    return dt

dt = tempchange(38,6)
newlatdef =latdef(60,0.00009,dt)
print(newlatdef)