from datetime import datetime
import sys


birthdate = input("Wat is uw geboortedatum? (ddmmjjjj): ")
birth_day = int(birthdate[0:2])
birth_month = int(birthdate[2:4])
birth_year = int(birthdate[4:8])

vandaag = datetime.today()

leeftijd = vandaag.year - birth_year
minimale_leeftijd = 18

if (vandaag.month, vandaag.day) < (birth_month, birth_day):
    leeftijd -= 1

print(f"U bent {leeftijd} jaar oud.")

# Exit code
soort_code = int(input("Soort exit (0,1,2,3): "))

if soort_code < minimale_leeftijd:
    if soort_code == 0:
        print("Je krijgt geen toegang, vanwege.....")
        sys.exit(0)
    elif soort_code == 1:
        print(f"Process finished with exit code 1. Je krijgt geen toegang, u .....")
        sys.exit(1)
    elif soort_code == 2:
        print(f"Process finished with exit code 2. Je krijgt geen toegang, je hebt te weinig saldo")
        sys.exit(2)
    elif soort_code == 3:
        print(f"Process finished with exit code 3. Je krijgt geen toegang, ID is niet geldig.")
        sys.exit(3)
    else:
        print("Je krijgt toegang tot de casino. Wij wensen u heel veel speelplezier!")

    #=======================Roullette spel===============================


inzet = float(input("Wat is je inzet in euro: "))
minimale_inzet = 5
print(f"Je inzet is €{inzet:.2f}")
if inzet < minimale_inzet:
   print("Je hebt te weinig saldo,")
   inzet = float(input("Wat is je inzet in euro: "))
   print(f"Je inzet is €{inzet:.2f}")
if inzet > minimale_inzet:
    print("Let's play, place your bet and choose one of the following options")
else:
    print("Je hebt te weinig saldo,")
 #===========================================================================
rekening = 100.00          # voorbeeldbedrag
round_number = 1

print("Welkom bij Roulette!")

while True:
    print("\n--- Dit zijn de gok opties: ---")
    print("1 rood")
    print("2 zwart")
    print("3 even")
    print("4 oneven")
    print("0 stop")

    try:
        choice = int(input("Kies uw gok (0-4): "))
    except ValueError:
        print("Ongeldige invoer, gebruik een getal.")
        continue

    # Stoppen bij 0
    if choice == 0:
        print("U heeft het spel gestopt.")
        break

    # Ongeldige keuze
    if choice not in [1, 2, 3, 4]:
        print("Ongeldige keuze, probeer opnieuw.")
        continue

    print(f"U koos optie {choice}.")
    # Inzet vragen
    try:
        inzet = float(input("Wat is uw inzet: € "))
    except ValueError:
        print("Ongeldige invoer, gebruik een getal.")
        continue

    # Validatie inzet
    if inzet <= 0:
        print("Inzet moet hoger zijn dan €0.")
        continue

    if inzet > rekening:
        print(f"Inzet is hoger dan uw rekening (€{rekening:.2f}).")
        continue

    # Rekening updaten
    rekening -= inzet

    # Spin berekenen
    spin = (round_number * 7) % 37
    round_number += 1

    # Bepalen kleur en even/oneven
    if spin % 2 == 0:
        odd_even = "even"
    else:
        odd_even = "oneven"

    if spin <= 18:
        color = "zwart" if spin % 2 == 0 else "rood"
    else:
        color = "rood" if spin % 2 == 0 else "zwart"

    # Wincondities
    gewonnen = False

    if choice == "1" and color == "rood":
        gewonnen = True
    elif choice == "2" and color == "zwart":
        gewonnen = True
    elif choice == "3" and odd_even == "even":
        gewonnen = True
    elif choice == "4" and odd_even == "oneven":
        gewonnen = True

    # Uitbetaling
    if gewonnen:
        winst = inzet * 2
        rekening += winst
        print(f"\n WINST! Het balletje landde op {spin} ({color}, {odd_even}).")
        print(f"U wint €{winst:.2f}!")
    else:
        print(f"\n Verloren. Het balletje landde op {spin} ({color}, {odd_even}).")
        print("U wint niets.")

    print(f"Uw nieuwe saldo is: €{rekening:.2f}")
