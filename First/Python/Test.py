from datetime import datetime

def time_overlap(event1, event2):
    start1 = datetime.strptime(event1[0], '%H:%M')
    end1 = datetime.strptime(event1[1], '%H:%M')
    start2 = datetime.strptime(event2[0], '%H:%M')
    end2 = datetime.strptime(event2[1], '%H:%M')

    latest_start = max(start1, start2)
    earliest_end = min(end1, end2)

    if latest_start < earliest_end:
        overlap_start = latest_start.strftime('%H:%M')
        overlap_end = earliest_end.strftime('%H:%M')
        return True, overlap_start, overlap_end
    else:
        return False, None, None

# First user event
print('Please write the starting time of your 1st event (example"10:30"): ')
start1 = input()
print('Please write the ending time of your 1st event (example"15:00"): ')
end1 = input()

# Second user event
print('Please write the starting time of your 2nd event (example"10:30"): ')
start2 = input()
print('Please write the ending time of your 2nd event (example"15:00"): ')
end2 = input()

# Third user event
print('Please write the starting time of your 3rd event (example"10:30"): ')
start3 = input()
print('Please write the ending time of your 3rd event (example"15:00"): ')
end3 = input()

event_1 = [start1, end1]
event_2 = [start2, end2]
event_3 = [start3, end3]

# output
print(time_overlap(event_1, event_2))
print(time_overlap(event_2, event_3))
print(time_overlap(event_3, event_1))



# Examples...

# event_1 = ["02:15", "04:00"]
# event_2 = ["04:00", "06:00"]
# print(time_overlap(event_1, event_2))

# event_1 = ["01:00", "02:35"]
# event_2 = ["01:25", "06:00"]
# print(time_overlap(event_1, event_2))

# event_1 = ["10:15", "11:15"]
# event_2 = ["14:30", "16:40"]
# print(time_overlap(event_1, event_2))