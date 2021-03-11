"""
4 2
1 2 2 4

"""
"

def countTriplets(arr, r):
    counter = 0
    numbers = {}
    pairs = {}

    for i in reversed(arr):
        if r*i in pairs:
            counter += pairs[r*i]
        if r*i in numbers:
            pairs[i] = pairs.get(i,0) + numbers[r*i] 
        numbers[i] = numbers.get(i,0) + 1
    return counter 
