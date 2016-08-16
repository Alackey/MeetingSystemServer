from django.core.serializers.json import Serializer as Builtin_Serializer
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views import View
from . import models
import json


class LoginView(View):
    def post(self, request):
        body = json.loads(request.body.decode('utf-8'))

        try:
            user = models.User.objects.get(name=body['name'])
        except ObjectDoesNotExist:
            return JsonResponse({
                'error': True, 'errorMessage': 'User Not Found'
            })

        if user.password == body['password']:
            return JsonResponse({'error': False, 'id': user.id})
        else:
            return JsonResponse({
                'error': True, 'errorMessage': 'Incorrect Password'
            })


class UserView(View):
    def get(self, request):
        employeeID = request.GET.get('employeeID')
        serializer = Serializer()
        user = serializer.serialize(
            [models.User.objects.get(employeeID=employeeID)]
        )
        return JsonResponse(user[1:-1], safe=False)


class MeetingView(View):
    def post(self, request):
        body = json.loads(request.body.decode('utf-8'))
        return JsonResponse({'error': False})


# Override Django serializer
class Serializer(Builtin_Serializer):
    def get_dump_object(self, obj):
        return self._current
