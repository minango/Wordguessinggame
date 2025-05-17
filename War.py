import random
ranks1 = list(range(2, 15))
ranks2 = list(range(2, 15))
ranks3 = list(range(2, 15))
ranks4 = list(range(2, 15))
card = ranks1 + ranks2 + ranks3 + ranks4
random.shuffle(card)
player1_card = card[:26]
player2_card = card[26:]
s = input("⚔️戦争⚔️\nEnterキーを押すとスタートします")
if s == "":
    turn = 0
    max_turn = 52
    while player1_card and player2_card and turn < max_turn:
        turn += 1
        input(f"\n🔁 {turn}ターン目：Enterを押してください")
        card1 = player1_card.pop()
        card2 = player2_card.pop()
        if card1 > card2:
            win = "player1"
            pile = [card1, card2]
            random.shuffle(pile)
            player1_card = pile + player1_card
        elif card2 > card1:
            win = "player2"
            pile = [card1, card2]
            random.shuffle(pile)
            player2_card = pile + player2_card
        else:
            win = False
        if win:
            print(f"player1は{card1}, player2は{card2} → {win}の勝利❗️")
        else:
            print(f"引き分け！ player1: {card1}, player2: {card2}")
        if turn % 10 == 0:
            random.shuffle(player1_card)
            random.shuffle(player2_card)
    print("\n🎲 ゲーム終了 🎲")
    print(f"ターン数: {turn}")
    print(f"player1の残りカード: {len(player1_card)}")
    print(f"player2の残りカード: {len(player2_card)}")
    if len(player1_card) > len(player2_card):
        print("🎉 player1の勝ち！")
    elif len(player2_card) > len(player1_card):
        print("🎉 player2の勝ち！")
    else:
        print("🤝 引き分け！")
