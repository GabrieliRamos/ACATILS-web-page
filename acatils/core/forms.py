from django import forms
from django.views.generic import ListView
from django.core.mail.message import EmailMessage
from django.core.mail import send_mail


from acatils.settings import EMAIL_HOST_USER
from .models import News


class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    subject = forms.CharField(label='Assunto', max_length=100)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        content = f'Nome: {name}\nE-mail: {email}\nAssunto: {subject}\n\n\nMensagem: \n\n{message}'

        email_message = EmailMessage(
            subject = subject,
            body = content,
            from_email = EMAIL_HOST_USER,
            to= [email],
            reply_to= (email,),
        )

        email_message.send()
