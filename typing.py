import random
import time
import threading
word_list = [
    "りんご", "みかん", "ばなな", "すいか", "もも", "めろん", "いちご", "なし", "ぶどう", "さくらんぼ",
    "おちゃ", "こうちゃ", "こーひー", "みず", "じゅーす", "ぎゅうにゅう", "のり", "たまご", "にく", "さかな",
    "いぬ", "ねこ", "うま", "しか", "さる", "ぞう", "きりん", "くま", "たぬき", "うさぎ",
    "とり", "かえる", "へび", "かに", "くらげ", "いか", "たこ", "ぺんぎん", "わに", "こあら",
    "いす", "つくえ", "とけい", "かべ", "まど", "でんき", "ほん", "ざっし", "ふく", "ぼうし",
    "かさ", "くつ", "けいたい", "でんわ", "せんたくき", "れいぞうこ", "そうじき", "てれび",
    "おもちゃ", "けんだま", "こま", "しゃぼんだま", "ふうせん", "すごろく", "ぱずる", "さいころ", "ゆうえんち",
    "やま", "かわ", "うみ", "そら", "はな", "き", "もり", "つき", "たいよう", "ほし",
    "こうえん", "がっこう", "いえ", "まち", "でんしゃ", "えき", "くうこう", "びじゅつかん",
    "うれしい", "かなしい", "たのしい", "こわい", "さびしい", "ねむい", "つかれた", "はらへった", "びっくり",
    "じしん", "てんき", "じてん", "ひこうき", "れんしゅう", "べんきょう", "せんせい", "がっこう", "しゅくだい",
    "けいたい", "でんわ", "しゃしん", "うんてん", "じどうしゃ", "しごと", "やすみ", "しんごう", "ちず",
    "びょういん", "いりぐち", "でぐち", "たいよう", "ちきゅう", "ふうけい", "かいがん", "かわぐち", "さんち", "うちゅう", "やまみち",
    "たにま", "ほっきょく", "なんきょく", "けいさん", "もんだい", "かいとう", "せいかい", "しけん", "れきし", "すうがく", "ぶんがく",
    "りか", "びじゅつ", "おんがく", "こううん", "ふこう", "しあわせ", "あんぜん", "きけん", "たいせつ", "じゆう", "へいわ", "じだい", "しんせつ"
]
count = 0
miss_count = 0
game_over = False
name = input("名前を入力してください: ")
def end():
    global game_over
    time.sleep(30)
    game_over = True
def file_keep():
    global count, miss_count, name
    with open("typing_scores.txt", "a", encoding="utf-8") as file:
        file.write(f"{name}-{count}個-{miss_count}ミス\n")
    scores = []
    with open("typing_scores.txt", "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split("-")
            if len(parts) == 3:
                uname = parts[0]
                try:
                    ucount = int(parts[1].replace("個", ""))
                    umiss = parts[2].replace("ミス", "")
                    scores.append((uname, ucount, umiss))
                except ValueError:
                    continue
    scores.sort(key=lambda x: x[1], reverse=True)
    print("🏆 ランキング 🏆")
    for i, (uname, ucount, umiss) in enumerate(scores[:5], start=1):
        print(f"{i}位: {uname} - {ucount}個 - {umiss}ミス")
def play_game():
    global game_over, count, miss_count
    e = threading.Thread(target=end)
    e.start()
    while not game_over:
        word = random.choice(word_list)
        print(word)
        user_input = input(">> ")
        if user_input != word:
            print("ミス❗️")
            miss_count += 1
        else:
            count += 1
    print(f"\n時間切れ❗️\n打てた数: {count}個 - ミス: {miss_count}回\n")
    file_keep()
print("タイピングゲーム💻")
input("Enterキーを押すとスタートします")
print("Ready...")
time.sleep(2)
print("Go!")
play_game()