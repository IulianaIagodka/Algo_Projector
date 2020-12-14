# Enter your code here. Read input from STDIN. Print output to STDOUT
def minCost(costs):
    for i in range(1,len(costs)):
        x = costs[i]
        #print (x)
        y = costs[i-1]
       # print(y)
        x[0] += min(y[1], y[2])
        x[1] += min(y[0], y[2])
        x[2] += min(y[0], y[1])
    return min(costs[-1])

n = int(input())
minTotalCost = 0
costs = [list(map(int,input().strip().split())) for i in range(n)]
minTotalCost += (minCost(costs))
print (minTotalCost)