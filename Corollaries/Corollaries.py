#!/usr/bin/env python
# coding: utf-8

# Corollaries
# ---

# # Import Libraries

# In[2]:


import numpy as np 
from matplotlib import pyplot as plt 
import matplotlib.patches as mpatches


# # Corollary on PC-lite 

# The related equation on the emergence of extreme tendencies on PC-lite model is descibed as below: 
# 
# $$\gamma_{\mathcal{B}} = \frac{(1+\alpha)}{\alpha(1 - \alpha)}$$
# 
# or which is simply a two-degree equation as given below;
# 
# $$\gamma_{\mathcal{B}} \alpha^2 + \left(1-\gamma_{\mathcal{B}}\right) \alpha + 1 = 0$$
# 
# which will have two roots described as below; 
# 
# $$\alpha_1 = \frac{-(1-\gamma_{\mathcal{B}}) 
# - \sqrt{\left(1-\gamma_{\mathcal{B}}\right)^2 - 4\gamma_{\mathcal{B}}}}{2\gamma_{\mathcal{B}}}$$
# 
# 
# $$\alpha_2 = \frac{-(1-\gamma_{\mathcal{B}}) 
# - \sqrt{\left(1-\gamma_{\mathcal{B}}\right)^2 + 4\gamma_{\mathcal{B}}}}{2\gamma_{\mathcal{B}}}$$
# 
# We will write a function named ```PCLiteRoots(gammaB)``` to derive the roots for the given $\alpha \in [0,1]$ and $\gamma_{\mathcal{B}} > \left(3 + 2\sqrt{2}\right)$

# In[10]:


def PCLiteRoots(gammaB): 
    alpha_1 = np.array((-(1-gammaB) - np.sqrt((1 - gammaB) ** 2 - 4 * gammaB)) / (2 * gammaB))
    alpha_2 = np.array((-(1-gammaB) + np.sqrt((1 - gammaB) ** 2 - 4 * gammaB)) / (2 * gammaB))
    return alpha_1, alpha_2


# Lets calculate the roots for $\alpha \in [0,1]$ and $\gamma_{\mathcal{B}} \in \Big[3+2\sqrt{2}, 100\Big)$

# In[23]:


start_1 = 3 + 2 * np.sqrt(2)
GammaB_1 = np.arange(start_1, 100, 0.01)

alpha_1_PClite, alpha_2_PClite = PCLiteRoots(GammaB_1)


# Lets plot the roots!

# In[71]:


#Plot setting
color1 = '#7c2a20'
color2 = '#34475b'
ratio = 2
plt.figure(figsize = [4 * ratio, 3 * ratio])
FontS = 10
linewidthM = 2.5
plt.rcParams.update(plt.rcParamsDefault)
plt.rcParams['text.usetex'] = True
plt.rcParams['font.size'] = FontS
plt.rcParams['font.family'] = "serif"
plt.rcParams['font.serif']= "Computer Modern"

plt.plot(GammaB_1, alpha_1_PClite, color = color1, linewidth = linewidthM)
plt.plot(GammaB_1, alpha_2_PClite, color = color2, linewidth = linewidthM)

patch1 = mpatches.Patch(color = color1, label = r'$\alpha_1$')
patch2 = mpatches.Patch(color = color2, label = r'$\alpha_2$')
plt.legend(handles = [patch1, patch2], loc ='upper center', bbox_to_anchor = (0.5, 1.10), frameon = 1, ncol = 2)
plt.rcParams.update({'font.size':FontS})

plt.xlabel(r'$\gamma_{\mathcal{B}}$', fontsize = FontS)
plt.ylabel(r'$\alpha$', fontsize = FontS)
plt.xlim(0, 100)
plt.ylim(0, 1)
x_ticks = [0, start_1, 20, 40, 60, 80, 100]
x_label = ['0',r'$\quad 3+2\sqrt{2}$','20', '40','60','80','100']
plt.xticks(x_ticks, x_label, fontsize = FontS)
plt.savefig("PC-LiteCorollary.png", format = 'png', dpi = 500)
plt.show()


# The result is 
# ![Corollary 1](PC-liteCorollary.png)

# # Corollary on PC 

# The related equation on the emergence of extreme tendencies on PC model is descibed as below: 
# 
# $$\frac{\gamma_{\mathcal{B}}}{d} = \frac{(1+\alpha)}{\alpha(1 - \alpha)}$$
# 
# or which is simply a two-degree equation as given below;
# 
# $$\gamma_{\mathcal{B}} \alpha^2 + \left(d-\gamma_{\mathcal{B}}\right) \alpha + d\gamma_{\mathcal{B}} = 0$$
# 
# which will have two roots described as below; 
# 
# $$\alpha_1 = \frac{-(d-\gamma_{\mathcal{B}}) 
# - \sqrt{\left(d-\gamma_{\mathcal{B}}\right)^2 - 4d\gamma_{\mathcal{B}}}}{2\gamma_{\mathcal{B}}}$$
# 
# 
# $$\alpha_2 = \frac{-(d-\gamma_{\mathcal{B}}) 
# - \sqrt{\left(d-\gamma_{\mathcal{B}}\right)^2 + 4d\gamma_{\mathcal{B}}}}{2\gamma_{\mathcal{B}}}$$
# 
# We will write a function named ```PCRoots(d, gammaB)``` to derive the roots for the given $\alpha \in [0,1]$ and $\gamma_{\mathcal{B}} > \left(3 + 2\sqrt{2}\right)d$

# In[72]:


def PCRoots(d, gammaB): 
    alpha_1 = np.array((-(d-gammaB) - np.sqrt((d - gammaB) ** 2 - 4 * gammaB)) / (2 * gammaB))
    alpha_2 = np.array((-(d-gammaB) + np.sqrt((d - gammaB) ** 2 - 4 * gammaB)) / (2 * gammaB))
    return alpha_1, alpha_2


# Lets calculate the roots for $\alpha \in [0,1]$, $\gamma_{\mathcal{B}} \in \{\big(3+2\sqrt{2}\big), 10, 30\}$ and 
# $d\in [0, 1]$

# In[77]:


GammaB_2 = 3 + 2 * np.sqrt(2)
GammaB_3 = 10
GammaB_4 = 30
d = np.arange(0, 1, 10 ** (-5))
alpha_1_PC1, alpha_2_PC1 = PCRoots(d, GammaB_2) 
alpha_1_PC2, alpha_2_PC2 = PCRoots(d, GammaB_3) 
alpha_1_PC3, alpha_2_PC3 = PCRoots(d, GammaB_4) 


# Lets plot the roots!

# In[88]:


# Plot setting 
color1 = '#7c2a20'
color2 = '#34475b'
ratio = 2
plt.figure(figsize = [4 * ratio, 3 * ratio])
FontS = 16
linewidthM = 2.5
LS1, LS2, LS3='-', '-.', '--'
plt.rcParams.update(plt.rcParamsDefault)
plt.rcParams['text.usetex'] = True
plt.rcParams['font.size'] = FontS
plt.rcParams['font.family'] = "serif"
plt.rcParams['font.serif']= "Computer Modern"



plt.plot(d, alpha_1_PC1, color = color1, linewidth = linewidthM, linestyle = LS1)
plt.plot(d, alpha_1_PC2, color = color1, linewidth = linewidthM, linestyle = LS2)
plt.plot(d, alpha_1_PC3, color = color1, linewidth = linewidthM, linestyle = LS3)

plt.plot(d, alpha_2_PC1, color = color2, linewidth = linewidthM, linestyle = LS1)
plt.plot(d, alpha_2_PC2, color = color2, linewidth = linewidthM, linestyle = LS2)
plt.plot(d, alpha_2_PC3, color = color2, linewidth = linewidthM, linestyle = LS3)



plt.text(0.75, 0.57, '$\gamma_B= 3+2\sqrt{2}$',fontsize = FontS,  color = 'black',
         bbox = dict(facecolor = 'white', edgecolor = '#e1e0e1' , boxstyle = 'round'))
plt.text(0.82, 0.80, '$\gamma_B= 10$',fontsize = FontS,  color = 'black',
         bbox = dict(facecolor = 'white', edgecolor = '#e1e0e1' , boxstyle = 'round'))
plt.text(0.65, 0.94, '$\gamma_B= 30$', fontsize = FontS,  color = 'black', 
         bbox = dict(facecolor = 'white', edgecolor = '#e1e0e1' , boxstyle = 'round'))

patch1 = mpatches.Patch(color = color1, label = r'$\alpha_1$')
patch2 = mpatches.Patch(color = color2, label = r'$\alpha_2$')
plt.legend(handles = [patch1, patch2], loc = 'upper center', bbox_to_anchor=(0.5, 1.10), frameon = 1, ncol = 2) 

plt.xlim(0, 1)
plt.ylim(0, 1)

plt.rcParams.update({'font.size':FontS})
plt.xlabel(r'$d$', fontsize = FontS)
plt.ylabel(r'$\alpha$',fontsize = FontS)
plt.savefig("PCCorollary.png", format = 'png', dpi = 500)
plt.show()


# The result is 
# ![Corollary 2](PCCorollary.png)
