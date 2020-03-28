from django import forms
class TextForm(forms.Form):
    textinfo=forms.CharField(label='펀딩 내용 ',widget=forms.Textarea(attrs={'class':'form-control'}))
