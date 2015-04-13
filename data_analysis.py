#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

def wavepacket(x,k,sigma):
    """ This function creates a wavepacket on the interval defined by x with wavevector k and standard deviation sigma."""
    return np.sin(k*x) *  np.exp(-(x**2)/(2*sigma**2))


def main():
        """This function sould call noisy_packet() to get a gaussian wave packet, call clean_data() to apply a low pass filter to the data and finally plot the result."""
        #TODO add your code here


def noisy_packet(x_values, k,sigma,noise_amplitude):
	"""This function should return a noisy gaussian wavepacket with wave vector k, standard deviation sigma and gaussian noise of standard deviation noise_amplitude. It currently just returns an array of zeros"""
        clean_y = wavepacket(x_values,k,sigma)
        noisy_y = clean_y + noise_amplitude*np.random.randn(len(x_values))
	return noisy_y

def clean_data(x_values,y_values):
	"""This function should take a set of y_values, perform the fourier transform on it, filter out the high frequency noise, transform the signal back into real space and return it."""

        pass
	#return y_clean

main()  # calls your main function
