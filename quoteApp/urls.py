from django.conf.urls import url
from . import views

app_name = 'quoteApp'

urlpatterns = [
    url(r'^quoteformpage/',views.quote_input_form.as_view(),name="quote_input_form")
]
