from django.shortcuts import render
from predict.forms import PredictForm
from rest_framework.response import Response 
import pandas as pd 
from django.shortcuts import render
import joblib


# Create your views here.
def status(data):
   try:
        model = joblib.load(open("logreg.sav", 'rb'))
        X = data 
        y_pred = model.predict(X) 
        print(y_pred)
        result = "The loan applicant is likely to default." if y_pred == 0 else "The loan applicant is not likely to default."
        return result 
   except ValueError as e: 
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST) 


def predict(request):
   if request.method =='POST':
      form = PredictForm(request.POST)

      if form.is_valid():
         Gender = form.cleaned_data['Gender']
         Married = form.cleaned_data['Married']
         Dependents = form.cleaned_data['Dependents']
         Education = form.cleaned_data['Education']
         Self_Employed = form.cleaned_data['Self_Employed']
         ApplicantIncome = form.cleaned_data['ApplicantIncome']
         CoapplicantIncome = form.cleaned_data['CoapplicantIncome']
         LoanAmount = form.cleaned_data['LoanAmount']
         Loan_Amount_Term = form.cleaned_data['Loan_Amount_Term']
         Credit_History = form.cleaned_data['Credit_History']
         Property_Area = form.cleaned_data['Property_Area']
         data = pd.DataFrame({'Gender':[Gender], 'Married':[Married], 'Dependents':[Dependents], 'Education':[Education],
         'Self_Employed':[Self_Employed], 'ApplicantIncome':[ApplicantIncome], 'CoapplicantIncome':[CoapplicantIncome], 
         'LoanAmount':[LoanAmount], 'Loan_Amount_Term':[Loan_Amount_Term], 'Credit_History':[Credit_History], 
         'Property_Area':[Property_Area]})
         result = status(data)
         return render(request, 'predict/result.html', {"data": result}) 
            
   form = PredictForm()
   return render(request, 'predict/predict.html', {'form':form})
