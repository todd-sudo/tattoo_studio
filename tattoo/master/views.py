from django.views.generic import ListView, DetailView, CreateView

from services.send_message_telegram import send_message
from services.views_exceptions import BaseView
from .forms import RecordToMasterForm
from .models import Master


class MastersListView(ListView, BaseView):
    """Выводит список мастеров"""
    model = Master
    context_object_name = 'masters'
    template_name = 'master/masters_list.html'


class MasterDetailView(DetailView, BaseView):
    """Выводит информацию о конкретном мастере"""
    model = Master
    context_object_name = 'master'
    template_name = 'master/master_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        master = context['master']
        context['skills'] = master.master_skills.all()
        context['form'] = RecordToMasterForm(self.request.POST or None)
        return context


class RecordToMaster(CreateView, BaseView):
    """Запись на сеанс к мастеру"""
    model = Master
    form_class = RecordToMasterForm

    def form_valid(self, form):
        form.instance.master_id = self.kwargs.get('pk')
        master = Master.objects.get(id=form.instance.master_id)
        master_telegram_id = master.telegram_id.all()
        client = form.save(commit=False)
        client.name = form.instance.name
        client.telegram_username = form.instance.telegram_username
        client.message = form.instance.message
        message = f'{client.name}\n{client.telegram_username}\n{client.message}'

        for tg_id in master_telegram_id:
            send_message(tg_id, message)

        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.master.get_absolute_url()

