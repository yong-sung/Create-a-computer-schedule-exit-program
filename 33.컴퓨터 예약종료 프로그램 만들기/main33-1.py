import os
import time

# 1. 컴퓨터를 3600초 (1시간) 후에 종료합니다.
os.system('shutdown /s /t 3600')

# 2. 5초 동안 대기합니다.
time.sleep(5.0)

# 3. 종료 작업을 취소합니다.
os.system('shutdown /a')
