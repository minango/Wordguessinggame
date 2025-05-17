import random
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
    "びょういん", "いりぐち", "でぐち",
    "たいよう", "ちきゅう", "ふうけい", "かいがん", "かわぐち", "さんち", "うちゅう", "やまみち",
    "たにま", "ほっきょく", "なんきょく",
    "けいさん", "もんだい", "かいとう", "せいかい", "しけん", "れきし", "すうがく", "ぶんがく",
    "りか", "びじゅつ", "おんがく",
    "こううん", "ふこう", "しあわせ", "あんぜん", "きけん", "たいせつ", "じゆう", "へいわ", "じだい", "しんせつ"
]
count=0
word=random.choice(word_list)
Number=["_"]*len(word)
print("単語当てゲーム📖")
name=input("名前を入力してください")
input("Enterキーを押すとスタートします")
print("文字数:"," ".join(Number))
print("平仮名を一文字入力。または答を入力")
while True:
    answer=input()
    count+=1
    if len(answer)!=1:
        if answer!=word:
            print("二文字以上入力しないでください⚠️")
            continue
        else:
            print(f"正解❗️（{count}回でクリアしました❗️)")
            with open("Wordguessingscores.txt", "a", encoding="utf-8") as file:
                file.write(f"{name}-{count}回\n")
            scores = []
            with open("Wordguessingscores.txt", "r", encoding="utf-8") as readfile:
                for line in readfile:
                    if "-" in line:
                        parts = line.strip().split("-")
                        if len(parts) == 2:
                            username = parts[0]
                            try:
                                attempts = int(parts[1].replace("回", ""))
                                scores.append((username, attempts))
                            except ValueError:
                                pass
            scores.sort(key=lambda x: x[1])
            print("\n🏆 ランキング TOP 5 🏆")
            for i, (username, attempts) in enumerate(scores[:5], start=1):
                print(f"{i}位: {username}（{attempts}回）")
            break
    if answer in word:
        print("その文字は含まれています❗️")
    else:
        print("その文字は含まれていません😭")