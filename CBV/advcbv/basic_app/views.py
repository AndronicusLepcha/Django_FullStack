from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# # Create your views here.
# class CBView(View):
#     def get(self,request):
#         return HttpResponse("Class Based View")

class Index(TemplateView):
    template_name = "index.html"

    #template injection
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme']='The coder Robot'
        return context

def index(request):
    return render(request,'index.html')