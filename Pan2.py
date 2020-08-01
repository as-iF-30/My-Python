import pandas as pi
import numpy as np

a = {"Name":["A", "B", "A"],"Age":[23,19,12]}
b=pi.DataFrame(a)
print(b)
c=b.groupby("Name")
print(c.sum())
print(c.agg(np.size))
