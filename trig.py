#!/usr/bin/python

#The following statements are used to import numpy and matplotlib.
import numpy as np
import matplotlib.pyplot as plt

# TODO fill in this function
def integrate(y, dx):
    print np.sum(y)*dx
        
# TODO write code here to setup arrays x and y = sin(x) and then plot them.
# After this is done implement your integrate function above integrate y

x = np.arange(0., np.pi, 0.01)
y = np.sin(x)

integrate(y, 0.01)
print np.trapz(y, dx = 0.01)
