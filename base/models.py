from django.db import models


class Loan_Data(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    married = models.IntegerField()
    dependents = models.IntegerField()
    education = models.IntegerField()
    self_employed = models.IntegerField()
    applicantIncome = models.BigIntegerField()
    coapplicantIncome = models.FloatField()
    loan_amount = models.FloatField(default=0.0)
    loan_amount_term = models.FloatField()
    credit_history = models.FloatField()
    property_area = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class FeedBack(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()  # New field for email
    mobile = models.CharField(max_length=15)  # New field for mobile
    feedback = models.TextField()

    def __str__(self):
        return self.name
