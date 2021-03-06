from time import sleep # the module that has the ability of The World
import sys # for killing the program when GAME OVERed
import main_en as en

reboot = 0

def typing(words, voice='default', offset=0.1): # typing effect
    for char in words:
        sleep(offset)
        sys.stdout.write(char)
        sys.stdout.flush()
    print()

def langsel():
    print('Please select your language.')
    print('English/日本語')
    lang = input()
    if lang.lower() == 'english':
        en.game_start()
    else:
        jap()

def jap():
    typing('始めたいなら「y」', 'default')
    shoken1 = input()
    if shoken1 == 'y':
        gameover('ちなみに外来語使うと死ぬよー')
    elif shoken1 == '':
        typing('または「始める」を入力')
        gamestart = input('')
        if gamestart == '始める' or gamestart == 'はじめる':
            char_make()
        else:
            gameover('うん。変なの入力するな。')
    elif shoken1.lower() == 'n':
        gameover('なら死ね')
    elif shoken1 == '死' or shoken1 == "自殺":
        gameover('''あー自殺しちゃった。とりあえずリセットしよ''')
    else:
        gameover('なんでも入力したところで死ぬよ')

def char_make():
    typing('あなたのキャラクターを作成します。')
    sleep(5)
    typing('キャラクターの名前は?')
    charaname = input()
    if charaname.lower() == "gaster" or charaname == "ガスター" or charaname == "がすたー":
        gaster_reboot()
    typing('男性、それとも女性?')
    gender = input()
    typing('以上でよろしいですか?')
    sleep(1)
    typing('名前: '+charaname)
    sleep(1)
    typing('性別: '+gender)
    sleep(3)
    typing('OK/...')
    chara_fakeconf = input()
    if chara_fakeconf == 'OK':
        gameover('OKって英語だよねー？')
    elif chara_fakeconf == '...' or chara_fakeconf == '..':
        typing('あれ、何か不満？')
        sleep(2.3)
        typing('だったらこっちで準備した設定でやるねー')
        sleep(3)
        typing('GAME START', 'sans', 0.3)
    else:
        gameover('いやいや、真面目に聞いてる?　とりあえず殺したから！')

def gameover(message):
    typing('GAME OVER', voice='default2', offset=0.6)
    sleep(3)
    typing(message, 'default2', 0.07)
    sleep(5)
    sys.exit()

def gaster_reboot():
    global reboot
    reboot += 1
    if reboot >= 3:
        gameover('お前らさーガスヒカリで遊ぶなよ！ということで殺します。')
    char_make()

langsel()
