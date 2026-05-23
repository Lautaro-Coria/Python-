def arithmetic_arranger(problems, show_answers=False):
    # Validación: máximo 5 problemas
    if len(problems) > 5:
        return "Error: Too many problems."

    line1 = []
    line2 = []
    line3 = []
    line4 = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        top = parts[0]
        operator = parts[1]
        bottom = parts[2]

        # Validar operador
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # Validar que sean números
        if not top.isdigit() or not bottom.isdigit():
            return "Error: Numbers must only contain digits."

        # Validar que tengan hasta 4 dígitos
        if len(top) > 4 or len(bottom) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calcular ancho
        width = max(len(top), len(bottom)) + 2

        # Crear líneas
        line1.append(top.rjust(width))
        line2.append(operator + bottom.rjust(width - 1))
        line3.append("-" * width)

        if show_answers:
            result = str(eval(top + operator + bottom))
            line4.append(result.rjust(width))

    arranged_problems = "    ".join(line1) + "\n" + "    ".join(line2) + "\n" + "    ".join(line3)
    if show_answers:
        arranged_problems += "\n" + "    ".join(line4)

    return arranged_problems


# Prueba rápida
print(arithmetic_arranger(["500 + 500", "2 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))