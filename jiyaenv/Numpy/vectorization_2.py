import numpy as np

restaurants=np.array(['KFC','McD','Subway','PizzaHut','Dominos'])

vactorized_upper=np.vectorize(str.upper)
print(vactorized_upper(restaurants))

