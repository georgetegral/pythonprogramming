def findThreeLargestNumbers(array):
    res = []
    for num in array:
        res = checkRes(res,num)
    return [res[2],res[1],res[0]]

def checkRes(res,num):
    n1 = None
    n2 = None
    n3 = None
    try:
        n1 = res[0]
    except:
        n1 = float('-inf')

    try:
        n2 = res[1]
    except:
        n2 = float('-inf')

    try:
        n3 = res[2]
    except:
        n3 = float('-inf')
    
    if num >= n1:
        n3 = n2
        n2 = n1
        n1 = num
    elif num >= n2:
        n3 = n2
        n2 = num
    elif num >= n3:
        n3 = num
    
    return [n1,n2,n3]

if __name__ == "__main__":
    print(findThreeLargestNumbers([20,2,50,50,4]))