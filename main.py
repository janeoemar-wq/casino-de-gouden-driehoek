# Week 1 oplossing: Casino de Gouden Driehoek startbudget en persoonsgegevens

# De casinokosten zijn vaste bedragen die de gebruiker moet betalen. Dit zijn "constanten" en staan daarom boven aan de code.
TICKET_PRICE = 10.00
CONSUMPTION_PRICE = 4.50
GAMBLING_TAX = 2.00

# In de eerste versie verzamelen we eerst de basisgegevens van de speler.
name = input("Wat is je naam? ").capitalize()
birthdate = input("Wat is je geboortedatum? (dd-mm-yyyy) ")
gender = input("Wat is je gender? (m/v/x) ").strip().lower()
startbudget = float(input("Hoeveel geld neem je mee naar Casino de Gouden Driehoek? € "))

# We kiezen een aanspreekvorm op basis van gender. Je kunt dit implementeren met 2 genders, of met meer genders. De uitgecommentarieerde versie laat de implementatie met 2 genders zien.
# salutation = f"Meneer {name}" if gender == "m" else f"Mevrouw {name}"
salutation = f"meneer {name}" if gender == "m" else f"mevrouw {name}" if gender == "v" else f"speler {name}"



# We rekenen eerst het totaal uit.
total = TICKET_PRICE + CONSUMPTION_PRICE + GAMBLING_TAX
balance = startbudget - total

# Daarna bepalen we of er nog genoeg geld over is.
has_budget = total <= startbudget
conclusie = "Je hebt nog genoeg budget voor toegang tot het casino." if has_budget else "Je hebt niet voldoende budget voor toegang tot het casino."

# Daarna volgt de output.
print("\nCasino de Gouden Driehoek")
print("-" * 25)
print(f"Welkom, {salutation}")
print()
print(f"Startbudget:    € {startbudget:.2f}")
print(f"Vaste kosten:   € {total:.2f}")
print(f"Saldo:          € {balance:.2f}")
print()
print(conclusie)