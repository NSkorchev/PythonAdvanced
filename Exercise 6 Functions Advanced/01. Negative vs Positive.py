# def sum_of_two_numbers(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#     def print_numbers():
#         pass
#
# sum_of_two_numbers(5, 6, 7, one=1, three=3)
def print_num(positive, negative):
    print(negative)
    print(positive)

    if positive > abs(negative):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")

numbers = [int(x) for x in input().split()]
positive_num = sum(x for x in numbers if x > 0)
negative_num = sum(x for x in numbers if x < 0)

print_num(positive_num, negative_num)