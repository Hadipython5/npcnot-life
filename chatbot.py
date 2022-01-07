import re
import random
import os
os.system('clear')

botm = ["こにちわ","nani",]
bots = ["こんばんわ","nani"]
botp = ["おはよ","nani"]
bot1 = ["すみませ私はただのロボットだです","何を言ってるの？私はただのロボットだ"]
bot2 = ["saya di buat oleh Samsul Hadi","私を作ったサムスルさんです"]
de = [r"""
わたしはなにもできますよ
'インドネシアご'を書いてみてください
"""]
nani = ["なにもしません","わたしいまあなたとはなします"]
suki = ["わたしはあなたのことがすき嘘だよわたしは木がすき てへ :-) ところであなたのなまえはだれですか"]

var = True
while var == True:
    user = input("user:\t")
    if re.findall(r'おはよ|ohayo',user):
        print("はなみ:\t",random.choice(botp))
    elif re.findall(r'こにちわ|konichiwa',user):
        print("はなみ:\t",random.choice(botm))
    elif re.findall(r'こんばんわ|konbanwa',user):
        print("はなみ:\t",random.choice(bots))
    elif re.findall(r'じかん|jikan',user):
        print(os.system('tty-clock'))
    elif re.findall(r'おげんきですか|ogenkidesuka',user):
        print("はなみ:\t",random.choice(bot1))
    elif re.findall(r'anata wa nani ga suki|あなたはなにがすき',user):
        print("はなみ:\t",random.choice(suki))
    elif re.findall(r'なまえ|namae',user):
        print("そうですかあなたの",user,"はならばよろしこおねがいします")
    elif re.findall(r'誰があなたを作ったのか|dare ga anata o tsukutta no ka',user):
        print("はなみ:\t",random.choice(bot2))
    elif re.findall(r'なにおしますか|nani o simasuka',user):
        print("はなみ:\t",random.choice(nani))
    elif re.findall(r'ganti bahasa|bahasa|インドネシアご',user):
        print(os.system('python npc.py'))
    elif re.findall(r'あなたはなにおできますか|anata wa nani o dekimasuka',user):
        print("はなみ:\t",random.choice(de))
    else:
        print("わたしはあなたのことばがわかりません")
var = False