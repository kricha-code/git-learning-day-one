import time

countdown_time = 10
while countdown_time > 0:
    time.sleep(1)
    print(f"Countdown: {countdown_time} seconds remaining")
    countdown_time -= 1
print("🚀 Liftoff!")
