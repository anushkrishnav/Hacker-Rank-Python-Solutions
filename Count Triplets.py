from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):
    v2 = defaultdict(int)
    print(v2)
    v3 = defaultdict(int)
    print(v3)
    count = 0
    for k in arr:
        count += v3[k]
        v3[k*r] += v2[k]
        v2[k*r] += 1

    return count

if __name__ == '__main__':
    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)
    print(ans)