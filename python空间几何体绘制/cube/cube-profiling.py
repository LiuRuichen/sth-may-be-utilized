import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np


font = font_manager.FontProperties(fname = r'C:\Windows\Fonts\STKAITI.TTF', size = 15)

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
z = np.linspace(-5, 5, 100)

fig = plt.figure(figsize=(13,5))

sub1 = fig.add_subplot(121, projection = '3d')
plt.title("正方体", FontProperties = font)
mesh_x, mesh_y = np.meshgrid(x, y)
surf1 = sub1.plot_surface(mesh_x, mesh_y, np.full((mesh_x.shape[0], mesh_x.shape[1]), -5), rstride = 1, cstride = 1, cmap = plt.cm.turbo, alpha = 0.8)
surf2 = sub1.plot_surface(mesh_x, mesh_y, np.full((mesh_x.shape[0], mesh_x.shape[1]), 5), rstride = 1, cstride = 1, cmap = plt.cm.turbo, alpha = 0.8)
mesh_x, mesh_z = np.meshgrid(x, z)
surf3 = sub1.plot_surface(mesh_x, np.full((mesh_x.shape[0], mesh_x.shape[1]), -5), mesh_z, rstride = 1, cstride = 1, cmap = plt.cm.turbo, alpha = 0.8)
surf4 = sub1.plot_surface(mesh_x, np.full((mesh_x.shape[0], mesh_x.shape[1]), 5), mesh_z, rstride = 1, cstride = 1, cmap = plt.cm.turbo, alpha = 0.8)
mesh_y, mesh_z = np.meshgrid(y, z)
surf5 = sub1.plot_surface(np.full((mesh_x.shape[0], mesh_x.shape[1]), -5), mesh_y, mesh_z, rstride = 1, cstride = 1, cmap = plt.cm.turbo, alpha = 0.8)
surf6 = sub1.plot_surface(np.full((mesh_x.shape[0], mesh_x.shape[1]), 5), mesh_y, mesh_z, rstride = 1, cstride = 1, cmap = plt.cm.turbo, alpha = 0.8)
cb = fig.colorbar(surf6, shrink = 0.7, aspect = 15)


r = 25
c = 25

sub2 = fig.add_subplot(122, projection = '3d')
plt.title("正方体框架", FontProperties = font)

mesh_x, mesh_y = np.meshgrid(x, y)
sub2.plot_wireframe(mesh_x, mesh_y, np.full((mesh_x.shape[0], mesh_x.shape[1]), -5), rstride = r, cstride = c, color = 'black', linewidth = 0.5)
sub2.plot_wireframe(mesh_x, mesh_y, np.full((mesh_x.shape[0], mesh_x.shape[1]), 5), rstride = r, cstride = c, color = 'black', linewidth = 0.5)

mesh_x, mesh_z = np.meshgrid(x, z)
sub2.plot_wireframe(mesh_x, np.full((mesh_x.shape[0], mesh_x.shape[1]), -5), mesh_z, rstride = r, cstride = c, color = 'black', linewidth = 0.5)
sub2.plot_wireframe(mesh_x, np.full((mesh_x.shape[0], mesh_x.shape[1]), 5), mesh_z, rstride = r, cstride = c, color = 'black', linewidth = 0.5)

mesh_y, mesh_z = np.meshgrid(y, z)
sub2.plot_wireframe(np.full((mesh_x.shape[0], mesh_x.shape[1]), -5), mesh_y, mesh_z, rstride = r, cstride = c, color = 'black', linewidth = 0.5)
sub2.plot_wireframe(np.full((mesh_x.shape[0], mesh_x.shape[1]), 5), mesh_y, mesh_z, rstride = r, cstride = c, color = 'black', linewidth = 0.5)


sub1.set_xlabel('x')
sub1.set_ylabel('y')
sub1.set_zlabel('z')

sub2.set_xlabel('x')
sub2.set_ylabel('y')
sub2.set_zlabel('z')

sub1.set_xlim(-10, 10)
sub1.set_ylim(-10, 10)
sub1.set_zlim(-10, 10)

sub2.set_xlim(-10, 10)
sub2.set_ylim(-10, 10)
sub2.set_zlim(-10, 10)

