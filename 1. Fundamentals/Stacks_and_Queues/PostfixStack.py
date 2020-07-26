# Evaluate postfix using a stack

#O(n) TC and SC since we are looping once and using stack
def evaluate_post_fix(exp):
    stack = MyStack()
    try:
        for char in exp:
            if char.isdigit():
                # Push numbers in stack
                stack.push(char)
            else:
                # use top two numbers and evaluate
                right = stack.pop()
                left = stack.pop()
                stack.push(str(eval(left + char + right)))
        # final answer should be a number
        return int(float(stack.pop()))
    except TypeError:
        return "Invalid Sequence"


print("Result: " + str(evaluate_post_fix("921*-8-4+")))
print("Result: " + str(evaluate_post_fix("921*-8--4+")))