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

# Chapter.10
def update_machine(pmf, likelihood, data):
    pmf *=likelihood[data]
    pmf.normalize()

# Chapter.11
def make_joint(pmf1, pmf2):
    X, Y = np.meshgrid(pmf1, pmf2)
    return pd.DataFrame(X * Y, columns = pmf1.qs, index=pmf2.qs)

def plot_joint(joint, cmap='Blues'):
    vmax = joint.to_numpy().max() * 1.1
    plt.pcolormesh(joint.columns, joint.index, joint, cmap=cmap, vmax=vmax, shading='nearest')
    plt.colorbar()
    plt.xlabel('A height')
    plt.ylabel('B height')

def plot_contour(joint):
    plt.contour(joint.columns, joint.index, joint, linewidths=1)

def normalize(joint):
    prob_data = joint.to_numpy().sum()
    joint /= prob_data
    return prob_data

# Chapter.12
def make_cdf_map(df, colname, by='Species'):
    fig, ax = plt.subplots(1, 1, figsize=(12, 3))
    cdf_map = {}
    grouped = df.groupby(by)[colname]
    for name, group in grouped:
        cdf_map[name] = Cdf.from_seq(group, name=name)
        ax.plot(cdf_map[name], label=name)
    plt.legend()
    return cdf_map

def make_norm_map(df, colname, by='Species'):
    norm_map = {}
    grouped = df.groupby(by)[colname]
    for name, group in grouped:
        mean = group.mean()
        std = group.std()
        norm_map[name] = ss.norm(mean, std)
    return norm_map

def update_penguin(prior, data, norm_map):
    hypos = prior.qs
    likelihood = [norm_map[hypo].pdf(data) for hypo in hypos]
    posterior = prior * likelihood
    posterior.normalize()
    return posterior

def update_naive(prior, data_seq, norm_maps):
    posterior = prior.copy()
    for data, norm_map in zip(data_seq, norm_maps):
        posterior = update_penguin(posterior, data, norm_map)
    return posterior

def make_multinorm_map(df, colnames, by='Species'):
    multinorm_map = {}
    grouped = df.groupby(by)
    for name, group in grouped:
        features = group[colnames]
        mean = features.mean()
        cov = features.cov()
        multinorm_map[name] = ss.multivariate_normal(mean, cov)
    return multinorm_map

# Chapter.13
def make_uniform(qs, name=None, **options):
    pmf = Pmf(1.0, qs, **options)
    pmf.normalize()
    if name:
        pmf.index.name = name
    return pmf

def update_norm(prior, data):
    mu_mesh, sigma_mesh, data_mesh = np.meshgrid(prior.columns, prior.index, data)
    densities = ss.norm(mu_mesh, sigma_mesh).pdf(data_mesh)
    likelihood = densities.prod(axis=2)

    posterior = prior * likelihood
    normalize(posterior)

    return posterior

def kde_from_pmf(pmf, n=101):
    kde = ss.gaussian_kde(pmf.qs, weights=pmf.ps)
    qs = np.linspace(pmf.qs.min(), pmf.qs.max(), n)
    ps = kde.evaluate(qs)
    kde_pmf = Pmf(ps, qs)
    kde_pmf.normalize()
    return kde_pmf

def update_norm_summary(prior, data):
    n, m, s = data
    mu_mesh, sigma_mesh = np.meshgrid(prior.columns, prior.index)

    like1 = ss.norm(mu_mesh, sigma_mesh/np.sqrt(n)).pdf(m)
    like2 = ss.chi2(n-1).pdf((n-1) * s**2 / sigma_mesh**2)

    posterior = prior * like1 * like2
    normalize(posterior)

    return posterior

# Chapter.14
def weibull_dist(lam, k):
    return ss.weibull_min(k, scale=lam)

def update_weibull(prior, data, complete=True):
    lam_mesh, k_mesh, data_mesh = np.meshgrid(prior.columns, prior.index, data)
    if complete:
        densities = weibull_dist(lam_mesh, k_mesh).pdf(data_mesh)
    else:
        densities = weibull_dist(lam_mesh, k_mesh).sf(data_mesh)
    likelihood = densities.prod(axis=2)

    posterior = prior * likelihood
    normalize(posterior)

    return posterior

def plot_lifelines(obs):
    for y, row in obs.iterrows():
        start = row['start']
        end = row['end']
        status = row['status']
        
        if status == 0:
            plt.hlines(y, start, end, color='C0')
        else:
            plt.hlines(y, start, end, color='C1')
            plt.plot(end, y, marker='o', color='C1')

    plt.gca().invert_yaxis()

def joint_weibull_mean(joint):
    lam_mesh, k_mesh = np.meshgrid(joint.columns, joint.index)
    means = weibull_dist(lam_mesh, k_mesh).mean()
    prod = means * joint
    return prod.to_numpy().sum()

# Chapter.15
def compute_probs(p0, p1):
    q0 = 1 - p0
    q1 = 1 - p1
    return [q0*q1, q0*p1, q1*p0, p0*p1]

def make_joint3(pmf1, pmf2, pmf3):
    joint2 = make_joint(pmf2, pmf1)
    joint2_pmf = Pmf(joint2.stack())
    joint3 = make_joint(pmf3, joint2_pmf)
    joint3.index = pd.MultiIndex.from_tuples(joint3.index)
    return Pmf(joint3.stack())

# Chapter.16
def transform(pmf, func):
    ps = pmf.ps
    qs = func(pmf.qs)
    return Pmf(ps, qs, copy=True)

