

# ----insert sort-----------
def insert_sort(L):
    for j in range(1,len(L)):
        key = L[j]
        i = j-1
        while i >= 0 and L[i] > key:
            L[i+1] = L[i]
            i = i-1
        L[i+1] = key
    return L

# ---merge sort ---------
def Merge(a,b):
    c=[]
    while len(a)!=0 and len(b)!=0:
        if a[0] > b[0]:
            c.append(b[0])
            b.pop(0)
        else:
            c.append(a[0])
            a.pop(0)
    return c+a+b


def merge_sort(l):
    n = len(l)
    L = l[:n//2]
    R = l[n//2:]
    if len(L) != 1:
        L = merge_sort(L)
    if len(R)!=1:
        R = merge_sort(R)
    return Merge(L, R)

# ----------Quick sort----------
def partition(A, p, q):
    x = A[p]
    i = p
    for j in range(p+1, q+1):
        if A[j] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i]
    A[i],A[p]=A[p],A[i]
    return A, i


def Quick_sort(A, p, r):
    if p < r:
        A,q=partition(A,p,r)
        A = Quick_sort(A, p, q-1)
        A = Quick_sort(A, q+1, r)
    return A


# -----------Count Sort------------
def count_sort(A):
    k = max(A)
    n = len(A)
    B = [0]*n
    C = [0]*k
    for j in A:
        C[j-1] = C[j-1]+1
    for i in range(1,k):
        C[i] = C[i] + C[i-1]
    for j in A[::-1]:
        B[C[j-1]-1]= j
        C[j-1] = C[j-1]-1
    return B



# -------Radicsort------------
def radix_sort(L):
    n = len(L)
    for i in range(3):
        A = [x//(10**i)%10 for x in L]
        k = max(A)
        B = [0] * n
        C = [0] * k
        for j in A:
            C[j - 1] = C[j-1] + 1
        for i in range(1, k):
            C[i] = C[i] + C[i-1]
        for j in range(n)[::-1]:
            B[C[A[j]-1]-1] = L[j]
            C[A[j]-1] = C[A[j]-1]-1
        L = B
    return L



A = [236, 455, 128, 133, 269, 421, 536, 768]
# print(insert_sort(list(A)))
# print(merge_sort(list(A)))
# print(Quick_sort(list(A), 0, len(A)-1))
print(count_sort(A))
print(radix_sort(A))
# print(list(A))

