from django import forms
from .models import Link, Categoria

class RegLinkModelForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ["web","link","categoria"]
        labels = {
            "web":"Web",
            "link":"Link",
            "categoria":"Categoria",
        }
        widgets = {
            "web": forms.TextInput(attrs={'class':'form-control'}),
            "link": forms.TextInput(attrs={'class':'form-control'}),
            "categoria": forms.Select(attrs={'class':'form-control'}),
        }
       
class RegCategoriaModelForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["categoria","descripcion"]
        labels = {
            "categoria":"Categoria",
            "descripcion":"Descripcion",
        }
        widgets = {
            "categoria": forms.TextInput(attrs={'class':'form-control'}),
            "descripcion": forms.Textarea(attrs={'class':'form-control'}),
        }
        

