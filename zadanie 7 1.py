"""zadanie 1"""
new_file_path = "nowy_tekst1.txt"
root_file_path = "tekst_zrodlowy1.txt"

with open(root_file_path, "r") as file:
    tekst = file.read()

słowa = tekst.split()
słowa_długie = {słowo for słowo in słowa if len(słowo) >= 7}

with open(new_file_path, "a") as file:
    file.write("\n".join(słowa_długie))

"""zadanie 2"""
new_file_path = "nowy_tekst2.txt"
root_file_path = "tekst_zrodlowy2.txt"

with open(root_file_path, "r") as file:
    with open(new_file_path, "a") as new_file:
        for x in file:
            new_file.write(x)

"""zadanie 3"""
new_file_path = "nowy_tekst3.txt"
root_file_path = "tekst_zrodlowy3.txt"

with open(root_file_path, "r") as file:
    with open(new_file_path, "a") as new_file:
        tekst = []
        for x in file:
            tekst.append(x)
        for x in tekst (len(tekst), 0,-1):
            new_file.write(x)
        
