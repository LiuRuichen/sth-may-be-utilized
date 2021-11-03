# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 10:43:53 2021
"""
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np


font = font_manager.FontProperties(fname = r'C:\Windows\Fonts\STKAITI.TTF', size = 15)

# center and radius
center = [0, 0, 0]
radius = 10

theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, np.pi, 100)
x = radius * np.outer(np.sin(phi), np.cos(theta)) + center[0]
y = radius * np.outer(np.sin(phi), np.sin(theta)) + center[1]
z = radius * np.outer(np.cos(phi), np.ones(np.size(theta))) + center[2]

fig = plt.figure()

#子图1：球体表面, rstride是行之间的跨度, cstride是列之间的跨度
sub = fig.add_subplot(121, projection='3d')
surf = sub.plot_surface(x, y, z, rstride = 1, cstride = 1, cmap = plt.cm.turbo, alpha = 0.8)
cb = fig.colorbar(surf, shrink = 0.4, aspect = 15)
sub.set_xlabel('x')
sub.set_ylabel('y')
sub.set_zlabel('z')
sub.set_xlim(-10, 10)
sub.set_ylim(-10, 10)
sub.set_zlim(-10, 10)
plt.title("球体", FontProperties = font)

#子图2：球体框架, rstride是行之间的跨度, cstride是列之间的跨度
sub = fig.add_subplot(122, projection='3d')
sub.plot_wireframe(x, y, z, rstride = 8, cstride = 8)
sub.set_xlabel('x')
sub.set_ylabel('y')
sub.set_zlabel('z')
sub.set_xlim(-10, 10)
sub.set_ylim(-10, 10)
sub.set_zlim(-10, 10)
plt.title('球体框架', FontProperties = font)