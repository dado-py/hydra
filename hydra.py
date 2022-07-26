from tkinter import *



while True:

    def rooting2():
        root2 = Tk()
        root2.configure(bg='green')
        root2.resizable(width=False, height=False)
        root2.geometry('300x150')

        myB = Button(root2, text="  EXIT  ", command=two_window())
        myB.place(x=120, y=70)
        root2.mainloop()



  



    def two_window():
        if root.quit():
            print("haloooo")
            while True:
                rooting2()








    root = Tk()
    Label(root,  text ="hydraaaa").pack()
    myB = Button(root, text="  EXIT  ", )
    myB.place(x=120, y=70)

    root.configure(bg='blue')
    root.resizable(width=False, height=False)
    root.geometry('300x150')
    root.title("hydra")
    myB = Button(root, text="  EXIT  ", command=two_window())
    myB = Button(root, text="  EXIT  ", command=two_window())
    myB.place(x=120, y=70)
    root.mainloop()