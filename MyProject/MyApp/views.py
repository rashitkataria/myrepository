from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from .forms import NameForm

def home(request):

	return render(request, 'home.html')

def emp_detail(request):
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			""" print('form is valid')
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			email = form.cleaned_data['email']
			age = form.cleaned_data['age']
			print(first_name)
			print(last_name)
			print(email) """
			obj = Main() #gets new object
			obj.f_name = form.cleaned_data['first_name']
			obj.l_name = form.cleaned_data['last_name']
			obj.email = form.cleaned_data['email']
			obj.age = form.cleaned_data['age']
			obj.save()

		else:
			print('form is not valid')

	form = NameForm()
	return render(request, 'form.html', {'form_template':form})

def detail_fetch(request):
	data = Main.objects.all()
	#print(data)
	
	return render (request, 'detail.html', {'detail_data':data})

def form_template(request):
	
	return render(request, 'forms_bootstrap.html')
