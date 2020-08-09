#!/usr/local/bin/python3 

import time 

"""
A countdown timer that takes in the number of seconds that it minutes that the timer
should run for.
"""
def countdown_timer(value, timer_type):
    t = value * 60
    while t != 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("{} complete!".format(timer_type))

def main():
    # Getting user input
    print("welcome to the pomodoro timer")
    print("Enter the number of minutes that you want to study for: ")
    study_time = int(input())
    print("Enter the number of minutes that you want to take a break for: ")
    break_time = int(input())
    print("Enter the number of times you want to repeat this loop: ")
    repeat_count = int(input())
    # Reading user input back to user
    print("Okay, you're going to study for {} minutes and relax for {} minutes, and this will repeat {} times.".format(study_time, break_time, repeat_count))
     
    # Make these immutable, and multiply by 60 for minutes
    for _ in range(repeat_count):
        countdown_timer(study_time, "pomodoro")  
        countdown_timer(break_time, "break")
    print("You have completed your pomodoro session. Goodbye!")

if __name__ == "__main__":
    main()
