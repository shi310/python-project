import math
import random

# 这是方格的数据
# -1 代表银行
# 0 代表空地
# data = [0,0,0,0,0,0,0,0,0,0,0,0]
# data = [0,0,0,0,0,0,-1,0,0,0,0,0]
# data = [0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,-1,0,0,0,0,0]
data = [0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0]




# 玩家数组对象
class Players:
    def __init__(self) -> None:
        self.data: list[Player] = []
    
    def from_dict(self, json: list[dict[str, int]]):
        for _json in json:
            self.data.append(Player().from_dict(_json))
        return self

# 玩家对象
class Player:
    def __init__(self) -> None:
        self.location = 0
        self.balance = 0
        self.turns = 0
    
    def from_dict(self, json: dict):
        keys = json.keys()

        if 'location' in keys and json['location'] != None:
            self.location = json['location']
        
        if 'balance' in keys and json['balance'] != None:
            self.balance = json['balance']
        
        if 'turns' in keys and json['turns'] != None:
            self.turns = json['turns']

        if 'id' in keys and json['id'] != None:
            self.id = json['id']

        if 'step' in keys and json['step'] != None:
            self.step = json['step']

        return self

# 玩家实例
players_data = [
    {
        "id": 1,
        "location" : 0,
        "balance" : 0,
        "turns" : 0,
        "step":0,
    },
    {
        "id": 2,
        "location" : 0,
        "balance" : 0,
        "turns" : 0,
        "step":0,

    },
    {
        "id": 3,
        "location" : 0,
        "balance" : 0,
        "turns" : 0,
        "step":0,

    },
    {
        "id": 4,
        "location" : 0,
        "balance" : 0,
        "turns" : 0,
        "step":0,

    },
]   
players = Players().from_dict(players_data)

# 建造费用
pay_build = 1

# 建造的概率
build_probability = 1

# 过路费
pay_pass = 10

# 游戏结束
is_game_over = False

# 圈数
rounds = 4

# 路过银行的费用
pay_bank = 1

# 名次
winer:list[int] = []

print('游戏开始')

# 游戏开始
while not is_game_over:

    over_plyaers = 0
    for player in players.data:
        if player.turns >= rounds:
            over_plyaers += 1
    
    if over_plyaers == len(players.data):
        is_game_over = True
        break

    for player in players.data:

        if player.turns < rounds:

            # 掷骰子
            dice = random.randint(1,6)
            print('玩家 %d 正在掷骰子, 点数为: %d' % (player.id, dice))

            # 刷新移动步数
            player.location += dice
            # 如果超过起点就重置为新的坐标
            if player.location >=  len(data):
                player.location = player.location - len(data)
            print('玩家 %d 目前的位置为: %d' % (player.id, player.location))

            # 刷新移动的步数
            player.step += dice
            print('玩家 %d 移动步数: %d' % (player.id, player.step))

            # 计算圈数
            player.turns = math.floor(player.step / len(data))
            if player.turns >= rounds:
                    winer.append(player.id)
            print('玩家 %d 圈数: %d' % (player.id, player.turns))
            

            

            if data[player.location] == 0:
                print('玩家 %d 目前的位置没有任何建筑' % (player.id))

                is_build = random.uniform(0,1)
                if is_build < build_probability:
                    print('玩家 %d 决定建造' % (player.id))

                    data[player.location] = player.id
                    player.balance -= pay_build
                    print('玩家 %d 在位置 %d 上建造了房子 花费 %d , 余额为: %d' % (player.id,player.location,pay_build,player.balance))
                else:
                    print('玩家 %d 放弃建造' % (player.id))



            elif data[player.location] == -1:
                player.balance -= pay_bank
                print('玩家 %d 经过了银行, 支付 %d  , 余额为: %d' % (player.id,pay_bank,player.balance))

            
            elif data[player.location] != player.id:
                print('玩家 %d 经过了玩家 %d 的建筑, 支付 %d 过路费  , 余额为: %d' % (player.id,data[player.location],pay_pass,player.balance))
                player.balance -= pay_pass
                
                for _p in players.data:
                    if _p.id == data[player.location]:
                        _p.balance += pay_pass
            
            for p in players.data:
                print('玩家 %d 的余额为 %d' % (p.id, p.balance))

            print('----------------------------------')

for i in range(0,len(winer)):
    players.data[winer[i]-1].balance += (0-i+len(winer)-i-1) * pay_pass
    print('玩家 %d 获得第 %d 名 奖励: %d 分' % (players.data[winer[i]-1].id, i+1, (0-i+len(winer)-i-1) * pay_pass))

print('----------------------------------')

for player in players.data:
    print('玩家 %d 得分: %d' % (player.id, player.balance))


    
