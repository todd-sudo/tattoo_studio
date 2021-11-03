from django import forms

from .models import ContactModel


class ContactForm(forms.ModelForm):
    """Форма обратной связи"""
    class Meta:
        model = ContactModel
        fields = ('name', 'telegram_username', 'message')
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Ваше имя', 'id': 'fname', 'name': 'fname'}),
            'telegram_username': forms.TextInput(attrs={
                'placeholder': '@username', 'subject': 'subject'}),
            'message': forms.Textarea(attrs={
                'placeholder': 'Текст сообщения',
                'name': 'msg',
                'id': 'msg',
            })
        }

