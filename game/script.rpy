# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define m = Character("Io me medesimo")
define mum = Character("Mamma")
define s = Character("Silvia")
define ps = Character("Professoressa Silvia")

define np = Character("Professoressa Neelie", kind=nvl, color ="#abc")
define npBig = Character("Professoressa Neelie", kind=nvl, color ="#abc",what_size=34)
define npSmall= Character("Professoressa Neelie", kind=nvl, color ="#abc",what_size=18)

define p = Character("Professoressa Eileen", color = "#ff0000")

define name = "Personaggio Principale"

default stanco = False


define slowdissolve = Dissolve(1.5)




# The game starts here.

label start:

    scene black

    m "Sto dormendo."
    m "Sto sognando."
    m "Sto dormendo così bene..."
    m "Dormirei tutti i giorni!"
    m "Ma aspetta, io dormo già tutte le notti!"
    m "Che bello..."

    jump sveglia

label sveglia:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    "DRRRRRRRRRRRINN!!"

    "Suona la sveglia. "

    m "oh no... sono così stanco, voglio dormire! Non vorrei alzarmi dal letto..."

    menu:

        "Mi alzo, è ora di andare a scuola":
            $ stanco = True
            jump autobus

        "Dormo ancora cinque minuti":
            jump mamma

label autobus:

    m "Mi vesto, faccio colazione e mi preparo per andare alla fermata dell'autobus."

    show lucy happy

    mum "Buona giornata figliuolo! Fai amicizia con gli amici e fatti inscuolare dalla scuola!"

    "La mamma da un bacetto al suo figlio, che sarei io"

    m "Ciao mamma, ti voglio bene!"

    scene bg meadow

    m "Dopo queste scene toccanti e strappalacrime, raggiungo la fermata."

    m "L'autobus non si fa aspettare, sono arrivato giusto in tempo. "

    show sylvie blue normal

    s "Ciao [name]!"

    "Questa ragazza si chiama Silvia, è una mia compagna."

    m "Ciao Silvia. Comunque io non mi chiamo Personaggio Principale..."

    python:
        name=renpy.input("Come mi chiamo?")

        name.strip() or "Innominato"

    m "Io mi chiamo [name]"

    show sylvie blue giggle

    s "Ah giusto, me lo dimentico sempre, è un nome così difficile!"

    "Chiacchieriamo del più e del meno lungo tutto il tragitto"

    scene bg club

    "Finalmente l'autobus raggiunge la scuola, proprio quando stavamo per cominciare a parlare del per e del diviso"

    show sylvie blue smile

    s "Ciao Personaggio Dal Nome Difficile!"

    m "Non cambierai mai!"

    jump storia

label mamma:

    scene black

    m "Torno nel mondo dei sogni"

    m "Wow che bello, che bello..."

    m "Come sto bene in questo letto caldo...!"

    scene bg room

    "ARRRRRRR!"

    show lucy mad

    m "vengo svegliato da una mamma arrabbiatissima"

    mum "Sei in ritardo figliastro!"

    mum "Sei pigro e meriti una sculacciata!"

    jump morte

label storia:

    scene bg lecturehall

    "Oggi per cominciare avremo una lezione di storia"

    show eileen happy

    "Entra la nostra professoressa"

    p "Buongiorno a tutti ragazzi"

    show eileen vhappy

    p "Oggi parleremo della Guerra dei cent'anni, nella quale ha combattuto la leggendaria Giovanna d'Arco."

    "La professoressa comincia a parlare di monarchie dell'età feudale, di intrighi politici e questioni economiche."

    if stanco:
        "La spiegazione è molto noiosa e io sento i miei occhi pian piano chiudersi..."
        "Non ho dormito abbastanza evidentemente..."

        scene black

        "Mi metto a sognare di cavalieri valorosi e dame eleganti"

        "Anche io sono lì, vestito con indumenti del tempo. Che interessante!"

        scene bg lecturehall

        show eileen concerned

        p "[name]!"

        p "Vorrei vederti più attento in classe. Forse non ti sembra un argomento interessante?"

        m "Ecco, io..."

        p "Allora, dimmi, in quale anno è finita la Guerra dei Cent'Anni?"

        menu:
            "Nel 1453":

                show eileen happy

                p "Beh, che dire, oggi ti è andata bene"

            "Nel 953":
                jump morte

            "Nel 1653":
                jump morte

    else:
        "è stato tutto molto interessante!"

        "fra poco inizia la lezione di ginnastica"

    jump ginnastica

label ginnastica:

    show lucy happy at right behind eileen

    "ecco la professoressa di ginnastica"
    "dovrebbe essere una lezione interessante, la professoressa ci ha annunciato che avremmo avuto una dimostrazione di combattimento con teletrasporto"

    pause 1

    show lucy mad at left
    with Dissolve(.5)

    pause .5

    show lucy mad behind eileen
    with slowdissolve

    hide eileen
    with fade

    define flashbulb = Fade(1,0.5,0.2,color='#ff0')

    scene bg meadow
    with flashbulb

    show lucy happy
    with pixellate

    pause .5

    with vpunch

    pause .4

    with hpunch

    pause .1
    with hpunch

    show lucy happy at left
    with move

    show lucy mad at right
    with blinds

    show lucy happy at center
    with squares

    scene bg lecturehall
    with ImageDissolve("imagedissolve circlewipe.png",1,10)

    show lucy happy
    with ImageDissolve("imagedissolve teleport.png",1,10)

    hide lucy happy
    with moveoutleft

    "wow, abbiamo imparato molto oggi"
    "mi sento già un po' più forte e preparato a vincere contro i cattivi!"

    jump intervallo

label intervallo:

    "DRRRRRRINNN!!"

    "Suona la campanella,{nw}"
    with ImageDissolve("imagedissolve circlewipe.png",1,10)
    extend "è ora\n dell'\n intervallo"

    scene bg club

    "Andiamo di fuori, è una bellissima giornata"

    show sylvie green normal

    s "ciao [name]!"
    s "ho ripassato {w}il tuo nome{w=.5} durante la lezione di storia, ora me lo ricordo!"
    m "Grazie! Comunque.."
    m "{cps=*0.5}{s}non eri vestita di{/cps} blu prima?{/s}"
    s "dopo la {a=jump:ginnastica}lezione di ginnastica{/a} {u}mi sono cambiata{/u}"

    show sylvie green giggle

    s "mica come te, {i}puzzone!{/i}"
    m "sei sempre {p}molto onesta,{p=1} sei un'amica!"

    show sylvie green surprised

    s "oooh, {b}FRIENDZONE!{/b}"
    m "{cps=20}no, ecco, io ...{/cps}"

    show sylvie green giggle

    s "lo sapevo {space=20}  che {vspace=20} ti saresti {k=2}imbarazzato{/k}"
    m "..."
    s "ciao, io devo andare, {alpha=.5}il mio intervallo è finito,{/alpha} {alpha=.2}devo ripassare il nome di tante altre persone{/alpha}!"
    s "{color=#080}{size=+10}Ciao{/size}oo!{/color}"

    show sylvie smile

    hide sylvie
    with moveoutright

    jump mathematics

label mathematics:

    "DRRRRINNNN!"

    extend "L'intervallo est finito. {w} ora di tornare in classe"

    scene bg lecturehall

    "Ora abbiamo l'ora di {alpha=.5}matematica{/alpha}"

    show eileen normal at left

    "La professoressa di matematica si chiama Neelie. "

    extend "Lei e la professoressa di storia sono sorelle gemelle. "

    np "Buongiorno ragazzi"

    "Buongiorno siglora professoressa!"

    np "Oggi studiamo le equazioni di primo grado!"

    "Yeeeee!"

    nvl hide dissolve
    nvl show squares


    jump testmate

label testmate:


    define menu = nvl_menu
    menu:
        np "Quale valore di x risolve l'equazione `2x=6`?"

        "x=1":
            jump morte
        "x=2":
            np "caro, ritenta!"

            nvl clear
            jump testmate

        "x=3":
            np "Corretto!"
            jump matematica2

label matematica2:

    nvl clear

    npSmall "Allora, ragazzi, vi voglio dire un segreto per passare l'esame con me."

    npSmall "Ascoltate attentamente ma non ditelo in giro"

    npBig "NON COPIATE!!!!"
    with hpunch
    extend "Non passate bigliettini! "
    with vpunch
    npBig "Insomma, {cps=*.5} {k=3} non vi azzardate a fare i furbetti con me {/k} {/cps}"

    np "In questo modo, avrete salva la vita."

    npBig "SONO STATA CHIARAAAAAAA!!!!?????"
    with vpunch
    with hpunch
    with hpunch
    with vpunch

    " sissignora professoressa"

    np "non ho sentito bene"

    "{size=+10} sissignora professoressa Neelie! {/size}"

    np "oooooooooooh!"

    jump matematica3

label matematica3:

    jump chimica

label chimica:

    scene bg lecturehall

    "Finalmente l'ultima lezione"

    "La lezione di chimica"

    show sylvie green smile

    ps "Buongiorno ragazzi!"

    extend "La vostra professoressa di chimica è malata quindi oggi vi sostituirò io!"

    m "Silvia, cosa ci fai tu qui in cattedra, sei seria?"

    ps "Durante l'intervallo ho studiato tanto e adesso sono diventata professoressa!"

    m "Silvia è una ragazza eccezionale, non smette mai di stupirmi"

    ps "Allora, ragazzi, cerchiamo di imparare un po' di chimica!"

    image style2 = Text("l'acqua in chimica si chiama H2O", color ="#a0ffa0")

    ps "La lettera H sta per idrogeno"

    show sylvie green giggle at left
    with move

    show screen letteraHH

    ps "in inglese si dice Hydrogen"

    show sylvie green smile at left


    hide screen letteraHH
    pause 1
    show screen letteraH()

    ps "forse anche in latino inizia per H"

    hide screen letteraH
    pause 1
    show screen solido()

    ps "la lettera O indica l'ossigeno"

    hide screen solido
    pause 1
    show screen solidoruotato()

    ps "in inglese si dice Oxygen"

    hide screen solidoruotato
    pause 1
    show screen letteraH2()

    ps "Guardate attentamente"

    pause 2

    hide screen letteraH2
    pause 1
    show screen style1

    pause 2

    hide screen style1
    pause 1
    show screen textstyle

    pause 1.5

    ps "Tutto chiaro?"

    "Sissignora maestra Silvia!"

    m "Sei una professoressa bravissima!"

    "DRRRRRINN!"

    ps "Oh è il suono dell campanella"

    show sylvie green giggle

    ps "La scuola è finita, andate in pace"

    hide sylvie

    "rumore di sedie che si spostano e voci di studenti stanchi e affamati, ma felici"

    scene bg club

    m "Torno anche io a casa."

    extend "Ripenso alle lezioni di oggi."

    scene bg uni

    m "storia, ginnastica, matematica, chimica..."

    m "che cosa mi ha insegnato la scuola?"

    scene bg meadow

    m "che cosa farò da grande?"

    m "chi sono io?"

    scene bg room

    "sono tornato a casa"

    show lucy happy

    mum "Ciao pargolo, {w} raccontami come è andata oggi a scuola!"

    mum "oggi ho preparato il tuo cibo preferito"

    mum "Lavati le mani"

    m "ciao mammina, oggi a scuola ho imparato tante cose interessantissime"

    m "ma ho un dubbio, come sarà il futuro?"

    mum "Caro, tutto dipende dalle funzioni casuali."

    mum "Per la precisione dai metodi della classe renpy.random"

    "mia mamma pronuncia sempre parole sagge"

    m "beh allora staremo a vedere cosa esce!"

    jump finalerandom

label finalerandom:

    scene black

    "10 anni più tardi..."

    pause 1

    $ fine = renpy.random.randint(1,4)

    if fine==1 :
        jump finalescienziato
    elif fine==2:
        jump finaleponti
    elif fine==3:
        jump finalebicicletta
    else:
        jump finalecasalingo

label finalescienziato:

    scene bg lecturehall
    with dissolve

    m "la scuola mi piace così tanto, che ho continuato a studiare anche durante le vacanze"

    m "sono andato all'università e sono diventato uno SCIENZIATO"

    m "ho anche fondato la mia scuola privata"

    m "l'ho chiamata SCUOLA DEGLI SCIENZIATI"

    m "da troppo studio ho perso quasi completamente la vista"

    m "poco male, perché ormai conosco tutti i libri del mondo a memoria."

    jump fine

label finaleponti:

    scene bg meadow
    with dissolve

    m "durante le vacanze ho scoperto una passione per la musica"

    m "e per il gioco d'azzardo"

    m "ho abbandonato gli studi e uno stile di vita sano"

    m "per dedicarmi allo studio del flauto dolce."

    m "sono riuscito a guadagnare qualche soldo suonando in concerto o girovagando"

    m "ma ho perso tutto giocando i miei risparmi alla roulette."

    m "oggi vivo sotto un ponte"

    m "suono per me stesso e per i passanti"

    m "non ho un soldo, ma mi sento molto felice"

    jump fine

label finalebicicletta:

    scene bg uni
    with dissolve

    m "durante le vacanze mi hanno regalato una bicicletta."

    m "il veicolo a due ruote è diventato presto la mia passione"

    m "passato qualche anno, ho trovato lavoro in un negozio di biciclette"

    m "ho imparato a riparare le biciclette e a rendermi utile alla comunità"

    m "ho le mani sporche ma sono in forma come non mai"

    jump fine

label finalecasalingo:

    scene bg club
    with dissolve

    m "ho passato le vacanze corteggiando Silvia"

    show sylvie blue giggle

    m "siamo andati in gita in barca, le ho preso dei fiori e le ho scritto lettere d'amore"

    m "quache anno dopo ci siamo sposati"

    show sylvie green giggle

    m "lei ogni tanto si dimentica ancora il mio nome"

    m "ma come sempre ritorna a studiare ed esercitarsi e dopo poco tempo riesce a ricordarsi come mi chiamo"

    m "oggi abbiamo 6 figli"

    m "sono così tanti che non ci ricordiamo più come si chiamano"

    m "quando saranno grandi sceglieranno da soli il loro nome"

    m "Silvia ha avuto una carriera di successo, anzi multiple carriere"

    m "lei eccelle in ogni cosa che fa, perché si impegna molto."

    m "allora io spesso rimango a casa con i bambini"

    m "insieme a loro intrattengo tante attività e hobby."

    m "io e i bambini tutti membri dell'aerodromo locale, del gruppo di lettura locale, "

    m "del gruppo di camminate locale, del gruppo di ricamo "

    m " e recentemente ci siamo iscritti al gruppo di tiro con l'arco e freccette."

    m " sono un papà molto impegnato e fortunato."



    jump fine

label fine:

    scene black
    with squares

    "FINE"

    return






label morte:

    scene black

    "Sei morto"

    return
