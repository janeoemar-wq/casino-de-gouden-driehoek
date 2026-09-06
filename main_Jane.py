
from datetime import datetime
print('Beste casino bezoeker,\n\nOm toegang te krijgen tot onze casino hebben wij de volgende gegevens nodig.\nWilt u de onderstaande vragen beantwoorden?\n')

# -----------------------------------------------------Variabelen NAW casino bezoeker ----
gender = input("Wat is uw geslacht? (man/vrouw/anders): ").lower()
surname = input("Wat is uw voornaam?? ").capitalize()
lastname = input("Wat is uw achternaam? ").capitalize()

# ------------------------------------------------------DEF-IF-ELIF-ELSE RETURN Aanspreekvorm/aanhef----
def aanhef(gender, surname, lastname):
    if gender == "man":
        return f"heer {surname} {lastname}"
    elif gender == "vrouw":
        return f"mevrouw {surname} {lastname}"
    else:
        return f"{surname} {lastname}"

print(f"Welkom {aanhef(gender, surname, lastname)}")

# ----WHILE-TRUE/ TRY/ BREAK/ EXEPT ---------------------Geboortedatum ----
from datetime import datetime
while True:
    datum_input = input("Wat is uw geboortedatum? (dd-mm-jjjj): ")
    try:
        dateofbirth = datetime.strptime(datum_input, "%d-%m-%Y")
        print("Geldige datum!\n")
        break
    except ValueError:
        print("Ongeldige datum, probeer opnieuw.\n")

# --- Budgetcontrole ---
print('LET OP! Voor toegang tot het casino heeft u een startbudget van minimaal € 50.00 nodig.\n')

min_inzet = 50.00
startbudget = float(input("Wat is uw startbudget: € "))

# Dynamische budgetcontrole
if startbudget < min_inzet:
    print(f"U heeft niet voldoende budget voor toegang tot het casino.")
else:
    print("U heeft voldoende budget voor toegang tot het casino.")

# --- Vaste kosten ---
ENTRANCE = 10.00
CONSUMPTION = 3.00
ADMINISTRATION = 3.50
TOTAL_COSTS = ENTRANCE + CONSUMPTION + ADMINISTRATION

rekening = startbudget - TOTAL_COSTS

# --- Printout ---
print("\n--- Casino de Gouden Driehoek ---")
print(f"Geachte {aanhef(gender, surname, lastname)},")
print(f"Startbudget:            € {startbudget:.2f}")
print(f"Vaste kosten:           € {TOTAL_COSTS:.2f}")
print(f"Resterend saldo:        € {rekening:.2f}")

print("\nWij wensen u heel veel speelplezier!")