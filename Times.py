import datetime

# this is the time that the first/second truck leaves the hub
# we will not use truck 3
# driver will pick up second trip on truck one
first_truck_list = ['8:00:00']
second_truck_list = ['8:00:00']


def check_time_first_truck(distance):
    new_time = distance / 18  # max speed for each truck defined by the school
    minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))  # distance in minutes
    final_time_formatted = minutes + ':00'
    first_truck_list.append(final_time_formatted)  # add to the list
    sum = datetime.timedelta()  # this is what well use to add time each time its iterated
    for i in first_truck_list:
        (h, m, s) = i.split(':')
        d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        sum += d
    return sum  # return the new MAX Time after appending each iteration


def check_time_second_truck(distance):
    new_time = distance / 18  # max speed for each truck defined by the school
    minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))  # distance in minutes
    final_time_formatted = minutes + ':00'
    second_truck_list.append(final_time_formatted)  # add to the list
    sum = datetime.timedelta()  # this is what well use to add time each time its iterated
    for i in second_truck_list:
        (h, m, s) = i.split(':')
        d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        sum += d
    return sum  # return the new MAX Time after appending each iteration


