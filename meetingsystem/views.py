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

        try:
            user = serializer.serialize(
                [models.User.objects.get(employeeID=employeeID)]
            )
        except ObjectDoesNotExist:
            return JsonResponse({
                'error': True, 'errorMessage': 'User Not Found'
            })
        return JsonResponse({'error': False, 'user': user[1:-1]}, safe=False)


class UserAllView(View):
    def get(self, request):
        serializer = Serializer()
        users = serializer.serialize(
            models.User.objects.all()
        )
        return JsonResponse({'error': False, 'data': users})


class MeetingView(View):
    def post(self, request):
        body = json.loads(request.body.decode('utf-8'))
        # Create meeting
        meeting = models.Meeting(
            owner=body['owner'],
            title=body['title'],
            description=body['description'],
            room=body['room'],
            startTime=body['startTime'],
            endTime=body['endTime'],
            date=body['date'],
            employees=body['employees'],
            accepted=body['accepted'],
            declined=body['declined'],
            isActive=body['isActive']
        )
        meeting.save()
        # Add meeting info to schedule
        # for employee in meeting.employees:
        #     temp_schedule = models.Schedule(
        #         type=
        #         id=
        #         title=
        #         startTime=
        #         endTime=
        #         date=
        #     )
        #     temp_schedule.save()
        return JsonResponse({'error': False, 'id': meeting.id})


# Override Django serializer: Serializer only returns object fields
class Serializer(Builtin_Serializer):
    def get_dump_object(self, obj):
        return self._current
