# ai_guesser.py

def guess_number():
    print("Denke an eine Zahl zwischen 1 und 100.")
    input("Drücke Enter, wenn du bereit bist...")

    low = 1
    high = 100
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        print(f"Ich rate: {guess}")
        feedback = input("Ist das zu hoch (h), zu niedrig (l) oder richtig (r)? ").lower()

        if feedback == 'r':
            print(f"Yay! Ich habe die Zahl in {attempts} Versuchen erraten.")
            break
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print("Bitte gib h, l oder r ein.")

if __name__ == "__main__":
    guess_number()
