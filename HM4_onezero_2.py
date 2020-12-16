def findMax(strArr, m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    def count(s):
        return sum(1 for c in s if c == "0"), sum(1 for c in s if c == "1")

    for z, o in [count(s) for s in strArr]:
        for x in range(m, -1, -1):
            for y in range(n, -1, -1):
                if x >= z and y >= o:
                    dp[x][y] = max(1 + dp[x - z][y - o], dp[x][y])

    return dp[m][n]

myInput = list(map(int, input().strip().split()))
n = int(myInput[0])
hasZeroes = myInput[1]
hasOnes = myInput[2]
stringArr = []
for i in range(n):
    stringArr.append(input())

print(findMax(stringArr, hasZeroes, hasOnes))
