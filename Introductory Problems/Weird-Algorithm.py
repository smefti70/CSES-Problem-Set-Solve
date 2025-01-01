def weird_algo(n):
     while n != 1:
         print(n, ' ', end='')
         if n % 2 != 0:
             n = n * 3 + 1
         else:
             n = n // 2
     print(n)

n = int(input())
weird_algo(n)