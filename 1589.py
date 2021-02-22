
def maxSumRangeQuery(nums, requests):
    n = len(nums)
    diff = [0] * (n+1)
    for request in requests:
       	diff[request[0]] += 1
        diff[request[1]+1] -= 1
    #print(diff)
    freq = [0] * n
    pre = 0
    for i in range(n):
        pre = pre + diff[i]
        freq[i] = pre
    #print(freq)
    #print(nums)
    freq.sort()
    nums.sort()
    #print(freq)
    #print(nums)

    res = 0
    divider = 10**9 + 7
    for i in range(n):
        res = (res + freq[i] * nums[i]) % divider
    return res

nums = [1,2,3,4,5]
requests = [[1,3],[0,1]]
print(maxSumRangeQuery(nums,requests))