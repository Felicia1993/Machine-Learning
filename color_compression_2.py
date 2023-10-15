from sklearn.datasets import load_sample_image
import matplotlib.pyplot as plt
import numpy as np
import warnings; warnings.simplefilter('ignore')
from sklearn.cluster import MiniBatchKMeans

image = load_sample_image("china.jpg")
plt_axes = plt.axes(xticks=[], yticks=[])
plt_axes.imshow(image)
plt.show()

data = image / 255.0
data = data.reshape(427 * 640, 3)
data.shape

def plot_pixels(data, title, colors=None, N=10000):
    if colors is None:
        colors = data

    state = np.random.RandomState(0)
    i = state.permutation(data.shape[0])[:N]
    print("i = ", i)
    colors = colors[i]
    R,G,B = data[i].T
    fig, ax = plt.subplots(1, 2, figsize=(16, 6))
    fig.suptitle(title, size=20)
    ax[0].scatter(R,G,color=colors, marker='.')
    ax[0].set(xlabel='Red', ylabel='Green', xlim=(0,1), ylim=(0,1))
    ax[1].scatter(R, B, color=colors, marker='.')
    ax[1].set(xlabel='Red', ylabel='Blue', xlim=(0, 1), ylim=(0, 1))

plot_pixels(data, 'Input color shape: 16 million possible color')
# plt.show()

k_means = MiniBatchKMeans(16)
k_means.fit(data)
predict_data = k_means.cluster_centers_[k_means.predict(data)]
plot_pixels(data, 'reduced color shape: 16 color',predict_data)

image_recolored = predict_data.reshape(image.shape)
fig, ax = plt.subplots(1,2, figsize=(16,6))
fig.subplots_adjust(wspace=0.05)
ax[0].imshow(image)
ax[0].set_title('Original image', size=16)
ax[1].imshow(image_recolored)
ax[1].set_title('16-color image', size=16)
plt.show()




