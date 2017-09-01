class LinearProg:
    def __init__(self,constraints_matrix,optimizing_parameter):
        #Linear Programming involves constraints and a LINEAR optimizing function
        self.constraints=constraints_matrix
        self.parameters=optimizing_parameter
        #The above parameters are numpy matrices,that characterize the problem

    #This function finds the optimum of the given objective function within the feasible region (charecrterized by the constraints)
    def optimize(self):

        # TODO Implement using Simplex algorithm
        pass
