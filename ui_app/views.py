# https://pypi.org/project/requests/
import requests
from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse, Http404
from json import loads
from Dashboard.settings import SERVER_DEVELOPMENT

class RestaurantsView(View):
    def get(self, request):
        restaurants = requests.get(SERVER_DEVELOPMENT + '/restaurants/')
        arr1 = []
        res_1 = loads(restaurants.text)
        print(res_1["results"][0])
        for i in res_1["results"]:
            arr1.append((i['name'], i['city'], i["street"], i['house_number'], i['phone_number']))
        print(arr1[0][0])
        ctx = {
            'restaurants': arr1,
        }
        return render(request, 'base.html', ctx)

class RestaurantDetailView(View):
    def get(self, request, restaurant_id):
        pass
        # url_restaurant = requests.get('http://127.0.0.1:8001/restaurants/')
