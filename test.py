import numpy as np
import LP
from LP import LinearProg

constraints_matrix=np.array([[1,0],[0,1]])
objectives=np.array([[1],[0]])
optimizing_parameters=np.array([4,5])
lp=LinearProg(constraints_matrix,objectives,optimizing_parameters)
lp.optimize()
