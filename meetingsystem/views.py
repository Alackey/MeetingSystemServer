from django.http import JsonResponse
from django.views import View


class UserView(View):
    def get(self, request):
        return JsonResponse({'hello': 'world'})
