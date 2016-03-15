from django.conf.urls import url
from django.views.generic import TemplateView

from paste.views import NewPasteView, ShowView, AllPastesView, PageView


urlpatterns = [
    url(r'^$', NewPasteView.as_view(), name='new'),
    url(r'^show/(?P<id>\d+)/', ShowView.as_view(), name='show'),
    url(r'^about$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^all/$', AllPastesView.as_view(), name='all'),
    url(r'^all/(?P<page>\d+)/$', PageView.as_view(), name='all'),
    url(r'^help', TemplateView.as_view(template_name='help.html'), name='help'),

]
