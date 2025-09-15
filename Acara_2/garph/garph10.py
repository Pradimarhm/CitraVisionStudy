import matplotlib.pyplot as plt
import numpy as np


def identify_axes(ax_dict, fontsize=48):
    kw = dict(ha="center", va="center", fontsize=fontsize, color="darkgrey")
    for k, ax in ax_dict.items():
        ax.text(0.5, 0.5, k,
    transform=ax.transAxes, **kw)

np.random.seed(19680801)
hist_data = np.random.randn(1_500)

mosaic = """AA
 BC"""
fig = plt.figure()
axd = fig.subplot_mosaic(
    mosaic,
    gridspec_kw={
    "bottom": 0.25,
    "top": 0.95,
    "left": 0.1,
    "right": 0.5,
    "wspace": 0.5,
    "hspace": 0.5,
    },
)
identify_axes(axd)
axd = fig.subplot_mosaic(
    mosaic,
    gridspec_kw={
    "bottom": 0.05,
    "top": 0.75,
    "left": 0.6,
    "right": 0.95,
    "wspace": 0.5,
    "hspace": 0.5,
    },
)
identify_axes(axd)



plt.show()
