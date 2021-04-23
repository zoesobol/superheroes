from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from . import models
from bootstrap_datepicker_plus import DatePickerInput
from django.forms.widgets import DateInput
from ckeditor.fields import RichTextField

class FormularioRegistro(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'login-form form-control', 'placeholder': 'Email'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'login-form form-control', 'placeholder':'Nombre'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'login-form form-control', 'placeholder':'Apellido'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(FormularioRegistro, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'login-form form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password1'].widget.attrs['class'] = 'login-form form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Ingrese contraseña'
        self.fields['password2'].widget.attrs['class'] = 'login-form form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Vuelva a ingresar contraseña'



class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(LoginForm,self).__init__(*args,**kwargs)
        self.fields["username"].widget.attrs.update({'class' : 'login-form form-control','placeholder' : "Nombre de usuario", 'type' : 'text'})
        self.fields["password"].widget.attrs.update({'class' : 'login-form form-control','placeholder' : "Contraseña", 'type' : 'text'})



class SuperheroeForm(forms.ModelForm):
    name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Superheroe'}))
    header_image = forms.ImageField(label="Imagen de fondo", widget=forms.FileInput(attrs={'class': 'form-control'}))
    profile_image = forms.ImageField(label="Foto de perfil", widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = models.Superheroe
        fields= '__all__'
        widgets = {
            'superpower': forms.CheckboxSelectMultiple(attrs={'empty_label':'None',' class': 'form-check-input', 'type':'checkbox'}),
            'heroe_villano': forms.RadioSelect(attrs={'empty_label':'None','class': 'form-check-input', 'type':'radio'}),
            'date': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    }

    def __init__(self, *args, **kwargs):
        super(SuperheroeForm, self).__init__(*args, **kwargs)

        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].label = 'Descripción'
        self.fields['date'].label = 'Fecha de Nacimiento'
        self.fields['superpower'].label = 'Superpoderes'
        self.fields['heroe_villano'].label = '¿Héroe o Villano?'
