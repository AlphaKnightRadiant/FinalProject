from django import forms
from RyaFree.models import Option

#class FormName(forms.Form):
#    name = forms.CharField()

class FreeForm(forms.Form):
    CHOICES = (('a','Monday'),
               ('b','Teusday'),
               ('c','Wednesday'),
               ('d','Thursday'),
               ('e','Friday'),
               ('f','Saturday'),
               ('g','Sunday'))
    a = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple())
class NewOption(forms.ModelForm):
    class Meta:
        model = Option
        fields = '__all__'
