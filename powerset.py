"""
Write a function that takes in an array of unique integers and returns its powerset.
Complexity: Space: O(n*2^n) | Time: O(n*2^n)
"""
def powerset(array):
    res = [[]] 
    for num in array:
        #Add subsets before the actual number
        for i in range(len(res)):
            currentSubset = res[i]
            res.append(currentSubset + [num])
    return res

def powersetrecursive(array, idx=None):
    if idx is None:
        idx = len(array) - 1
    if idx < 0:
        return [[]]
    num = array[idx]
    subsets =powersetrecursive(array, idx-1)
    for i in range(len(subsets)):
        currentSubset = subsets[i]
        subsets.append(currentSubset + [num])
    return subsets

if __name__ == "__main__":
    # execute only if run as a script
    print(powerset([1,2,3]))
    print(powersetrecursive([1,2,3,4]))