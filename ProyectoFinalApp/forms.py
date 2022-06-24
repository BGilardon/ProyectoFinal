from django import forms





class crearUsuario(forms.Form):
    nombre = forms.CharField(max_length=30)
    mail = forms.EmailField()
    nacimiento = forms.DateField()

class crearPosteo(forms.Form):
    titulo = forms.CharField(max_length=20)
    cuerpo = forms.CharField(max_length=200)    

class crearModerador(forms.Form):
    nombre = forms.CharField(max_length=30)
    mail = forms.EmailField()
    sector = forms.CharField(max_length=30)