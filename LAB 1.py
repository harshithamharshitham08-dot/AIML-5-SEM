'''A smart padlock uses a 4-digit numeric PIN (0000–9999).

Clues:

The PIN is made entirely of even digits: 0, 2, 4, 6, 8
The sum of the four digits is exactly 16'''

even_digits = [0, 2, 4, 6, 8]
valid_pins = []
for a in even_digits:
    for b in even_digits:
        for c in even_digits:
            for d in even_digits:
                if a + b + c + d == 16:
                    pin = f"{a}{b}{c}{d}"
                    valid_pins.append(pin)
print("Total Valid PINs:", len(valid_pins))
print(valid_pins)