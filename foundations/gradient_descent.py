class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        x=init
        if iterations==0:
            return round(x,5)
        for i in range(iterations):
            grad=2*x
            x=x-learning_rate*grad
        return round(x,5)

        
