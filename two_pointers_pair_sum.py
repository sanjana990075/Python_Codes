
def pair_sum(arr, target):
    arr.sort()
    l, r = 0, len(arr)-1
    while l < r:
        s = arr[l] + arr[r]
        if s == target:
            return True
        elif s < target:
            l += 1
        else:
            r -= 1
    return False

print(pair_sum([2,7,11,15], 9))
