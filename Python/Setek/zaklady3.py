from math import ceil

def paint_needed(height, width, area_per_can = 5):
    return height * width / area_per_can

def get_plural_form(can_count):
    if can_count <= 1:
        return "plechovku"
    elif can_count < 5:
        return "plechovky"
    else:
        return "plechovek"

height = int(input("Výška zdi je v m: "))
width = int(input("Šířka zdi v m: "))   

cans_needed = ceil(paint_needed(height, width))
print(f"Budete potřebovat {cans_needed} {get_plural_form(cans_needed)}")