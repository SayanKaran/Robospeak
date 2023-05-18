import gtts #google text to speech
import playsound

w="Welcome To Robospeech World 1.2.2, Created By Sayan"
sound = gtts.gTTS(w, lang="en")
sound.save("Welcome2.mp3")
playsound.playsound("Welcome2.mp3")

m="Enter a sentance or paragraph which you want to convert into speech."
sound = gtts.gTTS(m, lang="en-US")
sound.save("Welcome3.mp3")
playsound.playsound("Welcome3.mp3")
x=input("Enter: ")

z="In which language do you want to listen (1->English, 2->French, 3->Hindi)"
sound = gtts.gTTS(z, lang="en")
sound.save("Welcome1.mp3")
playsound.playsound("Welcome1.mp3")
y=int(input("In which language do you want to listen (1->English, 2->French, 3->Hindi): "))


match y:
    case 1:
       n="Your Choise is English"
       sound = gtts.gTTS(n, lang="en")
       sound.save("Welcome4.mp3")
       playsound.playsound("Welcome4.mp3")

       print("In English")
       sound = gtts.gTTS(x, lang="en")
       sound.save("Welcome.mp3")
       playsound.playsound("Welcome.mp3")
    case 2:
       n="Your Choise is French"
       sound = gtts.gTTS(n, lang="fr")
       sound.save("Welcome4.mp3")
       playsound.playsound("Welcome4.mp3")

       print("In French")
       sound = gtts.gTTS(x, lang="fr")
       sound.save("Welcome.mp3")
       playsound.playsound("Welcome.mp3")
    case 3:
       n="Your Choise is Hindi"
       sound = gtts.gTTS(n, lang="hi")
       sound.save("Welcome4.mp3")
       playsound.playsound("Welcome4.mp3")

       print("In Hindi")
       sound = gtts.gTTS(x, lang="hi")
       sound.save("Welcome.mp3")
       playsound.playsound("Welcome.mp3")
    case _:
       n="Sorry there are no any language present."
       sound = gtts.gTTS(n, lang="en-US")
       sound.save("Welcome4.mp3")
       playsound.playsound("Welcome4.mp3")
       print("Sorry there are not any language present.")
