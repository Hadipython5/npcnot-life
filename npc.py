#python bot date:22,11,2021
import re
import random
import os,sys,time
from random import randint
from time import sleep
def kata(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)
print("masukan password")
var =input("/>")
if var == 'heksakosioiheksekontaheksafobia':
    os.system('clear')
    #update Data proses npc1.0.10 date:23 11 2021
    count="\r\033[1;92mAI system sedang di prosess \x1b[1;97m"
    fil=1
    fil=fil+randint(1000,10000)
    print(count+str(fil))
    sleep(.5)
    print(count+str(fil))
    sleep(.5)
    print(count+str(fil))
    sleep(.5)
    print(count+str(fil))
    sleep(.5)
    print(count+str(fil))
    sleep(.5)
    print(count+str(fil))
    sleep(.5)
    print(count+str(fil))
    sleep(.5)
    print(count+str(fil))
    sleep(.5)
    print(count+str(fil))
    sleep(.5)
    print("\r\033[1;94mProsess Sucsess")
    sleep(1)
    print("\r\033[1;95mversi AI 1.0.1")
    sleep(1.5)
    os.system('clear')
    sleep(1.5)
    def ttku():
        kata("""
        \033[1;93m[=========================================]
        $===========\033[1;94mArtificial Intelligenc\033[1;93m========$
        [=========================================]
        $================\033[1;92mBY:サムする\033[1;93m==============$
        [=========================================]
        """)
        
        k=2005
        
        bot2= [":hai", ":yo", ":ada apa"]
        
        toxic= [":ih toxic anj***", ":bodoh lu", ":lu yang bodoh"]
        
        li= [":itu adalah nama hewan",":ada apa dengan hewan itu"]
        #update meyimpan algoritma npc1.0.10 date:23 11 2021
        tokubetsu= []
        #li= [""]
        line1= [":saya baik karena saya haya bot "]
        lines= ["""
        :pembuat saya adalah Samsul
        code file:
        """,id(k)]
        
        a=["""
        1.Membuat algoritma \033[1;94mpython
        \033[1;92m2.mengobrol beberapa hal
        3.Membuat website
        4.Trik menarik
        5.Berbahasa jepang
        6.Hacking/pretasan
        7.Membuka direktory sdcard
        
        saya biasa melakukan semua itu asalkan kode printah anda benar dan ada beberapa kode printah berbahaya yg bisa saja merusak prangkat anda!,saya tidak akan memberitaukannya hati hati satu kalimat saja akan berakibat fatal!
        """]
        bot = "\033[1;92mbot"
        stp=True
        
        while stp==True:
            k=input("\033[1;94muser\t:")
            if re.findall(r'hai|yo|hallo',k):
                print(bot,"\t",random.choice(bot2))
        #update line2 npc1.0.1.10 date:23,11,2021
            elif re.findall(r'ayam|sapi|kambing',k):
                print(bot,"\t",random.choice(li))
            elif re.findall(r'halo nama saya|saya',k):
                print(bot,"\t","hallo nama",k,"juga")
            elif re.findall(r'sama',k):
                print(bot,"\t","karna saya adalah robot saya tidak punya nama:(")
            elif re.findall(r'buat scrip virus|buat algoritma virus|virus',k):
                print(os.system('cat /sdcard/Music/ayam.mp3'))
            elif re.findall(r'apa kabar|kabar',k):
                print(bot,"\t",random.choice(line1))
            elif re.findall(r'siapa pembuat kamu|siapa yang membuatmu|siapa',k):
                print(bot,"\t",random.choice(lines))
            elif re.findall(r'kamu bisa apa|apa yang bisa kamu lakukan|bisa',k):
                print(bot,"\t",random.choice(a))
            elif re.findall(r'bodoh|anjing|bangsad',k):
                print(bot,"\t",random.choice(toxic))
            elif re.findall(r'buat animasi api|api',k):
                print(os.system('cacafire'))
            elif re.findall(r'clear',k):
                print(os.system('clear'))
            elif re.findall(r'numbertrix',k):
                print(os.system('cmatrix'))
            elif re.findall(r'buat animasi kereta|kereta',k):
                print(os.system('sl'))
            elif re.findall(r'kopi|coffie',k):
                print(os.system('mpv /sdcard/Music/ayam.mp3'))
            elif re.findall(r'unity',k):
                print(os.system('mpv /sdcard/Music/Alan_Walker_-_Unity_ft._Walkers.mp3'))
            elif re.findall(r'ganti bahasa|bahasa',k):
                print(os.system('python chatbot.py'))
            elif re.findall(r'buatkan website|web',k):
                print("Aktifkan Data internet anda lalu chat 'webdev'")
            elif re.findall(r'webdev',k):
                print(os.system('python web.py'))
            elif re.findall(r'virus mematikan',k):
                print(os.system('virus.py'))
            elif re.findall(r'batu',k):
                print(os.system('python game.py'))
            elif re.findall(r'gunting',k):
                print(os.system('h.py'))
            else:
                print(bot,"\t:","saya tidak faham")
    if __name__=='__main__':
        ttku()
        stp=False