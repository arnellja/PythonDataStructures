lyst = [100,200, 300, 500, 500, 675, 800]
target = 675

def binary_search_recursion (lyst, target, low_point, high_point):
    if (lyst[len(lyst)/2] > target):
        return binary_search_recursion(lyst, target, low_point, len(lyst)/2)
    elif (lyst[len(lyst)/2] < target):
        return binary_search_recursion(lyst, target, len(lyst)/2, high_point)
    else:
        return True

if (binary_search_recursion(lyst, target, 0, len(lyst))):
    print("the target was ", target)