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
        total = Pmf.add_dist(total, other)
    return total

# Chapter.7
def make_mixture(pmf, pmf_seq):
    df = pd.DataFrame(pmf_seq).fillna(0).T
    df *= np.array(pmf)
    total = df.sum(axis=1)
    return Pmf(total)

# Chapter.8
def make_poisson_pmf(lam, qs):
    ps = ss.poisson(lam).pmf(qs)
    pmf = Pmf(ps, qs)
    pmf.normalize()
    return pmf

def update_poisson(pmf, data):
    k = data
    lams = pmf.qs
    likelihood = ss.poisson(lams).pmf(k)
    posterior = pmf * likelihood
    posterior.normalize()
    return posterior

def expo_pdf(t, lam):
    return lam * np.exp(-lam * t)

# Chapter.9
def kde_from_sample(sample, qs):
    kde = ss.gaussian_kde(sample)
    ps = kde(qs)
    pmf = Pmf(ps, qs)
    pmf.normalize()
    return pmf

def compute_prob_win(diff, sample_diff):
    def prob_overbid(sample_diff):
        return np.mean(sample_diff > 0)
    def prob_worse_than(diff, sample_diff):
        return np.mean(sample_diff < diff)
    
    if diff > 0:
        return 0
    
    p1 = prob_overbid(sample_diff)
    p2 = prob_worse_than(diff, sample_diff)

    return p1 + p2

def total_prob_win(bid, posterior, sample_diff):
    total = 0
    for price, prob in posterior.items():
        diff = bid - price
        total += prob * compute_prob_win(diff, sample_diff)
    return total

def compute_gain(bid, price, sample_diff):
    diff = bid - price
    prob = compute_prob_win(diff, sample_diff)

    if -250 <= diff <= 0:
        return 2 * price * prob
    else:
        return price * prob
    
def expected_gain(bid, posterior, sample_diff):
    total = 0
    for price, prob in posterior.items():
        total += prob * compute_gain(bid, price, sample_diff)
    return total

