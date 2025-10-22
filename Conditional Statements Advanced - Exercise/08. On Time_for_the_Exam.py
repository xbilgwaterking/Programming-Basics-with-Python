test_hour = int(input())
test_minutes = int(input())
student_hour = int(input())
student_minutes = int(input())


test_start_time = test_hour * 60 + test_minutes
student_arrive_time = student_hour * 60 + student_minutes

if student_arrive_time > test_start_time:
    print("Late")
    time_diff = student_arrive_time - test_start_time
    if time_diff < 60:
        print(f"{time_diff} minutes after the start")
    else:
        hours = time_diff // 60
        minutes = time_diff % 60
        print(f"{hours}:{minutes:02d} hours after the start")

elif student_arrive_time == test_start_time or test_start_time - student_arrive_time <= 30:
    print("On time")
    if student_arrive_time != test_start_time:
        minutes = test_start_time - student_arrive_time
        print(f"{minutes} minutes before the start")

elif student_arrive_time < test_start_time:
    print("Early")
    time_diff = test_start_time - student_arrive_time
    if time_diff < 60:
        print(f"{time_diff} minutes before the start")
    else:
        hours = time_diff // 60
        minutes = time_diff % 60
        print(f"{hours}:{minutes:02d} hours before the start")
