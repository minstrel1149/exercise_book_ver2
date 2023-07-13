from pathlib import Path
import pandas as pd
import numpy as np
import scipy.stats as ss
from scipy.interpolate import interp1d
from scipy.special import expit
from fractions import Fraction
from empiricaldist import Pmf, Cdf
import matplotlib.pyplot as plt
from collections import Counter
import statsmodels.formula.api as smfa

# Chapter.1
def prob(ser):
    return ser.mean()

def conditional(proposition, given):
    return prob(proposition[given])

# Chapter.2
def update(table):
    table['unnorm'] = table['prior'] * table['likelihood']
    table['posterior'] = table['unnorm'] / table['unnorm'].sum()
    return table

# Chapter.3
def update_dice(pmf, data):
    hypos = pmf.qs
    likelihood = 1 / hypos
    impossible = (data > hypos)
    likelihood[impossible] = 0
    pmf *= likelihood
    pmf.normalize()
    return pmf

# Chapter.4
def make_binomial(n, p):
    ks = np.arange(n + 1)
    ps = ss.binom(n, p).pmf(ks)
    return Pmf(ps, ks)

