import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

fig, ax = plt.subplots(figsize=(14, 6))

x = np.linspace(-2*np.pi, 3*np.pi, 1000)
y = np.sin(x)

# Plot the sine curve
ax.plot(x, y, 'k-', linewidth=2.5)

# Set axis limits
ax.set_xlim(-2.5*np.pi, 3.5*np.pi)
ax.set_ylim(-1.5, 1.5)

# Draw axes
ax.axhline(y=0, color='k', linewidth=1)
ax.axvline(x=0, color='k', linewidth=1)

# Add arrows at axis ends
arrow_x1 = FancyArrowPatch((0.45*np.pi, 0), (0.6*np.pi, 0),
                          arrowstyle='-|>', mutation_scale=25, 
                          linewidth=2, color='black')
ax.add_patch(arrow_x1)

arrow_x2 = FancyArrowPatch((1.45*np.pi, 0), (1.6*np.pi, 0),
                          arrowstyle='<|-', mutation_scale=25, 
                          linewidth=2, color='black')
ax.add_patch(arrow_x2)

arrow_x3 = FancyArrowPatch((2.45*np.pi, 0), (2.6*np.pi, 0),
                          arrowstyle='-|>', mutation_scale=25, 
                          linewidth=2, color='black')
ax.add_patch(arrow_x3)


arrow_x1m = FancyArrowPatch((-0.45*np.pi, 0), (-0.6*np.pi, 0),
                          arrowstyle='-|>', mutation_scale=25, 
                          linewidth=2, color='black')
ax.add_patch(arrow_x1m)

arrow_x2m = FancyArrowPatch((-1.45*np.pi, 0), (-1.6*np.pi, 0),
                          arrowstyle='<|-', mutation_scale=25, 
                          linewidth=2, color='black')
ax.add_patch(arrow_x2m)

arrow_x3m = FancyArrowPatch((-2.45*np.pi, 0), (-2.6*np.pi, 0),
                          arrowstyle='-|>', mutation_scale=25, 
                          linewidth=2, color='black')
ax.add_patch(arrow_x3m)

 

# Add tick marks and labels
ticks_x = [0, np.pi, 2*np.pi]
labels_x = ['0', 'π', '2π']
ax.set_xticks(ticks_x)
ax.set_xticklabels(labels_x)

# Remove default spines for cleaner look
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# Add axis labels
ax.text(3.5*np.pi, -0.15, 'x', fontsize=14, fontweight='bold')
ax.text(-0.1, 1.5, 'dx/dt', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()