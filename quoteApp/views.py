from django.shortcuts import render
from django.views.generic import View,TemplateView

# Create your views here.


class Home_Page(TemplateView):
    template_name = 'quoteApp/quoteformpage.html'


class quote_input_form(TemplateView):
    template_name = 'quoteApp/quote_form_page.html'
