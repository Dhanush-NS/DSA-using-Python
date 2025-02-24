# def print_items(n):
#     for i in range(n):
#         print(i)
    
# print_items(10)

# here the O(n) becoz only one n is performing the task

# def print_items(n):
#     for i in range(n):
#         print(i)
#     for j in range(n):
#         print(j)

# print_items(10)

# DROP CONSTANTS
# two n's so n + n = 2n but we drop constant so that would be O(n)


# def print_items(n):
#     for i in range(n):
#         print(i)
#         for j in range(n):
#             print(j)

# print_items(10)

# so here the n * n = n2(square) so the case id O(n2)


# def print_items(n):
#     for i in range(n):
#         for j in range(n):
#             print(i,j)
#     for k in range(n):
#         print(k)

# print_items(10)

# The case here is O(n2) and another n performing task that is O(n2 + n)
# so the n2 dominates single n so we drop the non-dominants
# THE ANSWER is O(n2)

# def items(n):
#     return n + n
# items(1)

# it performs task only one time even though we have n two times but it is just the addition of n so the complexity is O(1)
# but what if return more than 1 n means like return n + n + n even though then the complexity would be O(1) if we have millions of return n then also we have O(1) only
  

