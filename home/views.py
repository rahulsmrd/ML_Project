from django.shortcuts import render,HttpResponse
import joblib
from home.ml_model import *
from home.models import *

# Create your views here.

def index(request):
    if request.method =="POST":
        symptoms=[]
        if request.POST.get('symptom1'):
            symptoms.append(request.POST.get('symptom1').lower())
        if request.POST.get('symptom2'):
            symptoms.append(request.POST.get('symptom2').lower())
        if request.POST.get('symptom3'):
            symptoms.append(request.POST.get('symptom3').lower())
        if request.POST.get('symptom4'):
            symptoms.append(request.POST.get('symptom4').lower())
        if request.POST.get('symptom5'):
            symptoms.append(request.POST.get('symptom5').lower())

        trained_model = joblib.load("trained_model.pkl")
        data=create_symptoms_data(symptoms)
        disease=trained_model.predict([data])
        disease_predicted=get_disease(disease[0])
        print(disease_predicted,symptoms)
        # url_disease=disease_url.objects.get(disease_name=disease_predicted.lower())
        return render(request,'home/index.html',{'message':True,'disease':disease_predicted,'symptoms':symptoms})
    return render(request,'home/index.html',{'symptoms_list':symptoms_list})