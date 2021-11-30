import torch
from torchvision import transforms
import torchvision
import matplotlib.pyplot as plt
  
# 让torch判断是否使用GPU，建议使用GPU环境，因为会快很多
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
 

def get_dataloader_workers():  
    """使用4个进程来读取数据。"""
    return 4

def loaddata(batch_size):
    mnist_train = torchvision.datasets.MNIST(root = r'./data', 
                                                train = True, 
                                                download = False, 
                                                transform = transforms.ToTensor())

    mnist_test = torchvision.datasets.MNIST(root = r'./data', 
                                               train = False, 
                                               download = False, 
                                               transform = transforms.ToTensor())
    
    train_iter = torch.utils.data.DataLoader(mnist_train, 
                                         batch_size = batch_size, 
                                         shuffle = True, 
                                         num_workers = 0)

    test_iter = torch.utils.data.DataLoader(mnist_test, 
                                        batch_size = batch_size, 
                                        shuffle = False, 
                                        num_workers = 0)
    
    
    return train_iter, test_iter



def visualizing(imgs, num_rows, num_cols, titles = None, scale = 1.5):
    figsize = (num_cols * scale, num_rows * scale)
    _, axes = plt.subplots(num_rows, num_cols, figsize=figsize)
    axes = axes.flatten()
    for i, (ax, img) in enumerate(zip(axes, imgs)):
        if torch.is_tensor(img):
            # 图片张量
            ax.imshow(img.numpy())
        else:
            # PIL图片
            ax.imshow(img)
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)
        if titles:
            ax.set_title(titles[i])
    return axes


train_iter, test_iter = loaddata(8)
X_img = torch.full([70, 1, 28, 28], 0).float()

num = 0
for i in range(0, 10):  
    occupied_len = 0
    count = 0
    for X, y in train_iter:
        mask = torch.eq(y,i)
        if y[mask].shape[0] <= 7 - occupied_len:
            X_img[num: y[mask].shape[0] + num] = X[mask]
            num += y[mask].shape[0]
            occupied_len += y[mask].shape[0]
            count += 1
        else:
            X_img[num: 7 - occupied_len + num] = X[mask][0: 7 - occupied_len]
            num += (7 - occupied_len)
            break 

visualizing(
        X_img.reshape((70, 28, 28)), 10, 7)