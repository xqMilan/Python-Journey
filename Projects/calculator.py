operator = input("Willkommen zu deinem Taschenrechner!\n"
"Bitte wähle einen Operator (+, -, *, /): \n")
number1 = float(input("Gebe die erste Zahl an\n"))
number2 = float(input("Gebe die zweite Zahl an\n"))

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    if number2 != 0:
        result = number1 / number2
    else:
        result = "Fehler! Division durch 0 nicht erlaubt."
else:
    result = "Ungültiger Operator!"  

print(f"{number1} {operator} {number2} = {result}")