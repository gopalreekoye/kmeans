#reekoye gopal
#rkygop001
#20/05/2021

#test module

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from kmeans import KMeans

df=pd.DataFrame({
    'x': [2,2,8,5,7,6,1,4],
    'y': [10,5,4,8,5,4,2,9]})

print(pd.shape)

clusters = len(np.unique(pd))
print(clusters)

k=KMeans(K=clusters, max_iters=150, plot_steps=False)
y-pred=k.predict(pd)

k.plot()
