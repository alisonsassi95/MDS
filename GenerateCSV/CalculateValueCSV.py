
import os
import csv

def calculateTotal(SOFA, ICC, AGE):
    # Menor pontuação total

    def calculatePointSOFA(SOFA):

        if SOFA <= 8:
            scorePointSOFA = 1
        elif SOFA >= 9 and SOFA <= 11:
            scorePointSOFA = 2    
        elif SOFA >= 12 and SOFA <= 14:
            scorePointSOFA = 3
        elif SOFA > 14:
            scorePointSOFA = 4
        else:
            print("the scorePointSOFA with problem")
            scorePointSOFA = 1000

        return scorePointSOFA

    def calculatePointICC(ICC):

        if ICC == 4:
            scorePointICC = 3
        else:
            scorePointICC = 0
           
        return scorePointICC

    def calculatePointAgeGroup(AGE):

        if AGE <= 49:
            scorePointAgeGroup = 1
        elif AGE >= 50 and AGE <= 69:
            scorePointAgeGroup = 2    
        elif AGE >= 70 and AGE <= 84:
            scorePointAgeGroup = 3
        elif AGE >= 85:
            scorePointAgeGroup = 4
        else:
            print("the scorePointAgeGroup with problem")
            scorePointAgeGroup = 1000

        return scorePointAgeGroup

    scoreCalculateTotal = (
                            calculatePointAgeGroup(AGE) + 
                            calculatePointICC(ICC) + 
                            calculatePointSOFA(SOFA)
                          )

    return scoreCalculateTotal

def calculateFragility(ECOG):

    scoreFragility = ECOG

    return scoreFragility

def calculateSOFA(NEUROLOGICAL,CARDIOVASCULAR,RESPIRATORY,COAGULATION,HEPATIC,RENAL):

    scoreCalculateSOFA = (
        int(NEUROLOGICAL) + 
        int(CARDIOVASCULAR) +
        int(RESPIRATORY) +
        int(COAGULATION) +
        int(HEPATIC) +
        int(RENAL))

    return scoreCalculateSOFA

def toListCSV(DATA_LIST):
    data = []
    data.append(str(list(DATA_LIST.values())).replace("'","").replace("[","").replace("]",""))
    DataCSV = str(data).replace("'","").replace("[","").replace("]","")
    
    return DataCSV

def createFileIfNotExist(Data_Header):
    NameCSV = 'data_Calculate_AMIB.csv'
    existFile = os.path.exists(NameCSV)

    if not (existFile):        
        arq = open(NameCSV,'w')
        arq.write(Data_Header)
        arq.close()
        return True

def insertOneRegisterInFile(DATA_REGISTER):

    arq = open('data_Calculate_AMIB.csv','a')
    arq.write('\n')
    print('Data register')
    print(DATA_REGISTER)
    arq.write(DATA_REGISTER)
    arq.close()
    
    return True


# Main Program

existFile = os.path.exists('data.csv')
if not (existFile):
    print("Arquivo CSV nao existe.")
    exit()

createFileIfNotExist('ID,PATIENT,AGE,NEUROLOGICAL,CARDIOVASCULAR,RESPIRATORY,COAGULATION,HEPATIC,RENAL,ICC,ECOG,3SCORE_SOFA,2SCORE_FRAGILITY,1CALCULATE_TOTAL')

with open("data.CSV") as fileCSV:
    readingCSV = csv.DictReader(fileCSV, delimiter=",")
    ValuesCalculateTotal = []

    for line in readingCSV:

        scoreSOFA = calculateSOFA(
                                  NEUROLOGICAL=line.get("NEUROLOGICAL"),
                                  CARDIOVASCULAR=line.get("CARDIOVASCULAR"),
                                  RESPIRATORY=line.get("RESPIRATORY"),
                                  COAGULATION=line.get("COAGULATION"),
                                  HEPATIC=line.get("HEPATIC"),
                                  RENAL=line.get("RENAL")
                                  )
        
        line['3SCORE_SOFA'] = scoreSOFA
        scoreFragility = calculateFragility(line.get("ECOG"))
        line['2SCORE_FRAGILITY'] = scoreFragility
        scoreTotal = calculateTotal(SOFA= int(scoreSOFA), ICC= int(line.get("ICC")), AGE= int(line.get("AGE")) )
        line['1CALCULATE_TOTAL'] = scoreTotal
        
        insertOneRegisterInFile(toListCSV(line))
