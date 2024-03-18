from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from deshawnapi.models import Appointment, Walker


class AppointmentView(ViewSet):

    def retrieve(self, request, pk=None):
        appointment = Appointment.objects.get(pk=pk)
        serialized = AppointmentSerializer(appointment, many=False)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def list(self, request):
        appointments = Appointment.objects.all()
        serialized = AppointmentSerializer(appointments, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        client_walker_id = request.data["walkerId"]
        walker_instance = Walker.objects.get(pk=client_walker_id)

        appointment = Appointment()
        appointment.walker = walker_instance
        appointment.date = request.data["appointmentDate"]
        appointment.save()

        serialized = AppointmentSerializer(appointment, many=False)

        return Response(serialized.data, status=status.HTTP_201_CREATED)


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ("id", "walker", "date")
