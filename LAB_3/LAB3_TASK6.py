def cumulative_sum(lis):
    cum_sum=[lis[0]]
    for item in lis[1:]:
        cum_sum.append(cum_sum[len(cum_sum)-1]+item)
    return cum_sum

print("The cumulatice sum list is :::",cumulative_sum([1,2,3]))
    
    
