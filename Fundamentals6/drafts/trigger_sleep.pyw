import os

# 0 for no hibernation,
# 1 for sleeping,
# 0 to indicate no force (safely suspend).
# Windows command to put the system to sleep
os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

