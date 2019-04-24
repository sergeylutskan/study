# Find a cumulative sum of input arguments and return a list of it

def partial_sums(*a):
    ans = [0]
    for i in range(0,len(a)):
        ans.append(a[i]+ans[i])
    return ans


print(partial_sums(1, 0.5, 0.25, 0.125))
