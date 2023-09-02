import numpy as np
import os




def compute_solids(np,y,thickness,xlen,ylen,top,bottom,rad):
    for i in range(np):
        if ((y(i) <=(top + rad)) and (y(i) > top) and (y(i) > (bottom + rad))):
            n1 = n1 + 1
            h = top + rad - y(k)
            v1 = v1 + (1.0/3.0)*np.pi*h*h*(3*rad-h)
        elif((y(i) <= top) and (y(i) > (top - rad)) and(y(i) > (bottom + rad))) :
            n2 = n2 + 1
            h = y(i) + rad - top
            v2 = v2 + (4.0/3.0)*np.pi*rad*rad*rad- (1.0/3.0)*np.pi*h*h*(3*rad-h)

        elif((y(i)<= (top - rad)) and (y(i) > (bottom + rad))):
            n3 = n3 + 1
            v3 = v3 + (4.0/3.0)*np.pi*rad*rad*rad

        elif ((y(i) < (top - rad)) and (y(i) > bottom) and (y(i) <= (bottom + rad))):
            n4 = n4 + 1
            h = bottom + ra - y(k)
            v4 = v4 + (4.0/3.0)*np.pi*rad*rad*rad \
             - (1.0/3.0)*np.pi*h*h*(3*rad-h)

        elif ((y(i) <= bottom) and (y(i) > (bottom - rad)) and (y(i) <  top-rad)):
            n5 = n5 + 1
            h = y(i) + ra - bottom
            v5 = v5 + (1.0/3.0)*np.pi*h*h*(3*rad-h)

        elif ((y(i) < bottom + rad) and (y(i) > (top - rad)) and (y(i) <= top) and (y(i) >= bottom)):
            n6 = n6 + 1
            ht = y(i) + rad - top
            hb = bottom + rad - y(i)
            v6 = v6 + (4.0/3.0)*np.pi*rad*rad*rad - \
                (1.0/3.0)*np.pi*ht*ht*(3*rad-ht) - \
                (1.0/3.0)*np.pi*hb*hb*(3*rad-hb)

        elif ((y(i) <= bottom) and (y(i) >= (top-rad))):
            n7 = n7 + 1
            ht = y(i) + rad - top
            hb = y(i) + rad - bottom
            v7 = v7 - (1.0/3.0)*np.pi*ht*ht*(3*rad-ht) + \
                (1.0/3.0)*np.pi*hb*hb*(3*rad-hb)

        elif ((y(i) > top) and (y(i) <= (bottom + rad))):
            n8 = n8 + 1
            ht = top + rad - y(i)
            hb = bottom + rad - y(i)
            v8 = v8 + (1.0/3.0)*np.pi*ht*ht*(3*rad-ht) - \
                (1.0/3.0)*np.pi*hb*hb*(3*rad-hb)
            
    pvol = xlen*ylen*thickness
    psvol = v1 + v2 + v3 + v4 + v5 + v6 + v7 + v8
    pd = psvol/pvol
    return pd










