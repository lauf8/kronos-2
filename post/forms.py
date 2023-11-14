from django import forms


class PostForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    text = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={"class": "form-check-label"}))