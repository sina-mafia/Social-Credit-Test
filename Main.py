# Made by Nima
from tkinter import *
import pygame
import sys
import time
import os

pygame.mixer.init()
background_music = pygame.mixer.Sound("SCT\Sounds\Ching_Cheng_Hanji.mp3")
correct_answer = pygame.mixer.Sound("SCT\Sounds\Yay.mp3")
wrong_answer = pygame.mixer.Sound("SCT\Sounds\Social_Credit_Siren.mp3")
john_xina_calling = pygame.mixer.Sound("SCT\Sounds\Discord_call.mp3")
john_xina_joined = pygame.mixer.Sound("SCT\Sounds\Discord_join.mp3")
john_xina_leave = pygame.mixer.Sound("SCT\Sounds\Discord_leave.mp3")
pygame.mixer.Sound.play(background_music)

score = 0            
words = "Hello it's me, John Xina. It seems like you have very low social credit points And I'm afraid that We will have to execute you."

def john_xina_talking():
    for char in words:
        time.sleep(0.15)
        sys.stdout.write(char)
        sys.stdout.flush()

def check():
    if score < 2:
                window.destroy()
                pygame.mixer.Sound.stop(correct_answer)
                pygame.mixer.Sound.stop(wrong_answer)
                pygame.mixer.Sound.stop(background_music)
                pygame.mixer.Sound.play(john_xina_calling)
                os.system('cls||clear')
                print("John Xina started a call")
            
                time.sleep(5)
                print("<John Xina>: ")
                pygame.mixer.Sound.play(john_xina_joined)
                john_xina_talking()
                pygame.mixer.Sound.play(john_xina_leave)
                print("\n")
                print("\n")
                print("""Your Execution date is TOMORROW. Glory to the CCP!\n""")
                print("您的执行日期是明天. 荣耀归于中共!")
                exit()
                   
def next():
    global label2
    button.destroy()
    label.config(image=label_photo2)
    label2 = Label(window,text="WHO IS THIS PERSON? 这个人是谁？",font=("IMPACT",35),padx=60)
    label2.place(x=1,y=440)
        
    def answer():
        global score
        if(x.get()==0):
            label.config(image=social_credit1)
            pygame.mixer.Sound.play(wrong_answer,loops=2)
            radiobutton1.destroy()
            radiobutton2.destroy()
            label2.place(x=100000000,y=100000000)
            
            label.after(4500, lambda: label.config(image=label_photo3))
            label2.after(4500, lambda: label2.place(x=1,y=440))
            radiobutton3.after(4500, lambda: radiobutton3.place(x=420,y=375))
            radiobutton4.after(4500, lambda: radiobutton4.place(x=200,y=375))
            
            score -= 1
                        
        elif(x.get()==1):
            label.config(image=social_credit2)
            pygame.mixer.Sound.play(correct_answer)
            radiobutton1.destroy()
            radiobutton2.destroy()
            label2.place(x=100000000,y=100000000)
            
            label.after(3400, lambda: label.config(image=label_photo3))
            label2.after(3400, lambda: label2.place(x=1,y=440))
            radiobutton3.after(3400, lambda: radiobutton3.place(x=420,y=375))
            radiobutton4.after(3400, lambda: radiobutton4.place(x=200,y=375))
            
            score += 1
    
    def answer2():
        global score
        if(x.get()==2):
            label.config(image=social_credit2)
            pygame.mixer.Sound.play(correct_answer)
            radiobutton3.destroy()
            radiobutton4.destroy()
            label2.place(x=100000000,y=100000000)
            
            label.after(3400, lambda: label.config(image=label_photo4))
            label2.after(3400, lambda: label2.config(text="IS TAIWAN A COUNTRY? 台湾是一个国家吗？",font=("IMPACT",30),padx=62))
            label2.after(3400, lambda: label2.place(x=0,y=448))
            radiobutton5.after(3400, lambda: radiobutton5.place(x=400,y=383))
            radiobutton6.after(3400, lambda: radiobutton6.place(x=150,y=383))
            
            score += 1
            
        elif(x.get()==3):
            label.config(image=social_credit1)
            pygame.mixer.Sound.play(wrong_answer,loops=2)
            radiobutton3.destroy()
            radiobutton4.destroy()
            label2.place(x=100000000,y=100000000)
            
            label.after(4500, lambda: label.config(image=label_photo4))
            label2.after(4500, lambda: label2.config(text="IS TAIWAN A COUNTRY? 台湾是一个国家吗？",font=("IMPACT",30),padx=62))
            label2.after(4500, lambda: label2.place(x=0,y=448))
            radiobutton5.after(4500, lambda: radiobutton5.place(x=400,y=383))
            radiobutton6.after(4500, lambda: radiobutton6.place(x=150,y=383))
            
            score -= 1
    
    def answer3():
        global score
        if(x.get()==5):
            label.config(image=social_credit2)
            pygame.mixer.Sound.play(correct_answer)
            radiobutton5.destroy()
            radiobutton6.destroy()
            label2.place(x=100000000,y=100000000)
            score += 1
            
            
        elif(x.get()==4):
            label.config(image=social_credit1)
            pygame.mixer.Sound.play(wrong_answer,loops=2)
            radiobutton5.destroy()
            radiobutton6.destroy()
            label2.place(x=100000000,y=100000000)
            score -= 1
            
        check()
        time.sleep(5)
        exit()
        
                
            
    
    radiobutton1 = Radiobutton(window,
                          text="JOHN SINA", 
                            variable=x,
                            value=0,
                            font=("Impact",30),
                            #indicatoron=0,
                            command=answer
                            )
    radiobutton1.place(x=420,y=375)
    
    radiobutton2 = Radiobutton(window,
                          text="JOHN XINA", 
                            variable=x,
                            value=1,
                            font=("Impact",30),
                            #indicatoron=0,
                            command=answer
                            )
    radiobutton2.place(x=200,y=375)

    radiobutton3 = Radiobutton(window,
                          text="THE VOK", 
                            variable=x,
                            value=2,
                            font=("Impact",30),
                            #indicatoron=0,
                            command=answer2
                            )
    
    radiobutton4 = Radiobutton(window,
                          text="THE ROCK", 
                            variable=x,
                            value=3,
                            font=("Impact",30),
                            #indicatoron=0,
                            command=answer2
                            )
    
    radiobutton5 = Radiobutton(window,
                          text="YES", 
                            variable=x,
                            value=4,
                            font=("Impact",30),
                            width=11,
                            #indicatoron=0,
                            command=answer3
                            )
    
    radiobutton6 = Radiobutton(window,
                          text="NO", 
                            variable=x,
                            value=5,
                            font=("Impact",30),
                            width=11,
                            #indicatoron=0,
                            command=answer3
                            )

window = Tk()
icon = PhotoImage(file="SCT\Images\Icon.png")
window.title("社会信用测试, 做出明智的选择 !")
window.geometry("800x500")
window.iconphoto(True,icon)
window.config(background="red")

label_photo = PhotoImage(file="SCT\Images\Label_Photo.png")
label_photo2 = PhotoImage(file="SCT\Images\John_Xina.png")
label_photo3 = PhotoImage(file="SCT\Images\The_vok.png")
label_photo4 = PhotoImage(file="SCT\Images\Wondering.png")
label_photo5 = PhotoImage(file="SCT\Images\John_Xina_Calling.png")
label_photo6 = PhotoImage(file="SCT\Images\John_Xina_In_A_Call.png")
label = Label(window,
              image=label_photo)
label.pack()

button = Button(window,
                text="START TEST",
                font=("IMPACT",45),
                command=next)
button.place(x=425,y=300)

x = IntVar()
social_credit1 = PhotoImage(file="SCT\Images\-Social_Credit.png")
social_credit2 = PhotoImage(file="SCT\Images\+Social_Credit.png")

window.mainloop()