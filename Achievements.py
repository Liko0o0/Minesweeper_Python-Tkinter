## ----- Importation des Modules -----##
from tkinter import *
from tkinter import Button, Label, messagebox
from pygame import mixer
from pathlib import Path
import os
from Main import icon

## ----- Constants -----##
ACHIEVEMENT_UNLUCKY = "Unlucky"
ACHIEVEMENT_QUICK = "Quick"
ACHIEVEMENT_RECKLESS = "Reckless"
ACHIEVEMENT_CHAMPION = "Champion"
ACHIEVEMENT_LUCKY = "Lucky"
ACHIEVEMENT_COMPLETIONIST = "Completionist"
ACHIEVEMENT_COLLECTOR = "Collector"

## ----- Linked files -----##
appdata_path = Path(os.getenv('APPDATA')) / "Minesweeper"
s_path = appdata_path / "achievements.txt"
button_sound = Path(__file__).parent / "Sound/button_click.mp3"
secret_sound = Path(__file__).parent / "Sound/easter_egg.mp3"

## ----- Music and sound ----- ##
button_click = mixer.Sound(button_sound)
button_click.set_volume(0.3)
secret = mixer.Sound(secret_sound)
secret.set_volume(0.3)


def read_achievement():
    with open(str(s_path), "r") as file:
        lignes = file.read().splitlines()
    return set(lignes)


def write_achievement(succes):
    with open(str(s_path), "a") as file:
        file.write(succes + "\n")

## ----- Main program ----- ##


def achievements_loop(mute, theme, language, unlucky, reckless, quick, champion, lucky, completionist):

    # Allows to center the window for all screen dimensions
    def window_center(width, heigth):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (heigth/2)
        window.geometry('%dx%d+%d+%d' % (width, heigth, x, y))

## ----- Creation of the window ----- ##
    window = Tk()
    if language == 'french':
        window.title('Démineur - Succes')
    else:
        window.title('Minesweeper - Achievements')
    window_center(844, 604)
    window.resizable(False, False)
    window.iconbitmap(icon)

    def back():
        import Main
        button_click.play()
        Main.music_playing += 1
        window.destroy()
        Main.menu(mute, theme, language)

    def enter(name, size, event):  # Event come from the bind method
        name.configure(bg="#CAB7B9", font=("Small fonts", size+2))
        if theme == 'dark':
            name.configure(bg="#514154", font=("Small fonts", size+2))

    def exit(name, size, event):  # Event come from the bind method
        name.configure(bg="#E1CCCE", font=("Small fonts", size))
        if theme == 'dark':
            name.configure(bg="#3E2C41", font=("Small fonts", size))

## ----- Canvas creation -----##
    main = Canvas(window, width=840, height=600, bg='#a39193')
    main.grid(row=0, column=0, rowspan=10, sticky=NW)
    line_y1 = main.create_line(
        25, 175, 25, 525, width=4, fill="#726566")
    line_y2 = main.create_line(
        210, 175, 210, 525, width=4, fill="#726566")
    line_y3 = main.create_line(
        815, 175, 815, 525, width=4, fill="#726566")
    line_x1 = main.create_line(
        25, 175, 815, 175, width=4, fill="#726566")
    line_x2 = main.create_line(
        25, 225, 815, 225, width=4, fill="#726566")
    line_x3 = main.create_line(
        25, 275, 815, 275, width=4, fill="#726566")
    line_x4 = main.create_line(
        25, 325, 815, 325, width=4, fill="#726566")
    line_x5 = main.create_line(
        25, 375, 815, 375, width=4, fill="#726566")
    line_x6 = main.create_line(
        25, 425, 815, 425, width=4, fill="#726566")
    line_x7 = main.create_line(
        25, 475, 815, 475, width=4, fill="#726566")
    line_x8 = main.create_line(
        25, 525, 815, 525, width=4, fill="#726566")

    title = Label(window, text=" Démineur ")
    title.grid(row=0, column=0, columnspan=1, padx=310, pady=25, sticky=NW)
    title.config(font=("Small fonts", 35), bg='#E1CCCE', relief=RIDGE)

    subtitle = Label(window, text=" Succes ")
    subtitle.grid(row=0, column=0, columnspan=1,
                  padx=350, pady=95, sticky=NW)
    subtitle.config(font=("Small fonts", 25, "bold"),
                    bg='#E1CCCE', relief=RIDGE, foreground="#68228b")

## ---- Information creation -----##
    # Lose in the 1st click
    title_unlucky = Label(window, text=" Malchanceux ")
    title_unlucky.grid(
        row=0, column=0, columnspan=1, pady=186, padx=48, sticky=NW)
    title_unlucky.configure(
        font=("Small fonts", 14, "bold"), bg='#E1CCCE', relief=RIDGE)
    subtitle_unlucky = Label(
        window, text="                                                  ?                                                  ")
    subtitle_unlucky.grid(
        row=0, column=0, columnspan=1, pady=186, padx=240, sticky=NW)
    subtitle_unlucky.configure(font=(
        "Small fonts", 14, "bold"), bg='#E1CCCE', relief=RIDGE, foreground="#766B65")

    # Win in - 15sec on easy / 45sec on medium / 1min10 on difficult
    title_quick = Label(window, text=" Expéditif ")
    title_quick.grid(row=0, column=0, columnspan=1,
                     pady=236, padx=68, sticky=NW)
    title_quick.configure(
        font=("Small fonts", 14, "bold"), bg='#E1CCCE', relief=RIDGE)
    subtitle_quick = Label(
        window, text="                                                  ?                                                  ")
    subtitle_quick.grid(
        row=0, column=0, columnspan=1, pady=236, padx=240, sticky=NW)
    subtitle_quick.configure(font=(
        "Small fonts", 14, "bold"), bg='#E1CCCE', relief=RIDGE, foreground="#766B65")

    # Lose 10 times in a row
    title_reckless = Label(window, text=" Téméraire ")
    title_reckless.grid(row=0, column=0, columnspan=1,
                        pady=286, padx=61, sticky=NW)
    title_reckless.configure(
        font=("Small fonts", 14, "bold"), bg='#E1CCCE', relief=RIDGE)
    subtitle_reckless = Label(
        window, text="                                                  ?                                                  ")
    subtitle_reckless.grid(
        row=0, column=0, columnspan=1, pady=286, padx=240, sticky=NW)
    subtitle_reckless.configure(font=(
        "Small fonts", 14, "bold"), bg='#E1CCCE', relief=RIDGE, foreground="#766B65")

    # Win 3 times in a row
    title_champion = Label(window, text=" Champion ")
    title_champion.grid(row=0, column=0, columnspan=1,
                        pady=336, padx=61, sticky=NW)
    title_champion.configure(
        font=("Small fonts", 14, "bold"), bg='#E1CCCE', relief=RIDGE)
    subtitle_champion = Label(
        window, text="                                                  ?                                                  ")
    subtitle_champion.grid(
        row=0, column=0, columnspan=1, pady=336, padx=240, sticky=NW)
    subtitle_champion.configure(font=(
        "Small fonts", 14, "bold"), bg='#E1CCCE', relief=RIDGE, foreground="#766B65")

    # Discover a cell with a number >= 6
    title_lucky = Label(window, text=" Chanceux ")
    title_lucky.grid(row=0, column=0, columnspan=1,
                     pady=386, padx=62, sticky=NW)
    title_lucky.configure(
        font=("Small fonts", 14, "bold"), bg='#E1CCCE', relief=RIDGE)
    subtitle_lucky = Label(
        window, text="                                                  ?                                                  ")
    subtitle_lucky.grid(
        row=0, column=0, columnspan=1, pady=386, padx=240, sticky=NW)
    subtitle_lucky.configure(font=(
        "Small fonts", 14, "bold"), bg='#E1CCCE', relief=RIDGE, foreground="#766B65")

    # Win in all difficulties
    title_completionist = Label(window, text=" Complétionniste ")
    title_completionist.grid(
        row=0, column=0, columnspan=1, pady=436, padx=33, sticky=NW)
    title_completionist.configure(
        font=("Small fonts", 14, "bold"), bg='#E1CCCE', relief=RIDGE)
    subtitle_completionist = Label(
        window, text="                                                  ?                                                  ")
    subtitle_completionist.grid(
        row=0, column=0, columnspan=1, pady=436, padx=240, sticky=NW)
    subtitle_completionist.configure(font=(
        "Small fonts", 14, "bold"), bg='#E1CCCE', relief=RIDGE, foreground="#766B65")

    # Unlock all achievements
    title_collector = Label(window, text=" Collectionneur ")
    title_collector.grid(
        row=0, column=0, columnspan=1, pady=486, padx=41, sticky=NW)
    title_collector.configure(
        font=("Small fonts", 14, "bold"), bg='#E1CCCE', relief=RIDGE)
    subtitle_collector = Label(
        window, text="                                                  ?                                                  ")
    subtitle_collector.grid(
        row=0, column=0, columnspan=1, pady=486, padx=240, sticky=NW)
    subtitle_collector.configure(font=(
        "Small fonts", 14, "bold"), bg='#E1CCCE', relief=RIDGE, foreground="#766B65")

    btn_back = Button(window, width=20, height=1, bg="#E1CCCE", text="RETOUR", font=(
        "Small fonts", 15, "bold"), relief=RAISED, borderwidth=3, foreground="black")
    btn_back.grid(row=0, pady=545, padx=290, sticky=NW)
    btn_back.config(activebackground="#CAB7B9", command=back)
    btn_back.bind('<Enter>', lambda event, btn=btn_back: enter(btn, 15, event))
    btn_back.bind('<Leave>', lambda event, btn=btn_back: exit(btn, 15, event))

    if language == 'english':
        title.config(text=' Minesweeper ')
        subtitle.config(text=' Achievements')
        subtitle.grid(padx=335)
        title_unlucky.config(text=' Unlucky ')
        title_unlucky.grid(padx=44)
        title_reckless.config(text=' Reckless ')
        title_reckless.grid(padx=40)
        title_lucky.config(text=' Lucky ')
        title_completionist.config(
            text=' Completionist ', font=("Small fonts", 13, "bold"))
        title_quick.config(text=' Quick ')
        title_quick.grid(padx=44)
        title_collector.config(text=' Collector ')
        btn_back.config(text="BACK")

    def update_achievement(achievement, french, english):
        if achievement not in read_achievement():
            write_achievement(achievement)
            if language == 'french':
                messagebox.showinfo("Succès débloqué",
                                    f"Vous avez débloqué le succès : {french}")
            else:
                messagebox.showinfo("Achievements unlocked",
                                    f"You unlocked the achievement : {english}")
            import Main
            setattr(Main, achievement, True)

    def achievement_unlucky():
        if unlucky:
            if language == 'french':
                subtitle_unlucky.configure(
                    text=" Faire exploser une bombe au premier clique ")
            elif language == 'english':
                subtitle_unlucky.configure(
                    text=" Detonate a bomb at the first click ")
            if theme == 'light':
                subtitle_unlucky.configure(foreground="black")
            elif theme == 'dark':
                subtitle_unlucky.configure(foreground="#e2d8c9")
            update_achievement(ACHIEVEMENT_UNLUCKY, "Malchanceux", "Unlucky")

    def achivement_quick():
        if quick:
            if theme == 'light':
                subtitle_quick.configure(foreground="black")
            else:
                subtitle_quick.configure(foreground="#e2d8c9")
            if language == 'french':
                subtitle_quick.configure(
                    text=" Gagner en moins de (15s-Facile/45s-Moyen/1m-Difficile) ")
            else:
                subtitle_quick.configure(
                    text=" Win in less than (15s-Easy/45s-Medium/1m-Hard) ")
            update_achievement(ACHIEVEMENT_QUICK, "Expeditif", "Quick")

    def achivement_reckless():
        if reckless:
            if theme == 'light':
                subtitle_reckless.configure(foreground="black")
            else:
                subtitle_reckless.configure(foreground="#e2d8c9")
            if language == 'french':
                subtitle_reckless.configure(
                    text=" Perdre 10 fois d'affilée ")
            else:
                subtitle_reckless.configure(
                    text=" Lose 10 times in a row ")
            update_achievement(ACHIEVEMENT_RECKLESS, "Temeraire", "Reckless")

    def achivement_champion():
        if champion:
            if theme == 'light':
                subtitle_champion.configure(foreground="Black")
            else:
                subtitle_champion.configure(foreground="#e2d8c9")
            if language == 'french':
                subtitle_champion.configure(
                    text=" Gagner 3 fois d'affilée ")
            else:
                subtitle_champion.configure(
                    text=" Win 3 times in a row ")
            update_achievement(ACHIEVEMENT_CHAMPION, "Champion", "Champion")

    def achivement_lucky():
        if lucky:
            if theme == 'light':
                subtitle_lucky.configure(foreground="Black")
            else:
                subtitle_lucky.configure(foreground="#e2d8c9")
            if language == 'french':
                subtitle_lucky.configure(
                    text=" Découvrir une case avec 6 bombes ou plus autour ")
            else:
                subtitle_lucky.configure(
                    text=" Discover a cell with 6 mines or more around ")
            update_achievement(ACHIEVEMENT_LUCKY, "Chanceux", "Lucky")

    def achivement_completionist():
        if completionist:
            if theme == 'light':
                subtitle_completionist.configure(foreground="Black")
            else:
                subtitle_completionist.configure(foreground="#e2d8c9")
            if language == 'french':
                subtitle_completionist.configure(
                    text=" Gagner une partie dans chaque difficulté ")
            else:
                subtitle_completionist.configure(
                    text=" Win a game in each difficulty ")
            update_achievement(ACHIEVEMENT_COMPLETIONIST,
                               "Completionniste", "Complementionist")

    # ?
    def GG():
        import Main
        Main.mixer.music.pause()
        secret.play()

        def easter_egg(text, colors, index, total_iterations):
            if index < total_iterations:
                couleur = colors[index % len(colors)]
                text.configure(foreground=couleur)
                window.after(150, easter_egg, text, colors,
                             index + 1, total_iterations - 1)
            else:
                text.configure(foreground='black')
                Main.mixer.music.unpause()

        subtitle_flash = [subtitle_unlucky, subtitle_quick, subtitle_reckless,
                          subtitle_champion, subtitle_lucky, subtitle_completionist,
                          subtitle_collector]

        title_flash = [title_unlucky, title_quick, title_reckless,
                       title_champion, title_lucky, title_completionist, title_collector]

        colors = [
            "#F94144", "#F3722C", "#F8961E", "#F9C74F", "#90BE6D",
            "#43AA8B", "#4D908E", "#577590", "#277DA1", "#577590",
            "#4D908E", "#43AA8B", "#90BE6D", "#F9C74F", "#F8961E",
            "#F3722C",
        ]

        for i, title in enumerate(title_flash):
            window.after(0, easter_egg, title, colors, i, 270)
        for i, sous_titre in enumerate(subtitle_flash):
            window.after(0, easter_egg, sous_titre, colors, i, 270)

    def achievement_collector():
        if completionist and lucky and champion and reckless and quick and unlucky:
            if theme == 'light':
                subtitle_collector.configure(foreground="Black")
            else:
                subtitle_collector.configure(foreground="#e2d8c9")
            if language == 'french':
                subtitle_collector.configure(
                    text=" Débloquer tous les succès ! ")
            else:
                subtitle_collector.configure(
                    text=" Unlock all the achievements ! ")
            update_achievement(ACHIEVEMENT_COLLECTOR,
                               "Collectionneur", "Collector")
            GG()

    if theme == 'dark':
        main.config(bg="#261C2C", width=844, height=604, highlightthickness=0)
        title.config(bg="#3E2C41", fg='#e2d8c9')
        subtitle .config(bg="#3E2C41", fg='#8806ce')
        title_unlucky.config(bg="#3E2C41", fg='#e2d8c9')
        title_reckless.config(bg="#3E2C41", fg='#e2d8c9')
        title_champion.config(bg="#3E2C41", fg='#e2d8c9')
        title_lucky.config(bg="#3E2C41", fg='#e2d8c9')
        title_completionist.config(bg="#3E2C41", fg='#e2d8c9')
        title_quick.config(bg="#3E2C41", fg='#e2d8c9')
        title_collector.config(bg="#3E2C41", fg='#e2d8c9')
        subtitle_unlucky.config(bg="#3E2C41")
        subtitle_reckless.config(bg="#3E2C41")
        subtitle_champion.config(bg="#3E2C41")
        subtitle_lucky.config(bg="#3E2C41")
        subtitle_completionist.config(bg="#3E2C41")
        subtitle_quick.config(bg="#3E2C41",)
        subtitle_collector.config(bg="#3E2C41")
        btn_back.config(bg="#3E2C41", fg='#e2d8c9', activebackground="#312334")

    achievement_unlucky()
    achivement_quick()
    achivement_reckless()
    achivement_champion()
    achivement_lucky()
    achivement_completionist()
    achievement_collector()
