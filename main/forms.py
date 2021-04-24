from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from . import models
from bootstrap_datepicker_plus import DatePickerInput
from django.forms.widgets import DateInput
from ckeditor.fields import RichTextField
from s3upload.widgets import S3UploadWidget

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



superpower_choices = (
    ('Volar', 'Volar'),
    ('Superinteligencia', 'Superinteligencia'),
    ('Vista de rayo láser', 'Vista de rayo láser'),
    ('Billetera gorda', 'Billetera gorda'),
)


class SuperheroeForm(forms.ModelForm):
    


    name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Superheroe'}))
    header_image = forms.URLField(label="Imagen de fondo", widget=S3UploadWidget(dest='example_destination'))
    profile_image = forms.URLField(label="Foto de Perfil", widget=S3UploadWidget(dest='example_destination'))
    superpower = forms.MultipleChoiceField(required=False, choices=superpower_choices, label='Superheroes', widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input', 'type':'checkbox'}))

    class Meta:
        model = models.Superheroe
        fields= '__all__'
        widgets = {
            'heroe_villano': forms.RadioSelect(attrs={'class': 'form-check-input', 'type':'radio'}),
            'date': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    }

    def __init__(self, *args, **kwargs):
        super(SuperheroeForm, self).__init__(*args, **kwargs)

        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].label = 'Descripción'
        self.fields['date'].label = 'Fecha de Nacimiento'
        self.fields['heroe_villano'].label = '¿Héroe o Villano?'
        #self.fields['superpower'] = forms.MultipleChoiceField(choices=superpower_choices, label='Superpoderes', widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input', 'type':'checkbox'}))
