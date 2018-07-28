
# coding: utf-8

# In[200]:


import matplotlib.pyplot as plt
import numpy as np


# In[201]:


n = 2000


# In[261]:


t = np.linspace(0, 20, n)


# In[262]:


def f(x):
    return [ 5 * x[i] for i in range(len(x))]


# In[263]:


#y = f(t)
# for i in range(len(t)):
    # print(t[i], y[i])


# In[264]:


import math


# In[265]:


pi = math.acos(-1)


# In[266]:


print(pi)


# In[267]:


omega = pi/4


# In[268]:


z = f(t)


# In[269]:


y = [f(t)[i] * math.sin(omega * t[i]) for i in range(n)]


# In[270]:


x = [f(t)[i] * math.cos(omega * t[i]) for i in range(n)]


# In[271]:


fig = plt.figure()


# In[272]:


from scipy.stats import multivariate_normal


# In[273]:


import matplotlib


# In[274]:


from mpl_toolkits.mplot3d import Axes3D  # 3Dプロットにはこれが必須


# In[275]:


ax = fig.add_subplot(111)


# In[276]:


ax.scatter(x, y)


# In[277]:


ax.tick_params(labelbottom="off",bottom="off") # x軸の削除
ax.tick_params(labelleft="off",left="off") # y軸の削除


# In[278]:


plt.axis("off")


# In[279]:


ax.spines["right"].set_color("none")  # 右消し
ax.spines["left"].set_color("none")   # 左消し
ax.spines["top"].set_color("none")    # 上消し
ax.spines["bottom"].set_color("none") # 下消し


# In[280]:


plt.show()

