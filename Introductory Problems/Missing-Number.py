def missing_number(n, given_sum):
    total_sum = (n * (n+1)) // 2
    return total_sum - given_sum

n = int(input())
numbers = [int(x) for x in input().split()]
given_sum = sum(numbers)
print(missing_number(n, given_sum))