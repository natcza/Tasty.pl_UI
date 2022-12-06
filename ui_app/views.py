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
        restaurant_list = []
        load_data_json = loads(restaurants.text)
        print(load_data_json["results"][0])
        for i in load_data_json["results"]:
            restaurant_list.append((i['name'], i['city'], i["street"], i['house_number'], i['phone_number']))
        ctx = {
            'restaurants': restaurant_list,
        }
        return render(request, 'base.html', ctx)

class RestaurantDetailView(View):
    def get(self, request, pk):
        pass
        # url_restaurant = requests.get('http://127.0.0.1:8001/restaurants/')
