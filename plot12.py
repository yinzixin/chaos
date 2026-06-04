import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# dx/dt = sin(x)
# Analytical solution: x(t) = 2 * arctan(tan(x0/2) * exp(t))
# This comes from the implicit formula t = ln|(csc x0 + cot x0) / (csc x + cot x)|


ode = lambda _t, x: [np.sin(x[0])]

t_eval = np.linspace(0, 7, 800)

fig, ax = plt.subplots(figsize=(8, 6))

# Initial conditions in different basins
x0_positive = [ 0, 0.2, 0.25*np.pi, 0.6*np.pi, np.pi]   # (0, pi)  → converge to pi
x0_negative = [-0.2, -0.25*np.pi,- 0.6*np.pi, -np.pi]  # (-pi, 0) → converge to -pi
x0_high     = [3.5, 4.5, 5.0,  2*np.pi-0.01]         # (pi, 2pi) → converge to pi (numerical only)

cmap_pos = plt.cm.Blues(np.linspace(0.4, 0.9, len(x0_positive)))
cmap_neg = plt.cm.Oranges(np.linspace(0.4, 0.9, len(x0_negative)))
cmap_hi  = plt.cm.Greens(np.linspace(0.4, 0.9, len(x0_high)))

# Positive basin
for x0, c in zip(x0_positive, cmap_pos):
    sol = solve_ivp(ode, (0, 7), [x0], t_eval=t_eval, max_step=0.02)
    ax.plot(sol.t, sol.y[0], '-', color=c, lw=1.5, alpha=0.8)
    ax.plot(0, x0, 'o', color=c, ms=5, zorder=5)

# Negative basin: numerical only (formula works symmetrically)
for x0, c in zip(x0_negative, cmap_neg):
    sol = solve_ivp(ode, (0, 7), [x0], t_eval=t_eval, max_step=0.02)
    ax.plot(sol.t, sol.y[0], '-', color=c, lw=1.5, alpha=0.8)
    ax.plot(0, x0, 'o', color=c, ms=5, zorder=5)

# High basin: numerical only
for x0, c in zip(x0_high, cmap_hi):
    sol = solve_ivp(ode, (0, 7), [x0], t_eval=t_eval, max_step=0.02)
    ax.plot(sol.t, sol.y[0], '-', color=c, lw=1.5, alpha=0.8)
    ax.plot(0, x0, 'o', color=c, ms=5, zorder=5)

# Fixed points
stable_fps   = [-np.pi, np.pi]
unstable_fps = [-2*np.pi, 0, 2*np.pi]
for fp in stable_fps:
    ax.axhline(fp, color='green', ls='--', lw=1, alpha=0.5)
for fp in unstable_fps:
    ax.axhline(fp, color='red', ls=':', lw=1, alpha=0.5)

ax.set_yticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi])
ax.set_yticklabels([r'$-2\pi$', r'$-\pi$', r'$0$', r'$\pi$', r'$2\pi$'])
ax.set_xlabel('$t$', fontsize=13)
ax.set_ylabel('$x(t)$', fontsize=13)
ax.set_title(r'Solution trajectories of $\dot{x} = \sin x$', fontsize=13)
ax.set_ylim(-np.pi - 0.4, 2*np.pi + 0.4)
ax.grid(True, alpha=0.25)

# Legend proxy
# from matplotlib.lines import Line2D
# handles = [
#     Line2D([0], [0], color='steelblue',  lw=2, label=r'$x_0\in(0,\pi)$'),
#     Line2D([0], [0], color='darkorange', lw=2, label=r'$x_0\in(-\pi,0)$'),
#     Line2D([0], [0], color='seagreen',   lw=2, label=r'Numerical: $x_0\in(\pi,2\pi)$'),
#     Line2D([0], [0], color='green', lw=1, ls='--', label=r'Stable FP ($\pm\pi$)'),
#     Line2D([0], [0], color='red',   lw=1, ls=':', label=r'Unstable FP ($0,\pm2\pi$)'),
# ]
# ax.legend(handles=handles, fontsize=8, loc='lower right')


plt.tight_layout()
plt.savefig('plot12.png', dpi=150, bbox_inches='tight')
plt.show()
