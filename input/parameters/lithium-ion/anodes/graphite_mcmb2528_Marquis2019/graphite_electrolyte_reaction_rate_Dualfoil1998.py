import autograd.numpy as np


def graphite_electrolyte_reaction_rate_Dualfoil1998(T, T_inf, E_r, R_g):
    """
    Reaction rate for Butler-Volmer reactions between graphite and LiPF6 in EC:DMC.

    References
    ----------
    .. [2] http://www.cchem.berkeley.edu/jsngrp/fortran.html

    Parameters
    ----------
    T: :class: `numpy.Array`
        Dimensional temperature
    T_inf: double
        Reference temperature
    E_r: double
        Reaction activation energy
    R_g: double
        The ideal gas constant

    Returns
    -------
    :`numpy.Array`
        Reaction rate
    """
    m_ref = 2 * 10 ** (-5)
    arrhenius = np.exp(E_r / R_g * (1 / T_inf - 1 / T))

    return m_ref * arrhenius
