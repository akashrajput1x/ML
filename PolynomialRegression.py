import numpy as np

class PolynomialRegression:
    
    def fit(self, x, y, learning_rate = 1, no_of_iterations = 10000):
        """
        m samples of n dimensional data
        x = [[x11, x12...x1n],
             [x21, x22...[2n],
             ...
             [xm1, xm2...[mn]]
    
        m outputs for m samples of data
        y = [y1, y2, y3...ym]

        """
        # no of dimensions in data and no of samples of data
        dimensions = len(x[0])
        
        a = learning_rate                               #learning rate
        n = no_of_iterations                            #no of iterations
        self.p = np.ones(dimensions)                    #power
        self.w = np.zeros(dimensions)                   #slope
        self.b = 0                                      #constant

        for iteration in range(n):

            yh = self.predict(x)
            
            """
            Function(yh, y) = (yh - y)^2

            Cost Function = (1 / m) Summation of(i = 1 to m)  Function (yh(i), y(i))
            """
            # error between predicted value and true value
            error = yh - y
            """
            # # reducing of cost using gradient descent
            # # gradient descent with respect to power of each dimension
            # for i in range(dimensions):
            #     dimension = x[:, i]
            #     log_dimension = np.log(dimension)
            #     self.p[i] -= a * (error * self.w[i] * log_dimension * dimension ** self.p[i]).mean()

            # # gradient descent with respect to slope of each dimensione
            # # because of slow learning rate using of changed power will not effect much
            # for i in range(dimensions):
            #     dimension = x[:, i]
            #     self.w[i] -= a * (error * dimension ** self.p[i]).mean()

            # # gradient descent with respect to constant
            # self.b -= a * error.mean()
            """

            """ Vectorization of reducing of cost"""
            
            log_dimensions = np.log(x)                                          # log of dimensions
            dimension_powers = x ** self.p                                      # dimension values with their powers
            error_term = error[:, np.newaxis] * dimension_powers                # Error term is error * dimension_powers
            self.p -= a * (error_term * self.w * log_dimensions).mean(axis=0)   # Gradient descent with respect to power of each dimension
            self.w -= a * error_term.mean(axis=0)                               # Gradient descent with respect to slope of each dimension
            self.b -= a * error.mean()                                          # Gradient descent with respect to constant


    def predict(self, x):
        # # predicting values using row approach
        # yh = np.zeros(samples)
        # for i in range(samples):
        #     yh[i] = self.predict(x[i])

        # # predicting values column approach
        # # column is preferred becuase of parallel multiplication of vector
        # yh = np.zeros(len(x))
        # for i in range(len(x[0])):
        #     dimension = x[:, i]
        #     yh += self.w[i] * np.power(dimension, self.p[i])
        # yh += self.b
        
        """Vectorization of prediction"""
        dimension_powers = x ** self.p                        # dimension values with their powers
        yh = np.sum(self.w * dimension_powers, axis=1)        # Compute the weighted sum of the dimension powers
        yh += self.b                                          # Add the constant term
        return yh

    def print(self):
        print()
        print("Power : ", self.p)
        print("Slope : ", self.w)
        print("Constant : ", self.b)
        print()

if __name__ == "__main__":

    x = np.array([
        [0.1, 0.2],
        [0.3, 0.3],
        [0.5, 0.4],
        [0.6, 0.7],
        [1, 0.9]
        ])
    y = np.array([0.001, 0.027, 0.125, 0.343, 1])
    model = PolynomialRegression()
    model.fit(x, y)
    model.print()

    data = np.array([[8, 5]])
    print(f"Predicted value for {data} : {model.predict(data)}")