
# coding: utf-8

# In[200]:


import matplotlib.pyplot as plt
import numpy as np


# In[201]:


n = 2000


# In[202]:


t = np.linspace(0, 40, n)


# In[203]:


def f(x):
    return [ 5 * x[i] for i in range(len(x))]


# In[204]:


#y = f(t)
# for i in range(len(t)):
    # print(t[i], y[i])


# In[205]:


import math


# In[206]:


pi = math.acos(-1)


# In[207]:


print(pi)


# In[208]:


omega = pi/4


# In[209]:


z = f(t)


# In[210]:


y = [f(t)[i] * math.sin(omega * t[i]) for i in range(n)]


# In[211]:


x = [f(t)[i] * math.cos(omega * t[i]) for i in range(n)]


# In[223]:


fig = plt.figure()


# In[224]:


from scipy.stats import multivariate_normal


# In[225]:


import matplotlib


# In[226]:


from mpl_toolkits.mplot3d import Axes3D  # 3Dプロットにはこれが必須


# In[227]:


ax = fig.add_subplot(111, projection='3d')


# In[228]:


ax.scatter3D(x, y, z)


# In[229]:


ax.tick_params(labelbottom="off",bottom="off") # x軸の削除
ax.tick_params(labelleft="off",left="off") # y軸の削除


# In[230]:


plt.axis("off")


# In[231]:


ax.spines["right"].set_color("none")  # 右消し
ax.spines["left"].set_color("none")   # 左消し
ax.spines["top"].set_color("none")    # 上消し
ax.spines["bottom"].set_color("none") # 下消し


# In[232]:


plt.show()

