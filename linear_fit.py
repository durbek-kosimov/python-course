import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')
%matplotlib inline

sns.lmplot('weight', 'mpg', data=df) # fit linear equation line
plt.show()
