from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic

from . import models

# Create your views here.
class TestView(generic.TemplateView):
# class TestView(generic.ListView):
	template_name = 'denzo/index.html'

	def get_context_data(self, **kwargs):
		context = super(TestView, self).get_context_data(**kwargs)
		context['patient_list'] = models.PatientInfo2.objects.all()
		context['cardio_pt'] = models.PatientInfo2.objects.filter(category="Cardiology")
		context['endo_pt'] = models.PatientInfo2.objects.filter(category="Endocrinology")
		context['gastro_pt'] = models.PatientInfo2.objects.filter(category="Gastroenterology")
		context['nephro_pt'] = models.PatientInfo2.objects.filter(category="Nephrology")
		context['neuro_pt'] = models.PatientInfo2.objects.filter(category="Neurology")

		# context['cardio_count'] = models.PatientInfo2.objects.get(category="Cardiology")
		return context

# def index(request):
# 	patient_list = models.PatientInfo2.objects.all()
# 	category_list = models.PatientInfo2.objects.filter(category=self.category)


# 	context ={
# 		'patient_list': patient_list,
# 		'category_list': category_list,
# 	}

# 	return render(request, 'denzo/index.html', context)
	# context_dict = {'boldmessage': "I am bold font from the context"}
	# return render(request, 'denzo/index.html', context_dict)

# class Test(generic.TemplateView):
# 	template_name = 'denzo/index.html'

# 	def get_context_data(self, **kwargs):
# 		context = super(Test, self).get_context_data(**kwargs)

# 		context['init_test'] = models.

# class OverviewListView(generic.TemplateView):
# 	template_name = 'denzo/index.html'

# 	def get_context_data(self, **kwargs):
# 		context = super(OverviewListView, self).get_context_data(**kwargs)
# 		context['patient_list'] = models.PatientInfo.objects.all()
# 		context['physician_list'] = models.PhysicianInfo.objects.all()

# 		return context