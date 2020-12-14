# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
The people of RGB Street have decided to paint each of their houses red, green, or blue.
They've also decided that no two neighboring houses will be painted the same color.
The neighbors of house i are houses i-1 and i+1. The first and last houses are not neighbors.
You will be given three integer sequences R, G and B. Ri, Gi and Bi are the costs of painting the i-th house red,
green, and blue, respectively.
Find the minimal total cost required to perform the work.
Input Format
First line of input contains a single integer n — the number of houses. Each of the following n lines contains three integers Ri, Gi and Bi each.
"""
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