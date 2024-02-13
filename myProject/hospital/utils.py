from datetime import datetime, time, timedelta
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required




def time_slot(start_time, end_time, interval):
    slots = []
    current_time = datetime.combine(datetime.today(), start_time) 
    end_datetime = datetime.combine(datetime.today(), end_time)   
    while current_time <= end_datetime:
        slots.append(current_time.strftime('%H:%M'))
        current_time = current_time + interval
    return slots

def is_slot_available(doctor, date, time_str):
    time_format = '%H:%M'
    try:
        appointment_time = datetime.strptime(time_str, time_format).time()
    except ValueError:
        return False
    
    return not doctor.appointment_set.filter(date=date, time=appointment_time).exists()


def doctor_required(function):
    @login_required
    def wrap(request, *args, **kwargs):
        if request.user.is_doctor:
            return function(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap