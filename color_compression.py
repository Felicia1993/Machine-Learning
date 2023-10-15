from sklearn.datasets import load_sample_image
import matplotlib.pyplot as plot
import numpy as np
import warnings; warnings.simplefilter('ignore')
from sklearn.cluster import MiniBatchKMeans



image = load_sample_image("flower.jpg")
axes = plot.axes(xticks=[], yticks=[])
axes.imshow(image)
# plot.show()

shape = image.shape
print(shape)

data = image / 255.0 # use 0...1 scale
data = data.reshape(427 * 640, 3)
print(data)

def plot_pixels(data, title, colors=None, N=10000):
    if colors == None:
        colors = data
    rng = np.random.RandomState(0)
    i = rng.permutation(data.shape[0])[:N]
    colors = colors[i]
    R,G,B = data[i].T
    fig,ax = plot.subplots(1,2,figsize=(16,6))
    ax[0].scatter(R,G,color  = colors, marker = '.' )
    ax[0].set(xlabel = 'Red', ylabel = 'Green', xlim=(0,1), ylim=(0,1))
    ax[1].scatter(R, G, color=colors, marker='.')
    ax[1].set(xlabel='Red', ylabel='Blue', xlim=(0, 1), ylim=(0, 1))
    fig.suptitle(title, size=20)


# plot_pixels(data, title="Input color space: 16 million possible colors")

k_means = MiniBatchKMeans(16)
k_means.fit(data)

new_colors = k_means.cluster_centers_[k_means.predict(data)]
plot_pixels(data, colors=new_colors, title='reduce color space: 16 color')
colors_reshape = new_colors.reshape(image.shape)
fig, ax = plot.subplots(1, 2, figsize=(16, 6), subplot_kw=dict(xticks=[], yticks=[]))
fig.subplots_adjust(wspace=0.05)
ax[0].imshow(image)
ax[0].set_title('original image')
ax[1].imshow(colors_reshape)
ax[1].set_title('16-color image', size= 16)
plot.show()



