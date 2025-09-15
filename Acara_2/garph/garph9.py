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
    """
    .a.
    bAc
    .d.
    """,
        gridspec_kw={
        # set the height ratios between the rows
        "height_ratios": [1, 3.5, 1],
        # set the width ratios between the columns
        "width_ratios": [1, 3.5, 1],
        },
    )
identify_axes(axd)

plt.show()
