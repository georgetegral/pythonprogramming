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

if __name__ == "__main__":
    # execute only if run as a script
    print(powerset([1,2,3]))