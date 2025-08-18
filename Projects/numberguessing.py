import random 
zahl = random.randint(1,100)
guesses = 0
game_done = False

print("Willkommen zum Zahlenraten-Spiel!")
print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht. Kannst du sie erraten?")

while not game_done:
    guess = int(input("Versuche es mal... \n"))
    guesses = guesses + 1

    if guess_1 == zahl:
        print(f"Erzlichen glückwunsch! Du hast nach {guesses} versuchen die Zahl erraten.")
        game_done = True
    elif guess_1 < zahl:
        print("Leider falsch! Die Zahl ist grösser")
    elif guess_1 > zahl:
        print("Leider falsch! Die Zahl ist kleiner")