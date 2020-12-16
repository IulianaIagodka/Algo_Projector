import sys

dp = [[[-1 for i in range(3)] for j in range(2)] for k in range(1)]
print(dp)
def countString(zeroes, ones, strArr, i):
    if zeroes < 0 or ones < 0:
        return -sys.maxsize - 1
    if i >= len(strArr):
        return 0

    if dp[zeroes][ones][i] != -1:
        return dp[zeroes][ones][i]

    zero = 0
    one = 0
    for j in strArr[i]:
        if j == "0":
            zero += 1
        else:
            one += 1
    x = 1 + countString(zeroes - zero, ones - one, strArr, i + 1)
    y = countString(zeroes, ones, strArr, i + 1)
    dp[zeroes][ones][i] = max(x, y)
    return dp[zeroes][ones][i]


myInput = list(map(int, input().strip().split()))
n = int(myInput[0])
hasZeroes = myInput[1]
hasOnes = myInput[2]
stringArr = []
for i in range(n):
    stringArr.append(input())

print(countString(hasZeroes, hasOnes, stringArr, 0))




