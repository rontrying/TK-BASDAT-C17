def convert_minutes_to_hours(minutes):
    hours = minutes // 60
    minutes = minutes % 60
    if hours > 0:
        return f"{hours} jam {minutes} menit"
    else:
        return f"{minutes} menit"