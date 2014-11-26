from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView
from django.shortcuts import render_to_response

# Create your views here.
def hello(request):
	name = "Denis:) "
	html = "<html><body> Hi %s, this works for you :)</body></html>"%name
	return HttpResponse(html)

def hello_template(request):
	name = "Denis:) "
	job = "Software developer"
	t = get_template('hello.html')
	html = t.render(Context({
		'name': name,
		'job': job
		}))
	return HttpResponse(html)

def hello_template_simple(request):
	job = "Programmer :)"
	name = "Denis"
	return render_to_response("hello.html", {"name": name, "job": job})

class HelloTemplate(TemplateView):
	template_name = "hello_class.html"

	def get_context_data(self, **kwargs):
		context = super(HelloTemplate, self).get_context_data(**kwargs)
		context['name'] = "Denis"
		return context

