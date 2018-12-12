from django.urls import reverse_lazy
from django.shortcuts import render
from socioABMC.models import Socio
from socioABMC.SocioForm import SocioForm
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

# Create your views here.
error = 'Cantidad de Socios superada, no se puede crear mas Socios'

def valida():
	cant = Socio.objects.count()
	if cant < 4:
		return True
	else:
		return False


class Index(ListView):
	model = Socio
	template_name = 'index.html'
	context_object_name = "socios"
	success_url = reverse_lazy('index')



def alta(request):
	if valida():	
		if request.method == 'POST':
			form = SocioForm(request.POST)
			if form.is_valid():
				form.save()
				return render(request,'templates/index.html')	
		else:
			form = SocioForm()
			return render(request,'alta.html',{'form':form})	
	else:
		global error
		error = 'Cantidad de Socios superada, no se puede crear mas Socios'
	return render(request,'alta.html',{'error':error})


