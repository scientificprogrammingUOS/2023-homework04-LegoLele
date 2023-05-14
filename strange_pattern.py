import numpy as np

# implement the function strange pattern

def strange_pattern(tuple: tuple):
    if (len(tuple) != 2):
        raise IndexError("The given tuple has to be of length 2")

    array = np.arange(tuple[0]*tuple[1]).reshape(tuple[0],tuple[1]).astype(bool)
    
    it_1 = 0
    for i in array:
        it_2 = 0
        for q in i:
            array[it_1][it_2] = (it_1 + it_2) % 3 == 0

            it_2 += 1
        
        it_1 += 1


    return array

def print_pattern(array: np.array):
    index = 0
    for row in array:
        # horizontal lines
        for i in array[0]:
            print("--", end="")
        print("-")

        print("|", end="")
        for value in array[index]:
            if value:
                value = "x"
            else:
                value = " "
            print(f"{value}|", end="")
        print("")
        index += 1
    
    # last line
    for i in array[0]:
        print("--", end="")
    print("-")
        


if __name__ == "__main__":
    pattern = strange_pattern((5,10))
    print_pattern(pattern)
