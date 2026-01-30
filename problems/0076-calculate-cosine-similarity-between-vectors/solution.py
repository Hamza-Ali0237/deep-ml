
import numpy as np

def cosine_similarity(v1, v2):
	# Implement your code here
    if v1.shape == v2.shape:
        dot_prod = np.dot(v1, v2)
        v1_norm = np.linalg.norm(v1, ord=2)
        v2_norm = np.linalg.norm(v2, ord=2)
        norm_mult = v1_norm * v2_norm
        cos_sim = dot_prod / norm_mult
        return cos_sim
    else:
        return None
