from PySide2.QtWidgets import *
from PySide2.QtUiTools import *
from PySide2.QtGui import *
from random import *

app = QApplication()
app.setWindowIcon(QIcon('logo1.png'))
ui = QUiLoader().load('User_interface.ui')
cntChoice = 0
Name = ['魔女的炎之花', '魔女常然之羽', '魔女破灭之时', '魔女的心之火', '焦灼的魔女帽']
attributes = ['生命值', '生命值 ', '攻击力', '攻击力 ', '防御力', '防御力 ', '元素充能效率', '元素精通', '暴击率', '暴击伤害']
attriOfMain = ['生命值', '生命值 ', '攻击力', '攻击力 ', '防御力', '元素充能效率', '物理伤害加成', '火元素伤害加成', '元素精通', '暴击率', '暴击伤害', '治疗加成']
datasOfMainAttri = [[717, 920, 1123, 1326, 530, 1733, 1936, 2139, 2343, 2545, 2749, 2952, 3155, 3358, 3561, 3764, 3967, 4171, 4374, 4577, 4780],  # HP 0
                    [7, 9, 11, 12.9, 14.9, 16.9, 18.9, 20.9, 22.8, 24.8, 26.8, 28.8, 30.8, 32.8, 34.7, 36.7, 38.7, 40.7, 42.7, 44.6, 46.6],  # HP% 1
                    [47, 60, 73, 86, 100, 113, 126, 139, 152, 166, 179, 192, 205, 219, 232, 245, 258, 272, 285, 298, 311],  # ATK 2
                    [7, 9, 11, 12.9, 14.9, 16.9, 18.9, 20.9, 22.8, 24.8, 26.8, 28.8, 30.8, 32.8, 34.7, 36.7, 38.7, 40.7, 42.7, 44.6, 46.6],  # ATK% 3
                    [8.7, 11.2, 13.7, 16.2, 18.6, 21.1, 23.6, 26.1, 28.6, 31, 33.5, 36, 38.5, 40.9, 43.4, 45.9, 48.4, 50.8, 53.3, 55.8, 58.3],  # DEF% 4
                    [7.8, 10, 12.2, 14.4, 16.6, 18.8, 21, 23.2, 25.4, 27.6, 29.8, 32, 34.2, 36.4, 38.6, 40.8, 43, 45.2, 47.4, 49.6, 51.8],  # Elm Recharge 5
                    [8.7, 11.2, 13.7, 16.2, 18.6, 21.1, 23.6, 26.1, 28.6, 31, 33.5, 36, 38.5, 40.9, 43.4, 45.9, 48.4, 50.8, 53.3, 55.8, 58.3],  # Phy DMG% 6
                    [7, 9, 11, 12.9, 14.9, 16.9, 18.9, 20.9, 22.8, 24.8, 26.8, 28.8, 30.8, 32.8, 34.7, 36.7, 38.7, 40.7, 42.7, 44.6, 46.6],  # %Elm DMG% 7
                    [28, 36, 44, 52, 60, 68, 76, 84, 91, 99, 107, 115, 123, 131, 139, 147, 155, 163, 171, 179, 187],  # EM 8
                    [4.7, 6, 7.3, 8.6, 9.9, 11.3, 12.6, 13.9, 15.2, 16.6, 17.9, 19.2, 20.5, 21.8, 23.2, 24.5, 25.8, 27.1, 28.4, 29.8, 31.1],  # CRIT rate% 9
                    [9.3, 12, 14.6, 17.3, 19.9, 22.5, 25.2, 27.8, 30.5, 33.1, 35.7, 38.4, 41, 43.7, 46.3, 49, 51.6, 54.2, 56.9, 59.5, 62.2],  # CRIT dmg% 10
                    [5.4, 6.9, 8.4, 10, 11.51, 13, 14.5, 16.1, 17.6, 19.1, 20.6, 22.1, 23.7, 25.2, 26.7, 28.2, 29.8, 31.3, 32.8, 34.3, 35.9]]  # Healing Bonus% 11
datas = [[209.13, 239, 268.88, 298.75],  # 小生命值
         [4.08, 4.66, 5.25, 5.83],  # 百分比生命值
         [13.62, 15.56, 17.51, 19.45],  # 小攻击力
         [4.08, 4.66, 5.25, 5.83],  # 百分比攻击力
         [16.2, 18.52, 20.83, 23.15],  # 小防御力
         [5.1, 5.82, 6.56, 7.29],  # 百分比防御力
         [4.53, 5.18, 5.83, 6.48],  # 元素充能效率
         [16.32, 18.65, 20.98, 23.31],  # 元素精通
         [2.72, 3.11, 3.5, 3.89],  # 暴击率
         [5.44, 6.22, 6.99, 7.77]]  # 暴击伤害
flag = [False]  # [是否已选择圣遗物]
typeOfRelic = 0
attriOfRelic = []
level = 0
mainAttri = [0, 0]


def show(typeofrelic, attributeofrelic, mainAttri):
    img = QPixmap(f"image/rrelic{typeofrelic+1}.png")
    ui.pic.clear()
    ui.relicName.setText(Name[typeofrelic])
    macont = attriOfMain[mainAttri[0]]
    if mainAttri[0] in [1, 3, 4, 6, 7, 9, 10, 11]: macont += ':+ {:.1f}%'.format(datasOfMainAttri[mainAttri[0]][mainAttri[1]])
    else: macont += f': +{datasOfMainAttri[mainAttri[0]][mainAttri[1]]}'
    cont = f'  + {level}\n'
    for i in attributeofrelic:
        if i[0] in [1, 3, 5, 6, 8, 9]:
            n = 0
            for q in i[1]: n += datas[i[0]][q]
            cont += '·'+attributes[i[0]]+': + {:.1f}%'.format(n)  # 一位小数+%显示
        else:
            n = 0
            for q in i[1]: n += datas[i[0]][q]
            cont += '·'+attributes[i[0]]+f': + {round(n)}'  # 整数显示
        cont += '\n'
    ui.pic.setPixmap(img)
    ui.mainAttribute.setText(macont)
    ui.Attri.setText(cont)


def getmainattri(tor, nope):  # 为圣遗物生成主词条
    t = []
    if tor == 0: return [0, 0]
    elif tor == 1: return [2, 0]
    elif tor == 2:
        t = [1, 4, 3, 5, 8][randint(0, 4)]
        while attriOfMain[t] in nope: t = [1, 4, 3, 5, 8][randint(0, 4)]
    elif tor == 3:
        t = [1, 4, 3, 6, 7, 8][randint(0, 5)]
        while attriOfMain[t] in nope: t = [1, 4, 3, 6, 7, 8][randint(0, 5)]
    elif tor == 4:
        t = [1, 4, 3, 8, 9, 10, 11][randint(0, 6)]
        while attriOfMain[t] in nope: t = [1, 4, 3, 8, 9, 10, 11][randint(0, 6)]
    return [t, 0]


def create1():  # 随机生成圣遗物
    global typeOfRelic, attriOfRelic, level, mainAttri
    level = 0
    attriOfRelic = []
    typeOfRelic = randint(0, 4)
    a = sample(range(0, 9), randint(3, 4))
    for i in a:  # 随机生成三或四种属性
        attriOfRelic.append([i, [randint(0, 3)]])  # 第一个是属性种类，共10种。第二个是四个数据中随机选一个作属性值\\
    mainAttri = getmainattri(typeOfRelic, [attributes[i[0]] for i in attriOfRelic])
    show(typeOfRelic, attriOfRelic, mainAttri)
    flag[0] = True


def create2():  # 自定义生成圣遗物
    global typeOfRelic, attriOfRelic, level, mainAttri
    level = 0
    typeOfRelic = -ui.relicTypeButton.checkedId()-3
    if typeOfRelic == -1: typeOfRelic = randint(0, 4)
    choice = []
    if ui.ckb1.isChecked(): choice.append(0)
    if ui.ckb2.isChecked(): choice.append(1)
    if ui.ckb3.isChecked(): choice.append(2)
    if ui.ckb4.isChecked(): choice.append(3)
    if ui.ckb5.isChecked(): choice.append(4)
    if ui.ckb6.isChecked(): choice.append(5)
    if ui.ckb7.isChecked(): choice.append(6)
    if ui.ckb8.isChecked(): choice.append(7)
    if ui.ckb9.isChecked(): choice.append(8)
    if ui.ckb10.isChecked(): choice.append(9)
    num = randint(3, 4)
    while len(choice) < num:
        if typeOfRelic == 0: a = randint(1, 9)
        elif typeOfRelic == 1: a = sample([0, 1, 3, 4, 5, 6, 7, 8, 9], 1)[0]
        else: a = randint(0, 9)
        if a not in choice:
            choice.append(a)
    attriOfRelic = [[i, [randint(0, 3)]] for i in choice]
    mainAttri = getmainattri(typeOfRelic, [attributes[i] for i in choice])
    show(typeOfRelic, attriOfRelic, mainAttri)
    flag[0] = True


def getattri():  # 圣遗物词条强化
    num = len(attriOfRelic)
    if num == 3:  # 词条不足4条时，补足4条
        a = randint(0, 9)
        while a in [i[0] for i in attriOfRelic] and attributes[a] != attriOfMain[mainAttri[0]]:
            a = randint(0, 9)
        attriOfRelic.append([a, [randint(0, 3)]])
    else:  # 已有4条词条，随机选一条并随机选一个数值进行强化
        s, d = randint(0, 3), randint(0, 3)
        attriOfRelic[s][1].append(d)


def levelUp1():  # 圣遗物升1级
    global level
    if not flag[0] or level == 20:
        return
    if level in [3, 7, 11, 15, 19]:
        level += 1
        getattri()
    else: level += 1
    mainAttri[1] += 1
    show(typeOfRelic, attriOfRelic, mainAttri)


def levelUp4():  # 升4级
    global level
    if not flag[0] or level == 20:
        return
    l = min(4, 20-level)
    for i in range(l):
        levelUp1()


def levelUp():  # 升满级
    global level
    if not flag[0] or level == 20:
        return
    while level < 20:
        levelUp1()


def preOverFlow(b):  # 只能选择四个以下
    if ui.ckb1.isChecked() == b:
        ui.ckb1.setEnabled(b)
    if ui.ckb2.isChecked() == b:
        ui.ckb2.setEnabled(b)
    if ui.ckb3.isChecked() == b:
        ui.ckb3.setEnabled(b)
    if ui.ckb4.isChecked() == b:
        ui.ckb4.setEnabled(b)
    if ui.ckb5.isChecked() == b:
        ui.ckb5.setEnabled(b)
    if ui.ckb6.isChecked() == b:
        ui.ckb6.setEnabled(b)
    if ui.ckb7.isChecked() == b:
        ui.ckb7.setEnabled(b)
    if ui.ckb8.isChecked() == b:
        ui.ckb8.setEnabled(b)
    if ui.ckb9.isChecked() == b:
        ui.ckb9.setEnabled(b)
    if ui.ckb10.isChecked() == b:
        ui.ckb10.setEnabled(b)


def func(a):  # 自定义词条
    global cntChoice
    if a == 0: cntChoice -= 1
    else: cntChoice += 1
    if cntChoice >= 4: preOverFlow(False)  # 选中4个后，禁用其他选项
    else:  # 小于4个时，开放所有选项
        ui.ckb1.setEnabled(True)
        ui.ckb2.setEnabled(True)
        ui.ckb3.setEnabled(True)
        ui.ckb4.setEnabled(True)
        ui.ckb5.setEnabled(True)
        ui.ckb6.setEnabled(True)
        ui.ckb7.setEnabled(True)
        ui.ckb8.setEnabled(True)
        ui.ckb9.setEnabled(True)
        ui.ckb10.setEnabled(True)


def init():
    ui.ckb1.stateChanged.connect(func)
    ui.ckb2.stateChanged.connect(func)
    ui.ckb3.stateChanged.connect(func)
    ui.ckb4.stateChanged.connect(func)
    ui.ckb5.stateChanged.connect(func)
    ui.ckb6.stateChanged.connect(func)
    ui.ckb7.stateChanged.connect(func)
    ui.ckb8.stateChanged.connect(func)
    ui.ckb9.stateChanged.connect(func)
    ui.ckb10.stateChanged.connect(func)
    ui.createAsChoosed.clicked.connect(create2)
    ui.randomCreate.clicked.connect(create1)
    ui.levelup1.clicked.connect(levelUp1)
    ui.levelup4.clicked.connect(levelUp4)
    ui.levelup.clicked.connect(levelUp)


init()
ui.show()
app.exec_()
