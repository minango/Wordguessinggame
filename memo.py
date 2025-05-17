filename = "memo.txt"
while True:
    memo = input("メモを入力してください：")
    with open(filename, "a", encoding="utf-8") as f:
        f.write(memo + "\n")
    another = input("別のメモを追加しますか？（y/n）：")
    if another.lower() != "y":
        break
    else:
        print("次のメモを追加してください。")
print("メモの追加が完了しました！")
