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


class RoomsView(View):
    # Create room
    def post(self, request):
        body = json.loads(request.body.decode('utf-8'))

        room = models.Room.objects.create(
            name=body['name'],
            capacity=body['capacity']
        )
        return JsonResponse({'error': False})


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


class MeetingsOverlapView(View):
    # Check rooms and meetings that for overlapping
    def get(self, request):
        date = request.GET.get('date')
        employees = eval(request.GET.get('employees'))
        startTime = request.GET.get('startTime')
        endTime = request.GET.get('endTime')
        duration = request.GET.get('duration')
        room_names = {}

        # Get rooms with enough capacity
        rooms = models.Room.objects.filter(capacity__gte=len(employees))
        for room in rooms:
            room_names[room.name] = ""

        # Check meetings based on date, time, or duration
        serializer = Serializer()
        for room, value in room_names.items():

            # Check if the time is availble in rooms
            if date and startTime and endTime:
                meetings = models.Meeting.objects.filter(
                    room=room,
                    date=date,
                    startTime__lte=endTime,
                    endTime__gte=startTime
                )
                room_names[room] = True if meetings else False

            # Get all meetings for the date and room number
            elif date and duration:
                meetings = models.Meeting.objects.filter(
                    room=room,
                    date=date
                )
                meetings_ser = serializer.serialize(meetings)
                room_names[room] = meetings_ser

        return JsonResponse({'error': False, 'rooms': room_names})


class TimeBlocksView(View):
    # Get timeblocks for employees with specific date range
    def get(self, request):
        employees = eval(request.GET.get('employees'))
        startDate = request.GET.get('startDate')
        endDate = request.GET.get('endDate')
        date = request.GET.get('date')
        time_blocks = []

        # Get timeblocks and add them to list
        for employee in employees:
            # Specific date is givin
            if date is not None:
                time_blocks += models.TimeBlock.objects.filter(
                    employeeID=employee,
                    date=date
                )

            # Range of dates
            else:
                time_blocks += models.TimeBlock.objects.filter(
                    employeeID=employee,
                    date__range=(startDate, endDate)
                )

        serializer = Serializer()
        time_blocks_ser = serializer.serialize(time_blocks)
        return JsonResponse({'error': False, 'timeblocks': time_blocks_ser})

    # Add timeblock
    def post(self, request):
        body = json.loads(request.body.decode('utf-8'))

        timeblock = models.TimeBlock.objects.create(
            employeeID=body['employeeID'],
            type=body['type'],
            meetingID=body['meetingID'],
            title=body['title'],
            startTime=body['startTime'],
            endTime=body['endTime'],
            date=body['date']
        )
        timeblock.save()
        return JsonResponse({'error': False, 'id': timeblock.id})


class InvitesView(View):
    # Get invites for user
    def get(self, request, employeeID):
        serializer = Serializer()
        invites = models.Invite.objects.filter(owner=employeeID)
        invites_array = serializer.serialize(invites)
        return JsonResponse({'error': False, 'data': invites_array})


# Override Django serializer: Serializer returns object fields and obj id
class Serializer(Builtin_Serializer):
    def get_dump_object(self, obj):
        result = self._current
        # Add id to resulting dict if in obj
        if obj.id is not None:
            result['id'] = obj.id
        return result
