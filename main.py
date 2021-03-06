from time import sleep # the module that has the ability of The World
import sys # for killing the program when GAME OVERed
import main_en as en # Import English version

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # hiding that f**king annoying message

from pygame import mixer # playing BGMs and SEs
mixer.init()

reboot = 0

def typing(words, voice='default', offset=0.1): # typing effect
    for char in words:
        sleep(offset)
        sys.stdout.write(char)
        text_sound(voice)
        sys.stdout.flush()
    print()

def text_sound(voice='default'): # voices for type()
    if voice == 'default': # default voice from UNDERTALE (frisk)
        mixer.music.load('voices\\default.wav')
        mixer.music.play()
    elif voice == 'default2': # second default voice from UNDERTALE (chara)
        mixer.music.load('voices\\default2.wav')
        mixer.music.play()
    elif voice == 'sans':
        mixer.music.load('voices\\sans.wav')
        mixer.music.play()
    elif voice == 'select': # selecting commands
        mixer.music.load('voices\\select.wav')
        mixer.music.play()
    elif voice == 'papyrus':
        mixer.music.load('voices\\papyrus.wav')
        mixer.music.play()

def langsel(): # Language selection
    print('Please select your language.')
    print('English/日本語')
    lang = input()
    if lang.lower() == 'english':
        en.game_start() # English version
    else:
        jap()

def jap(): #Japanese gameplay
    mixer.Channel(1).play(mixer.Sound('bgm\\wind.wav'), loops=-1) # The void sound
    typing('始めたいなら「y」', 'default')
    shoken1 = input()
    if shoken1 == 'y':
        gameover('ちなみに外来語使うと死ぬよー')
    elif shoken1 == '':
        typing('または「始める」を入力')
        gamestart = input('')
        if gamestart == '始める' or gamestart == 'はじめる':
            text_sound('select') # selecting commands
            char_make()
        else:
            gameover('うん。変なの入力するな。')
    elif shoken1 == '死' or shoken1 == "自殺":
        gameover('''あー自殺しちゃった。とりあえずリセットしよ''')
    elif shoken1.lower() == 'n':
        gameover('なら死ね')
    else:
        gameover('なんでも入力したところで死ぬよ')

def char_make(): # character creation
    mixer.Channel(1).play(mixer.Sound('bgm\\chara_make.wav'), loops=-1)
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
        mixer.Channel(1).fadeout(5000)
        sleep(3)
        typing('GAME START', 'sans', 0.3)
    elif chara_fakeconf == "":
        gameover('いやいや、真面目に聞いてる?　とりあえず殺したから！')
    else:
        gameover('なんでも入力した＝死だから…')

def gameover(message): # GAME OVER
    mixer.Channel(1).play(mixer.Sound('bgm\\gameover.wav'))
    typing('GAME OVER', voice='default2', offset=0.6)
    sleep(3)
    typing(message, 'default2', 0.07)
    mixer.Channel(1).fadeout(5000)
    sleep(5)
    sys.exit()

def gaster_reboot(): # Reboot for typing Gaster
    global reboot
    reboot += 1
    if reboot >= 3:
        gameover('お前らさーガスヒカリで遊ぶなよ！ということで殺します。')
    char_make()

langsel() # Language selection
