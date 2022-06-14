"""import csv

with open("data.CSV") as fileCSV:
    readingCSV = csv.DictReader(fileCSV, delimiter=",")
    for line in readingCSV:
        ID = line.get("ID")
        PATIENT = line.get("PATIENT")
        AGE = line.get("AGE")
        GENDER =  line.get("GENDER")
        NEUROLOGICAL =  line.get("NEUROLOGICAL")
        CARDIOVASCULAR =  line.get("CARDIOVASCULAR")
        RESPIRATORY =  line.get("RESPIRATORY")
        COAGULATION =  line.get("COAGULATION")
        HEPATIC =  line.get("HEPATIC")
        RENAL =  line.get("RENAL")
        ICC =  line.get("ICC")
        ECOG =  line.get("ECOG")
        line['LARANJA'] = 0
        print(line)
                """

SOFA = 14

if SOFA <= 8:
    scorePointSOFA = 1
elif SOFA > 9 and SOFA < 12:
    scorePointSOFA = 2    
elif SOFA > 12 and SOFA <= 14:
    scorePointSOFA = 3
elif SOFA > 14:
    scorePointSOFA = 4
else:
    print("Erro na captura do valor SOFA: %s"% SOFA)

print(scorePointSOFA)