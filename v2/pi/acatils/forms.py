from django import forms


class ContatoForm(forms.Form):
    nome =  forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem')


class NoticiaForm(forms.Form):
    titulo = forms.CharField(label='Nome', max_length=100)
    autor = forms.CharField(label='E-mail', max_length=100)
    texto = forms.CharField(label='Texto')
