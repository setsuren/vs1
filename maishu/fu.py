import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

s = Series(np.random.randint(0, 10, size=30))
print(s)
print(s.plot())
s.plo