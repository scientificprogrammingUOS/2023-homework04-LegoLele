import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    if (isinstance(loc, int or float) == False):
        raise TypeError("Given parameter loc is not of type int or float")
    if (isinstance(scale, int or float) == False):
        raise TypeError("Given parameter scale is not of type int or float")
    if (isinstance(lower_bound, int or float) == False):
        raise TypeError("Given parameter lower_bound is not of type int or float")
    if (isinstance(upper_bound, int or float) == False):
        raise TypeError("Given parameter upper_bound is not of type int or float")
    if (upper_bound <= lower_bound):
        raise ValueError("Given parameter upper_bound has to be greater than given parameter lower_bound")

    array = np.random.normal(loc=loc, scale=scale, size=100)

    filter1 = array >= lower_bound
    array = array[filter1]
    filter2 = array <= upper_bound
    array = array[filter2]

    mean = np.mean(array)
    std = np.std(array)

    return (mean, std)


if __name__ == "__main__":
   print(gaussian_analysis(200, 100, 5, 100))
