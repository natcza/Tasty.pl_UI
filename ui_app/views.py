# https://pypi.org/project/requests/
import requests
from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse, Http404
from json import loads
from Dashboard.settings import SERVER_DEVELOPMENT


class RestaurantsView(View):
    def get(self, request):
        # print('blablabla', request.data)
        url_restaurant = requests.get(SERVER_DEVELOPMENT + '/restaurants/')
        code = url_restaurant.status_code
        # print(f'c: {code}')
        if code == 200:
            print(f'c: {url_restaurant.status_code}')
            # print('blablabla', request.data)
            arr1 = []
            loads_restaurant = loads(url_restaurant.text)
            lr_results = loads_restaurant['results']

            print(f'lrr: {lr_results}')
            for i in lr_results:
                arr1.append((i['name'], i['city']))
            print(arr1[0][0])
            ctx = {
                'restaurants': arr1,
            }
            return render(request, 'base.html', ctx)
        elif code == 404:
            raise Http404("No MyModel matches the given query.")


class RestaurantDetailView(View):
    def get(self, request, restaurant_id):
        pass
        # url_restaurant = requests.get('http://127.0.0.1:8001/restaurants/')
