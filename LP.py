import numpy as np

class LinearProg:
    def __init__(self,constraints_matrix,objectives,optimizing_parameter):
        #Linear Programming involves constraints and a LINEAR optimizing function
        self.constraints=constraints_matrix
        self.parameters=optimizing_parameter
        self.objectives=objectives
        #The above parameters are numpy matrices,that characterize the problem

    #This function finds the optimum of the given objective function within the feasible region (charecrterized by the constraints)
    def optimize(self):
        #converting to standard LP form using slack Variables

        self.tableau=np.hstack([
                           np.zeros([self.constraints.shape[0],1]),
                           self.objectives,
                           self.constraints,
                           np.eye(self.constraints.shape[0])
                           ])

        print (self.tableau)
        def update_tableau(*args,**kwargs):
            #TODO update tableau function
            pass
        pass
