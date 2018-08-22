# Build and return a list.
# E.g. [0, 1, 2, 3, ... , 999999999]


def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums


# Sums it.
sum_of_first_n = sum(firstn(1000000))



# A generator that yields items instead of returning a list.
# def firstn(n):
#     num = 0
#     while num < n:
#         yield num
#         num += 1
#
#
# sum_of_first_n = sum(firstn(1000000))