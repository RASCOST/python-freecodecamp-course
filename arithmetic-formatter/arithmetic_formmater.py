def search_errors(problems):
    # if problems > 4 => Error: Too many problems
    if len(problems) > 5:
        return 'Error: Too many problems.'

    for problem in problems:
        # if not appropriate operators '+' and '-' => Error: Operator must be '+' or '-'
        if '+' not in problem and '-' not in problem:
            return "Error: Operator must be '+' or '-'."

        numbers = problem.split()

        # if not only digits => Error: Numbers must only contain digits
        if not numbers[0].isdigit() or not numbers[2].isdigit():
            return 'Error: Numbers must only contain digits.'

        # if not numbers <= 4 digits => Error: Numbers cannot be more than four digits
        if not len(numbers[0]) < 5 or not len(numbers[2]) < 5:
            return 'Error: Numbers cannot be more than four digits.'

def calculate(op1, op2, operator):
    if '+' == operator:
        return int(op1) + int(op2)

    return int(op1) - int(op2)

def arithmetic_arranger(problems, show_results=False):
    error = search_errors(problems)
    operand1_line = ''
    operand2_line = ''
    dashes_line = ''
    results_line = ''

    if error:
        return error

    for problem in problems:
        operand1 = problem.split()[0]
        operator = problem.split()[1] + ' ' # one space between the operator and the longest operand
        operand2 = problem.split()[2]
        dashes = '-'
        results = str(calculate(operand1, operand2, operator.strip()))

        if len(problem.split()[0]) >= len(problem.split()[2]):
            # numbers right-aligned
            operand1 = '  ' + operand1
            operator += ' ' * (len(problem.split()[0]) - len(problem.split()[2]))
            dashes = dashes * len(operand1)
        else:
            # numbers right-aligned
            operand1 = ' ' * (len(problem.split()[2]) - len(problem.split()[0]) + 2) + operand1
            dashes = dashes * len(operator + operand2)

        # four spaces between each problem
        operand1_line += operand1 + ' ' * 4

        # operator in the same line as second operand
        # four spaces between each problem
        operand2_line += operator + operand2 + ' ' * 4
        
        # put dashes at the bottom of each problem
        dashes_line += dashes + ' ' * 4
        results_line += ' ' * (len(dashes) - len(results)) + results + ' ' * 4

    if show_results:
        return f"{operand1_line.rstrip()}\n{operand2_line.rstrip()}\n{dashes_line.rstrip()}\n{results_line.rstrip() if show_results else ''}"

    return f"{operand1_line.rstrip()}\n{operand2_line.rstrip()}\n{dashes_line.rstrip()}"
