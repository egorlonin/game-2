import pyttsx3
engine = pyttsx3.init()
import random
engine.say("перед вами три двери. В какую зайдете?")
engine.runAndWait()
while True:
    b = input()
    if int(b) == 1:
        engine.say("вы перед сундуком. В нем может быть что угодно.")
        engine.runAndWait()
    elif int(b) == 2:
        engine.say("перед вами милый дракошка, которого хочет съесть тимур пахомов")
        engine.runAndWait()
    a = input()
    if a == ("открыть сундук"):
        a = random.randint(0,100)
    if int(a) < 50:  #он тоже не работает
        engine.say("там оказалось золото. Вы получили 1 гривну")
        engine.runAndWait()
    else:
        engine.say("сундук открылся и оказался пустым, но в углу на дне оказался маленький павук. Он укусил тебя и ты умер. уох.")
        engine.runAndWait()
    n = input ()
    if n == ("Ударить тимура битой"):
        n = random.randint (0,100)
    if int(n) > 69:   #я не знаю почему он не работает.
        engine.say("Вы оглушили тимура, дракончик теперь ходит с вами")
        engine.runAndWait()
    else:
        engine.say("вы не оглушили тимура.Вы бросились обратно, но дверь была закрыта и тимур перекусил вами")
        engine.runAndWait()
    if n == ("не вмешиваться"):
        engine.say("тимур поел")
        engine.runAndWait()
