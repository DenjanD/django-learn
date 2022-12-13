from django import forms

class classForm(forms.Form):
    title = forms.CharField(label="Judul Postingan")
    body = forms.CharField(
        label="Isi Postingan",
        widget=forms.Textarea(attrs={"rows":"5"}))