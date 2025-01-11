from django.shortcuts import render
from django.views.generic import TemplateView

def function_base_view(request):
    return render(request, 'func_template.html')

class ClassBaseView(TemplateView):
    template_name = 'class_template.html'
