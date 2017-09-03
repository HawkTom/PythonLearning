
def countArrangement(N):

    def helper(i, X):
        if i == 1:
            return 1
        key = (i, X)
        if key in cache:
            return cache[key]
        total = 0
        for j in range(len(X)):
            if X[j] % i == 0 or i % X[j] == 0:
                total += helper(i - 1, X[:j] + X[j + 1:])
        cache[key] = total
        print(cache)
        return total
    return helper(N, tuple(range(1, N + 1)))

# cache = {}
# print(countArrangement(5))


def singleNonDuplicate(nums):
    if len(nums) == 1:
        return nums[0]
    h0 = 0
    h1 = len(nums) - 1
    mi = (h0 + h1) // 2
    if nums[mi] == nums[mi+1]:
        if mi % 2 == 1:
            return singleNonDuplicate(nums[:mi])
        else:
            return singleNonDuplicate(nums[mi:])
    else:
        if mi % 2 == 0:
            return singleNonDuplicate(nums[:mi+1])
        else:
            return singleNonDuplicate(nums[mi+1:])



# print(singleNonDuplicate([1,1,2,2,5,5,4,4,9]))

def numberOfArithmeticSlices( A):
    n = len(A)
    total = 0
    for i in range(n-2):
        for j in range(3+i,6):
            L = A[i:j]
            print(L)
            if len(set([L[i + 1] - L[i] for i in range(len(L) - 1)])) == 1:
                total += 1
    return total

print(numberOfArithmeticSlices([1,2,3,4,5]))