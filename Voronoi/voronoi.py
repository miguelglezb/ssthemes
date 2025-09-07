import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

npoints = np.random.randint(10,15)
points = np.random.rand(npoints, 2)  # 10 random points in 2D

# Compute the Voronoi tessellation
vor = Voronoi(points)

# Plot the Voronoi tessellation
fig, ax = plt.subplots()
voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='orange')
ax.plot(points[:, 0], points[:, 1], 'bo')  # Plot the original points
plt.show()


#TODO: Function that fills the cells with an increasing circle. 