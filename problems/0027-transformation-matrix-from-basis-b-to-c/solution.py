def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	import numpy as np

    B = np.array(B)
    C = np.array(C)

    C_inv = np.linalg.inv(C)
    P = np.matmul(C_inv, B)
    
    return P