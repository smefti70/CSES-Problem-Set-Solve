def increasing_array(numbers):
    moves = 0
    for i in range(1,len(numbers)):
        if numbers[i-1] > numbers[i]:
            diff = numbers[i-1] - numbers[i]
            numbers[i] += diff
            moves += diff
    return moves

n = int(input())
arr = [int(x) for x in input().split()]

print(increasing_array(arr))
