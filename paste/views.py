from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, View
# Create your views here.
from markdown import markdown

from paste.models import Code


class NewPasteView(TemplateView):
    template_name = 'new.html'

    def post(self, request, *args, **kwargs):
        org_text = request._post['code']
        md_text = markdown(org_text)
        code = Code(org_text=org_text, md_text=md_text)
        code.save()
        return redirect('/show/%s/' % code.id)


class ShowView(TemplateView):
    template_name = 'show.html'

    def get_context_data(self, **kwargs):
        code = get_object_or_404(Code, id=kwargs.get('id', 0))
        return {'code': code}


class AllPastesView(TemplateView):
    template_name = 'all.html'

    def get_context_data(self, **kwargs):
        pastes = Code.objects.all()[:10]
        total_pages = len(Code.objects.all())
        page = dict(total_page=range(1, total_pages/10 + 1), current=1)
        return dict(pastes=pastes, page=page)


class PageView(TemplateView):
    template_name = 'all.html'

    def get_context_data(self, **kwargs):
        p = int(kwargs.get('page'))
        start = (p - 1) * 10
        pastes = Code.objects.all()[start: start + 10]
        total_pages = Code.objects.count()
        page = dict(total_page=range(1, total_pages/10 + 1), current=int(kwargs.get('page')), page_num=total_pages/10)
        return dict(pastes=pastes, page=page)


