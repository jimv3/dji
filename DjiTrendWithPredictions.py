# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import fbprophet as fb
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# %%
data = pd.read_csv('DJI_monthly.csv', parse_dates=['Date'])
data.head()


# %%
data.tail()


# %%
data.plot(x='Date', y='Adj Close', kind='bar')
plt.show()


# %%
data['LogClose'] = data['Adj Close'].apply(np.log)
data.plot(x='Date', y='LogClose', kind='bar')
plt.show()


# %%
fig = go.Figure(data=go.Bar(x=data['Date'], y=data['Adj Close']))
fig.show()


# %%
