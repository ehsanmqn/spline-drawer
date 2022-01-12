import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

# 
# Draw spline curve by given points
# 
def draw_spline_by_points(x, y, k, file=None):

    # Prepare tck
    l = len(x)
    t = np.linspace(0, 1, l - 2, endpoint=True)
    t = np.append([0, 0, 0], t)
    t = np.append(t, [1, 1, 1])
    tck = [t, [x, y], k]
    u3 = np.linspace(0, 1, (max(l * 2, 70)), endpoint=True)

    # Evaluate
    out = interpolate.splev(u3, tck)

    # Read image from disk
    img = plt.imread(file)

    # Plot it
    fig, ax = plt.subplots()
    ax.imshow(img)
    ax.plot(x, y, 'k--', label='Control polygon', marker='o', markerfacecolor='red')
    ax.plot(out[0], out[1], 'b', linewidth=2.0, label='B-spline curve')
    ax.axis('off')

    # Save result into statics files
    filename =  "static/" + file.split('/')[-1:][0].split('.')[0] +  "-draw.jpg"
    plt.savefig(filename)
    plt.close()

    return filename

# 
# Interpolate points and draw spline curve
# 
def interpolate_and_draw_spline_by_points(x, y, k, file=None):

    # Prepare tck
    tck, u = interpolate.splprep([x, y], k=k, s=0)
    u = np.linspace(0, 1, num=50, endpoint=True)
    out = interpolate.splev(u, tck)

    # Read image from disk
    img = plt.imread(file)

    # Plot it
    fig, ax = plt.subplots()
    ax.imshow(img)
    ax.plot(x, y, 'k--', label='Control polygon', marker='o', markerfacecolor='red')
    ax.plot(out[0], out[1], 'b', linewidth=2.0, label='B-spline curve')
    ax.axis('off')

    # Save result into statics files
    filename = "static/" + file.split('/')[-1:][0].split('.')[0] + "-interpolate.jpg"
    plt.savefig(filename)
    plt.close()

    return filename