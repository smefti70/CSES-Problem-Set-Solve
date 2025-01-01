# def longest_repetition(str):
#     count = {}
#     for i in range(len(str)):
#         count[str[i]] = 1
#     for i in range(len(str)):
#         letter_count = 1
#         for j in range(i+1,len(str)):
#             if str[i] == str[j]:
#                 letter_count += 1
#                 count[str[i]] = max(letter_count,count[str[i]])
#             else:
#                 i = j
#                 break
#     max_value = 0
#     for key, value in count.items():
#         if value > max_value:
#             max_value = value
#     return max_value
# string = input()
# print(longest_repetition(string))
# Solved Worked but got TLE :)

def longest_repetition(str):
    max_count = 1
    current_count = 1

    for i in range(1, len(str)):
        if str[i] == str[i-1]:
            current_count += 1
        else:
            current_count = 1
        max_count = max(max_count, current_count)
    return max_count

string = input()
print(longest_repetition(string))