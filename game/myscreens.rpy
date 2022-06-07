###   Screens nella lezione di chimica

screen letteraHH():
    frame:
        add Text("H = Iddrogeno") at unrotate

screen letteraH():
    frame:
        xalign 0.5 ypos 50
        add "sylvie green giggle"


screen solido():
    frame:
        xalign 0.5 ypos 50
        add Solid("#a0ffa0",xsize=100, ysize=200)

screen solidoruotato():
    frame:
        xalign 0.5 ypos 50
        add Solid("#a0ffa0",xsize=100, ysize=200) rotate 33.1



screen letteraH2():
    frame:
        add Text("O = ossigeno") at unrotate

transform unrotate:
    zoom 0.7 rotate 88.1
    linear 1.0 rotate 0

screen style1():
    text "Questo è tutto ragazzi":
        style "my_text"
        color "#a0ffa0"

screen textstyle():
    frame:
        textbutton "I am a button":
            text_color "#a0ffa0"
