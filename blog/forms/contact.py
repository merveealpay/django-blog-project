from django import forms
from django.core.mail import send_mail

from blog.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name_surname', 'email', 'message')

    def send_email(self, message):
        send_mail(
            subject='Contact Formundan Yeni Mesaj Var!',
            message=message,
            from_email=None,
            recipient_list=['merveealpay@gmail.com'],
            fail_silently=False
        )
