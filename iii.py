import random
import time
from typing import List

# 牌的初始化
def generate_deck() -> List[str]:
    small_cards = [str(i) for i in range(1, 11)]
    big_cards = [f"大{i}" for i in range(1, 11)]
    deck = []
    for card in small_cards + big_cards:
        deck.extend([card] * 4)
    red_cards = ["2", "7", "10", "大2", "大7", "大10"]
    return deck, red_cards


# 判断是否能组成顺子
def can_form_sequence(cards: List[str]) -> bool:
    if len(cards) != 3:
        return False

    def get_card_value(card: str) -> int:
        if card.startswith('大'):
            return int(card[1:]) + 10
        return int(card)

    values = sorted([get_card_value(card) for card in cards])
    if (values[1] - values[0] == 1 and values[2] - values[1] == 1) or \
            set(cards) == set(['2', '7', '10']) or set(cards) == set(['大2', '大7', '大10']):
        return True
    return False


# 判断是否为叉叉
def is_cross(cards: List[str]) -> bool:
    if len(cards) != 3:
        return False
    num_cards = [card for card in cards if not card.startswith('大')]
    big_cards = [card for card in cards if card.startswith('大')]
    if len(num_cards) == 2 and len(big_cards) == 1 and num_cards[0] == num_cards[1] and num_cards[0][1:] == big_cards[0][1:]:
        return True
    elif len(num_cards) == 1 and len(big_cards) == 2 and big_cards[0] == big_cards[1] and num_cards[0][1:] == big_cards[0][1:]:
        return True
    return False


# 判断是否为坎
def is_triplet(cards: List[str]) -> bool:
    return len(cards) == 3 and cards[0] == cards[1] == cards[2]


# 判断是否为对
def is_pair(cards: List[str]) -> bool:
    return len(cards) == 2 and cards[0] == cards[1]


# 计算胡数
def calculate_hu(player: 'Player', red_cards: List[str]) -> int:
    hand = player.hand
    hu_count = 0
    for i in range(len(hand)):
        for j in range(i + 1, len(hand)):
            for k in range(j + 1, len(hand)):
                sub_group = [hand[i], hand[j], hand[k]]
                if can_form_sequence(sub_group):
                    if set(sub_group).issubset(set(red_cards)):
                        hu_count += 9
                    else:
                        hu_count += 3
                elif is_cross(sub_group):
                    if set([sub_group[0][1:] if sub_group[0].startswith('大') else sub_group[0],
                            sub_group[1][1:] if sub_group[1].startswith('大') else sub_group[1],
                            sub_group[2][1:] if sub_group[2].startswith('大') else sub_group[2]]).issubset(set(['2', '7', '10'])):
                        hu_count += 9
                    else:
                        hu_count += 3
                elif is_triplet(sub_group):
                    if sub_group[0] in red_cards:
                        hu_count += 6
                    else:
                        hu_count += 1
    return hu_count

class Player:
    def __init__(self, name: str):
        self.name = name
        self.hand = []
        self.is_hu = False
        self.score = 0

    def draw_card(self, deck: list):
        """摸牌方法"""
        card = deck.pop()
        self.hand.append(card)
        print(f"{self.name} 摸到了一张牌：{card}")
        return card

    def discard_card(self) -> str:
        """玩家打牌方法"""
        print(f"\n{self.name} 当前的手牌：{', '.join(self.hand)}")
        while True:
            try:
                card_to_discard = input(f"{self.name} 选择打出一张牌：")
                if card_to_discard in self.hand:
                    self.hand.remove(card_to_discard)
                    print(f"{self.name} 打出牌：{card_to_discard}")
                    return card_to_discard
                else:
                    print("你必须打出手中已有的牌，请重新选择。")
            except KeyboardInterrupt:
                print("\n检测到用户中断，游戏退出。")
                exit(0)  # 退出程序

    def decide_action(self, card: str, red_cards: List[str], deck: list) -> str:
        """玩家决策方法"""
        actions = []

        # 检查是否可以吃
        if self.can_eat(card):
            actions.append("吃")
        
        # 检查是否可以碰
        if self.hand.count(card) == 2:
            actions.append("碰")
        
        # 总是可以选择比
        actions.append("比")

        # 加入不要选项
        actions.append("不要")

        # 如果可以选择多个操作，列出让玩家选择
        if actions:
            print(f"{self.name} 可以选择以下操作: {', '.join(actions)}")
            while True:
                action = input(f"{self.name} 请选择操作: {', '.join(actions)}: ")
                if action in actions:
                    print(f"{self.name} 选择了：{action} {card}")
                    if action == "不要":
                        # 如果选择不要，则摸牌并出牌
                        self.draw_card(deck)
                        discarded_card = self.discard_card()
                        return discarded_card
                    else:
                        return action
                else:
                    print(f"无效选择，请重新选择：{', '.join(actions)}")
        else:
            print(f"{self.name} 选择了：不要 {card}")
            # 如果没有其他操作，直接摸牌并出牌
            self.draw_card(deck)
            discarded_card = self.discard_card()
            return discarded_card

    def can_eat(self, card: str) -> bool:
        """
        判断是否能吃牌。例如，如果手牌中有能与之组成顺子的牌，则可以吃。
        这里我们假设吃牌逻辑为：如果手牌中有相邻的牌（差1或差2），可以吃。
        """
        card_value = int(card) if not card.startswith('大') else int(card[1:])
        # 寻找手牌中是否有能吃该牌的组合
        for c in self.hand:
            c_value = int(c) if not c.startswith('大') else int(c[1:])
            if abs(card_value - c_value) <= 2:  # 可以吃的逻辑
                return True
        return False


class Computer(Player):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def discard_card(self) -> str:
        card_to_discard = random.choice(self.hand)
        self.hand.remove(card_to_discard)
        print(f"{self.name} 打出牌：{card_to_discard}")
        return card_to_discard

    def can_eat(self, card: str) -> bool:
        """
        判断是否能吃牌。例如，如果手牌中有能与之组成顺子的牌，则可以吃。
        这里我们假设吃牌逻辑为：如果手牌中有相邻的牌（差1或差2），可以吃。
        """
        card_value = int(card) if not card.startswith('大') else int(card[1:])
        # 寻找手牌中是否有能吃该牌的组合
        for c in self.hand:
            c_value = int(c) if not c.startswith('大') else int(c[1:])
            if abs(card_value - c_value) <= 2:  # 可以吃的逻辑
                return True
        return False

    def decide_action(self, card: str, red_cards: List[str]) -> str:
        actions = []
        if self.can_eat(card):  # 可以吃牌
            actions.append("吃")
        if len([c for c in self.hand if c == card]) == 2:  # 可以碰牌
            actions.append("碰")
        actions.append("比")  # 暂时直接放入比牌选项
        actions.append("不要")

        action = random.choice(actions)
        print(f"{self.name} 选择了：{action} {card}")
        if action == "吃":
            self.hand.append(card)
        elif action == "碰":
            self.hand = [c for c in self.hand if c != card]
        return action


# 检查胡牌
def check_hu(player: Player, red_cards: List[str]) -> bool:
    hu_count = calculate_hu(player, red_cards)
    if hu_count >= 1:
        print(f"{player.name} 胡牌！胡数: {hu_count}")
        player.is_hu = True
        player.score += hu_count
        return True
    return False


# 游戏主逻辑
def game() -> None:
    deck, red_cards = generate_deck()
    random.shuffle(deck)
    player = Player("玩家")
    computer = Computer("电脑")

    # 发牌
    for _ in range(5):
        player.draw_card(deck)
        computer.draw_card(deck)

    while not player.is_hu and not computer.is_hu:
        # 玩家出牌
        discarded_card = player.discard_card()
        player_action = player.decide_action(discarded_card, red_cards, deck)  # 传递 deck 参数
        computer_action = computer.decide_action(discarded_card, red_cards)
        computer.draw_card(deck)
        if check_hu(computer, red_cards):
            break

        # 电脑出牌
        discarded_card = computer.discard_card()
        player_action = player.decide_action(discarded_card, red_cards, deck)  # 传递 deck 参数
        player.draw_card(deck)
        if check_hu(player, red_cards):
            break

    # 游戏结束后输出分数并询问是否继续
    print(f"本局结束，{player.name} 分数: {player.score}，{computer.name} 分数: {computer.score}")
    continue_game = input("是否继续下一局？(y/n): ")
    if continue_game.lower() != 'y':
        print("游戏结束")
    else:
        game()  # 继续下一局


# 运行游戏
if __name__ == "__main__":
    game()