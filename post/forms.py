from django import forms


class PostForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    text = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))

