import matplotlib.pyplot as plt
import numpy as np


def identify_axes(ax_dict, fontsize=48):
    kw = dict(ha="center", va="center", fontsize=fontsize, color="darkgrey")
    for k, ax in ax_dict.items():
        ax.text(0.5, 0.5, k,
    transform=ax.transAxes, **kw)

np.random.seed(19680801)
hist_data = np.random.randn(1_500)

axd = plt.figure(constrained_layout=True).subplot_mosaic(
    [
    ["main", "zoom"],
    ["main", "BLANK"],
    ],
    empty_sentinel="BLANK",
    gridspec_kw={"width_ratios": [2, 1]},
)
identify_axes(axd)

plt.show()
