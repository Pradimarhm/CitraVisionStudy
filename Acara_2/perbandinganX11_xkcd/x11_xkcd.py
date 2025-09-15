import matplotlib._color_data as mcd
import matplotlib.patches as mpatch
import matplotlib.pyplot as plt
overlap = {name for name in mcd.CSS4_COLORS
    if "xkcd:" + name in mcd.XKCD_COLORS}
fig = plt.figure(figsize=[9, 5])
ax = fig.add_axes([0, 0, 1, 1])
n_groups = 3
n_rows = len(overlap) // n_groups + 1
for j, color_name in enumerate(sorted(overlap)):
    css4 = mcd.CSS4_COLORS[color_name]
    xkcd = mcd.XKCD_COLORS["xkcd:" + color_name].upper()
    col_shift = (j // n_rows) * 3
    y_pos = j % n_rows
    text_args = dict(va='center', fontsize=10, weight='bold' if css4 == xkcd else None)
    ax.add_patch(mpatch.Rectangle((0 + col_shift, y_pos), 1, 1, color=css4))
    ax.add_patch(mpatch.Rectangle((1 + col_shift, y_pos), 1, 1, color=xkcd))
    ax.text(0 + col_shift, y_pos + .5, ' ' + css4, alpha=0.5, **text_args)
    ax.text(1 + col_shift, y_pos + .5, ' ' + xkcd, alpha=0.5, **text_args)
    ax.text(2 + col_shift, y_pos + .5, ' ' + color_name, **text_args)
    
for g in range(n_groups):
    ax.hlines(range(n_rows), 3*g, 3*g + 2.8, color='0.7', linewidth=1)
    ax.text(0.5 + 3*g, -0.5, 'X11', ha='center', va='center')
    ax.text(1.5 + 3*g, -0.5, 'xkcd', ha='center', va='center')
    
ax.set_xlim(0, 3 * n_groups)
ax.set_ylim(n_rows, -1)
ax.axis('off')
plt.show()
