import threading
import random
import time
import sys
is_flying = False
is_allowed = False
has_pressed = False
def wait_for_input():
    global is_flying, is_allowed, has_pressed
    input()
    has_pressed = True
    if not is_allowed:
        is_flying = True
print("💫反射神経ゲーム💫")
input("Enterキーを押すとスタートします")
input_thread = threading.Thread(target=wait_for_input)
input_thread.daemon = True
input_thread.start()
print("Ready...")
wait_time = random.randint(3, 10)
start_wait = time.time()
while time.time() - start_wait < wait_time:
    if is_flying:
        print("⚠️ フライング！")
        sys.exit()
    time.sleep(0.01)
is_allowed = True
print("Enter❗️")
start = time.time()
while not has_pressed:
    time.sleep(0.01)
end = time.time()
reaction = end - start
print(f"あなたの反射速度は {reaction:.3f} 秒です！")