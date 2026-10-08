def extract_laverma_id(filepath):
    ids_laverma = set()
    # öffnet Datei
    with open(filepath, 'r', encoding='latin-1') as file:
        for line in file:
            # prüft ob nach strip(zeilenumbrüche) noch Zeichen übrig sind, wenn ja, wird nächste zeile ausgeführt
            if line.strip():
                # splittet die Zeile in eigene Datensätze und trennt sie durch ein komma, danach wird index 0 ausgewählt
                raw_line = line.split(",")[0]

                #prüft jeden einzelnen Buchstaben ob er eine Zahl ist und setzt ihn ohne Trennung("") wieder zusammen
                clean_line = "".join(filter(str.isdigit, raw_line))


                if clean_line:
                    # führende nullen entfernen und dem tuple ids_laverma anhängen
                    ids_laverma.add(int(clean_line))

    return ids_laverma


def extract_orgamax_id(filepath):
    ids_orgamax = set()
    # öffne Datei
    with open(filepath, 'r', encoding='latin-1') as file:
        for line in file:
            # prüft ob nach strip(zeilenumbrüche) noch Zeichen übrig sind, wenn ja, wird nächste zeile ausgeführt
            if line.strip():
                # splittet die Zeile in eigene Datensätze und trennt sie durch ein komma, danach wird index 0 ausgewählt
                raw_line = line.split(",")[0]

                #prüft jeden einzelnen Buchstaben ob er eine Zahl ist und setzt ihn ohne Trennung("") wieder zusammen
                clean_line = "".join(filter(str.isdigit, raw_line))


                if clean_line:
                    # führende nullen entfernen und dem tuple ids_laverma anhängen
                    ids_orgamax.add(int(clean_line))

    return ids_orgamax

#DATEN einlesen

file_laverma = "Z:/!!NKE/VERGLEICH/laverma.txt"
file_orgamax = "Z:/!!NKE/VERGLEICH/Export_ORGAMAX.txt"

#Funktionen ausführen und den return in variable speichern

laverma_ids = extract_laverma_id(file_laverma)
orgamax_ids = extract_orgamax_id(file_orgamax)

# SETS MITEINANDER VERGLEICHEN UND FILTERN
# Überschneidungen mit INTERSECTION FILTERN 
common_ids = laverma_ids.intersection(orgamax_ids)
# Differenz ermitteln ENTWEDER mit ".difference" oder "-"
only_laverma = laverma_ids - orgamax_ids
only_orgamax = orgamax_ids - laverma_ids


print(f"Die Anzahl der Dateien die sich in LAVERMA befinden beträgt: {len(laverma_ids)}")
print(f"Die Anzahl der Dateien die sich in ORGAMAX: {len(orgamax_ids)}")
print(f"Die Anzahl der Dateien die sich ÜBERSCHNEIDEN beträgt: {len(common_ids)}")

print("-"*30)

y = 1
print(f"Nur in LAVERMA enthalten:")
for item in only_laverma:
    print(f"{y}. - {item}")
    y += 1
print("-"*30)

z = 1
print(f"Nur in ORGAMAX enthalten:")
for item in only_orgamax:
    print(f"{z}. - {item}")
    z += 1
print("-"*30)



print(f"Auflistung von den ID's die in beiden Dateien enthalten sind:")
x = 1
for item in common_ids:
    print(f"{x}. - {item}")
    x += 1