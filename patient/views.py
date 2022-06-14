from django.shortcuts import redirect, render
import pandas as pd
from .models import DataPatient
# Create your views here.

def home(request):
    return render(request, 'home.html')



def patient(request):
    model = pd.read_pickle('Model_MDS.pickle')

    patient = request.GET['patient']
    age = request.GET['age']
    neurological = request.GET['neurological']
    cardiovascular = request.GET['cardiovascular']
    respiratory = request.GET['respiratory']
    coagulation = request.GET['coagulation']
    hepatic = request.GET['hepatic']
    renal = request.GET['renal']
    icc = request.GET['icc']
    ecog = request.GET['ecog']
    '''scoreSOFA = calculateSOFA(
                                NEUROLOGICAL=neurological,
                                CARDIOVASCULAR=cardiovascular,
                                RESPIRATORY=respiratory,
                                COAGULATION=coagulation,
                                HEPATIC=hepatic,
                                RENAL=renal
                                )
    scoreFragility = ecog
    scoreTotal = calculateTotal(SOFA= int(scoreSOFA), ICC= int(line.get("ICC")), AGE= int(age) )
    '''
    scoreSOFA = '29'
    scoreFragility = ecog #(só é valido para pessoas acima de 60 anos)
    #scoreTotal = '30'

    list_var = []

    list_var.append(age)
    list_var.append(neurological)
    list_var.append(cardiovascular)
    list_var.append(respiratory)
    list_var.append(coagulation)
    list_var.append(hepatic)
    list_var.append(renal)
    list_var.append(icc)
    list_var.append(ecog)
    list_var.append(scoreSOFA)
    list_var.append(scoreFragility)
    #list_var.append(scoreTotal)

    print(list_var)

    classification = model.predict([list_var])
    
    print('A classificação é ', classification)

    DataPatient.objects.create(
        patient=patient,
        age=age,
        neurological=neurological,
        cardiovascular=cardiovascular,
        respiratory=respiratory,
        coagulation=coagulation,
        hepatic=hepatic,
        renal=renal,
        icc=icc,
        ecog=ecog,
        classification=classification[0]
    )

    return render(request, 'patients.html', {'patient':patient,'classification_result': classification[0]})



def db_record(request):
    dataPacientReturn = DataPatient.objects.all()

    context = {
        'patient_records': dataPacientReturn
    }

    return render(request, 'database.html', context)

