import time
from plyer import notification

print("Water Reminder")
print("You will be reminded to drink water every hour")

while True:
    notification.notify(
        title="Drink your water!",
        message="Time to get hydrated again.",
        timeout=10,
    )
    time.sleep(60*60)
