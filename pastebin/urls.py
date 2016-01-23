from django.conf.urls import url
from django.views.generic import TemplateView

from paste.views import NewPasteView, ShowView


urlpatterns = [
    url(r'^$', NewPasteView.as_view(), name='new'),
    url(r'^show/(?P<id>\d+)/', ShowView.as_view(), name='show'),
    url(r'^about$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^all', TemplateView.as_view(template_name='all.html'), name='all'),
    url(r'^help', TemplateView.as_view(template_name='help.html'), name='help'),

]
