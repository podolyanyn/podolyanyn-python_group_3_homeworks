def make_operation(numbers=input("enter digit through a space: "), operator=input("enter operator (+, -, *): ")):


    try:
        nums = [int(n) for n in numbers.split()]
        if not nums:
            return "error: not digit"

        result = nums[0]
        for num in nums[1:]:
            if operator == '+':
                result += num
            elif operator == '-':
                result -= num
            elif operator == '*':
                result *= num
            else:
                return "error unknow operator"

        return result

    except ValueError:
        return "error: enter no digit values"
print(make_operation())
