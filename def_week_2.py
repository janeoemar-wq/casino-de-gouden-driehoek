from datetime import datetime
import sys

name = input("Wat is uw naam? ").capitalize()
gender = input("Wat is uw gender? (m/v/x) ").strip().lower()
salutation = f"Beste meneer {name}" if gender == "m" else f"Beste mevrouw {name}" if gender == "v" else f"Beste speler {name}"
print(salutation)

birthdate = input("Wat is uw geboortedatum? (ddmmjjjj): ")
birth_day = int(birthdate[0:2])
birth_month = int(birthdate[2:4])
birth_year = int(birthdate[4:8])
vandaag = datetime.today()

leeftijd = vandaag.year - birth_year
minimale_leeftijd = 18

if (vandaag.month, vandaag.day) < (birth_month, birth_day):
    leeftijd -= 1

print(f"Bedankt voor de gegevens, U bent {leeftijd} jaar oud.")
print()
# Exit codes
soort_code = int(input("Soort exit (0,1,2,3): "))

if soort_code < minimale_leeftijd:
    if soort_code == 0:
        print("U krijgt geen toegang. u staat op onze black list")
        sys.exit(0)
    elif soort_code == 1:
        print(f"Process finished with exit code 1. U krijgt geen toegang, u bent te jong.")
        sys.exit(1)
    elif soort_code == 2:
        print(f"Process finished with exit code 2. U krijgt geen toegang, u hebt te weinig budget.")
        sys.exit(2)
    elif soort_code == 3:
        print(f"Process finished with exit code 3. U krijgt geen toegang, uw ID is niet geldig.")
        sys.exit(3)
    else:
        print("U krijgt toegang tot de casino.")
    print()

    #Roullette spel
inzet = float(input("Wat is uw inzet in euro: "))
minimale_inzet = 5
print(f"Uw inzet is €{inzet:.2f}")
if inzet < minimale_inzet:
   print("U heeft helaas te weinig saldo,")
   inzet = float(input("Wat is uw inzet in euro: "))
   print(f"Uw inzet is €{inzet:.2f}")
if inzet > minimale_inzet:
    print()
    print("==========  Let's play, place your bet and choose on of the following options  =========")
else:
    print("U heeft helaas te weinig saldo,")
    print()
rekening = 100.00
round_number = 1
print()
print("                                 Welkom bij Roulette!         ")

while True:
    print("\n--- Dit zijn de gok opties: ---")
    print(' ' * 6 + '1' + " " * 6 + 'rood')
    print(' ' * 6 + '2' + " " * 6 + 'zwart')
    print(' ' * 6 + '3' + " " * 6 + 'even')
    print(' ' * 6 + '4' + " " * 6 + 'oneven')
    print(' ' * 6 + '0' + " " * 6 + 'stop')

    try:
        choice = int(input("Kies uw gok (0-4): "))
    except ValueError:
        print("Ongeldige invoer, gebruik een getal.")
        continue

    # Stoppen bij 0

    if choice == 0:
        print(f"{salutation}, u heeft het spel gestopt. Bedankt voor het spelen.")
        print(f"Uw saldo is: €{rekening:.2f}")
        print("Tot de volgende keer bij Casino de Gouden Driehoek!")
        break

    # Ongeldige keuze
    if choice not in [1, 2, 3, 4]:
        print("Ongeldige keuze, probeer opnieuw.")
        continue

    print(f"U koos optie {choice}.")
    # Vragen inzet
    try:
        inzet = float(input("Welk bedrag wilt u inzetten: € "))
    except ValueError:
        print("Ongeldige invoer, gebruik een getal.")
        continue

    # Validatie inzet
    if inzet <= 0:
        print("Uw inzet moet hoger zijn dan €0.")
        continue

    if inzet > rekening:
        print(f"Uw Inzet is hoger dan uw rekening (€{rekening:.2f}).")
        continue

    # Rekening updaten
    rekening -= inzet

    # Spin berekenen
    spin = (round_number * 7) % 37
    round_number += 1

    # Bepalen kleur/ even/oneven
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
        print("U verliest.")

    print(f"Uw nieuwe saldo is: €{rekening:.2f}")
