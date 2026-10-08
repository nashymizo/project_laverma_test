def extract_ids_from_laverma(filepath):
    laverma_ids = set()
    with open(filepath, 'r', encoding='latin-1') as file:
        for line in file:
            if line.strip():
                raw_id = line.split(',')[0]
                # Filtert rigoros alle unsichtbaren Zeichen heraus, behält nur Ziffern
                clean_id = ''.join(filter(str.isdigit, raw_id))
                
                if clean_id:
                    # Entfernt am Schluss die führenden Nullen
                    laverma_ids.add(clean_id.lstrip('0'))
    return laverma_ids

def extract_ids_from_orgamax(filepath):
    orgamax_ids = set()
    with open(filepath, 'r', encoding='latin-1') as file:
        for line in file:
            if line.strip():
                # Behält ebenfalls strikt nur reine Ziffern bei
                clean_id = ''.join(filter(str.isdigit, line))
                
                if clean_id:
                    orgamax_ids.add(clean_id.lstrip('0'))
    return orgamax_ids

# Dateien einlesen
file1 = "Z:/!!NKE/VERGLEICH/laverma.txt"
file2 = "Z:/!!NKE/VERGLEICH/Export_ORGAMAX.txt"

ids_laverma = extract_ids_from_laverma(file1)
ids_orgamax = extract_ids_from_orgamax(file2)

# Mengen vergleichen
common_ids = ids_laverma.intersection(ids_orgamax)
only_in_laverma = ids_laverma.difference(ids_orgamax)
only_in_orgamax = ids_orgamax.difference(ids_laverma)

# Ergebnisse ausgeben
print("--- Auswertung ---")
print(f"Gesamtanzahl IDs in laverma.txt: {len(ids_laverma)}")
print(f"Gesamtanzahl IDs in Export_ORGAMAX.txt: {len(ids_orgamax)}\n")
print(f"Übereinstimmende IDs in beiden Dateien: {len(common_ids)}")
print(f"IDs, die NUR in laverma.txt existieren: {len(only_in_laverma)}")
print(f"IDs, die NUR in Export_ORGAMAX.txt existieren: {len(only_in_orgamax)}\n")

# Neue Ausgabe für die übereinstimmenden IDs
if common_ids:
    print("Folgende IDs sind in BEIDEN Dateien vorhanden:")
    # sorted() sortiert die IDs zur besseren Übersicht aufsteigend
    for shared_id in sorted(common_ids):
        print(shared_id)
    print() # Setzt eine leere Zeile als Trenner

# Optional: Fehlende IDs anzeigen lassen
if only_in_laverma:
    print("Beispiel für IDs, die im Export fehlen:")
    print(list(only_in_laverma)[:5])

if only_in_orgamax:
    print("Beispiel für IDs, die in der Laverma-Datei fehlen:")
    print(list(only_in_orgamax)[:5])