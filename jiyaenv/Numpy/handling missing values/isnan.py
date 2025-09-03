#np.isnan(array)

import numpy as np

arr=np.array([1,2,np.nan,4,np.nan,5])

print(np.isnan(arr))

#not
print(np.nan == np.nan)