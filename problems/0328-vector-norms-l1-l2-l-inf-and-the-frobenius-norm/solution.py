import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.
    
    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', or 'frobenius')
    
    Returns:
        The computed norm as a float
    """
    if norm_type == "l1":
        l1_norm = np.linalg.norm(arr, ord=1)
        l1_norm = l1_norm.astype(np.float16)
        return f"{l1_norm:.4f}" 
    elif norm_type == "l2":
        l2_norm = np.linalg.norm(arr, ord=2)
        l2_norm = l2_norm.astype(np.float16)    
        return f"{l2_norm:.4f}"
    elif norm_type == "frobenius":
        if arr.ndim == 2:
            fro_norm = np.linalg.norm(arr, ord='fro')
            # fro_norm = fro_norm.astype(np.float16)
            return fro_norm
        else:
            return None
    else:
        return None