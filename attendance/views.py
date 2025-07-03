from django.shortcuts import render
from rest_framework import viewsets
from .models import Attendance
from .serializers import AttendanceSerializer
from django.db.models import Count
from django.db.models.functions import TruncMonth

# Create your views here.
# attendance/views.py

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


def monthly_attendance(request):
    data = (
        Attendance.objects.annotate(month=TruncMonth('date'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )
    labels = [entry['month'].strftime('%b %Y') for entry in data]
    counts = [entry['count'] for entry in data]
    return render(request, 'charts.html', {
        'labels': labels,
        'counts': counts,
        'chart_title': 'Monthly Attendance Overview'
    })
