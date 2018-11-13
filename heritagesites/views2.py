from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import HeritageSite


def index(request):
	return HttpResponse("Hello, world. You're at the UNESCO Heritage Sites index page.")


class AboutPageView(generic.TemplateView):
	template_name = 'heritagesites/about.html'


class HomePageView(generic.TemplateView):
	template_name = 'heritagesites/home.html'


class SiteListView(generic.ListView):
	model = HeritageSite
	context_object_name = 'sites'
	template_name = 'heritagesites/site.html'
	paginate_by = 50

	def get_queryset(self):
		return HeritageSite.objects.all().select_related('heritage_site_category').order_by('site_name') # TODO write ORM code to retrieve all Heritage Sites

class SiteDetailView(generic.DetailView):
	model = HeritageSite
	context_object_name = 'site'
	template_name = 'heritagesites/site_detail.html'# TODO add the correct template string value

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import HeritageSite, CountryArea

def index(request):
	return HttpResponse("Hello, world. You're at the UNESCO Heritage Sites index page.")


class AboutPageView(generic.TemplateView):
	template_name = 'heritagesites/about.html'


class HomePageView(generic.TemplateView):
	template_name = 'heritagesites/home.html'

class SiteListView(generic.ListView):
	model = CountryArea
	context_object_name = 'countries'
	template_name = 'country_area.html'
	paginate_by = 20

	def get_queryset(self):
		return HeritageSite.objects.all().select_related('heritage_site_category').order_by('site_name')

CountryAreaDetailView(generic.DetailView):

