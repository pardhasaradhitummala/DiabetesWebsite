import pickle
from pathlib import Path

from django.shortcuts import render

file_dir = Path(__file__).resolve().parent.parent



def home(request):
    return render(request,'index.html')

def get_prediction(request):
    loaded_model = pickle.load(open(str(file_dir) + "\\finalized_model.sav", 'rb'))
    num_preg = float(request.POST['num_preg'])
    glucose_conc = float(request.POST['glucose_conc'])
    diastolic_bp = float(request.POST['diastolic_bp'])
    insulin = float(request.POST['insulin'])
    bmi = float(request.POST['bmi'])
    diab_pred = float(request.POST['diab_pred'])
    age = float(request.POST['age'])
    skin = float(request.POST['skin'])
    result = loaded_model.predict([[num_preg,glucose_conc,diastolic_bp,insulin,bmi,diab_pred,age,skin]])
    if result == 0:
        msg = "congrats you are Non Diabetic"
    else:
        msg = "sorry you are diabetic"
    return render(request, 'out.html',{'msg':msg})
