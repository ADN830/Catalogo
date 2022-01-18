import tkinter as tK


def main():
    root = tK.Tk()
    root.title('Catalogo de Peliculas')
    root.iconbitmap()
    root.resizable(0, 0)

    frame = tK.Frame(root)
    frame.pack()
    frame.config(width=480, height=320)
  
    root.mainloop()


if __name__ == '__mina__':
    main()
