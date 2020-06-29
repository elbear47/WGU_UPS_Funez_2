import datetime


# this is the time that the first truck leaves the hub
first_time_list = ['8:00:00']


def check_time_first_truck(distance):
    new_time = distance / 18  # max speed for truck
    distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))  # format distance in minutes
    final_time = distance_in_minutes + ':00'
    first_time_list.append(final_time)
    sum = datetime.timedelta()
    for i in first_time_list:
        (h, m, s) = i.split(':')
        d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        sum += d
    return sum  # return the times after appending each iteration




