#import numpy module
import numpy as np

#define numpy array as input
x=np.array([1,2,3,4,5])

# define the no of column 
N =3

#Show vander array out put Method1
np.vander(x,increasing=True)

#show Vander array out with Method2
np.column_stack([x**(N-1-i) for i in range(N)])

