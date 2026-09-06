from datetime import datetime
import sys

TICKET_PRICE = 10.00
CONSUMPTION_PRICE = 4.50
GAMBLING_TAX = 2.00
MIN_AGE = 18
MIN_INZET = 5.00

# INPUT GEGEVENS (week 1 novi)

name = input("Wat is je naam? ").capitalize()
birthdate = input("Wat is je geboortedatum? (dd-mm-yyyy) ")
gender = input("Wat is je gender? (m/v/x) ").strip().lower()
startbudget = float(input("Hoeveel geld neem je mee naar Casino de Gouden Driehoek? € "))

# AANHEF (week 1 novi)

salutation = (f"meneer {name}" if gender == "m" else f"mevrouw {name}" if gender == "v" else f"speler {name}")

# LEEFTIJDCHECK (week 2)

birth_day, birth_month, birth_year = birthdate.split("-")
age = 2026 - int(birth_year)

if age < MIN_AGE:
    print(f"Je bent {age} jaar oud. Je moet minimaal {MIN_AGE} jaar zijn om binnen te komen.")
    sys.exit(1)

#VASTE KOSTEN (week 1)
total = TICKET_PRICE + CONSUMPTION_PRICE + GAMBLING_TAX
balance = startbudget - total
has_budget = total <= startbudget
conclusie = ("Je hebt nog genoeg budget voor toegang tot het casino.")
if has_budget
else
   print("Je hebt niet voldoende budget voor toegang tot het casino.")

# -----------------------------
# PRINTOUT (week 1)
# -----------------------------
print("\nCasino de Gouden Driehoek")
print("-" * 25)
print(f"Welkom, {salutation}\n")
print(f"Startbudget:    € {startbudget:.2f}")
print(f"Vaste kosten:   € {total:.2f}")
print(f"Saldo:          € {balance:.2f}\n")
print(conclusie)

if balance < MIN_INZET:
    print("Je hebt niet genoeg saldo om te spelen.")
    sys.exit(1)

# -----------------------------
# ROULETTE (week 2)
# -----------------------------
round_number = 1

while True:
    print("\nKies één van de volgende opties:")
    print("1. Rood")
    print("2. Zwart")
    print("3. Even")
    print("4. Oneven")
    print("0. Stop")

    try:
        choice = int(input("Kies je gok (0 om te stoppen): "))
    except ValueError:
        print("Ongeldige invoer, kies een nummer.")
        continue

    if choice == 0:
        break

    if choice not in [1, 2, 3, 4]:
        print("Ongeldige keuze, probeer opnieuw.")
        continue

    # -----------------------------
    # INZET VRAGEN
    # -----------------------------
    try:
        stake = float(input("Hoeveel wil je inzetten? € "))
    except ValueError:
        print("Ongeldige invoer, gebruik een getal.")
        continue

    if stake <= 0:
        print("Inzet moet hoger zijn dan €0.")
        continue

    if stake > balance:
        print("Je hebt niet genoeg saldo voor deze inzet.")
        continue

    balance -= stake

    # -----------------------------
    # SPIN BEREKENEN
    # -----------------------------
    spin = (round_number * 7) % 37

    # -----------------------------
    # KLEUR & EVEN/ONEVEN
    # -----------------------------
    if spin == 0:
        color = "groen"
        odd_even = "geen"
    else:
        if spin <= 18:
            if spin % 2 == 0:
                color = "zwart"
                odd_even = "even"
            else:
                color = "rood"
                odd_even = "oneven"
        else:
            if spin % 2 == 0:
                color = "rood"
                odd_even = "even"
            else:
                color = "zwart"
                odd_even = "oneven"

    # -----------------------------
    # WINST BEPALEN
    # -----------------------------
    win = False

    if choice == 1 and color == "rood":
        win = True
    elif choice == 2 and color == "zwart":
        win = True
    elif choice == 3 and odd_even == "even":
        win = True
    elif choice == 4 and odd_even == "oneven":
        win = True

    # -----------------------------
    # UITKOMST PRINTEN
    # -----------------------------
    print(f"De bal valt op {color} ({spin}).")

    if win:
        print(f"Je wint € {stake:.2f}")
        balance += stake * 2
    else:
        print(f"Je verliest € {stake:.2f}")

    print(f"Nieuw saldo: € {balance:.2f}")

    round_number += 1

# -----------------------------
# EINDSALDO
# -----------------------------
print("\nEindsaldo:", f"€ {balance:.2f}")
print("Bedankt voor het spelen bij Casino de Gouden Driehoek!")
