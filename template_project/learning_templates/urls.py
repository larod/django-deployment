from django.conf.urls import url
from learning_templates import views

app_name = 'learning_templates'

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$',views.other,name='other')
]
