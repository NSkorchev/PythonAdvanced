# class ValueToSmall(Exception):
#     pass
#
# class ValueToHigh(Exception):
#     pass
#
# amount = float(input())
#
# if amount <= 0:
#     raise ValueToSmall("Amount can not be negative or zero")
#
# if amount > 100:
#     raise ValueToHigh("Amount is to high")
class ValueCannotBeNegative(Exception):
    pass


for _ in range(5):
    try:
        num = float(input("Enter a number: "))
        if num < 0:
            raise ValueCannotBeNegative
    except ValueError:
        print("This is not a valid number.")

try:
    nums = [1, 2, 3]
    nums[3]
except KeyError:
    print("from exception")
else:
    print("from else")
finally:
    print("from finally")