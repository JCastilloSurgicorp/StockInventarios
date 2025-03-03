from django import forms

class inputAsist(forms.Form):
    input = forms.CharField(widget=forms.Textarea,label="", max_length=200)