from django import forms

class InputForm(forms.Form):
    
    name = forms.FloatField(label='name')
    gender = forms.FloatField(label='gender')
    married = forms.FloatField(label='married')
    dependents = forms.FloatField(label='depentents')
    education = forms.FloatField(label='education')
    self_employed = forms.FloatField(label='self_employed')
    applicantIncome = forms.FloatField(label='applicantIncome')
    coapplicantIncome = forms.FloatField(label='coapplicantIncome')
    loan_amount_term = forms.FloatField(label='loan_amount_term')
    credit_history = forms.FloatField(label='credit_history')
    property_area = forms.FloatField(label='property_area')