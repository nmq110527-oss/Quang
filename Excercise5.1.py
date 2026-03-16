import time

current_time = time.time()

total_seconds = int(current_time)

days = total_seconds // (24 * 3600)
remaining = total_seconds % (24 * 3600)

hours = remaining // 3600
remaining = remaining % 3600

minutes = remaining // 60
seconds = remaining % 60

print(f"Days since epoch: {days}")
print(f"Current time: {hours:02d}:{minutes:02d}:{seconds:02d}")