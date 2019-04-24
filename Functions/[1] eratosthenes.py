# Sieve of Eratosthenes

def eratosthenes(N):
    nums = []
    ans = []
    if N < 4:
        return
    for i in range(2,N+1):
        nums.append(i)

    while nums:
        for i in nums[1:]:
            if i % nums[0] == 0:
                ans.append(i)
                nums.remove(i)
        nums = nums[1:]
 

    print(*ans)



eratosthenes(15)
