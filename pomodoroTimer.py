import time

# Function to display time in mm:ss format
def format_time(seconds):
    mins, secs = divmod(seconds, 60)
    return f'{mins:02}:{secs:02}'

# Pomodoro Timer function
def pomodoro_timer(work_duration, short_break, long_break, cycles):
    for cycle in range(1, cycles + 1):
        print(f"Cycle {cycle}/{cycles}: Work session starting!")
        countdown(work_duration, "Work session")
        
        if cycle % 4 == 0:
            print("Long break time!")
            countdown(long_break, "Long break")
        else:
            print("Short break time!")
            countdown(short_break, "Short break")
    
    print("Pomodoro session complete! Great job!")

# Function to handle countdown
def countdown(duration, session_type):
    while duration:
        print(f"{session_type}: {format_time(duration)}", end="\r")
        time.sleep(1)
        duration -= 1
    print(f"{session_type} finished! Time for the next step!\n")

if __name__ == "__main__":
    # Pomodoro Settings
    work_duration = 25 * 60  # 25 minutes
    short_break = 5 * 60  # 5 minutes
    long_break = 15 * 60  # 15 minutes
    cycles = 4  # 4 Pomodoro cycles
    
    # Start the Pomodoro Timer
    pomodoro_timer(work_duration, short_break, long_break, cycles)
