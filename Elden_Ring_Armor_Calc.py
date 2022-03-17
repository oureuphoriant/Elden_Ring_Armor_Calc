import csv
import os.path
import PySimpleGUI as sg
from operator import attrgetter

if not os.path.exists("Elden_Ring_Armor_Calc.csv"):
    csvBackup = [
        ["active","name","type","weight","physical","strike","slash","pierce","magic","fire","lightning","holy","immunity","robustness","focus","vitality","poise"],
        ["Y","Helm of Placeholding","head",1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        ["Y","Armor of Placeholding","chest",1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        ["Y","Gauntlets of Placeholding","hands",1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        ["Y","Greaves of Placeholding","legs",1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]
    with open('Elden_Ring_Armor_Calc.csv', 'w', newline='') as file:
        csv.writer(file, delimiter=',').writerows(csvBackup)

with open("Elden_Ring_Armor_Calc.csv") as armor_csv:
    reader = csv.reader(armor_csv)
    data = [row for row in reader]

inputLayout = [
    [
        sg.Text("Weight Without Armor", size=(16)),
        sg.InputText(key="initWeight", size=(6)),
        sg.Text("Priority:"),
    ],
    [
        sg.Text("Weight Capacity", size=(16)),
        sg.InputText(key="capacity", size=(6)),
        sg.Checkbox("Physical", key="physicalFlag", default=False, size=(8)),
        sg.Text("Multiplier:"),
        sg.InputText(key="physicalCoef", size=(4), default_text="1"),
    ],
    [
        sg.Text("Target Percentage", size=(16)),
        sg.InputText(key="percent", default_text=69.9, size=(6)),
        sg.Checkbox("Strike", key="strikeFlag", default=False, size=(8)),
        sg.Text("Multiplier:"),
        sg.InputText(key="strikeCoef", size=(4), default_text="1"),
    ],
    [
        sg.Text("Armor:",size=23),
        sg.Checkbox("Slash", key="slashFlag", default=False, size=(8)),
        sg.Text("Multiplier:"),
        sg.InputText(key="slashCoef", size=(4), default_text="1"),
    ],
    [
        sg.Checkbox("Head", key="headFlag", default=True, size=(20)),
        sg.Checkbox("Pierce", key="pierceFlag", default=False, size=(8)),
        sg.Text("Multiplier:"),
        sg.InputText(key="pierceCoef", size=(4), default_text="1"),
    ],
    [
        sg.Checkbox("Chest", key="chestFlag", default=True, size=(20)),
        sg.Checkbox("Magic", key="magicFlag", default=False, size=(8)),
        sg.Text("Multiplier:"),
        sg.InputText(key="magicCoef", size=(4), default_text="1"),
    ],
    [
        sg.Checkbox("Hands", key="handsFlag", default=True, size=(20)),
        sg.Checkbox("Fire", key="fireFlag", default=False, size=(8)),
        sg.Text("Multiplier:"),
        sg.InputText(key="fireCoef", size=(4), default_text="1"),
    ],
    [
        sg.Checkbox("Legs", key="legsFlag", default=True, size=(20)),
        sg.Checkbox("Lightning", key="lightningFlag", default=False, size=(8)),
        sg.Text("Multiplier:"),
        sg.InputText(key="lightningCoef", size=(4), default_text="1"),
    ],
    [
        sg.Text("",size=23),
        sg.Checkbox("Holy", key="holyFlag", default=False, size=(8)),
        sg.Text("Multiplier:"),
        sg.InputText(key="holyCoef", size=(4), default_text="1"),
    ],
    [
        sg.Text("",size=23),
        # sg.Text("",size=1),
        # sg.Button("Inventory",size=17),
        # sg.Text("",size=1),
        sg.Checkbox("Immunity", key="immunityFlag", default=False, size=(8)),
        sg.Text("Multiplier:"),
        sg.InputText(key="immunityCoef", size=(4), default_text="0.1"),
    ],
    [
        sg.Text("",size=23),
        sg.Checkbox("Robustness", key="robustnessFlag", default=False, size=(8)),
        sg.Text("Multiplier:"),
        sg.InputText(key="robustnessCoef", size=(4), default_text="0.1"),
    ],
    [
        sg.Text("",size=1),
        sg.Button("Calculate",size=17),
        sg.Text("",size=1),
        sg.Checkbox("Focus", key="focusFlag", default=False, size=(8)),
        sg.Text("Multiplier:"),
        sg.InputText(key="focusCoef", size=(4), default_text="0.1"),
    ],
    [
        sg.Text("",size=23),
        sg.Checkbox("Vitality", key="vitalityFlag", default=False, size=(8)),
        sg.Text("Multiplier:"),
        sg.InputText(key="vitalityCoef", size=(4), default_text="0.1"),
    ],
    [
        sg.Text("",size=1),
        sg.Button("Exit",size=17),
        sg.Text("",size=1),
        sg.Checkbox("Poise", key="poiseFlag", default=False, size=(8)),
        sg.Text("Multiplier:"),
        sg.InputText(key="poiseCoef", size=(4), default_text="1"),
    ],
]


class LaunchValues:
    def __init__(
        args,
        weight,
        headFlag,
        chestFlag,
        handsFlag,
        legsFlag,
        physicalFlag,
        physicalCoef,
        strikeFlag,
        strikeCoef,
        slashFlag,
        slashCoef,
        pierceFlag,
        pierceCoef,
        magicFlag,
        magicCoef,
        fireFlag,
        fireCoef,
        lightningFlag,
        lightningCoef,
        holyFlag,
        holyCoef,
        immunityFlag,
        immunityCoef,
        robustnessFlag,
        robustnessCoef,
        focusFlag,
        focusCoef,
        vitalityFlag,
        vitalityCoef,
        poiseFlag,
        poiseCoef,
    ):
        args.weight = weight
        args.headFlag = headFlag
        args.chestFlag = chestFlag
        args.handsFlag = handsFlag
        args.legsFlag = legsFlag
        args.physicalFlag = physicalFlag
        args.physicalCoef = physicalCoef
        args.strikeFlag = strikeFlag
        args.strikeCoef = strikeCoef
        args.slashFlag = slashFlag
        args.slashCoef = slashCoef
        args.pierceFlag = pierceFlag
        args.pierceCoef = pierceCoef
        args.magicFlag = magicFlag
        args.magicCoef = magicCoef
        args.fireFlag = fireFlag
        args.fireCoef = fireCoef
        args.lightningFlag = lightningFlag
        args.lightningCoef = lightningCoef
        args.holyFlag = holyFlag
        args.holyCoef = holyCoef
        args.immunityFlag = immunityFlag
        args.immunityCoef = immunityCoef
        args.robustnessFlag = robustnessFlag
        args.robustnessCoef = robustnessCoef
        args.focusFlag = focusFlag
        args.focusCoef = focusCoef
        args.vitalityFlag = vitalityFlag
        args.vitalityCoef = vitalityCoef
        args.poiseFlag = poiseFlag
        args.poiseCoef = poiseCoef


class Armor:
    def __init__(
        armor,
        name,
        type,
        weight,
        physical,
        strike,
        slash,
        pierce,
        magic,
        fire,
        lightning,
        holy,
        immunity,
        robustness,
        focus,
        vitality,
        poise,
    ):
        armor.name = name
        armor.type = type
        armor.weight = weight
        armor.physical = physical
        armor.strike = strike
        armor.slash = slash
        armor.pierce = pierce
        armor.magic = magic
        armor.fire = fire
        armor.lightning = lightning
        armor.holy = holy
        armor.immunity = immunity
        armor.robustness = robustness
        armor.focus = focus
        armor.vitality = vitality
        armor.poise = poise


armorArray = []
for i in range(len(data)):
    if i > 0: # ignore header
        if data[i][0]=="Y": # only use active
            tempArmor = Armor(
                name=data[i][1],
                type=data[i][2],
                weight=float(data[i][3]),
                physical=float(data[i][4]),
                strike=float(data[i][5]),
                slash=float(data[i][6]),
                pierce=float(data[i][7]),
                magic=float(data[i][8]),
                fire=float(data[i][9]),
                lightning=float(data[i][10]),
                holy=float(data[i][11]),
                immunity=float(data[i][12]),
                robustness=float(data[i][13]),
                focus=float(data[i][14]),
                vitality=float(data[i][15]),
                poise=float(data[i][16]),
            )
            armorArray.append(tempArmor)


def calcArmorValue(launchValues, armorPiece):
    value = 0
    if launchValues.physicalFlag:
        value = value + (armorPiece.physical * launchValues.physicalCoef)
    if launchValues.strikeFlag:
        value = value + (armorPiece.strike * launchValues.strikeCoef)
    if launchValues.slashFlag:
        value = value + (armorPiece.slash * launchValues.slashCoef)
    if launchValues.pierceFlag:
        value = value + (armorPiece.pierce * launchValues.pierceCoef)
    if launchValues.magicFlag:
        value = value + (armorPiece.magic * launchValues.magicCoef)
    if launchValues.fireFlag:
        value = value + (armorPiece.fire * launchValues.fireCoef)
    if launchValues.lightningFlag:
        value = value + (armorPiece.lightning * launchValues.lightningCoef)
    if launchValues.holyFlag:
        value = value + (armorPiece.holy * launchValues.holyCoef)
    if launchValues.immunityFlag:
        value = value + (armorPiece.immunity * launchValues.immunityCoef)
    if launchValues.robustnessFlag:
        value = value + (armorPiece.robustness * launchValues.robustnessCoef)
    if launchValues.focusFlag:
        value = value + (armorPiece.focus * launchValues.focusCoef)
    if launchValues.vitalityFlag:
        value = value + (armorPiece.vitality * launchValues.vitalityCoef)
    if launchValues.poiseFlag:
        value = value + (armorPiece.poise * launchValues.poiseCoef)
    return value


def nextArmor(launchValues, remainingWeight, armorArray, armorPiece):
    armorValue = calcArmorValue(launchValues, armorPiece)
    popList = []
    nextPiece = False
    nextIncr = False
    armorRate = 0
    for i in range(len(armorArray)):
        nextValue = calcArmorValue(launchValues, armorArray[i])
        nextRate = nextValue / armorArray[i].weight
        if nextValue <= armorValue:
            popList.append(i)
        elif (armorArray[i].weight - armorPiece.weight) > remainingWeight:
            popList.append(i)
        elif nextRate > armorRate:
            nextPiece = armorArray[i]
            armorRate = nextRate
    for j in reversed(range(len(popList))):
        armorArray.pop(popList[j])
    if nextPiece:
        nextIncr = (nextValue - armorValue) / (nextPiece.weight - armorPiece.weight)
    return [nextPiece, nextIncr]


def initArmorArrays(armorArray):
    helmArray = []
    chestArray = []
    gauntletArray = []
    legArray = []
    for i in range(len(armorArray)):
        match armorArray[i].type:
            case "head":
                if launchValues.headFlag:
                    helmArray.append(armorArray[i])
            case "chest":
                if launchValues.chestFlag:
                    chestArray.append(armorArray[i])
            case "hands":
                if launchValues.handsFlag:
                    gauntletArray.append(armorArray[i])
            case "legs":
                if launchValues.legsFlag:
                    legArray.append(armorArray[i])
            case _:
                raise Exception("Invalid Armor Type: " + armorArray[i])
    if not launchValues.headFlag:
        helmArray.append(
            Armor(
                name="",
                type="head",
                weight=float(0.0001),
                physical=float(0),
                strike=float(0),
                slash=float(0),
                pierce=float(0),
                magic=float(0),
                fire=float(0),
                lightning=float(0),
                holy=float(0),
                immunity=float(0),
                robustness=float(0),
                focus=float(0),
                vitality=float(0),
                poise=float(0)
            )
        )
    if not launchValues.chestFlag:
        chestArray.append(
            Armor(
                name="",
                type="chest",
                weight=float(0.0001),
                physical=float(0),
                strike=float(0),
                slash=float(0),
                pierce=float(0),
                magic=float(0),
                fire=float(0),
                lightning=float(0),
                holy=float(0),
                immunity=float(0),
                robustness=float(0),
                focus=float(0),
                vitality=float(0),
                poise=float(0)
            )
        )
    if not launchValues.handsFlag:
        gauntletArray.append(
            Armor(
                name="",
                type="hands",
                weight=float(0.0001),
                physical=float(0),
                strike=float(0),
                slash=float(0),
                pierce=float(0),
                magic=float(0),
                fire=float(0),
                lightning=float(0),
                holy=float(0),
                immunity=float(0),
                robustness=float(0),
                focus=float(0),
                vitality=float(0),
                poise=float(0)
            )
        )
    if not launchValues.legsFlag:
        legArray.append(
            Armor(
                name="",
                type="legs",
                weight=float(0.0001),
                physical=float(0),
                strike=float(0),
                slash=float(0),
                pierce=float(0),
                magic=float(0),
                fire=float(0),
                lightning=float(0),
                holy=float(0),
                immunity=float(0),
                robustness=float(0),
                focus=float(0),
                vitality=float(0),
                poise=float(0)
            )
        )
    return helmArray, chestArray, gauntletArray, legArray


def initOptimalArmor(launchValues, armorArray):
    helmArray, chestArray, gauntletArray, legArray = initArmorArrays(armorArray)
    helmPiece = min(helmArray, key=attrgetter("weight"))
    chestPiece = min(chestArray, key=attrgetter("weight"))
    gauntletPiece = min(gauntletArray, key=attrgetter("weight"))
    legPiece = min(legArray, key=attrgetter("weight"))
    remainingWeight = launchValues.weight - (
        helmPiece.weight + chestPiece.weight + gauntletPiece.weight + legPiece.weight
    )
    nextHelm = False
    nextChest = False
    nextGauntlet = False
    nextLeg = False
    helmIncr = False
    chestIncr = False
    gauntletIncr = False
    legIncr = False
    if len(helmArray) > 0:
        nextHelm, helmIncr = nextArmor(
            launchValues, remainingWeight, helmArray, helmPiece
        )
    else:
        helmIncr = False
    if len(chestArray) > 0:
        nextChest, chestIncr = nextArmor(
            launchValues, remainingWeight, chestArray, chestPiece
        )
    else:
        chestIncr = False
    if len(gauntletArray) > 0:
        nextGauntlet, gauntletIncr = nextArmor(
            launchValues, remainingWeight, gauntletArray, gauntletPiece
        )
    else:
        gauntletIncr = False
    if len(legArray) > 0:
        nextLeg, legIncr = nextArmor(launchValues, remainingWeight, legArray, legPiece)
    else:
        legIncr = False
    return (
        helmArray,
        chestArray,
        gauntletArray,
        legArray,
        helmPiece,
        chestPiece,
        gauntletPiece,
        legPiece,
        nextHelm,
        nextChest,
        nextGauntlet,
        nextLeg,
        helmIncr,
        chestIncr,
        gauntletIncr,
        legIncr,
    )


def optimalArmor(
    launchValues,
    helmArray,
    chestArray,
    gauntletArray,
    legArray,
    helmPiece,
    chestPiece,
    gauntletPiece,
    legPiece,
    nextHelm,
    nextChest,
    nextGauntlet,
    nextLeg,
    helmIncr,
    chestIncr,
    gauntletIncr,
    legIncr,
):
    while (
        len(helmArray) > 0
        or len(chestArray) > 0
        or len(gauntletArray) > 0
        or len(legArray) > 0
    ):
        maxIncr = max(helmIncr, chestIncr, gauntletIncr, legIncr)
        if nextHelm and helmIncr == maxIncr:
            helmPiece = nextHelm
        elif nextChest and chestIncr == maxIncr:
            chestPiece = nextChest
        elif nextGauntlet and gauntletIncr == maxIncr:
            gauntletPiece = nextGauntlet
        elif nextLeg:
            legPiece = nextLeg
        remainingWeight = launchValues.weight - (
            helmPiece.weight
            + chestPiece.weight
            + gauntletPiece.weight
            + legPiece.weight
        )
        helmIncr = False
        chestIncr = False
        gauntletIncr = False
        legIncr = False
        nextHelm, helmIncr = nextArmor(
            launchValues, remainingWeight, helmArray, helmPiece
        )
        nextChest, chestIncr = nextArmor(
            launchValues, remainingWeight, chestArray, chestPiece
        )
        nextGauntlet, gauntletIncr = nextArmor(
            launchValues, remainingWeight, gauntletArray, gauntletPiece
        )
        nextLeg, legIncr = nextArmor(launchValues, remainingWeight, legArray, legPiece)
        # summary = [helmPiece.name, chestPiece.name, gauntletPiece.name, legPiece.name]
    return helmPiece, chestPiece, gauntletPiece, legPiece


def calcArmorSet(launchValues, armorArray):
    (
        helmArray,
        chestArray,
        gauntletArray,
        legArray,
        helmPiece,
        chestPiece,
        gauntletPiece,
        legPiece,
        nextHelm,
        nextChest,
        nextGauntlet,
        nextLeg,
        helmIncr,
        chestIncr,
        gauntletIncr,
        legIncr,
    ) = initOptimalArmor(launchValues, armorArray)
    helmPiece, chestPiece, gauntletPiece, legPiece = optimalArmor(
        launchValues,
        helmArray,
        chestArray,
        gauntletArray,
        legArray,
        helmPiece,
        chestPiece,
        gauntletPiece,
        legPiece,
        nextHelm,
        nextChest,
        nextGauntlet,
        nextLeg,
        helmIncr,
        chestIncr,
        gauntletIncr,
        legIncr,
    )
    return [helmPiece.name, chestPiece.name, gauntletPiece.name, legPiece.name]


# Create the window
launchWindow = sg.Window("Elden Ring Armor Calculator", inputLayout, size=(440, 440))


def getTargeWeight(launchArray):
    if launchArray["initWeight"] and launchArray["capacity"] and launchArray["percent"]:
        return float(launchArray["capacity"]) * float(
            launchArray["percent"]
        ) / 100 - float(launchArray["initWeight"])
    else:
        return 999


# Create an event loop
while True:
    launchEvent, launchArray = launchWindow.read()
    # Proceed if user closes window
    if launchEvent == "Exit" or launchEvent == sg.WIN_CLOSED:
        launchWindow.close()
        break
    # or presses the 'Calculate' button
    elif launchEvent == "Calculate":
        weight = getTargeWeight(launchArray)
        launchValues = LaunchValues(
            weight,
            launchArray["headFlag"],
            launchArray["chestFlag"],
            launchArray["handsFlag"],
            launchArray["legsFlag"],
            launchArray["physicalFlag"],
            float(launchArray["physicalCoef"]),
            launchArray["strikeFlag"],
            float(launchArray["strikeCoef"]),
            launchArray["slashFlag"],
            float(launchArray["slashCoef"]),
            launchArray["pierceFlag"],
            float(launchArray["pierceCoef"]),
            launchArray["magicFlag"],
            float(launchArray["magicCoef"]),
            launchArray["fireFlag"],
            float(launchArray["fireCoef"]),
            launchArray["lightningFlag"],
            float(launchArray["lightningCoef"]),
            launchArray["holyFlag"],
            float(launchArray["holyCoef"]),
            launchArray["immunityFlag"],
            float(launchArray["immunityCoef"]),
            launchArray["robustnessFlag"],
            float(launchArray["robustnessCoef"]),
            launchArray["focusFlag"],
            float(launchArray["focusCoef"]),
            launchArray["vitalityFlag"],
            float(launchArray["vitalityCoef"]),
            launchArray["poiseFlag"],
            float(launchArray["poiseCoef"]),
        )
        resultHelm, resultChest, resultGauntlet, resultLeg = calcArmorSet(
            launchValues, armorArray
        )
        resultLayout = [
            [sg.Text("Head:", size=(6)), sg.Text(resultHelm)],
            [sg.Text("Chest:", size=(6)), sg.Text(resultChest)],
            [sg.Text("Hands:", size=(6)), sg.Text(resultGauntlet)],
            [sg.Text("Legs:", size=(6)), sg.Text(resultLeg)],
            [sg.Button("OK")],
        ]
        resultWindow = sg.Window("Optimal Set", resultLayout)
        while True:
            resultEvent, resultValues = resultWindow.read()
            # End program if user closes window
            # or presses the 'OK' button
            if resultEvent == "OK" or resultEvent == sg.WIN_CLOSED:
                resultWindow.close()
                break
