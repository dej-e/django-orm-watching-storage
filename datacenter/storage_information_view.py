from datacenter.models import Visit
from datacenter.models import format_duration
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = [
        {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            "duration": format_duration(visit.get_duration()),
            "is_strange": visit.is_long(minutes=10),
        } for visit in Visit.objects.filter(leaved_at__isnull=True)
    ]
    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
