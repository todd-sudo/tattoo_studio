from django.http import HttpResponseRedirect
from django.shortcuts import render

from services.send_message_telegram import send_message
from services.views_exceptions import BaseView
from .forms import ContactForm
from master.models import Master


class ContactView(BaseView):
    """Выводит страницу КОНТАКТЫ"""
    def get(self, request):
        form = ContactForm(request.POST or None)
        return render(request, 'contact/contact.html', {'form': form})


class ContactSendView(BaseView):
    """Отправляет сообщение из контактной формы в Telegram администраторам"""
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST or None)
        if form.is_valid():
            appeal = form.save(commit=False)
            appeal.name = form.cleaned_data['name']
            appeal.telegram_username = form.cleaned_data['telegram_username']
            appeal.message = form.cleaned_data['message']

            masters = Master.objects.all()
            message = f'{appeal.name}\n{appeal.telegram_username}\n{appeal.message}'

            for master in masters:
                for _id in master.telegram_id.all():
                    send_message(_id, message)

            appeal.save()
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/contact/')
