
# coding: utf-8

# In[34]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.finance as mf
from matplotlib.dates import date2num


# In[35]:

csv=pd.read_csv('USDJPY60.csv',
                 sep=',',
                 names=('YY.MM.DD', 'HH:MM', 'OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME'),
                 index_col=['YY.MM.DD', 'HH:MM'])


# In[36]:

data=csv
#data=csv['2016.11.08':'2016.11.11']
data


# In[37]:

date=[]
quote = []
for i, v in data.iterrows():
    t = pd.to_datetime(i[0] + ' ' + i[1]);
    date.append(t)
    quote.append((date2num(t), v['OPEN'], v['CLOSE'], v['HIGH'], v['LOW']))


# In[38]:

fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
ax.grid()
ax.set_xlim(date[0], date[-1])
mf.candlestick_ochl(ax, quote, width=0.02, colorup='g', colordown='r', alpha=0.75)
fig.autofmt_xdate()
plt.show()


# In[ ]:



