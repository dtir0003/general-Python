"""
This program asks the user to input time in seconds as well as the unit conversion from seconds to minutes
and from minutes to hours. There are two outputs given, the first one outputs the time using normal conversion
into hours, minutes and seconds, meanwhile the second one outputs the time using the user-given conversion.
"""

#Prompt the user to input time in seconds on Earth
time_secs_Earth = int(input("TIME ON EARTH\nInput a time in seconds:\n"))

#Compute the time on Earth into hours, minutes and seconds
total_mins_Earth = time_secs_Earth//60
rem_secs_Earth = time_secs_Earth%60
total_hours_Earth = total_mins_Earth//60
rem_mins_Earth = total_mins_Earth%60

#Output the time on Earth in one line
print("\nThe time on Earth is", total_hours_Earth,"hours", rem_mins_Earth,"minutes and", rem_secs_Earth,"seconds.\n")

#Prompt the user to input the conversions to minutes and hours on Trisolaris
secs_to_mins_Tri = int(input("TIME ON TRISOLARIS\nInput the number of seconds in a minute on Trisolaris:\n"))
mins_to_hours_Tri = int(input("Input the number of minutes in an hour on Trisolaris:\n"))

#Compute the time on Trisolaris into hours, minutes and seconds
total_mins_Tri = time_secs_Earth//secs_to_mins_Tri
rem_secs_Tri = time_secs_Earth%secs_to_mins_Tri
total_hours_Tri = total_mins_Tri//mins_to_hours_Tri
rem_mins_Tri = total_mins_Tri%mins_to_hours_Tri

#Output the time on Trisolaris in one line
print("\nThe time on Trisolaris is", total_hours_Tri,"hours", rem_mins_Tri,"minutes and", rem_secs_Tri,"seconds.")

#Prompt the user to input a duration of waiting time in seconds
wait_duration = int(input("\nTIME AFTER WAITING ON TRISOLARIS\nInput a duration in seconds:\n"))

#Add the initial time and the wait duration
wait_duration = time_secs_Earth + wait_duration

#Compute the total time on Trisolaris into hours, minutes and seconds
total_mins_wait = wait_duration//secs_to_mins_Tri
rem_secs_wait = wait_duration%secs_to_mins_Tri
total_hours_wait = total_mins_wait//mins_to_hours_Tri
rem_mins_wait = total_mins_wait%mins_to_hours_Tri

#Output the time on Trisolaris plus the waiting duration in one line
print("\nThe time on Trisolaris after waiting is", total_hours_wait,"hours", rem_mins_wait,"minutes and", rem_secs_wait,"seconds.")
