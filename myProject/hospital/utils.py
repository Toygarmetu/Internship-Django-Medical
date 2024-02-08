from datetime import datetime, time, timedelta


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
        # Convert string to time object for accurate comparison
        appointment_time = datetime.strptime(time_str, time_format).time()
    except ValueError:
        # Handle incorrect format, perhaps log an error or raise an exception
        return False
    
    return not doctor.appointment_set.filter(date=date, time=appointment_time).exists()