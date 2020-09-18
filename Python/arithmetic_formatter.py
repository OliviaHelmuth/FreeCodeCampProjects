def arithmetic_arranger(list, b=False):
    if len(list) > 5:
        return ("Error: Too many problems.")

    unformatted = []

    for item in list:
        number_1, operator, number_2 = item.split()

        try:
            int(number_1) and int(number_2)
        except:
            return ("Error: Numbers must only contain digits.")

        if len(number_1) > 4 or len(number_2) > 4:
            return ("Error: Numbers cannot be more than four digits.")

        if operator == "*" or operator == "/":
            return ("Error: Operator must be '+' or '-'.")

        if b:
            if operator == "+":
                solution = int(number_1) + int(number_2)
            if operator == "-":
                solution = int(number_1) - int(number_2)
        else:
            solution = ""

        unformatted.append([number_1, operator, number_2, solution])

    output = format_array(unformatted, b)
    return output


def format_array(unformatted, b):
    spacing = ""
    line_1 = ""
    line_2 = ""
    line_3 = ""
    line_4 = ""

    for item in unformatted:
        task_size = get_size(item)
        line_1 += spacing + "{:>{task_size}}".format(item[0],
                                                     task_size=task_size)
        line_2 += spacing + "{:<}{:>{task_size}}".format(
            item[1], item[2], task_size=task_size-1)
        line_3 += spacing + "{:->{task_size}}".format("", task_size=task_size)
        if b:
            line_4 += spacing + "{:>{task_size}}".format(
                item[3], task_size=task_size)
        spacing = "    "

    if b:
        return f"{line_1}\n{line_2}\n{line_3}\n{line_4}"
    return f"{line_1}\n{line_2}\n{line_3}"


def get_size(item):
    return max(len(item[0]), len(item[2])) + 2
