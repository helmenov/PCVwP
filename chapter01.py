#%% 
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
plt.style.use(['science','ieee'])

#%%
im = np.array(Image.open('data/empire.jpg'))

#%%
# Jupyterではセルをまたいで上書きできない．
fig = plt.figure()

#%%
ax1 = fig.add_subplot(1,1,1)
ax1.imshow(im)
fig

#%% (100,200),...,(400,500)
x = [100, 100, 400, 400]
y = [200, 500, 200, 500]

#%%
ax1.plot(x,y,'r*')
fig

#%% (100,200)-(100,500)-(400,200)
ax1.plot(x[:3],y[:3])
fig

#%%
ax1.set_title('Plotting: "empire.jpg"')
fig

# %%
