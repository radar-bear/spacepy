#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
plot: SpacePy specialized plotting routines

This package provides classes to plot various types of space physics data.

Authors: Brian Larsen and Steve Morley
Institution: Los Alamos National Laboratory
Contact: balarsen@lanl.gov


Copyright 2011-2015 Los Alamos National Security, LLC.

"""
import os
from matplotlib.patches import Wedge
from matplotlib import __version__ as mplv
import matplotlib.pyplot as plt
from spacepy import __path__ as basepath
from spacepy.datamodel import dmcopy
from .spectrogram import *
from .utils import *
from .carrington import *
from .colourmaps import plasma as _plasma
from .colourmaps import plasma_r as _plasma_r
from .colourmaps import viridis as _viridis
from .colourmaps import viridis_r as _viridis_r

plt.register_cmap(name='plasma', cmap=_plasma)
plt.register_cmap(name='plasma_r', cmap=_plasma_r)
plt.register_cmap(name='viridis', cmap=_viridis)
plt.register_cmap(name='viridis_r', cmap=_viridis_r)

def available(returnvals=False):
    spacepystyle = os.path.join('{0}'.format(basepath[0]), 'data', 'spacepy.mplstyle')
    spacepyaltstyle = os.path.join('{0}'.format(basepath[0]), 'data', 'spacepy_altgrid.mplstyle')
    polarstyle = os.path.join('{0}'.format(basepath[0]), 'data', 'spacepy_polar.mplstyle')
    lookdict = {'default': spacepystyle,
                'spacepy': spacepystyle,
                'spacepy_altgrid': spacepyaltstyle,
                'altgrid': spacepyaltstyle,
                'spacepy_polar': polarstyle,
                'polar': polarstyle
               }
    if returnvals:
        return lookdict
    else:
        return list(lookdict.keys())

def style(look=None, cmap='plasma'):
    '''
    Apply SpacePy's matplotlib style settings from a known style sheet.

    Parameters
    ----------
    look : str
    Name of style. For a list of available style names, see `spacepy.plot.available`.
    '''
    import matplotlib
    lookdict = available(returnvals=True)
    try:
        usestyle = lookdict[look]
    except KeyError:
        usestyle = lookdict['default']
    try:
        plt.style.use(usestyle)
    except AttributeError: #plt.style.use not available, old matplotlib?
        dum = matplotlib.rc_params_from_file(usestyle)
        styapply = dict()
        #remove None values as these seem to cause issues...
        for key in dum:
            if dum[key] is not None: styapply[key] = dum[key]
        for key in styapply:
            matplotlib.rcParams[key] = styapply[key]
    matplotlib.rcParams['image.cmap'] = cmap

#save current rcParams before applying spacepy style
oldParams = dict()
for key, val in matplotlib.rcParams.items():
        oldParams[key] = dmcopy(val)
style()

def revert_style():
    import matplotlib
    for key in oldParams:
        try:
            matplotlib.rcParams[key] = oldParams[key]
        except ValueError:
            pass

def dual_half_circle(center=(0,0), radius=1.0,
                     sun_direction='right', ax=None, colors=('w','k'),
                     **kwargs):
    """
    Plot two half circles to a plot with the specified face colors and
    rotation. This is normal to use to denote the sun direction in
    magnetospheric science plots.

    Other Parameters
    ----------
    center : array-like, 2 elements
        Center in data coordinates of the circles, default (0,0)
    radius : float
        Radius of the circles, defualt 1.0
    sun_direction : string or float
        The rotation direction of the first (white) circle. Options are ['down',
        'down right', 'right', 'up left', 'up right', 'up', 'down left', 'left']
        or an angle in degrees counter-clockwise from up. Default right.
    ax : matplotlib.axes
        Axis to plot the circles on.
    colors : array-like, 2 elements
        The two colors for the circle fill. The First number is the light and
        second is the dark.
    **kwargs : other keywords
        Other keywords to pass to matplotlib.patches.Wedge

    Returns
    -------
    out : tuple
        Tuple of the two wedge objects

    Examples
    --------
    >>> import spacepy.plot
    >>> spacepy.plot.dual_half_circle()

    """
    sun_dict = {'left':90,
                'right':-90,
                'up':0,
                'down':180,
                'up right':-45,
                'up left':45,
                'down right':45+180,
                'down left':-45+180,
                }
    try:
        angle = sun_dict[sun_direction]
    except KeyError:
        try:
            angle = float(sun_direction)
        except ValueError:
            raise(ValueError("Sun_direction was not understood, must be a float or {0}".format(sun_dict.keys())))
                
    theta1, theta2 = angle, angle + 180
    if ax is None:
        ax = plt.gca()
        
    w1 = Wedge(center, radius, theta1, theta2, fc=colors[0],transform=ax.transData._b, **kwargs)
    w2 = Wedge(center, radius, theta2, theta1, fc=colors[1], transform=ax.transData._b,**kwargs)
    for wedge in [w1, w2]:
        ax.add_artist(wedge)
    return (w1, w2)

def levelHist(data, var=None, levels=(3, 5, 7), target=None, colors=None, **kwargs):
    """
    Plot a histogram with up to 5 levels following a color cycle (e.g. Kp index "stoplight")

    Parameters
    ----------
    data : array-like, or dict-like
        Data for binning and plotting. If dict-like, the key providing an array-like 
        to plot must be given to var keyword argument.

    Other Parameters
    ----------
    var    : string
        Name of key in dict-like input that contains data
    levels : array-like, up to 5 levels
        Breaks between levels in data that should be shown as distinct colors
    target : figure or axes
        Target axes or figure window
    colors : array-like
        Colors to use for the color sequence (if insufficient colors, will use as a cycle)
    **kwargs : other keywords
        Other keywords to pass to spacepy.toolbox.binHisto

    Returns
    -------
    binned : tuple
        Tuple of the binned data and bins

    Examples
    --------
    >>> import spacepy.plot
    >>> spacepy.plot.levelHist(indata)

    """
    from spacepy.toolbox import binHisto
    #assume dict-like/key-access, before moving to array-like
    if var is not None:
        try:
            usearr = data[var]
        except KeyError:
            raise KeyError('')
    binwidth, nbins = binHisto(usearr, )
    fig, ax = set_target()
    ax.hist(data, bins=nbins, histtype='step', normed=True)
