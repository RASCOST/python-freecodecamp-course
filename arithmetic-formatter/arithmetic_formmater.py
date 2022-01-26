def searh_errors(problems):
    # if problems > 5 => Error: Too many problems
    if (problems.len() > 5):
        return 'Error: Too many problems.'

    for problem in problems:
        # if not appropriate operators '+' and '-' => Error: Operator must be '+' or '-'
        if ('+' not in problem or '-' not in problem):
            return "Error: Operator must be '+' or '-'"

        numbers = problem.split()

        # if not only digits => Error: Numbers must only contain digits
        if (not number[0].isdigit() or not number[2]):
            return 'Error: Numbers must only contain digits'

        # if not numbers <= 4 digits => Error: Numbers cannot be more than four digits
        if (not number[0].len() <= 4 or number[2] <= 4):
            return 'Error: Numbers cannot be more than four digits'

def arimethic_arranger(problems):
    error = search_errors(problems)

    if (not error):
        return error
