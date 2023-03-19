from django import forms
from .models import BankClient, Label



class BankClientForm(forms.ModelForm):
    class Meta:
        model = BankClient
        fields = ('__all__')
        widgets = {
            'age' :forms.TextInput(attrs={'class':'form-control','placeholder':'Age'}),
            'job' :forms.TextInput(attrs={'class':'form-control','placeholder':'Job'}),
            'marital' :forms.TextInput(attrs={'class':'form-control','placeholder':'Marital'}),
            'education' :forms.TextInput(attrs={'class':'form-control','placeholder':'Education'}),
            'housing' :forms.TextInput(attrs={'class':'form-control','placeholder':'Housing'}),
            'loan' :forms.TextInput(attrs={'class':'form-control','placeholder':'Loan'}),
            'campaign' :forms.TextInput(attrs={'class':'form-control','placeholder':'Campaign'}),
            'previous' :forms.TextInput(attrs={'class':'form-control','placeholder':'previous'}),
            'poutcome' :forms.TextInput(attrs={'class':'form-control','placeholder':'poutcome'}),
            'empvarrate' :forms.TextInput(attrs={'class':'form-control','placeholder':'Emp.var.rate'}),
            'conspriceidx' :forms.TextInput(attrs={'class':'form-control','placeholder':'Cons.prce.idx'}),
            'consconfidx' :forms.TextInput(attrs={'class':'form-control','placeholder':'Cons.conf.idx'}),
            'euribor3m' :forms.TextInput(attrs={'class':'form-control','placeholder':'Euribor3m'}),
            'nremployed' :forms.TextInput(attrs={'class':'form-control','placeholder':'Nr.employed'})
        }

class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ('__all__')
        # widgets = {
        #     'label' :forms.TextInput(attrs={'class':'form-control','placeholder':'Age'}),
        # }