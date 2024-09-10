from django import forms


class AddProductPform(forms.Form):
    name = forms.CharField(label='Наименование', widget=forms.TextInput)
    description = forms.CharField(label='Описание', widget=forms.Textarea)
    price = forms.IntegerField(label='Цена')
