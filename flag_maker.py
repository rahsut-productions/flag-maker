from tkinter import  *
import turtle as t
from tkinter import Menu, messagebox, filedialog

tk = Tk()

# name of window
tk.title("Flag Maker ਝੰਡਾ ਬਨਾਨ ਵਾਲਾ")

# just for display
eng = Label(tk, text="Flag Maker", fg='orange', font=("Arial", 25, "bold"), \
            anchor=W)
pb = Label(tk, text="ਝੰਡਾ ਬਨਾਨ ਵਾਲਾ", fg='green', font=("Arial", 25, "bold"), \
           anchor=W)
eng.pack()
pb.pack()

# functions
def Exit():
    exit()
    
def India():
    tk.withdraw()
    # hiding the turtle 
    t.hideturtle()
    t.clear()
    t.home()
    # Putting turtle at centre of canvas
    t.up()
    t.back(200)

    # Making rectangle
    t.down()
    t.forward(350)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(350)
    t.left(90)
    t.forward(200)
    t.back(133)

    # Orange stripe
    t.left(90)
    t.color('orange')
    t.begin_fill()
    t.forward(350)
    t.left(90)
    t.forward(66)
    t.left(90)
    t.forward(350)
    t.left(90)
    t.forward(66)
    t.end_fill()

    # Getting ready for green stripe
    t.color('black')
    t.forward(66)

    # Green stripe
    t.begin_fill()
    t.left(90)
    t.color('green')
    t.forward(350)
    t.right(90)
    t.forward(66)
    t.right(90)
    t.forward(350)
    t.right(90)
    t.forward(66)
    t.end_fill()


    # Getting in position for blue circle
    t.color('black')
    t.forward(10)
    t.right(90)
    t.up()
    t.forward(175)

    # Blue circle
    t.color('blue')
    t.down()
    t.circle(25)

    t.up()
    t.left(90)
    t.forward(25)

    # 24 hour dial
    for x in range(1, 25):
        t.down()
        t.forward(25)
        t.back(25)
        t.left(15)
        t.forward(25)
        t.back(25)

    # Official name of India
    t.up()
    t.back(150)
    t.left(90)
    t.forward(100)
    t.color('black')
    t.write("भारत गणराज्य", font=("Arial", 25, "normal"))

    # Official name of India in English
    t.forward(25)
    t.right(90)
    t.forward(250)
    t.write("Republic of India", font=("Arial", 25, "normal"))

    # Punjabi name
    t.left(90)
    t.back(25)
    t.right(90)
    t.back(280)
    t.write("ਭਾਰਤ ਗਣਰਾਜ", font=("Arial", 25, "normal"))
    tk.deiconify()
    

def Japan():
    tk.withdraw()
    # hiding the turtle 
    t.hideturtle()
    t.clear()
    t.home()
    # Getting turtle at centre
    t.up()
    t.back(150)

    # Making rectangle for flag
    t.down()
    for x in range(1, 3):
      t.forward(350)
      t.left(90)
      t.forward(200)
      t.left(90)

    # To get ready for the "red sun"
    t.left(90)
    t.forward(40)
    t.right(90)

    # making the "red sun"
    t.up()
    t.forward(175)
    t.down()
    t.color('red')
    t.begin_fill()
    t.circle(60)
    t.end_fill()

    # To write 
    t.color('black')
    t.up()
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(43)
    t.write("日本", font=("Arial", 25, "normal"))
    # japan name in punjabi
    t.right(90)
    t.forward(245)
    t.left(90)
    t.write("ਜਪਾਨ", font=("Arial", 25, "normal"))
    tk.deiconify()
    
def Qatar():
    tk.withdraw()
    # hiding the turtle 
    t.hideturtle()    
    t.clear()
    t.home()
    # Getting turtle at centre
    t.up()
    t.back(150)

    # Making rectangle for flag
    t.down()
    for x in range(1, 3):
      t.forward(350)
      t.left(90)
      t.forward(200)
      t.left(90)

    # making design
    t.forward(116)
    t.left(45)
    t.color('#8D1B3D')
    t.begin_fill()
    for x in range(1, 10):
      t.forward(15)
      t.left(90)
      t.forward(15)
      t.right(90)

    t.forward(13)
    t.right(45)
    t.forward(225)

    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(233)
    t.end_fill()

    # Name
    t.left(90)
    t.up()
    t.forward(35)
    t.right(90)
    t.color('black')
    t.write("دولة قطر", font=("Arial", 25, "normal"))
    t.right(90)
    t.forward(230)
    t.left(90)
    t.forward(10)
    t.write("ਕਤਰ ਰਾਜ", font=("Arial", 25, "normal"))
    tk.deiconify()

def Bangladesh():
    tk.withdraw()
    # hiding the turtle 
    t.hideturtle()    
    t.clear()
    t.home()
    t.begin_fill()
    t.color('#006747')

    # Putting turtle at centre of canvas
    t.up()
    t.back(200)

    # Making rectangle
    t.down()
    t.forward(350)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(350)
    t.left(90)
    t.forward(200)
    t.end_fill()
    t.color('#006A4F')

    # Red sun
    t.up()
    t.color('red')
    t.back(40)
    t.left(90)
    t.forward(150)
    t.down()
    t.begin_fill()
    t.circle(60)
    t.end_fill()

    # name of bangladesh in bangla
    t.color('black')
    t.up()
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(130)
    t.write("গণপ্রজাতন্ত্রী বাংলাদেশ", font=("Arial", 25, "normal"))

    # Name of bangladesh in punjabi
    t.right(90)
    t.forward(240)
    t.left(90)
    t.forward(10)
    t.write("ਬੰਗਲਾਦੇਸ਼ੀ ਲੋਕ-ਗਣਤੰਤਰ", font=("Arial", 25, "normal"))
    tk.deiconify()
    
def China():
    tk.withdraw()
    # hiding the turtle 
    t.hideturtle()    
    t.clear()
    t.home()
    # Putting turtle at centre of canvas
    t.up()
    t.back(175)

    # Making rectangle
    t.color('#DE2910')
    t.begin_fill()
    t.down()
    t.forward(350)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(350)
    t.left(90)
    t.forward(200)
    t.back(130)
    t.end_fill()

    # stars
    t.color('yellow')
    t.left(90)
    t.up()
    t.forward(10)
    t.write("★", font=("Arial", 40, "normal"))
    t.back(10)
    t.left(90)
    t.forward(45)
    t.right(90)
    t.forward(65)
    t.write("★", font=("Arial", 13, "normal"))
    t.back(55)
    t.left(90)
    t.back(20)
    t.right(90)
    t.forward(70)
    t.write("★", font=("Arial", 13, "normal"))
    t.back(70)
    t.left(90)
    t.back(25)
    t.right(90)
    t.forward(70)
    t.write("★", font=("Arial", 13, "normal"))
    t.back(70)
    t.left(90)
    t.back(25)
    t.right(90)
    t.forward(55)
    t.write("★", font=("Arial", 13, "normal"))

    #Official name of china in Simplified Chinese
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(15)
    t.color('black')
    t.write("中华人民共和国", font=("Arial", 25, "bold"))

    #Name of china in Punjabi
    t.right(90)
    t.forward(240)
    t.left(90)
    t.write("ਚੀਨੀ ਲੋਕ-ਗਣਤੰਤਰ", font=("Arial", 25, "normal"))
    tk.deiconify()

def Pakistan():
    tk.withdraw()
    # hiding the turtle 
    t.hideturtle()    
    t.clear()
    t.home()
    # Putting turtle at centre of canvas
    t.up()
    t.back(200)

    # Making rectangle
    t.down()
    t.forward(350)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(350)
    t.left(90)
    t.forward(200)

    # making green square
    t.left(90)
    t.forward(116)
    t.left(90)
    t.begin_fill()
    t.color('#01411C')

    for x in range(1, 3):
        t.forward(200)
        t.right(90)
        t.forward(232)
        t.right(90)

    # crecent moon + star
    t.end_fill()
    t.right(90)
    t.up()
    t.color('white')
    t.forward(25)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.write("☪", font=("Arial", 150, "normal"))

    # Name of pakistan urdu
    t.color('black')
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(100)
    t.write("اِسلامی جمہوریہ پاكِستان", font=("Arial", 25, "normal"))

    # name of pakistan in English
    t.right(90)
    t.forward(240)
    t.left(90)
    t.forward(50)
    t.write("Islamic Republic of Pakistan", font=("Arial", 23, "normal"))

    # name of Pakistan in Punjabi
    t.left(90)
    t.forward(280)
    t.right(90)
    t.write("ਪਾਕਿਸਤਾਨ ਇਸਲਾਮੀ ਗਣਰਾਜ", font=("Arial", 23, "normal"))
    tk.deiconify()

def Russia():
    tk.withdraw()
    # hiding the turtle 
    t.hideturtle()
    t.clear()
    t.home()
    # Putting turtle at centre of canvas
    t.up()
    t.back(200)

    # Making rectangle
    t.down()
    t.forward(350)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(350)
    t.left(90)
    t.forward(200)
    t.back(133)

    # blue stripe
    t.down()
    t.begin_fill()
    t.left(90)
    t.color('#0033A0')
    t.forward(350)
    t.right(90)
    t.forward(66)
    t.right(90)
    t.forward(350)
    t.right(90)
    t.forward(66)
    t.end_fill()

    # Getting ready for red stripe
    t.left(180)
    t.forward(66)

    # red stripe
    t.begin_fill()
    t.left(90)
    t.color('red')
    t.forward(350)
    t.right(90)
    t.forward(66)
    t.right(90)
    t.forward(350)
    t.right(90)
    t.forward(66)
    t.end_fill()

    # Name of russia in russian
    t.left(180)
    t.up()
    t.color('black')
    t.forward(105)
    t.write('Росси́йская Федера́ция', font=("Arial", 25, "normal"))

    #
    t.right(180)
    t.forward(240)
    t.left(90)
    t.back(120)
    t.write("ਰੂਸੀ ਸੰਘ", font=('Arial', 25, 'normal'))
    tk.deiconify()


def US():
    tk.withdraw()
    # hiding the turtle 
    t.hideturtle()
    t.clear()
    t.home()
    # Putting turtle at centre of canvas
    t.up()
    t.back(200)

    # Making rectangle
    t.down()
      
    t.forward(350)
    t.left(90)
    t.forward(200.2)
    t.left(90)
    t.forward(350)
    t.left(90)
    t.forward(200.2)

    # Blue square
    t.back(100)
    t.color('#3C3B6E')
    t.left(90)
    t.forward(150)
    t.begin_fill()
    for x in range(1, 3):
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(150)

    t.end_fill()

    # stripes
    t.up()
    t.color('#B22234')
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(200)
    t.right(90)


    t.down()

    stripe = 14.3

    for x in range(1, 5):
        t.begin_fill()
        t.forward(stripe)
        stripe = 14.3
        t.right(90)
        t.forward(200)
        t.right(90)
        t.forward(stripe)
        t.right(90)
        t.forward(200)
        t.right(90)
        t.end_fill()
        stripe = stripe * 3

    for x in range(1, 4):
        t.begin_fill()
        t.forward(stripe)
        stripe = 14.3
        t.right(90)
        t.forward(350)
        t.right(90)
        t.forward(stripe)
        t.right(90)
        t.forward(350)
        t.right(90)
        t.end_fill()
        stripe = stripe * 3

    # Getting rid of extra stripe (white one at bottom)
    t.forward(14.3)# don't combine this with the other 14.3 one.
    t.color('white')
    t.forward(14.3)
    t.right(90)
    t.forward(350)
    t.right(90)
    t.forward(14.3)

    # stars
    t.up()
    t.forward(170)
    t.right(90)
    t.color('white')

    star = 10

    for x in range(1, 5):
        for x in range(1, 7):
            t.forward(star)
            star = 15
            t.write("★", font=("Arial", 7, "normal"))
            star = star + 10

        t.back(135)
        t.right(90)
        t.forward(10)
        t.left(90)
        star = 20

        for x in range(1, 6):
            t.forward(star)
            star = 15
            t.write("★", font=("Arial", 7, "normal"))
            star = star + 10

        t.back(135)
        t.right(90)
        t.forward(10)
        t.left(90)

    for x in range(1, 7):
        t.forward(star)
        star = 15
        t.write("★", font=("Arial", 7, "normal"))
        star = star + 10

    # Name of America in english
    t.color('black')
    t.back(135)
    t.right(90)
    t.forward(125)
    t.right(90)
    t.write("United States of America", font=("Arial", 25, "normal"))

    # Name of america in Punjabi
    t.right(90)
    t.forward(220)
    t.left(90)
    t.back(40)
    t.write("ਸਯੁੰਕਤ ਰਾਜ ਅਮੇਰਿਕਾ", font=("Arial", 25, "normal"))
    tk.deiconify()
 
def USSR():
    tk.withdraw()
    # hiding the turtle 
    t.hideturtle()
    t.clear()
    t.home()
    # Putting turtle at centre of canvas
    t.up()
    t.back(200)

    # Making rectangle
    t.color('#CD0000')
    t.begin_fill()
    t.down()
    t.forward(350)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(350)
    t.left(90)
    t.forward(200)
    t.end_fill()
    t.back(120)

    # Hammer and Sickle + star
    t.color('yellow')
    t.left(90)
    t.up()
    t.forward(20)
    t.write("☭", font=("Arial", 45, "normal"))
    t.back(10)
    t.left(90)
    t.forward(57)
    t.right(90)
    t.forward(30)
    t.write("⭐", font=("Arial", 7, "normal"))

    # name of ussr russian
    t.color('black')
    t.right(90)
    t.forward(225)
    t.right(90)
    t.forward(190)
    t.write("Союз Советских Социалистических Республик", font=("Arial", 25, "normal"))

    # name of ussr punjabi
    t.right(90)
    t.forward(245)
    t.left(90)
    t.back(85)
    t.write("ਸੋਵੀਅਤ ਸਮਾਜਵਾਦੀ ਗਣਤੰਤਰਾਂ ਦਾ ਸੰਘ", font=("Arial", 25, "normal"))
    tk.deiconify()

def Germany():
    tk.withdraw()
    # hiding the turtle 
    t.hideturtle()
    t.clear()
    t.home()
    # putting turtle at centre
    t.back(175)
    t.down()

    # making rectangle
    for x in range(1, 3):
      t.forward(350)
      t.left(90)
      t.forward(200)
      t.left(90)

    # getting ready for black stripe
    t.left(90)
    t.forward(132)
    t.right(90)
    t.begin_fill()

    # Black stripe
    for x in range(1, 3):
      t.forward(350)
      t.left(90)
      t.forward(66)
      t.left(90)
    t.end_fill()

    # getting ready for red stripe
    t.color('red')
    t.begin_fill()

    # red stripe
    for x in range(1, 3):
      t.forward(350)
      t.right(90)
      t.forward(66)
      t.right(90)
    t.end_fill()

    # getting ready for yellow stripe
    t.right(90)
    t.forward(66)
    t.color('#FFCE00')
    t.left(90)

    # yellow stripe
    t.begin_fill()
    for x in range(1, 3):
      t.forward(350)
      t.right(90)
      t.forward(66)
      t.right(90)
    t.end_fill()

    # name of Germany in German
    t.right(90)
    t.color('black')
    t.up()
    t.forward(100)
    t.right(90)
    t.forward(25)
    t.write('Bundesrepublik Deutschland', font=('Arial', 25, "normal"))

    # name of Germany in Punjabi
    t.right(90)
    t.forward(230)
    t.left(90)
    t.back(45)
    t.write("ਜਰਮਨੀ ਦਾ ਸੰਘੀ ਗਣਰਾਜ", font=("Arial", 25, "normal"))
    
    tk.deiconify()

def DPRK():
    tk.withdraw()
    # hiding the turtle 
    t.hideturtle()
    t.clear()
    t.home()
    t.begin_fill()
    t.color('#024FA2')

    # Putting turtle at centre of canvas
    t.up()
    t.back(200)

    # Making rectangle
    t.down()
    t.forward(350)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(350)
    t.left(90)
    t.forward(200)
    t.end_fill()

    # white stripe function
    def white():
        t.begin_fill()
        t.color('white')
        t.forward(350)
        t.right(90)
        t.forward(5)
        t.right(90)
        t.forward(350)
        t.right(90)
        t.forward(5)
        t.end_fill()

    # white stripe 1
    t.back(150)
    t.left(90)
    white()

    # red stripe
    t.left(180)
    t.forward(5)
    t.begin_fill()
    t.color('red')
    t.left(90)
    t.forward(350)
    t.right(90)
    t.forward(95)
    t.right(90)
    t.forward(350)
    t.right(90)
    t.forward(95)
    t.end_fill()

    # white stripe 2
    t.left(180)
    t.forward(95)
    t.left(90)
    white()

    # white circle
    t.up()
    t.forward(15)
    t.right(90)
    t.forward(87)
    t.down()
    t.begin_fill()
    t.circle(35)
    t.end_fill()

    #star
    t.up()
    t.color('red')
    t.back(36)
    t.left(90)
    t.back(10)
    t.right(90)
    t.write("★", font=("Arial", 60, "normal"))

    # Name of dprk in korean
    t.right(90)
    t.forward(100)
    t.color('black')
    t.right(90)
    t.forward(55)
    
    t.write("조선민주주의인민공화국", font=("Arial", 25, "normal"))

    # name of dprk in punjabi
    t.right(90)
    t.forward(240)
    t.left(90)
    t.forward(15)
    t.write("ਕੋਰੀਆ ਜਨਵਾਦੀ ਲੋਕ-ਗਣਤੰਤਰ", font=("Arial", 25, "normal"))
    tk.deiconify()

def yemen():
    tk.withdraw()
    # hiding the turtle 
    t.hideturtle()
    t.clear()
   # positions turtle at centre
    t.back(150)

    # makes rectangle
    for x in range(1, 3):
      t.forward(350)
      t.left(90)
      t.forward(200)
      t.left(90)

    # gets in position for the red stripe
    t.left(90)
    t.forward(133)
    t.right(90)

    # red stripe
    t.color('#CE1126')
    t.begin_fill()
    for x in range(1, 3):
      t.forward(350)
      t.left(90)
      t.forward(66)
      t.left(90)
    t.end_fill()

    # gets in position for black stripe
    t.color('black')
    t.right(90)
    t.forward(66)
    t.left(90)

    # black stripe
    t.begin_fill()
    for x in range(1, 3):
      t.forward(350)
      t.right(90)
      t.forward(66)
      t.right(90)

    t.end_fill()

    # Yemen name in arabic
    t.up()
    t.right(90)
    t.forward(110)
    t.right(90)
    t.back(90)
    t.write("ٱلْجُمْهُورِيَّة ٱلْيَمَنِيَّة", font=("Arial", 25, "normal"))

    # Yemen name in punjabi
    t.right(90)
    t.forward(240)
    t.left(90)
    t.forward(10)
    t.write("ਯਮਨ ਗਣਰਾਜ", font=("Arial", 25, "normal"))

    tk.deiconify()

def Vietnam():
    tk.withdraw()
    # hiding the turtle
    t.home()
    t.hideturtle()
    t.clear()

    # positions turtle at centre
    t.back(150)

    t.down()
    t.color('#DE2910')
    t.begin_fill()
    # makes rectangle
    for x in range(1, 3):
      t.forward(350)
      t.left(90)
      t.forward(200)
      t.left(90)

    t.end_fill()

    # star
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(110)
    t.color('yellow')
    t.write("★", font=("Arial", 100, "normal"))
    t.up()

    # Name of vietnam in vietnamess
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(175)
    t.color('black')
    t.write("Cộng hòa xã hội chủ nghĩa Việt Nam", font=("Arial", 25, "normal"))

    # Name of vietnam in Punjabi
    t.right(90)
    t.forward(230)
    t.left(90)
    t.back(30)
    t.write("ਵੀਅਤਨਾਮ ਦਾ ਸਮਾਜਵਾਦੀ ਗਣਰਾਜ", font=("Arial", 25, "normal"))
    tk.deiconify()

    
    
def credit():
    messagebox.showinfo("Credits ਕ੍ਰੇਡਿਟਸ", "Made entirely by Tushar Passi \n\
ਤੁਸ਼ਾਰ ਪਾਸੀ ਨੇ ਸੱਭ ਕੁਚ ਬਣਾਇਆ") 

def about():
    messagebox.showinfo("About ਜਾਨ ਕਾਰੀ",  "This software makes flags. \n\
\n\
Countries: India, Japan, Qatar, Bangladesh, China, Pakistan, United States, \
Soviet Union, Germany, North Korea, Yemen, and Vietnam \n\
\n\
Software language: Mainly Punjabi and English but also (not as much): \
Arabic, Urdu, Hindi, Russian, Simplified Chinese, Bengali, Japanese, German, \
Korean, and Vietnamese \n\
\n\
ਇਹ ਸਾਫਟਵੇਰ ਝੰਡਾ ਬਣਾਂਦਾ| \n\
\n\
ਦੇਸ਼ਾ: ਭਾਰਤ, ਜਪਾਨ, ਕਤਰ, ਬੰਗਲਾਦੇਸ਼, ਚੀਨ, ਪਾਕਿਸਤਾਨ, ਸਯੁੰਕਤ ਰਾਜ, ਸੋਵੀਅਤ ਰਾਜ, ਜਰਮਨੀ, \
ਉੱਤਰ ਕੋਰੀਆ, ਯਮਨ, ਵੀਅਤਨਾਮ \n\
\n\
ਸਾਫਟਵੇਰ ਦੇ ਭਾਸਾ: ਜ਼ਿਆਦਾਤਰ ਪੰਜਾਬੀ ਅਤੇ ਅੰਗ੍ਰੇਜ਼ੀ ਪਰ (ਇਤਨਾ ਨਹੀਂ): ਅਰਬੀ, ਉਰਦੂ, ਹਿੰਦੀ, ਰੂਸੀ, \
ਸਰਲ ਚੀਨੀ, ਬੰਗਲਾ, ਜਪਾਨੀ, ਜਰਮਨ, ਕੋਰੀਅਨ, ਅਤੇ ਵੀਅਤਨਾਮੀ")
    
# menu
menu = Menu(tk)
tk.config(menu=menu)
fileoption = Menu(menu)

# File menu
menu.add_cascade(label="India ਭਾਰਤ", command=India)
menu.add_cascade(label="Japan ਜਪਾਨ", command=Japan)
menu.add_cascade(label="Qatar ਕਤਰ", command=Qatar)
menu.add_cascade(label="Bangladesh ਬੰਗਲਾਦੇਸ਼", command=Bangladesh)
menu.add_cascade(label="China ਚੀਨ", command=China)
menu.add_cascade(label="Pakistan ਪਾਕਿਸਤਾਨ", command=Pakistan)
menu.add_cascade(label="United States ਸਯੁੰਕਤ ਰਾਜ", command=US)
menu.add_cascade(label="Russia ਰੂਸ", command=Russia)
menu.add_cascade(label="Soviet Union ਸੋਵੀਅਤ ਰਾਜ", command=USSR)
menu.add_cascade(label="Germany ਜਰਮਨੀ", command=Germany)
menu.add_cascade(label="North Korea ਉੱਤਰ ਕੋਰੀਆ", command=DPRK)
menu.add_cascade(label="Yemen ਯਮਨ", command=yemen)
menu.add_cascade(label="Vietnam ਵੀਅਤਨਾਮ", command=Vietnam)
menu.add_cascade(label="Other options ਹੋਰ ਆਪਸ਼ਨ", menu=fileoption)
fileoption.add_cascade(label="About ਜਾਨ ਕਾਰੀ", command=about)
fileoption.add_cascade(label="Credits ਕ੍ਰੇਡਿਟਸ", command=credit)
fileoption.add_separator()
fileoption.add_cascade(label="Exit ਨਿਕਾਸ", command=Exit)

# window size
tk.geometry("400x150")

# mainloop
tk.mainloop()
