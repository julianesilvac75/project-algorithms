def study_schedule(permanence_period, target_time=None):
    try:
        students = 0

        for enter, exit in permanence_period:
            if enter <= target_time <= exit:
                students += 1
        
        return students
    except TypeError:
        return None
