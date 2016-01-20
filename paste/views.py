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
