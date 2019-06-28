hair_black = "CCAGCAATCGC"
hair_brown = "GCCAGTGCCG"
hair_blonde = "TTAGCTATCGC"

face_square = "GCCACGG"
face_round = "ACCACAA"
face_oval = "AGGCCTCA"

blue_eyes = "TTGTGGTGGC"
green_eyes = "GGGAGGTGGC"
brown_eyes = "AAGTAGTGAC"

female = "TGAAGGACCTTC"
male = "TGCAGGAACTTC"

race_white = "AAAACCTCA"
race_black = "CGACTACAG"
race_asian = "CGCGGGCCG"

eva = [female, race_white, hair_blonde, blue_eyes, face_oval]
larisa = [female, race_white, hair_brown, brown_eyes, face_oval]
matej = [male, race_white, hair_black, blue_eyes, face_oval]
miha = [male, race_white, hair_brown, green_eyes, face_square]

suspect = []

with open("DNA.txt", "r") as dna_file:
    found_dna = dna_file.read()

    def forensic(dna):
        if dna in found_dna and dna not in suspect:
            suspect.append(dna)

forensic(dna=female)
forensic(dna=male)
forensic(dna=race_white)
forensic(dna=race_black)
forensic(dna=race_asian)
forensic(dna=hair_black)
forensic(dna=hair_brown)
forensic(dna=hair_blonde)
forensic(dna=blue_eyes)
forensic(dna=green_eyes)
forensic(dna=brown_eyes)
forensic(dna=face_square)
forensic(dna=face_round)
forensic(dna=face_oval)

print(suspect)

if suspect == eva:
    print("It was Eva!")
elif suspect == larisa:
    print("It was Larisa!")
elif suspect == matej:
    print("It was Matej!")
elif suspect == miha:
    print("It was Miha!")
else:
    print("There is no suspect!")
