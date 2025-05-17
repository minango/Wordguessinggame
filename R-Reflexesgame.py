import threading
import random
import time
import sys
is_flying = False
is_allowed = False
has_pressed = False
def save_score(name, score):
    try:
        with open("scores.txt", "a") as file:
            file.write(f"{name},{score}\n")
    except Exception as e:
        print(f"エラーが発生しました: {e}")
def load_scores():
    try:
        with open("scores.txt", "r") as file:
            scores = []
            for line_num, line in enumerate(file.readlines(), 1):
                try:
                    name, score = line.strip().split(',')
                    scores.append((name, float(score)))
                except ValueError:
                    print(f"エラー: 行 {line_num} のデータに誤りがあります。 '{line.strip()}' は無効なデータです。")
        return sorted(scores, key=lambda x: x[1]) 
    except FileNotFoundError:
        return []
def wait_for_input():
    global is_flying, is_allowed, has_pressed
    input()
    has_pressed = True
    if not is_allowed:
        is_flying = True
print("💫反射神経ゲーム💫")
name = input("名前を入力してください: ")
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
save_score(name, reaction)
print("\nランキング：")
scores = load_scores()
for i, (name, score) in enumerate(scores[:5], 1):
    print(f"{i}. {name} - {score:.3f}秒")