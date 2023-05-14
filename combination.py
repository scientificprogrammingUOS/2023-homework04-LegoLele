import numpy as np 

# implement your function to combine two numpy arrays 

def combination(arr1, arr2, axis=0):
    arr1 = np.squeeze(arr1)
    arr2 = np.squeeze(arr2)

    print(arr1)
    print(arr2)

    print(arr1.shape[axis])
    print(arr2.shape[axis])

    print(arr1.ndim)
    print(arr2.ndim)
    
    if arr1.ndim < axis+1 or arr2.ndim < axis+1:
        raise ValueError("Cannot combine arrays along the given axis. Dimensions do not match.")


    return np.concatenate((arr1, arr2), axis=axis)


if __name__ == "__main__":
    
    
    print(combination(np.ones((2,2)),  np.array([[[[1, 2], [3, 4], [5, 6]]]])))