def search_errors(problems):
    # if problems > 4 => Error: Too many problems
    if len(problems) > 4:
        return 'Error: Too many problems.'

    for problem in problems:
        # if not appropriate operators '+' and '-' => Error: Operator must be '+' or '-'
        if '+' not in problem and '-' not in problem:
            return "Error: Operator must be '+' or '-'"

        numbers = problem.split()

        # if not only digits => Error: Numbers must only contain digits
        if not numbers[0].isdigit() or not numbers[2].isdigit():
            return 'Error: Numbers must only contain digits'

        # if not numbers <= 4 digits => Error: Numbers cannot be more than four digits
        if not len(numbers[0]) < 5 or not len(numbers[2]) < 5:
            return 'Error: Numbers cannot be more than four digits'

def arimethic_arranger(problems):
    error = search_errors(problems)
    first_line = ''
    second_line = ''
    third_line = ''

    if error:
        return error

    for problem in problems:
        operand1 = problem.split()[0]
        operator = problem.split()[1] + ' '
        operand2 = problem.split()[2]
        dashes = '-'
    # 1 space between the operator and the longest operand
        if len(problem.split()[0]) >= len(problem.split()[2]):
            operand1 = '  ' + operand1
            operator += ' ' * (len(problem.split()[0]) - len(problem.split()[2]))
            dashes = dashes * len(operand1)
        else:
            operand1 = ' ' * (len(problem.split()[2]) - len(problem.split()[0]) + 2) + operand1
            dashes = dashes * len(operator + operand2)

        first_line += operand1 + ' ' * 4
        second_line += operator + operand2 + ' ' * 4
        third_line += dashes + ' ' * 4
        print(operand1)
        print(operator + operand2)
        print(dashes)

    print(first_line)
    print(second_line)
    print(third_line)
    # operator in the same line as second operand
    # numbers right-aligned
    # four spaces between each problem
    # put dashes at the bottom of each problem
arimethic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"])
