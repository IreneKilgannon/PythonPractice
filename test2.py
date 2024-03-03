import numpy as np

import random

rolls = np.random.randint(1,7, 1000)

print(rolls.mean())

print(rolls [:10])

print(unique(rolls))