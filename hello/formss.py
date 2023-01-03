from django import forms
from .models import Post


class classForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'body'
        ]

        widgets={
            'title': forms.TextInput(
                attrs = {
                    'class' : 'form',
                    'placeholder':'Masukkan Judul',
                }
            )
        }
# class classForm(forms.Form):
#     title = forms.CharField(label="Judul Postingan")
#     body = forms.CharField(
#         label="Isi Postingan",
#         widget=forms.Textarea(attrs={"rows":"5"}))