import time
currentTime = time.time()
print(currentTime)
totalSeconds = int(currentTime)
currentSeconds = totalSeconds % 60
totalMinutes = totalSeconds // 60
currentMinutes = totalMinutes % 60
totalHours = totalMinutes // 60
currentHours = totalHours % 24
GMT = eval(input("请输入时区"))
print(currentHours + GMT,":",currentMinutes,":",currentSeconds)