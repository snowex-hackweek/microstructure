"""

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img

from scipy import fftpack
import scipy.optimize as opt

def cropped_indicator(image_filename, xlims=None, ylims=None):
    """
    Crops image if specified

    """
    if xlims is None:
        # Don't crop
        return np.asarray(img.imread(image_filename)[:, :, 0])  # [:,:,0] gets rid of channel information

    if ylims is None:
        # Assume square
        ylims = xlims

    return np.asarray(img.imread(image_filename)[xlims[0]:xlims[1], ylims[0]:ylims[1], 0])


def ice_indicator_function(image_filename):
    """
        read image and convert it to 1,0 indicator function
    """
    image = img.imread(image_filename)[:, :, 0]  # MJS added to get rid of channel information
    ice_indicator_function = np.asarray(image)
    return ice_indicator_function


def ice_volume_fraction(indicator_function):
    """
        compute ice volume fraction from an image indicator function
    """
    return np.mean(indicator_function)


def image_size(indicator_function):
    """
        get the size of the image
    """
    return indicator_function.shape


def ACF1D(acf2d, axis):
    """
        extract the 1D correlation function along a given axis (0 or 1)
    """
    # slc = [slice(None)] * len(acf2d.shape)
    # slc[axis] = slice(0, acf2d.shape[axis])
    # return acf2d[slc]
    nz, nx = acf2d.shape
    if axis == 1:
        return acf2d[0, 0:int((nx + 1) / 2)]
    elif axis == 0:
        return acf2d[0:int((nz + 1) / 2), 0]
    else:
        return "stuss"


def acf1d_fit_exp(r, acf1d, r_max):
    """
        fit the correlation data acf1d for given lags r in the range [0,r_max]
        to an exponential
        returns:
    """

    # set fitrange
    fitrange = (r < r_max)

    # define residual function for least squares fit
    def residual(p, r, acf):
        C0 = p[0]
        correlation_length = p[1]
        return (C0 * np.exp(-r / correlation_length) - acf)

    # initial values for the optimization
    p0 = np.array([0.2, 1e-3])

    # least square fit in the required range
    p_opt, info = opt.leastsq(residual, p0, args=(r[fitrange], acf1d[fitrange]))
    C0 = p_opt[0]
    correlation_length = p_opt[1]
    acf1d_exp = residual(p_opt, r, 0)

    return acf1d_exp, [C0, correlation_length]


def acf1d_fit_ts(r, acf1d, r_max):
    """
        fit the correlation data acf1d for given lags r in the range [0,r_max]
        to an exponential
    """

    # set fitrange
    fitrange = (r < r_max)

    # define residual function for least squares fit
    def residual(p, r, acf):
        C0 = p[0]
        correlation_length = p[1]
        repeat_distance = p[2]
        return (C0 * np.exp(-r / correlation_length) * np.sinc(2 * r / repeat_distance) - acf)

    # initial values for the optimization
    p0 = np.array([0.2, 1e-3, 1e-3])

    # least square fit in the required range
    p_opt, info = opt.leastsq(residual, p0, args=(r[fitrange], acf1d[fitrange]))
    C0 = p_opt[0]
    correlation_length = p_opt[1]
    repeat_distance = p_opt[2]
    acf1d_ts = residual(p_opt, r, 0)
    return acf1d_ts, [C0, correlation_length, repeat_distance]


def ACF2D(indicator_function):
    """
        compute the 2D correlation function for the indicator_function of an image
    """

    ##################################################
    # replace the following by the correct code
    ##################################################
    f_2 = ice_volume_fraction(indicator_function)
    aux = fftpack.fftn(indicator_function - f_2)
    power_spectrum = np.abs(aux) ** 2
    acf2d = fftpack.ifftn(power_spectrum)
    nx, nz = indicator_function.shape
    return acf2d.real / (nx * nz)

    # return np.zeros_like(indicator_function)


def ssa_from_acf_slope(volume_fraction, acf_slope_at_origin):
    """
        compute the ssa from given slope of an autocorrelation function
        C(r) at the origin and the volume fraction.
        This relation is often called Debye relation
    """
    ##################################################
    # replace the following by the correct code
    ##################################################
    rho_ice = 917
    return 4 * acf_slope_at_origin / volume_fraction / rho_ice