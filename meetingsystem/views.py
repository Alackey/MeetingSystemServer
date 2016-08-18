from django.core.serializers.python import Serializer as Builtin_Serializer
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views import View
from . import models
import json


class LoginView(View):
    # Check login
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


class UsersGetView(View):
    # Get specific user
    def get(self, request, employeeID):
        serializer = Serializer()

        try:
            user = serializer.serialize(
                [models.User.objects.get(employeeID=employeeID)]
            )
        except ObjectDoesNotExist:
            return JsonResponse({
                'error': True, 'errorMessage': 'User Not Found'
            })
        return JsonResponse({'error': False, 'user': user[0]}, safe=False)


class UsersView(View):
    # Get all users
    def get(self, request):
        serializer = Serializer()
        users = serializer.serialize(
            models.User.objects.all()
        )
        return JsonResponse({'error': False, 'data': users}, safe=False)

    # Add new user
    def post(self, request):
        body = json.loads(request.body.decode('utf-8'))
        user, created = models.User.objects.get_or_create(
            employeeID=body['employeeID']
        )
        if created:
            user.name = body['name']
            user.password = body['password']
            user.save()
            return JsonResponse({'error': False, 'id': user.id})
        else:
            return JsonResponse({
                'error': True,
                'errorMessage': 'EmployeeID already exists'
            })


class MeetingsView(View):
    # Create new meeting
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

        # Add timeblock for owner
        time_block = models.TimeBlock(
            employeeID=meeting.owner,
            type='MEETING',
            meetingID=meeting.id,
            title=meeting.title,
            startTime=meeting.startTime,
            endTime=meeting.endTime,
            date=meeting.date
        )
        time_block.save()

        # Add invites to employees InviteBox
        for employee in meeting.employees:
            invite = models.Invite.objects.create(
                owner=employee,
                meetingOwner=meeting.owner,
                meetingId=meeting.id,
                title=meeting.title,
                startTime=meeting.startTime,
                endTime=meeting.endTime,
                date=meeting.date
            )
            invite.save()
        return JsonResponse({'error': False, 'id': meeting.id})


class InvitesView(View):
    # Get invites for user
    def get(self, request, employeeID):
        serializer = Serializer()
        invites = models.Invite.objects.filter(owner=employeeID)
        invites_array = serializer.serialize(invites)
        return JsonResponse({'error': False, 'data': invites_array})


# Override Django serializer: Serializer only returns object fields
class Serializer(Builtin_Serializer):
    def get_dump_object(self, obj):
        return self._current
