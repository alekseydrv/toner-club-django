from django.shortcuts import render
from search.models import Products, Queries, Dependensies
from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json
 
 
def index(request):
    """
    View for home page
    """
    name_products = Products.objects.all()
    queriesList = Queries.objects.all()
    dependensyList = Dependensies.objects.values('markPrinter').annotate(markCount=Count('markPrinter'))

    return render(
        request,
        'index.html',
        context={'dependensies': dependensyList,'queries': queriesList},
    )

def ajax(request):
    """
    Ajax request for form on home page
    """
    markPrinter = request.GET.get('markPrinter') 
    #modelPrinters = serializers.serialize("json", Dependensies.objects.values('modelPrinter').filter(markPrinter=markPrinter))
    modelPrinters = Dependensies.objects.order_by('modelPrinter').filter(markPrinter=markPrinter)
    modelsList = {}

    for item in modelPrinters:
        modelsList[item.cartridgeId] = item.modelPrinter
    return JsonResponse(modelsList)
