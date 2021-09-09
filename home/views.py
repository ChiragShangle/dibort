from django.shortcuts import render
import requests

# Create your views here.
def contact(request):
	message = False
	if request.method == 'POST':
		data = {}
		for x in request.POST:
			data[x] = request.POST.get(x)
		url = "https://admin.dibortfx.com/form_api.php"
		r = requests.post(url, data=data)
		message = True
	return render(request, 'contact-us.html', {'message': message})

def live(request):
	message = False
	if request.method == 'POST':
		data = {}
		for x in request.POST:
			data[x] = request.POST.get(x)
		url = "https://admin.dibortfx.com/form_api.php"
		r = requests.post(url, data=data)
		message = True
		print(r.text)
	return render(request, 'open-live.html', {'message': message})

def demo(request):
	message = False
	if request.method == 'POST':
		data = {}
		for x in request.POST:
			data[x] = request.POST.get(x)
		url = "https://admin.dibortfx.com/form_api.php"
		r = requests.post(url, data=data)
		print(r.text)
		message = True
	return render(request, 'open-demo.html', {'message': message})