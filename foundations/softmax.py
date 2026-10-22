import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        z=z-np.max(z)
        e=np.exp(z)
        return np.round(e/np.sum(e),4)
        
