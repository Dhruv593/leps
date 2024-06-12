from django.shortcuts import render
import pickle as pkl
import numpy as np
from .models import *
from django.conf import settings
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder


def home(request):

    if request.method == "POST":
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        feedback = request.POST.get('feedback')

        # Insert data into the Django admin
        FeedBack.objects.create(
            name=name,
            email=email,
            mobile=mobile,
            feedback=feedback
        )
    return render(request, 'index.html')


def prediction(request):
    return render(request, 'prediction.html', )


def result(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        gender = request.POST.get('gender')
        married = request.POST.get('married')
        dependents = request.POST.get('dependents')
        education = request.POST.get('education')
        self_employed = request.POST.get('selfEmployed')
        applicant_income = request.POST.get('applicantIncome')
        coapplicant_income = request.POST.get('coapplicantIncome')
        loan_amount = request.POST.get('loanAmount')
        loan_amount_term = request.POST.get('loanAmountTeam')
        credit_history = request.POST.get('creditHistory')
        property_area = request.POST.get('propertyArea')

        Loan_Data.objects.create(
            name=name,
            gender=gender,
            married=married,
            dependents=dependents,
            education=education,
            self_employed=self_employed,
            applicantIncome=applicant_income,
            coapplicantIncome=coapplicant_income,
            loan_amount=loan_amount,
            loan_amount_term=loan_amount_term,
            credit_history=credit_history,
            property_area=property_area
        )
        # Retrieve form data
        gender = int(request.POST.get('gender'))
        married = int(request.POST.get('married'))
        dependents = int(request.POST.get('dependents'))
        education = int(request.POST.get('education'))
        self_employed = int(request.POST.get('selfEmployed'))
        applicant_income = float(request.POST.get('applicantIncome'))
        coapplicant_income = float(request.POST.get('coapplicantIncome'))
        loan_amount = float(request.POST.get('loanAmount'))
        loan_amount_term = float(request.POST.get('loanAmountTeam'))
        credit_history = float(request.POST.get('creditHistory'))
        property_area = int(request.POST.get('propertyArea'))

        # Load the trained model
        model = pkl.load(open('finalized_model.sav', 'rb'))

        # Perform prediction
        prediction = model.predict([[gender, married, dependents, education, self_employed, applicant_income,
                                   coapplicant_income, loan_amount, loan_amount_term, credit_history, property_area]])

        # Determine eligibility result
        if prediction == 1:
            result = 'Eligible'
        else:
            result = 'Not Eligible'
            
        # Pass prediction result to template
        context = {'result': result}
    return render(request, 'prediction.html', context)
    

def team(request):
    return render(request, 'team.html')