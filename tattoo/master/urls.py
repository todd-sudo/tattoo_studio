from django.urls import path

from . import views


urlpatterns = [
    path('master/<int:pk>/record', views.RecordToMaster.as_view(), name='record_to_master'),
    path('', views.MastersListView.as_view(), name='masters_list'),
    path('master/<int:pk>', views.MasterDetailView.as_view(), name='master_detail'),
]
