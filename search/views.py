from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from django.http import Http404

from .models import Products, Dependensies

class SearchResultsView(ListView):
	model = Products
	template_name = 'search_results.html'

	def get_queryset(self):
		mark = self.request.GET.get('markPrinter')
		model = self.request.GET.get('modelPrinter')

		if (mark != None) and (model != None):
			dependensies_list = Dependensies.objects.filter(Q(markPrinter__icontains=mark) and Q(modelPrinter__icontains=model))
		else:
			raise Http404("Не корректные данные запроса! Воспользуйтесь формой на <a href='/'>главной странице</a>!")
		
		idList = []
		for item in dependensies_list:
			idList.append(item.cartridgeId)
		object_list = Products.objects.filter(productId__in=idList)

		if not object_list:
			raise Http404("Не корректные данные запроса! Воспользуйтесь формой на главной странице!")
		else:
			return object_list