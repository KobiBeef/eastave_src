from django.shortcuts import render
from django.http import HttpResponse

from .import models

# Create your views here.
def index(request):
	context_dict = {'boldmessage': "I am bold font from the context"}
	return render(request, 'denzo/index.html', context_dict)

# class Test(generic.TemplateView):
# 	template_name = 'denzo/index.html'

# 	def get_context_data(self, **kwargs):
# 		context = super(Test, self).get_context_data(**kwargs)

# 		context['init_test'] = models.