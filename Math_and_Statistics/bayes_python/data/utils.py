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
    posterior = pmf * likelihood
    posterior.normalize()
    return posterior

# Chapter.4
def make_binomial(n, p):
    ks = np.arange(n + 1)
    ps = ss.binom(n, p).pmf(ks)
    return Pmf(ps, ks)

def update_euro(pmf, likelihood, dataset):
    posterior = pmf.copy()
    for data in dataset:
        posterior *= likelihood[data]
    posterior.normalize()
    return posterior

def update_binomial(pmf, data):
    k, n = data
    xs = pmf.qs
    likelihood = ss.binom(n, xs).pmf(k)
    posterior = pmf * likelihood
    posterior.normalize()
    return posterior

# Chapter.5
def update_train(pmf, data):
    hypos = pmf.qs
    likelihood = 1 / hypos
    impossible = (data > hypos)
    likelihood[impossible] = 0
    posterior = pmf * likelihood
    posterior.normalize()
    return posterior

# Chapter.6
def odds(p):
    return p / (1-p)

def prob(o):
    return o / (o+1)

def make_dice(sides):
    outcomes = np.arange(1, sides + 1)
    dice = Pmf(1/sides, outcomes)
    return dice

def add_dist_seq(seq):
    total = seq[0]
    for other in seq[1:]:
        total = total.add_dist(other)
    return total