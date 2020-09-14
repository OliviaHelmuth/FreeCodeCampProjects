def arithmetic_arranger(list, b=False):
    if len(list) > 5:
        print("Error: Too many problems.")
        return

    for item in list:
        number_1, operator, number_2 = item.split()

        try:
            int(number_1) and int(number_2)
        except:
            print("Error: Numbers must only contain digits.")
            return

        if len(number_1) > 4 or len(number_2) > 4:
            print("Error: Numbers cannot be more than four digits.")
            return

        if operator == "*" or operator == "/":
            print("Error: Operator must be '+' or '-'.")
            return

        if b:
            if operator == "+":
                solution = int(number_1) + int(number_2)
            if operator == "-":
                solution = int(number_1) - int(number_2)
            print(number_1 + operator + number_2)
            print(solution)
        else:
            print(number_1 + operator + number_2)


arithmetic_arranger(["3983 + 8333", "1 - 3801", "32 + 8",
                     "32 + 8",  "32 + 8"], True)
